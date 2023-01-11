from odoo import fields, models, _

class SetPersonalDoctor(models.TransientModel):
    _name = "set.personal.doctor.wizard"
    _description = "Set personal doctor wizard"

    doctor_id = fields.Many2one(
        comodel_name='hs3.doctor', string='New value of personal doctor',
    )

    def action_open_wizard(self):
        return {
            'name': _('Create personal doctor wizard'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'set.personal.doctor.wizard',
            'target': 'new',
            'context': {},
        }