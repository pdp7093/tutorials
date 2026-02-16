{
    "name":"Real Estate",
    "depends":["base"],
    "data" : [
        'security/ir.model.access.csv',
        'views/estate_menu.xml',
        'views/estate_property_views.xml',
        'views/property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offers_views.xml',
    ],
    "application":True,
    "installable":True,
}