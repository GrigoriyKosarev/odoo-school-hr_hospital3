from odoo import models, fields, _

class Diagnosis(models.Model):
    _name = 'hs3.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char(required=True)
    active = fields.Boolean(
        default=True, )
    doctor_id = fields.Many2one(
        comodel_name='hs3.doctor', required=True, )
    patient_id = fields.Many2one(
        comodel_name='hs3.patient', required=True, )
    disease_id = fields.Many2one(
        comodel_name='hs3.disease')
    date = fields.Datetime()
    purpose_of_diagnosis = fields.Char(
        required=True, string='Purpose of diagnosis')
    research_id = fields.Many2one(
        comodel_name='hs3.research', )