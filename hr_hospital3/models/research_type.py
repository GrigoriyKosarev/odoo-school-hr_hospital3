from odoo import models, fields, _, api
from odoo.exceptions import UserError, ValidationError

class ResearchType(models.Model):
    _name = 'hs3.research.type'
    _description = 'Research type'
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char('Name', index=True, required=True)
    parent_id = fields.Many2one(comodel_name='hs3.research.type', string='Parent research', index=True,
                                ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many(comodel_name='hs3.research.type', inverse_name='parent_id', string='Child Categories')

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive categories.'))

    @api.model
    def name_create(self, name):
        return self.create({'name': name}).name_get()[0]


