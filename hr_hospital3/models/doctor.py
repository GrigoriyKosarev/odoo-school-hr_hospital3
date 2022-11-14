from odoo import models, fields, _

class Doctor(models.Model):
    _name = 'hs3.doctor'
    _description = 'Doctor'

    full_name = fields.Char(required=True)
    specialty = fields.Char(required=True)