# -*- coding: utf-8 -*-
{
    "name": "Check Partner Trust",
    "author": "DK Company",
    "website": "http://www.dk.com",
    "version": "15.0.0.1",
    "depends": ["base", "sale_management"],
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/res_partner_views.xml",
        "wizard/sale_order_wizard_views.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
    "application": False,
    "auto_install": False,
}
