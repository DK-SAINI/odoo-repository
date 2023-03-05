# -*- coding: utf-8 -*-
{
    'name': "excel_report",

    'summary': """
        This module is for create excel report for sale.
        """,

    'description': """
        excel Report
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Report',
    'version': '14.0',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management'],
    'installable': True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'wizard/sale_wizard_view.xml',
    ],
    # only loaded in demonstration mode

}
