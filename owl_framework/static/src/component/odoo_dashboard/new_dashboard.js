/** @odoo-module **/

import { Component, useState} from "@odoo/owl";
import { OverviewComponent } from "./overview_component";
import { SalesComponent } from "./sales";
import { registry } from "@web/core/registry";

export class RootDashboard extends Component {
    setup() {
        
        this.state = useState({
            activeTab: 'overview',
        });

        this.setActiveTab = this.setActiveTab.bind(this);
    }

    setActiveTab(tab) {
        this.state.activeTab = tab;
    }

}

RootDashboard.components = {
    OverviewComponent,
    SalesComponent,
};
RootDashboard.template = "owl_framework.NewDashboard";
registry.category("actions").add("odoo_dashboard.new_dashboard", RootDashboard);