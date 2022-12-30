from odoo import models, fields, _

class Doctor(models.Model):
    _name = 'hs3.doctor'
    _description = 'Doctor'
    _inherit = 'hs3.person.mixin'

    active = fields.Boolean(
        default=True, )
    specialty = fields.Char(
        required=True, )
    is_intern = fields.Boolean(
        default=False, )
    mentor_id = fields.Many2one(
        comodel_name='hs3.doctor',
        domain="[('is_intern','=',False)]",
    )