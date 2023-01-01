odoo.define('odoo_custom_dashboard.dashboard', function (require) {
"use strict";

    var AbstractAction = require('web.AbstractAction');
    var ajax = require('web.ajax');
    var core = require('web.core');
    var rpc = require('web.rpc');
    var session = require('web.session');
    var web_client = require('web.web_client');
    var _t = core._t;
    var QWeb = core.qweb;

    var Custom_Dashboard = AbstractAction.extend({
        template: 'OdooCustomDashboard',
        events: {
            // 'click #jumb_on_sale_order_page':'onclick_sale_order',
            // 'click #jumb_on_sale_order_pivot_view': 'onclick_sale_pivot_view',
            // 'click #sale_order': 'get_top_ten_sale_order',
            'click #sale_total_options': 'get_sale_totals',
            'click #amount_due_options': 'get_amount_due',
            'click #amount_deposit_options': 'get_amount_deposit'
        },

        init: function(parent, context){
            this._super(parent, context);
            this.total_order = [];
            this.total_amount = [];
            this.total_customer = [];
            this.total_product = [];
        },

        willStart: function() {
            var self = this;
            return $.when(ajax.loadLibs(this), this._super()).then(function() {
               return self.fetch_data();
            });
        },

        fetch_data: function(){
            var self = this;
            var def1 = this._rpc({
                model:'sale.order',
                method:'get_order_total_amount'
            }).then(function(result){
                self.total_order = result['total_order']
                self.total_amount = result['total_amount']
                self.total_customer = result['total_customer']
                self.total_product = result['total_product']
            });
            return def1
        },

        start: function() {
            var self = this;
            // this.set("title", 'Dashboard11');
            return this._super().then(function(){
                self.get_top_ten_customer();
                self.get_top_ten_product();
                // self.get_top_ten_sale_order();
                self.get_sale_totals();
                self.get_amount_due();
                self.get_amount_deposit();
            });

        },

        // Show Top 10 Customer In Doughnut Graph
        get_top_ten_customer: function(){
            var self = this;
            var ctx = self.$(".canvas_1");
            // var barColors = ["red", "orange","blue","green","brown", "yellow", "Purple", "pink", "cyan", "gray"];
            var barColors = [
              "#b91d47",
              "#00aba9",
              "#2b5797",
              "#e8c3b9",
              "#1e7145",
              "#FF7F50",
              "#CCCCFF",
              "#9FE2BF",
              "#40E0D0",
              "#DFFF00"
            ];
            var borderColor = [
              "#b91d47",
              "#00aba9",
              "#2b5797",
              "#e8c3b9",
              "#1e7145",
              "#FF7F50",
              "#CCCCFF",
              "#9FE2BF",
              "#40E0D0",
              "#DFFF00"
            ];

            rpc.query({
                model: 'sale.order',
                method: 'get_top_ten_customer'
            }).then(function(result){

                var data = {
                    labels: result[1],
                    datasets:[{
                        data: result[0],
                        backgroundColor: barColors,
                        borderColor:borderColor,
                    }],

                };

               var options = {
                    legend: {
                        position: 'left'
                    },
                    title:{
                        display: true,
                        fullSize: true,
                        text: "TOP 10 CUSTOMERS",
                        align: 'end',
                        position:'bottom'
                    },
                    cutoutPercentage: 55,
                    fontStyle: 'em Verdana',
                };

                var chart = new Chart(ctx, {
                    // chart type you can add like bar, pie, doughnut, line, polarArea etc
                    type: "doughnut",
                    data: data,
                    options: options
                });
            });
        },
        // Doughnut Graph End

        // Show Top 10 Selling Product In Bar Graph
        get_top_ten_product: function(){
            var self = this;
            var ctx = self.$(".canvas_2");
            var barColors = [
              "#b91d47",
              "#00aba9",
              "#2b5797",
              "#e8c3b9",
              "#1e7145",
              "#FF7F50",
              "#CCCCFF",
              "#9FE2BF",
              "#40E0D0",
              "#DFFF00"
            ];
            rpc.query({
                model: 'sale.order',
                method: 'get_top_ten_product'
            }).then(function(result){

                var data = {
                    labels: result[1],

                    datasets:[{
                        // type: 'bar',
                        // label: 'Bar Dataset',
                        backgroundColor: barColors,
                        data: result[0],
                    },
                    // {
                    //     type: 'line',
                    //     label: 'Line Dataset',
                    //     backgroundColor: barColors,
                    //     data: result[0],
                    // }
                    ],
                };

               var options = {
                    legend: {display: false},
                    title:{
                        display: true,
                        fullSize: true,
                        text: "TOP 10 SELLING PRODUCTS",
                        align: 'end',
                        position:'bottom',
                    },
                    scales: {
                      xAxes: [{ticks: {min: 0}}],
                    }
                };

                var chart = new Chart(ctx, {
                    // chart type you can add like bar, pie, doughnut etc
                    type: "horizontalBar",
                    data: data,
                    options: options
                });

            });
        },
        // Bar Graph End

        // Redirect On Sale Order
        // onclick_sale_order:function(e){
        //     var self = this;
        //     e.stopPropagation();
        //     e.preventDefault();

        //     var options = {
        //         on_reverse_breadcrumb: self.on_reverse_breadcrumb,
        //     };
        //     self.do_action({
        //         name: _t("Sale Order"),
        //         type: 'ir.actions.act_window',
        //         res_model: 'sale.order',
        //         view_mode: 'tree,form,calendar',
        //         view_type: 'form',
        //         views: [[false, 'list'],[false, 'form']],
        //         domain: [['state','=', 'sale']],
        //         target: 'current'
        //     }, options)
        // },
        // Sale View End

        // Redirect On Sale Pivot View
        // onclick_sale_pivot_view:function(e){
        //     var self = this;
        //     e.stopPropagation();
        //     e.preventDefault();
        //     var options = {
        //         on_reverse_breadcrumb: self.on_reverse_breadcrumb,
        //     };

        //     self.do_action({
        //         name: _t("Sale Pivot View"),
        //         type: 'ir.actions.act_window',
        //         res_model: 'sale.order',
        //         view_mode: 'pivot',
        //         view_type: 'pivot',
        //         views: [[false, 'pivot']],
        //         domain: [['state','=', 'sale']],
        //         target: 'current'
        //     }, options)
        // },
        // Pivot View End

        // Get Top 10 Sale Order And Set In Table

        // get_top_ten_sale_order:function(events){
        //     var self = this;
        //     var options = $('#sale_order').val();
        //     rpc.query({
        //         model: 'sale.order',
        //         method: 'get_top_ten_sale_order',
        //         args:[options],
        //         domain: [['state', '=', 'sale']],
        //     }).then(function(result){
        //         $('#sale_data td').remove();
        //         var name = result.order;
        //         var amount = result.amount;
        //         var j = 0;
        //         var k = 1;
        //         $.each(result.amount, function(key, value) {
        //             $('#sale_data').append('<tr><td>'+k+'</td><td>'+name[j]+'</td><td>'+value+'</td></tr>')
        //             j++;
        //             k++;
        //         });

        //     });

        // },

        // get sales Total Weekly, montly, yearly
        get_sale_totals:function(events){
            var self = this;

            // get options like [this_week, this_month, this_year]
            var options = $('#sale_total_options').val();

            rpc.query({
                model: 'sale.order',
                method: 'get_sales_total',
                args:[options],
                domain: [['state', '=', 'sale']],
            }).then(function(result){
                $('#total_sales').empty();
                $('#total_sales').append('<b>'+result.toFixed(2)+'</b>');
            });
        },

        // get Invoice Due Amount for this_Week, this_month, this_year
        get_amount_due:function(events){
            var self = this;

            // get options like [due_this_week, due_this_month, due_this_year]
            var options = $('#amount_due_options').val();

            rpc.query({
                model: 'account.move',
                method: 'get_invoice_due_amount',
                args:[options],
                domain: [['move_type', '=', 'out_invoice']],
            }).then(function(result){
                // append result
                $('#due_amount').empty();
                $('#due_amount').append('<b>'+result.toFixed(2)+'</b>');
            });
        },

        // get Invoice Due Amount for this_Week, this_month, this_year
        get_amount_deposit:function(events){
            var self = this;

            // get options like [deposit_this_week, deposit_this_month, deposit_this_year]
            var options = $('#amount_deposit_options').val();

            rpc.query({
                model: 'account.payment',
                method: 'get_deposit_amount',
                args:[options],
            }).then(function(result){
                // append result
                $('#deposit_amount').empty();
                $('#deposit_amount').append('<b>'+result.toFixed(2)+'</b>');
            });
        },

    });

    core.action_registry.add('odoo_custom_dashboard', Custom_Dashboard);

    return Custom_Dashboard;

// end file
});
