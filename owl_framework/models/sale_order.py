# In your sale_order.py or a new file like sales_dashboard.py
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def get_sales_dashboard_data(self):
        # Get quotation count
        quotation_count = self.search_count([('state', 'in', ['draft', 'sent'])])

        # Get sale order count
        sale_order_count = self.search_count([('state', 'not in', ['draft', 'sent', 'cancel'])])

        # Get top 10 customers
        top_customers = self.read_group(
            [('state', 'not in', ['draft', 'sent', 'cancel'])],
            ['partner_id', 'amount_total:sum'],
            ['partner_id'],
            limit=10,
            orderby='amount_total desc'
        )
        print("=========___________==================>", top_customers)
        top_customers = [{'id': c['partner_id'][0], 'name': c['partner_id'][1], 'total_sales': c['amount_total']} for c in top_customers]

        # Get top 10 sale orders
        top_sale_orders = self.search_read(
            [('state', 'not in', ['draft', 'sent', 'cancel'])],
            ['name', 'partner_id', 'amount_total'],
            limit=10,
            order='amount_total desc'
        )

        return {
            'quotation_count': quotation_count,
            'sale_order_count': sale_order_count,
            'top_customers': top_customers,
            'top_sale_orders': top_sale_orders,
        }