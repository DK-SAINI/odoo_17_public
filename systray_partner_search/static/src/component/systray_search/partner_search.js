/** @odoo-module **/

import { registry } from "@web/core/registry";
import { _t } from "@web/core/l10n/translation";
import { useService } from "@web/core/utils/hooks";
import { AutoComplete } from "@web/core/autocomplete/autocomplete";

import { Component, useState } from "@odoo/owl";

class PartnerSearch extends Component {
    static props = {};
    static components = { AutoComplete };

    setup() {
        this.orm = useService("orm");
        this.userService = useService('user');
        this.action = useService("action");
        
        this.state = useState({
            value: "",
            isHide: false,
        });

        this.userService
            .hasGroup("systray_partner_search.bista_advance_search")
            .then(isHide => {
                this.state.isHide = isHide;
            });
    }

    get placeholder() {
        return _t("Search partner here...");
    }

    onSelect(option) {
        const prototype = Object.getPrototypeOf(option);

        this.state.value = prototype.label;
        this.openPartnerPage(prototype.id)
    }

    get sources() {
        return [this.optionsSource];
    }

    get optionsSource() {
        return {
            placeholder: _t("Loading..."),
            options: this.loadOptionsSource.bind(this),
        };
    }

    async loadOptionsSource(query) {
        const options = await this.fetchPartners(query);
        if (!options.length) {
            return [
                {
                    label: _t("No records"),
                    unselectable: true,
                },
            ];
        }
        return options;
    }

    async fetchPartners(query) {
        const response = await this.orm.call("res.partner", "search_read", [], {
            fields: ['id', 'name'],
            domain: [['name', 'ilike', query]],
            limit: 10,
        });
        return response.map((record) => ({
            id: record.id,
            label: record.name,
        }));
    }

    openPartnerPage(partnerId) {
        // if (partnerId) {
        //     const url = `/web#id=${partnerId}&model=res.partner&view_type=form`;
        //     window.location.href = url;
        // }
        this.action.doAction(
            {
                type: "ir.actions.act_window",
                res_model: "res.partner",
                views: [[false, "form"]],
                view_mode: "form",
                res_id: partnerId,
                target: "new",
            },
        );
    }   
}

PartnerSearch.template = "systray_partner_search.PartnerSearch";

registry.category("systray").add(
    "partnerSearchComponent",
    {
        Component: PartnerSearch,
    },
    { sequence: 111 }
);
