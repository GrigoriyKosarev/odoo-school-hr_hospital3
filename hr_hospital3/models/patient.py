from odoo import models, fields, _

class Patient(models.Model):
    _name = 'hs3.patient'
    _description = 'Patient'

    full_name = fields.Char(required=True, string='Full name')
    gender = fields.Selection(
        default='male',
        required=True,
        selection= [('male', _('Male')), ('female', _('Female'))]
    )
    birthday_date = fields.Date(string='Date of birth', required=True)
    age = fields.Integer(default='18')
    passport = fields.Char()
    contact_person = fields.Char(string='Contact person')

