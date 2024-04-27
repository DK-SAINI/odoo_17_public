# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    total_pending_qty = fields.Float(
        string="Pending Quantities", compute="_compute_total_pending_qty"
    )

    def _compute_total_pending_qty(self):
        for order in self:
            if order.order_line:
                order.total_pending_qty = (
                    sum(order.order_line.mapped("pending_qty")) or 0
                )
            else:
                order.total_pending_qty = 0


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    pending_qty = fields.Float(
        string="Pending Quantity",
        compute="_compute_pending_qty",
        store=True,
    )

    @api.depends(
        "move_ids.state",
        "move_ids.product_uom_qty",
        "move_ids.product_uom",
    )
    def _compute_pending_qty(self):
        for line in self:
            if line.qty_delivered_method == "stock_move":
                delivery_orders = self.env["stock.picking"].search(
                    [
                        ("state", "=", "done"),
                        ("sale_id", "=", line.order_id.id),
                        ("picking_type_id.code", "=", "outgoing"),
                    ]
                )
                delivered_qty = sum(
                    delivery_orders.mapped(
                        lambda order: order.move_ids.filtered(
                            lambda move: move.product_id
                            == line.product_id
                        ).product_uom_qty
                    )
                )

                line.pending_qty = line.product_uom_qty - delivered_qty

                if line.pending_qty < 0:
                    raise ValidationError(
                        "You cannot validat record because you enter more then qty."
                    )
            else:
                line.pending_qty = line.product_uom_qty
