# -*- coding: utf-8 -*-
{
    "name": "Customer Overdue Statement",
    "summary": """
        Using this module You can send Customer Overdue Statement by email.
        """,
    "author": "DK Company",
    "category": "Uncategorized",
    "version": "15.0.0.1",
    "depends": ["base", "account", "sale_management"],
    "license": "LGPL-3",
    "data": [
        "security/ir.model.access.csv",
        "wizard/customer_overdue_statement_views.xml",
        "views/customer_overdue_statement_report.xml",
        "views/mail_overdue_template.xml",
    ],
    "installable": True,
}
