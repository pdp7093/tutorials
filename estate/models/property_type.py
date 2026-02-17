from odoo import models, fields 


class EstatePropertyType(models.Model):
    _name="estate.property.type"
    _description = "Property Types"

    property_ids = fields.One2many(
        "estate.property",
        "property_type_id",
        string="Properties"
    )
    name=fields.Char(string="Name", required=True)

    _sql_constraints = [
        (
            'unique_property_type_name',
            'UNIQUE(name)',
            'Property type name must be unique.'
        )
    ]
