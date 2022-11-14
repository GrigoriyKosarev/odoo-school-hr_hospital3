from odoo import models, fields, _

class Patient(models.Model):
    _name = 'hs3.patient'
    _description = 'Patient'

    full_name = fields.Char(required=True)
    gender = fields.Selection(
        default='male',
        selection= [('male', _('Male')), ('female', _('Female'))]
    )
    birthday = fields.Date(string='Date of birth')
    age = fields.Integer(default='18')
    passport = fields.Char()
    contact_person = fields.Char()

