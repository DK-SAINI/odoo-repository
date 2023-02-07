# -*- coding: utf-8 -*-
{
    "name": "odoo_custom_dashboard",
    "description": """
        Custome Dashboard
    """,
    "author": "DK-SAINI",
    "website": "http://www.yourcompany.com",
    "category": "Dashboard",
    "version": "15.0.0.1",
    "depends": ["base", "sale_management", "account", "stock"],
    # always loaded
    "data": [
        "views/dashboard_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "odoo_custom_dashboard/static/src/js/dashboard.js",
            "odoo_custom_dashboard/static/src/css/dashboard.css",
            "https://cdnjs.cloudflare.com/ajax/libs/simple-line-icons/2.5.5/css/simple-line-icons.min.css",
            "https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.bundle.js"
            # no need this link
            # "https://pixinvent.com/stack-responsive-bootstrap-4-admin-template/app-assets/fonts/simple-line-icons/style.min.css",
        ],
        "web.assets_qweb": [
            "odoo_custom_dashboard/static/src/xml/dashboard_template.xml",
            "GGGG"
        ],
    },
    "license": "LGPL-3",
    "installable": True,
    "application": True,
    "auto_install": False,
}
