from odoo import models, fields, api 
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offer"

    price = fields.Float(string="Offer Price",required=True)

    partner_id = fields.Many2one("res.partner",string="Customer",required=True)

    property_id = fields.Many2one("estate.property",string="Property",required=True,ondelete="cascade")

    validity = fields.Integer(string="Validity (days)", default = 7)
    date_deadline = fields.Date(
        string="Deadline",compute="_compute_date_deadline",
        inverse="_inverse_date_deadline",store=True
    )

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date.date()+ relativedelta(days=record.validity)
            else:
                record.date_deadline = False 

    def _inverse_date_deadline(self):
        for record in self:
            if record.create_date and record.date_deadline:
                delta = record.date_deadline - record.create_date.date()
                record.validity = delta.days 


    status = fields.Selection(
        [
            ('accepted','Accepted'),
            ('refused','Refused'),
        ],
        string="Status",
        copy=False
    )
    def action_accept(self):
        for record in self:
            if record.property_id.state == "sold":
                raise UserError("Cannot accept offer on sold property.")
            
            #Update property 
            record.property_id.write({
                'state':'offer_accepted',
                'selling_price':record.price,
                'buyer_id' : record.partner_id.id
            })

            #Refuse other offers 
            other_offers = record.property_id.offer_ids - record
 
            other_offers.write({'status':'refused'})

            record.status = 'accepted'

    def action_refuse(self):
        for record in self:
            record.status = 'refused'