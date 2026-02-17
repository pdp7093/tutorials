from odoo import models,fields
from odoo.exceptions import UserError 
from odoo import api

class EstateProperty(models.Model):
    _inherit = 'estate.property'


    @api.ondelete(at_uninstall = False)
    def _check_state_before_delete(self):
        for record in self:
            if record.state not in ['new','canceled']:
                raise UserError("Cannot delete this property.")