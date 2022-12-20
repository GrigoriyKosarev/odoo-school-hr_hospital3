from odoo import exceptions, models, fields, api, _

class Contact(models.Model):
    _name = 'hs3.contact'
    _description = 'Contact'
    _inherit = 'hs3.person.mixin'

    active = fields.Boolean(
        default=True, )



