/** @odoo-module **/
import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";

// In this example, we show how components can be defined and created.

class Greeter extends Component {
    static template = "owl_framework.Greeter";
    
    setup() {
        this.state = useState({ word: 'Hello' });
    }

    toggle() {
        this.state.word = this.state.word === 'Hi' ? 'Hello' : 'Hi';
    }
}

// Main root component
class Root extends Component {
    static components = { Greeter };

    setup() {
        this.state = useState({ name: 'World'});
    }
}

Root.template = "owl_framework.Root";
registry.category("actions").add("owl_framework.root_playground", Root);
// mount(Root, document.body, { templates: TEMPLATES, dev: true });
