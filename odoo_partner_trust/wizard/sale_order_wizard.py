from odoo import models, fields, api


class SaleOrderWizard(models.TransientModel):
    _name = "sale.order.wizard"

    order_id = fields.Many2one("sale.order", string="Sale Order")
    partner_id = fields.Many2one(
        "res.partner", string="Customer", related="order_id.partner_id"
    )

    def approve_blacklisted_customer_order(self):
        # call the action_confirm method on the current sale order
        # include a context to prevent an infinite loop
        self.order_id.with_context(
            {"approve_blacklisted_customer_order": 1}
        ).action_confirm()
