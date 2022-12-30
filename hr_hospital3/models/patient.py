import datetime

from odoo import exceptions, models, api, fields, _

class Patient(models.Model):
    _name = 'hs3.patient'
    _description = 'Patient'
    _inherit = 'hs3.person.mixin'

    active = fields.Boolean(
        default=True, )
    birthday_date = fields.Date(
        string='Date of birth', required=True, )
    age = fields.Integer(
        compute='_compute_age',
        )
    passport = fields.Char()
    contact_id = fields.Many2one(
        comodel_name='hs3.contact', string='Contact', )
    personal_doctor_id = fields.Many2one(
        comodel_name='hs3.doctor', required=True, )


    @api.constrains('contact_id', 'personal_doctor_id')
    def check_fields(self):
        for patient in self:
            if patient.contact_id is False:
                raise ValueError('Contact ')

    @api.model_create_multi
    def create(self, values):
        print('+++start create+++')
        print(values)
        obj = super(Patient, self).create(values)
        return obj

    def write(self, values):
        # print('+++start write+++')
        for obj in self:
            if 'personal_doctor_id' in values:
                doctor_history_values = {
                    'name': f'{obj.contact_id.name} - {obj.personal_doctor_id.name}',
                    'active':True,
                    'patient_id':obj.id,
                    'doctor_id': values['personal_doctor_id'],
                    'appointment_date': datetime.date.today()
                }
                self.env['hs3.personal.doctor.history'].create(doctor_history_values)

        obj = super(Patient, self).write(values)
        return obj

    @api.depends('birthday_date')
    def _compute_age(self):
        for obj in self:
            if obj.birthday_date:
                date_today = datetime.date.today()
                extra_year = ((date_today.month, date_today.day) < (obj.birthday_date.month, obj.birthday_date.day))
                obj.age = date_today.year - obj.birthday_date.year - extra_year
            else:
                obj.age = 0

    @api.onchange('contact_id')
    def _onchange_set_full_name(self):
        for obj in self:
            obj.full_name = obj.contact_id.name
            obj.name = obj.contact_id.name
            obj.phone = obj.contact_id.phone
            obj.email = obj.contact_id.email
            obj.gender = obj.contact_id.gender

