/** @odoo-module **/

import { Component, useState, xml } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class Counter extends Component {
    static template = xml`<button t-on-click="() => state.count++"> Click! [<t t-esc="state.count"/>] </button>`;
    
    setup() {
        this.state = useState({ count: 0 });
    }
    
}

class Root extends Component {
    static template = xml`
    <div>
        <Counter/>
        <Counter/>
    </div>`;
  
    static components = { Counter };
}

registry.category("actions").add("owl_framework.inline_template", Root);