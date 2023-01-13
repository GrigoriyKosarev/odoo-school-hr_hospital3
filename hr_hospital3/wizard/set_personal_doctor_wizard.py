from odoo import fields, models, _

class SetPersonalDoctor(models.TransientModel):
    _name = 'set.personal.doctor.wizard'

    total_fees = fields.Float()

    # doctor_id = fields.Many2one(
    #     comodel_name='hs3.doctor', string='New value of personal doctor',
    # )
    # action_create
    def action_set_doctor(self):
        print("click action_set_doctor")
        return True

    # def action_open_wizard(self):
    #     return {
    #         'name': _('Create personal doctor wizard'),
    #         'type': 'ir.actions.act_window',
    #         'view_mode': 'form',
    #         'res_model': 'set.personal.doctor.wizard',
    #         'target': 'new',
    #         'context': {},
    #     }