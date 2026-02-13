from odoo import models, fields 

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offer"

    price = fields.Float(string="Offer Price",required=True)

    partner_id = fields.Many2one("res.partner",string="Customer",required=True)

    property_id = fields.Many2one("estate.property",string="Property",required=True,ondelete="cascade")