from odoo import models, fields


class Teachers(models.Model):
    _name = 'academy.teachers'

    name = fields.Char()
    biography = fields.Html()

    # course_ids = fields.One2many('academy.courses', 'teacher_id', string="Courses")
    course_ids = fields.One2many(comodel_name='product.template', inverse_name='teacher_id', string='Courses')


class Courses(models.Model):
    # _name = 'academy.courses'
    # _inherit = ['mail.thread', 'product.template']
    _inherit = 'product.template'

    name = fields.Char()
    # teacher_id = fields.Many2one('academy.teachers', string="Teacher")
    teacher_id = fields.Many2one(comodel_name='academy.teachers', string='Teacher')
