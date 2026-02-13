from odoo import models,fields,api
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string="Name",required= True)
    property_type_id= fields.Many2one(
        "estate.property.type",
        string="Property Type"
    )
    buyer_id = fields.Many2one(
        "res.partner",
        string="Buyer"
    )
    seller_id = fields.Many2one(
        "res.partner",
        string="Seller"
    )
    offer_ids=fields.One2many(
        "estate.property.offer",
        "property_id",
        string="Offers"
    )
    tag_ids = fields.Many2many(
        "estate.property.tag",
        string="Tags"
    )
    description = fields.Text(string="Description")
    postcode = fields.Char(string = "Postcode")
    
    expected_price = fields.Float(string="Expected Price")
    selling_price = fields.Float(string="Selling Price")

    date_availability = fields.Date(
        string="Available Form",
        default = lambda self:fields.Date.today()
    )

    bedrooms = fields.Integer(string="Bedrooms" , default=2)
    living_area = fields.Integer(string = "Living Area")
    facades = fields.Integer(string="Facades")

    garage = fields.Boolean(string = "Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string ="Garden Area")

    garden_orientation = fields.Selection(
        [
            ('north','North'),
            ('south','South'),
            ('east','East'),
            ('west','West'),
        ],
        string="Garden Orientation"
    )
    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10 
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0 
            self.garden_orientation = False 



    total_area=fields.Float(string="Total Area",compute="_compute_total_area")

    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for records in self:
            records.total_area = records.living_area+records.garden_area

    active = fields.Boolean(string="Active",default = True)  

    state = fields.Selection(
        [
            ('new','New'),
            ('offer_received','Offer Received'),
            ('offer_accepted','Offer Accepted'),
            ('sold','Sold'),
            ('cancelled','Cancelled')
        ],
        string="Status",
        required = False ,
        copy = False,
        default = 'new'
    )  