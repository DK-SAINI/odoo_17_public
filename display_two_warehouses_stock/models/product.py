# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    second_warehouse_id = fields.Many2one(
        "stock.warehouse",
        string="Stock In WH2",
    )

    def calculate_wh2_qty_total(self, product_id):
        product = self.env['product.product'].browse(product_id)
        
        if not product.second_warehouse_id:
            return 0
        quants = self.env["stock.quant"].search([
            ("product_id", "=", product.id),
            ("location_id", "=", product.second_warehouse_id.lot_stock_id.id),
        ])

        qty_count = sum(quant.quantity for quant in quants)
        return qty_count
