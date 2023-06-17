# -*- coding: utf-8 -*-

import base64
from odoo import models


class CustomerOverdueStatementWizard(models.TransientModel):
    _name = "customer.overdue.statement.wizard"
    _description = "Customer Overdue Statement Wizard"

    def generate_overdue_statement(self):
        # get selected customer ids
        partner = self._context.get("active_ids")

        # get mail template
        template_id = self.env.ref(
            "customer_overdue_statement.mail_template_overdue_payment"
        )

        for partner_id in partner:
            partner = self.env["res.partner"].search([("id", "=", partner_id)])
            account_obj = self.env["account.move"].search(
                [
                    ("partner_id", "=", partner_id),
                    ("amount_residual_signed", ">", 0),
                    ("move_type", "=", "out_invoice"),
                ]
            )

            data = {"account_obj": account_obj}

            if account_obj:
                report = self.env.ref(
                    "customer_overdue_statement.report_customer_overdue_statement_action"
                )._render_qweb_pdf(self.id)[0]

                print("@@@@@@@@@@@@@@@@@@@@", report)
                # attachment_data = {
                #     "name": "Report Name.pdf",
                #     "type": "binary",
                #     "datas": base64.b64encode(report),
                # }

                # template_id.with_context(data).send_mail(
                #     partner.id, attachment_ids=[(0, 0, attachment_data)]
                # )

        # template_id.send_mail(self.partner_id.id, force_send=True, attachment_ids=self.attachment_ids.ids)
