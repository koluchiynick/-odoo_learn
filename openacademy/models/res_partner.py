# -*- coding: utf-8 -*-

from odoo import models, fields


class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(string='Instructor')
    session_ids = fields.Many2many('openacademy.session', string='Session')
    teacher = fields.Selection([('teacher_level1', "teacher level 1"), ('teacher_level2', "teacher level 2")])
