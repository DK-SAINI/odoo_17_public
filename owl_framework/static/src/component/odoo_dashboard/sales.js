/** @odoo-module **/

import { Component, useState, onWillStart } from "@odoo/owl";

export class SalesComponent extends Component {
    setup() {
        this.state = useState({
            quotationCount: 0,
            saleOrderCount: 0,
            topCustomers: [],
            topSaleOrders: [],
        });

        onWillStart(async () => {
            await this.fetchSalesData();
        });
    }

    async fetchSalesData() {
        try {
            const result = await this.env.services.rpc({
                model: 'sale.order',
                method: 'get_sales_dashboard_data',
                args: [],
            });
            
            this.state.quotationCount = result.quotation_count;
            this.state.saleOrderCount = result.sale_order_count;
            this.state.topCustomers = result.top_customers;
            this.state.topSaleOrders = result.top_sale_orders;
            this.state.error = null;
        } catch (error) {
            console.error('Error fetching sales data:', error);
            this.state.error = "Failed to fetch sales data. Please try again later.";
        }
    }
}

SalesComponent.template = "owl_framework.SalesComponent";