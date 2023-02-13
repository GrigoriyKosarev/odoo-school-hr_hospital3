from odoo import models, fields


class Disease(models.Model):
    _name = 'hs3.disease'
    _description = 'Disease'

    name = fields.Char(required=True)
    active = fields.Boolean(
        default=True, )
    category_id = fields.Many2one(
        comodel_name='hs3.disease.type', )
