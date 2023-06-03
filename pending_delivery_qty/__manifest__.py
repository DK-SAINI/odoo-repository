# -*- coding: utf-8 -*-
{
    "name": "Pending Quantity Calculation",
    "version": "15.0.0.1",
    "summary": "Calculates pending quantity in sale order line",
    "description": "This module adds a pending_qty field to sale order line and calculates it from the delivery order.",
    "category": "Sales",
    "author": "Your Name",
    "depends": ["sale_management", "stock"],
    "data": [
        "views/sale_order_views.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
    "application": False,
    "auto_install": False,
}
