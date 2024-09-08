/** @odoo-module **/

import { Component, useState, onWillStart, useRef, onMounted } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { loadBundle } from "@web/core/assets";

export class Dashboard extends Component {
	setup() {
		this.state = useState({
			darkMode: false,
			chart: null
		});

		this.chartRef = useRef("chart");

		onWillStart(async () => {
			console.log("Loading Chart.js bundle...");
			await loadBundle("web.chartjs_lib");
			console.log("Chart.js bundle loaded.");
		});

		onMounted(async () => {
			console.log("Component mounted. Initializing chart...");
			await this.initChart();
		});

		console.log("Dashboard Loading...!");
	}

	async initChart() {
		console.log("Initializing chart...");
		console.log("Chart ref:", this.chartRef);
		if (this.chartRef.el) {
			console.log("Canvas element found.");
			const ctx = this.chartRef.el.getContext('2d');
			
			// Ensure Chart is available
			if (typeof Chart === 'undefined') {
				console.log("Chart is not defined. Waiting for it to load...");
				await new Promise(resolve => setTimeout(resolve, 1000)); // Wait for 1 second
				if (typeof Chart === 'undefined') {
					console.error("Chart is still not defined after waiting. Make sure Chart.js is loaded.");
					return;
				}
			}

			try {
				this.state.chart = new Chart(ctx, {
					type: 'bar',
					data: {
						labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
						datasets: [{
							label: '# of Votes',
							data: [12, 19, 3, 5, 2, 3],
							backgroundColor: [
								'rgba(255, 99, 132, 0.2)',
								'rgba(54, 162, 235, 0.2)',
								'rgba(255, 206, 86, 0.2)',
								'rgba(75, 192, 192, 0.2)',
								'rgba(153, 102, 255, 0.2)',
								'rgba(255, 159, 64, 0.2)'
							],
							borderColor: [
								'rgba(255, 99, 132, 1)',
								'rgba(54, 162, 235, 1)',
								'rgba(255, 206, 86, 1)',
								'rgba(75, 192, 192, 1)',
								'rgba(153, 102, 255, 1)',
								'rgba(255, 159, 64, 1)'
							],
							borderWidth: 1
						}]
					},
					options: {
						scales: {
							y: {
								beginAtZero: true
							}
						}
					}
				});
				console.log("Chart initialized:", this.state.chart);
				this.updateChartTheme();
			} catch (error) {
				console.error("Error initializing chart:", error);
			}
		} else {
			console.error("Canvas element not found.");
		}
	}

	toggleDarkMode() {
		this.state.darkMode = !this.state.darkMode;
		// if (this.state.chart) {
		// 	this.updateChartTheme();
		// }
	}

	updateChartTheme() {
		const textColor = this.state.darkMode ? 'white' : 'black';
		this.state.chart.options.plugins.legend.labels.color = textColor;
		this.state.chart.options.scales.x.ticks.color = textColor;
		this.state.chart.options.scales.y.ticks.color = textColor;
		this.state.chart.update();
	}
}

Dashboard.template = "owl_framework.dashboard";
registry.category("actions").add("owl_framework.dashboard", Dashboard);