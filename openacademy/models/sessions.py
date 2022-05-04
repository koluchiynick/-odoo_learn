# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Sessions(models.Model):
    _name = 'openacademy.sessions'
    _description = 'Open academy sessions'

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string='Start Date', required=True, default=fields.Date.today())
    end_date = fields.Date(string='End date', required=False)
    duration = fields.Integer(string='Duration', required=True)
    number_of_seats = fields.Integer(string="Number of seat", default=1)
    instructor = fields.Many2one('res.partner', string='Instructor', domain=['|', ('instructor', '=', True),
                                                                             ('teacher', 'in', ('teacher_level1',
                                                                                                'teacher_level2'))])
    course = fields.Many2one('openacademy.course', string='Course', required=True)
    attendees = fields.Many2many(comodel_name='res.partner', string='Attendees')
    percent_taken_seats = fields.Float(compute='_compute_percent_taken_seats', string='% of taken seats')
    active = fields.Boolean(default=True, string="Active")
    attendees_count = fields.Integer(string="Attendees count", compute='_compute_attendees_count', store=True)

    @api.depends('attendees')
    def _compute_attendees_count(self):
        for record in self:
            record.attendees_count = len(record.attendees)

    @api.depends('attendees', 'number_of_seats')
    def _compute_percent_taken_seats(self):

        for record in self:
            if not record.number_of_seats:
                record.percent_taken_seats = 0
            else:
                record.percent_taken_seats = len(record.attendees) * 100 / record.number_of_seats

    @api.onchange('number_of_seats', 'attendees')
    def _onchange_percent(self):

        total = len(self.attendees)

        if total > self.number_of_seats:
            self.percent = round(total / self.number_of_seats * 100)
            return {
                'warning': {
                    'title': "Incorrect value",
                    'message': "More participants than places",
                }
            }
        elif self.number_of_seats <= 0:
            return {
                'warning': {
                    'title': "Incorrect value",
                    'message': "Number of seats must be greater than zero",
                }
            }

    @api.constrains('instructor', 'attendees')
    def _check_instructor_in_attendees(self):
        for record in self:
            if record.instructor and record.instructor in record.attendees:
                raise ValidationError("Your instructor is in list of attendees")
