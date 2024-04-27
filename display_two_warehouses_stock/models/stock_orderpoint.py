# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockWarehouseOrderpoint(models.Model):
    _inherit = "stock.warehouse.orderpoint"

    qty_on_hand_second_wh = fields.Float(
        "Stock In WH2",
        readonly=True,
        compute="_compute_warehouse_qty_count",
        digits="Product Unit of Measure",
    )

    def _compute_warehouse_qty_count(self):
        for orderpoint in self:
            wh2_location_id = orderpoint.product_id.second_warehouse_id
            
            if not orderpoint.product_id.second_warehouse_id:
                orderpoint.qty_on_hand_second_wh = 0.0
                continue

            quants = self.env["stock.quant"].search(
                [
                    ("product_id", "=", orderpoint.product_id.id),
                    ("location_id", "=", wh2_location_id.lot_stock_id.id),
                ]
            )
            # Sum up the quantities of filtered stock quants
            qty_count = sum(quant.quantity for quant in quants)
            # Update the computed field value
            orderpoint.qty_on_hand_second_wh = qty_count
