# -*- coding: utf-8 -*-
{
    'name': "Hide sale price on website",
    "summary": "Hide product prices on the shop",
    'author': "DK-SAINI",
    'website': "http://www.yourcompany.com",
    "category": "Website",
    'version': '15.0.0.1',
    # any module necessary for this one to work correctly
    'depends': ['website_sale'],
    # always loaded
    'data': [
        'views/product_template_view.xml',
        "views/website_sale_template.xml",
    ],
    "installable": True,
}
