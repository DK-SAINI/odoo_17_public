# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_price_list_item_ids = fields.Many2many(
        'product.pricelist.item',
        string='Pricelist Prices',
        compute='_compute_pricelist_display',
        help='List of pricelists and their respective prices for this product.'
    )

    @api.depends('product_price_list_item_ids')
    def _compute_pricelist_display(self):
        PricelistItem = self.env['product.pricelist.item']
        for product in self:
            display_data = []
            for pricelist in self.env['product.pricelist'].search([('show_pricelist_prices', '=', True)]):
                # Check if a pricelist item already exists for this product and pricelist
                price_rule = PricelistItem.search([
                    ('pricelist_id', '=', pricelist.id),
                    ('product_tmpl_id', '=', product.id)
                ], limit=1)
                
                # If no price rule exists, create one
                if not price_rule:
                    price_rule = PricelistItem.create({
                        'pricelist_id': pricelist.id,
                        'product_tmpl_id': product.id,
                        'fixed_price': product.list_price,  # Defaulting to product list price
                    })
                
                # Add the pricelist item to the display data
                display_data.append(price_rule.id)
            
            # Assign computed pricelist items to the Many2many field
            product.product_price_list_item_ids = [(6, 0, display_data)]
