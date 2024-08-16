from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    has_duplicate_products = fields.Boolean(
        string="Has Duplicate Products",
        compute="_compute_has_duplicate_products",
        store=True,
    )
    merged_data = fields.Text(string="Merged Data")

    @api.depends("order_line.product_id")
    def _compute_has_duplicate_products(self):
        line = []
        for order in self:
            products = order.order_line.mapped("product_id")
            order.has_duplicate_products = len(order.order_line) != len((products))

    def action_merge_lines(self):
        for order in self:
            lines_to_merge = {}
            merged_products = (
                []
            )  # To keep track of merged products and their quantities

            for line in order.order_line:
                if line.product_id in lines_to_merge:
                    merged_line = lines_to_merge[line.product_id]
                    merged_line.product_uom_qty += line.product_uom_qty

                    # Keep track of merged product and quantity
                    merged_products.append(
                        {
                            "product_name": line.product_id.name,
                            "merged_qty": merged_line.product_uom_qty,
                        }
                    )
                    line.unlink()
                else:
                    lines_to_merge[line.product_id] = line

            order.merged_data = str(merged_products)
            # Log the note after merging lines
            if merged_products:
                note_body = "Quotation Merge:\n"
                for product in merged_products:
                    note_body += f"- {product['product_name']} with merged Qty: {product['merged_qty']}\n"

                order.message_post(
                    body=note_body, message_type="comment", subtype_xmlid="mail.mt_note"
                )

    @api.model
    def _send_quotation_merge_email(self):
        template = self.env.ref("order_line_bulk_import.quotation_merge_email_template")
        orders = self.search([('state', '=', 'draft')])
        for order in orders:
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&", order.merged_data)
            if order.merged_data:
                print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&", order.merged_data)
                email_values = {
                    "email_to": order.partner_id.email,
                    "email_cc": order.user_id.email,
                }
                template.send_mail(order.id, email_values=email_values, force_send=True)
