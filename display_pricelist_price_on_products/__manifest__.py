# -*- coding: utf-8 -*-
{
    'name': 'Display Pricelist Price on Products',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Display product price according to different pricelists on the product form.',
    'description': 'Allows displaying and hiding product prices based on pricelists in the product form view.',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['base', 'product', 'sale_management'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/product_pricelist_views.xml'
    ],
    'installable': True,
    'application': False,
}