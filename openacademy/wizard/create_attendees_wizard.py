# -*- coding: utf-8 -*-
from odoo import models, fields


class CreateAttendeesWizard(models.TransientModel):
    _name = 'create.attendees.wizard'
    _description = 'Create Attendees Wizard'

    def default_session(self):
        return self.env['openacademy.sessions'].browse(self._context.get('active_id'))

    sessions = fields.Many2many('openacademy.sessions', string='Sessions', required=True, default=default_session)
    attendees = fields.Many2many('res.partner', string='Attendees')

    def action_create_attendees(self):
        for record in self.sessions:
            record.attendees = self.attendees
