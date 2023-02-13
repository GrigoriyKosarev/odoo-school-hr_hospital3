from odoo import models, fields


class Sample(models.Model):
    _name = 'hs3.sample'
    _description = 'Sample'

    name = fields.Char()
