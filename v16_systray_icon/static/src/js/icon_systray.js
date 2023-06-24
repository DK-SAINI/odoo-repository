/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

const { Component } = owl;
    
class SaleActionSystray extends Component {
    
    setup() {
        this.action = useService("action");
    }

    async openSaleOrders(ev) {

        this.action.doAction({
            type: 'ir.actions.act_window',
            name: this.env._t('Sale Order'),
            target: 'new',
            res_model: 'sale.order',
            views: [[false, 'form']],
        });
    }

    async onCloseClick() {
        await this.props.closeSaleOrders();
    }

}

SaleActionSystray.template = 'v16_systray_icon.SaleOrderSystray';

registry.category("systray").add("v16_systray_icon.SaleOrderSystray123", {
    Component: SaleActionSystray,}, { sequence: 110 }
);