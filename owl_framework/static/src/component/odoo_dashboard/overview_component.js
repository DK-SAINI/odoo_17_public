/* @odoo-module */

import { Component, useState, onWillStart, useRef, onMounted } from "@odoo/owl";
import { loadBundle } from "@web/core/assets";

export class OverviewComponent extends Component {
    setup() {
        this.state = useState({
            charts: {},
        });

        this.chartRefs = {
            resultChart: useRef("resultChart"),
            progressChart: useRef("progressChart"),
            areaChart: useRef("areaChart"),
        };

        onWillStart(async () => {
            await loadBundle("web.chartjs_lib");
        });

        onMounted(() => {
            this.initCharts();
        });
        // this.initCharts = this.initCharts.bind(this);
    }

    initCharts() {
        this.initResultChart();
        this.initProgressChart();
        this.initAreaChart();
    }

    initResultChart() {
        const ctx = this.chartRefs.resultChart.el.getContext('2d');
        this.state.charts.resultChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
                datasets: [{
                    label: '2019',
                    data: [20, 35, 15, 30, 25, 20, 35, 20, 30],
                    backgroundColor: '#FFA500',
                }, {
                    label: '2020',
                    data: [35, 45, 30, 15, 35, 45, 10, 20, 15],
                    backgroundColor: '#000080',
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 50,
                    }
                }
            }
        });
    }

    initProgressChart() {
        const ctx = this.chartRefs.progressChart.el.getContext('2d');
        this.state.charts.progressChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                datasets: [{
                    data: [45, 55],
                    backgroundColor: ['#000080', '#FFA500'],
                }]
            },
            options: {
                responsive: true,
                cutout: '80%',
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });
    }

    initAreaChart() {
        const ctx = this.chartRefs.areaChart.el.getContext('2d');
        this.state.charts.areaChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                datasets: [{
                    label: 'Lorem ipsum',
                    data: [30, 40, 25, 50, 30, 60, 40],
                    fill: true,
                    backgroundColor: 'rgba(255, 165, 0, 0.2)',
                    borderColor: '#FFA500',
                }, {
                    label: 'Dolor Amet',
                    data: [50, 30, 45, 35, 55, 40, 70],
                    fill: true,
                    backgroundColor: 'rgba(0, 0, 128, 0.2)',
                    borderColor: '#000080',
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
}

OverviewComponent.template = "owl_framework.OverviewComponent";