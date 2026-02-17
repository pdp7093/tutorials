from odoo import models, fields


class ResUsers(models.Model):
    _inherit = "res.partner"

    property_ids = fields.One2many(
        "estate.property",
        "seller_id",
        string="Properties",
        domain = [('state','not in',['sold','canceled'])]
    )