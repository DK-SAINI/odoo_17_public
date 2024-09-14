/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { Counter } from "./inline_template";

class Card extends Component {
    static template = 'owl_framework.Card';
    static components = { Counter };
    
    setup() {
        this.state = useState({ showContent: true });
    }

    toggleDisplay() {
        this.state.showContent = !this.state.showContent;
    }
}

class Root extends Component {
    static template = "owl_framework.Root1"
    static components = { Card, Counter };
    

    // setup() {
    //   this.state = useState({a: 1, b: 3});
    // }
  
    // inc(key, delta) {
    //   this.state[key] += delta;
    // }
}

registry.category("actions").add("owl_framework.card", Root);