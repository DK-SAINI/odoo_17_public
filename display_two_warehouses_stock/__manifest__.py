# -*- coding: utf-8 -*-
{
    "name": "display_two_warehouses_stock",
    "summary": "Show Product Qty of second warehouse for product",
    "author": "My Company",
    "website": "https://www.yourcompany.com",
    "version": "17.0.0.1",
    "depends": ["base", "stock", "mrp"],
    "data": [
        "views/product_views.xml",
        "views/stock_orderpoint_views.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'display_two_warehouses_stock/static/src/**/*',
        ],
    },
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": True,
}
