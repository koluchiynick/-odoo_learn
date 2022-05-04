# -*- coding: utf-8 -*-

from odoo import models, fields


class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(string='Instructor')
    sessions = fields.Many2many('openacademy.sessions', string='Sessions')
    teacher = fields.Selection([('teacher_level1', "teacher level 1"), ('teacher_level2', "teacher level 2")])
