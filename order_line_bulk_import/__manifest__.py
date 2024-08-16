# -*- coding: utf-8 -*-
{
    "name": "Order Line Bulk Import",
    "description": """
        Quotation Order Lines Bulk Import From Wizard
    """,
    "author": "Dk Company",
    "website": "https://www.yourcompany.com",
    "category": "sale",
    "version": "17.0.0.1",
    "depends": ["base", "sale_management"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/sale_wizard_views.xml",
        "views/sale_order.xml",
        "views/res_config_settings_views.xml",
        "data/email_template_data.xml",
        "data/scheduled_action_data.xml",
    ],
    "installable": True,
    "application": False,
}
