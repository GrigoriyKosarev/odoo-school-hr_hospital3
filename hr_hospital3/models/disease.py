from odoo import models, fields, _

class Disease(models.Model):
    _name = 'hs3.disease'
    _description = 'Disease'

    name = fields.Char(required=True)
    name1 = fields.Char(required=True)