# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class QuotationBulkUpload(models.TransientModel):
    _name = "quotation.bulk.upload"
    _description = "Bulk Upload"

    line_ids = fields.One2many(
        "quotation.bulk.upload.line", "bulk_upload_id", string="Lines"
    )

    def action_bulk_upload(self):
        self.ensure_one()
        sale_order_id = self.env.context.get("active_id")
        sale_order = self.env["sale.order"].browse(sale_order_id)
        order_lines = []

        for line in self.line_ids:
            for product in line.product_ids:
                # Create order line for each product with specified quantity
                order_lines.append(
                    (
                        0,
                        0,
                        {
                            "product_id": product.id,
                            "product_uom_qty": line.quantity,
                        },
                    )
                )

        sale_order.write({"order_line": order_lines})




class QuotationBulkUploadLine(models.TransientModel):
    _name = "quotation.bulk.upload.line"
    _description = "Quotation Bulk Upload Line"

    bulk_upload_id = fields.Many2one(
        "quotation.bulk.upload",
        string="Wizard",
        required=True,
        ondelete="cascade",
    )
    product_ids = fields.Many2many(
        "product.product", string="Products", required=True
    )
    quantity = fields.Float(string="Quantity", default=1.0, required=True)

    @api.constrains("quantity")
    def _check_quantity(self):
        for record in self:
            if record.quantity <= 0:
                raise ValidationError(
                    "Quantity must be greater than zero."
                )
