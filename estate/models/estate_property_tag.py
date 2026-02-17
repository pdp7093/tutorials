from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Property Tag"

    name = fields.Char(string="Tag Name", required=True)
    color = fields.Integer("Color")
    _sql_constraints = [
        ('unique_tag_name',
         'UNIQUE(name)',
         'Tag name must be unique.')
    ]

