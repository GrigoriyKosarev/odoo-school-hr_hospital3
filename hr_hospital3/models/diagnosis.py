from odoo import models, fields, _

class Diagnosis(models.Model):
    _name = 'hs3.diagnosis'
    _description = 'Diagnosis'

    doctor = fields.Char(required=True)
    name = fields.Char(required=True)
    diseases = fields.Char(required=True)