# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductPricelist(models.Model):
    _inherit = "product.pricelist"

    show_pricelist_prices = fields.Boolean(
        string="Show Pricelist Prices",
        help="Toggle to display pricelist name and price rule on the product form.",
    )
