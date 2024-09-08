/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class Counter extends Component {
	setup(){

		this.state = useState({
			value: 0,
		})
	}

	increment(){
		this.state.value++;
	}

	decrement(){
		this.state.value--;
	}
}
Counter.template = "owl_framework.Counter";
registry.category("actions").add("owl_framework.counter", Counter);