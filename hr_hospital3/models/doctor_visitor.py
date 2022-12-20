import datetime

from odoo import models, fields, api, _

class DoctorVisitor(models.Model):
    _name = 'hs3.doctor.visitor'
    _description = 'Doctor visitor'

    name = fields.Char(
        string='Name', )
    active = fields.Boolean(
        default=True, )
    doctor_id = fields.Many2one(
        comodel_name='hs3.doctor', required=True, )
    patient_id = fields.Many2one(
        comodel_name='hs3.patient', required=True, )
    date_admission = fields.Datetime(
        string='Date of admission'
        # default=datetime.datetime.today()
        ,)
    diagnosis_id = fields.Many2one(
        comodel_name='hs3.diagnosis', )
    recommendation = fields.Char(
        string='Recommendation',
    )

    @api.onchange('doctor_id', 'patient_id')
    def _onchange_set_name(self):
        for obj in self:
            obj.name = f'{obj.patient_id.name} - {obj.doctor_id.name}'