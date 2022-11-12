from odoo import models, fields, _

class Patient(models.Model):
    _name = 'hs3.patient'
    _description = 'Patient'

    full_name = fields.Char()
    gender = fields.Selection(
        default='',
        selection= [('male', _('Male')), ('female', _('Female'))]
    )
    birthday = fields.Date()
    age = fields.Integer()
    passport = fields.Char()
    contact_person = fields.Char()

