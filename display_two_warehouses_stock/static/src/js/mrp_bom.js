/** @odoo-module **/

import { useState } from "@odoo/owl";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { BomOverviewLine } from "@mrp/components/bom_overview_line/mrp_bom_overview_line";

patch(BomOverviewLine.prototype, {
    /**
     * @override
     */

    async setup() {
        super.setup(...arguments);
        this.orm = useService("orm");
        this.state = useState({ wh2QtyTotal: 0 });
        const wh2QtyTotal = await this.calculateWh2QtyTotal();
        this.state.wh2QtyTotal = wh2QtyTotal;
    },

    async calculateWh2QtyTotal() {
        const result = await this.orm.call(
            'product.template',
            'calculate_wh2_qty_total',
            [false, this.props.data.product_id],
        );
        return result;
    }
    
});