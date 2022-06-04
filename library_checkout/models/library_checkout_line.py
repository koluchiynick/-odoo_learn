# -*- coding: utf-8 -*-

from odoo import fields, models


class CheckoutLine(models.Model):
    _name = "library.checkout.line"
    _description = "Checkout Request Line"
    
    checkout_id = fields.Many2one("library.checkout", required=True)
    book_id = fields.Many2one("library.book", required=True)
    note = fields.Char("Notes")
