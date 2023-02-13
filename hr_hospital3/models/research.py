from odoo import models, fields


class Research(models.Model):
    _name = 'hs3.research'
    _description = 'Research'

    active = fields.Boolean(
        default=True, )
    name = fields.Char()
    category_id = fields.Many2one(
        comodel_name='hs3.research.type', )
    patient_id = fields.Many2one(
        comodel_name='hs3.patient', )
    doctor_id = fields.Many2one(
        comodel_name='hs3.doctor', )
    sample_id = fields.Many2one(
        comodel_name='hs3.sample', )
    conclusion = fields.Char()
