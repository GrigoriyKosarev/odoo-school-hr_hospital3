from odoo import models, fields, _, api

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
    @api.onchange('mentor_id')
    def _compute_intern(self):
        for obj in self:
            obj.is_intern = obj.mentor_id