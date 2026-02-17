from odoo import models
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _inherit = "estate.property.offer"

    def create(self,vals_list):

        for vals in vals_list:
            property_id = vals.get('property_id')
            price = vals.get('price')

            if property_id and price:
                property_record = self.env['estate.property'].browse(property_id)

            #find highest existing offer 
            existing_offers = property_record.offer_ids 
            if existing_offers:
                max_price = max(existing_offers.mapped('price'))
                if price <=max_price:
                    raise UserError("You cannot create an offer lower than an existing offer.")
            offer = super().create(vals)

        if offer.property_id:
            offer.property_id.state = 'offer_received'

        return offer 
    