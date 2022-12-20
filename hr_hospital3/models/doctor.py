from odoo import models, fields, _

class Doctor(models.Model):
    _name = 'hs3.doctor'
    _description = 'Doctor'
    _inherit = 'hs3.person.mixin'

    active = fields.Boolean(
        default=True, )
    specialty = fields.Char(
        required=True, )