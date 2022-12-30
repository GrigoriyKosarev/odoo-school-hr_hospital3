from odoo import models, fields, _

class Research(models.Model):
    _name = 'hs3.research'
    _description = 'Research'

    active = fields.Boolean(
        default=True, )
    category_id = fields.Many2one(
        comodel_name='hs3.research.type', )
    patient_id = fields.Many2one(
        comodel_name='hs3.patient', )

