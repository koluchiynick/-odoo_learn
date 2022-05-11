# -*- coding: utf-8 -*-
from odoo import models, fields


class CreateAttendeesWizard(models.TransientModel):
    _name = 'create.attendees.wizard'
    _description = 'Create Attendees Wizard'

    def default_session(self):
        return self.env['openacademy.session'].browse(self._context.get('active_id'))

    session_ids = fields.Many2many('openacademy.session', string='Session', required=True, default=default_session)
    attendee_ids = fields.Many2many('res.partner', string='Attendee')

    def action_create_attendees(self):
        for record in self.session_ids:
            record.attendees = self.attendee_ids
