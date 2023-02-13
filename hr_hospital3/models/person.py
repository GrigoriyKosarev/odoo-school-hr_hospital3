from odoo import models, fields, api, _


class PersonMixin(models.AbstractModel):
    _name = 'hs3.person.mixin'
    _description = 'Person mixin'

    name = fields.Char()
    active = fields.Boolean(
        default=True, )
    full_name = fields.Char(
        required=True,
        string='Full name',
        )
    phone = fields.Char(
        required=False, )
    email = fields.Char(
        required=False, )
    photo = fields.Binary(
        required=False, )
    gender = fields.Selection(
        default='male',
        required=True,
        selection=[('male', _('Male')), ('female', _('Female'))], )

    @api.onchange('name')
    def _onchange_fullname(self):
        for obj in self:
            obj.full_name = obj.name
