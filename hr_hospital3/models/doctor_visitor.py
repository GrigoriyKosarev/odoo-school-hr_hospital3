from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class DoctorVisitor(models.Model):
    _name = 'hs3.doctor.visitor'
    _description = 'Doctor visitor'

    name = fields.Char()
    active = fields.Boolean(
        default=True, )
    doctor_id = fields.Many2one(
        comodel_name='hs3.doctor', required=True, )
    patient_id = fields.Many2one(
        comodel_name='hs3.patient', required=True, )
    date_admission = fields.Datetime(string='Date of admission', )
    diagnosis_id = fields.Many2one(comodel_name='hs3.diagnosis', )
    recommendation = fields.Char()
    research_id = fields.Many2one(
        comodel_name='hs3.research', )
    schedule_id = fields.Many2one(comodel_name='hs3.schedule',
                                  domain="[('finished','=',False)]", )
    finished = fields.Boolean(
        string='finished', )

    @api.onchange('doctor_id', 'patient_id')
    def _onchange_set_name(self):
        for obj in self:
            obj.name = f'{obj.patient_id.name} - {obj.doctor_id.name}'

    def write(self, vals):
        res = super(DoctorVisitor, self).write(vals)
        if vals.get('finished'):
            if self.schedule_id:
                self.schedule_id.write({'finished': vals['finished']})
        return res

    @api.constrains('active')
    def constrains_active(self):
        for obj in self:
            if not obj.active and obj.diagnosis_id:
                raise ValidationError(_('can`t delete with diagnosis'))

    @api.ondelete(at_uninstall=False)
    def _unlink_only_if_open(self):
        for obj in self:
            if obj.diagnosis_id:
                raise ValidationError(_('can`t delete with diagnosis'))
