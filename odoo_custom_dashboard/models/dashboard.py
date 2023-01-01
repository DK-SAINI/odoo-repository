# -*- coding: utf-8 -*-

from odoo import models, api
from datetime import date


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def get_order_total_amount(self):
        company_id = self.env.company.id
        sale_obj = self.env["sale.order"].search(
            [("company_id", "=", company_id)]
        )
        total_customer = self.env["res.partner"].search_count(
            [
                ("customer_rank", '>=', 0),
            ]
        )
        total_product = self.env["product.template"].search_count(
            [("type", "=", "product")]
        )
        total_order = sale_obj.filtered(lambda res: res.state == "sale")
        total_amount = sum(total_order.mapped("amount_total"))

        # numerize.numerize(total_amount), You Can replace 28 line with 25 line
        return {
            "total_order": len(total_order) or 0,
            "total_amount": "{:.2f}".format(total_amount) or 0.00,
            "total_customer": total_customer or 0,
            "total_product": total_product or 0,
        }

    @api.model
    def get_top_ten_customer(self):
        company_id = self.env.company.id
        query = (
            """select res_partner.name as customer, sale_order.partner_id, sum(sale_order.amount_total) as amount_total from sale_order inner join res_partner on res_partner.id = sale_order.partner_id where sale_order.company_id = """
            + str(company_id)
            + """ GROUP BY sale_order.partner_id,res_partner.name ORDER BY amount_total  DESC LIMIT 10;"""
        )

        self._cr.execute(query)
        docs = self._cr.dictfetchall()
        order = []
        for record in docs:
            order.append(record.get("amount_total"))
        day = []
        for record in docs:
            day.append(record.get("customer"))
        final = [order, day]
        return final

    @api.model
    def get_top_ten_product(self):
        company_id = self.env.company.id
        query = (
            """select DISTINCT(product_template.name) as product_name, sum(product_uom_qty) as total_qty from sale_order_line inner join product_product on product_product.id = sale_order_line.product_id inner join
       product_template on product_product.product_tmpl_id = product_template.id  where product_template.type = 'product' And sale_order_line.company_id = """
            + str(company_id)
            + """ group by product_template.id ORDER
       BY total_qty DESC Limit 10 """
        )

        self._cr.execute(query)
        top_product = self._cr.dictfetchall()

        qty = []
        name = []

        for res in top_product:
            qty.append(res.get("total_qty"))
            name.append(res.get("product_name"))
        return [qty, name]

    # @api.model
    # def get_top_ten_sale_order(self, options):
    #     # TO Do
    #     # Get Data Company Wise.
    #     company_id = self.env.company.id
    #     order = []
    #     amount = []
    #     if options == "monthly_sales":
    #         month = date.today().month
    #         query = (
    #             """select name, partner_id, amount_total FROM sale_order
    #             WHERE company_id = """
    #             + str(company_id)
    #             + """ and extract(month FROM date_order) ="""
    #             + str(month)
    #             + """ORDER BY amount_total DESC Limit 10"""
    #         )
    #         self._cr.execute(query)
    #         top_order = self._cr.dictfetchall()
    #         for res in top_order:
    #             order.append(res.get("name"))
    #             amount.append("{:.2f}".format(res.get("amount_total")))

    #     elif options == "year_sales":
    #         year = date.today().year
    #         query = (
    #             """select name, partner_id, amount_total FROM sale_order
    #             WHERE company_id = """
    #             + str(company_id)
    #             + """and extract(year FROM date_order) ="""
    #             + str(year)
    #             + """ORDER BY amount_total DESC Limit 10"""
    #         )
    #         self._cr.execute(query)
    #         top_order = self._cr.dictfetchall()
    #         for res in top_order:
    #             order.append(res.get("name"))
    #             amount.append("{:.2f}".format(res.get("amount_total")))

    #     else:
    #         day = date.today().day
    #         query = (
    #             """select name, partner_id, amount_total FROM sale_order
    #             WHERE company_id = """
    #             + str(company_id)
    #             + """and extract(day FROM date_order) ="""
    #             + str(day)
    #             + """ORDER BY amount_total DESC Limit 10"""
    #         )

    #         self._cr.execute(query)
    #         top_order = self._cr.dictfetchall()
    #         for res in top_order:
    #             order.append(res.get("name"))
    #             amount.append("{:.2f}".format(res.get("amount_total")))

    #     return {"order": order, "amount": amount}

    @api.model
    def get_sales_total(self, options):
        company_id = self.env.company.id
        year = date.today().year
        month = date.today().month
        week = date.today().isocalendar()[1]

        total = 0

        if options == "this_year":
            query = (
                """select SUM(amount_total) FROM sale_order
                WHERE sale_order.state = 'sale' AND company_id = """
                + str(company_id)
                + """AND extract(year FROM date_order) = """
                + str(year)
            )
            self._cr.execute(query)
            top_order = self._cr.dictfetchall()
            total = top_order[0].get("sum")

        elif options == "this_month":
            query = (
                """select SUM(amount_total) FROM sale_order
                WHERE sale_order.state = 'sale' AND company_id = """
                + str(company_id)
                + """AND extract(month FROM date_order) = """
                + str(month)
                + """AND extract(year FROM date_order) = """
                + str(year)
            )
            self._cr.execute(query)
            top_order = self._cr.dictfetchall()
            total = top_order[0].get("sum")
        else:
            query = (
                """select SUM(amount_total) FROM sale_order
                WHERE sale_order.state = 'sale' AND company_id = """
                + str(company_id)
                + """AND extract(week FROM date_order) = """
                + str(week)
                + """AND extract(year FROM date_order) = """
                + str(year)
            )
            self._cr.execute(query)
            top_order = self._cr.dictfetchall()
            total = top_order[0].get("sum")

        return 0 if total is None else total


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.model
    def get_invoice_due_amount(self, options):
        """
        Get due amount for this_week, month, year
        """
        company_id = self.env.company.id
        year = date.today().year
        month = date.today().month
        week = date.today().isocalendar()[1]

        total = 0

        if options == "due_this_year":
            query = (
                """select SUM(amount_residual_signed) FROM account_move
                WHERE account_move.move_type = 'out_invoice' AND
                company_id = """
                + str(company_id)
                + """ AND extract(year FROM create_date) = """
                + str(year)
            )
            self._cr.execute(query)
            sum_of_due_amount = self._cr.dictfetchall()
            total = sum_of_due_amount[0].get("sum")

        elif options == "due_this_month":
            query = (
                """select SUM(amount_residual_signed) FROM account_move
                WHERE account_move.move_type = 'out_invoice' AND
                company_id = """
                + str(company_id)
                + """AND extract(month FROM create_date) = """
                + str(month)
                + """AND extract(year FROM create_date) = """
                + str(year)
            )
            self._cr.execute(query)
            sum_of_due_amount = self._cr.dictfetchall()
            total = sum_of_due_amount[0].get("sum")
        else:
            query = (
                """select SUM(amount_residual_signed) FROM account_move
                WHERE account_move.move_type = 'out_invoice' AND
                company_id = """
                + str(company_id)
                + """AND extract(week FROM create_date) = """
                + str(week)
                + """AND extract(year FROM create_date) = """
                + str(year)
            )
            self._cr.execute(query)
            sum_of_due_amount = self._cr.dictfetchall()
            total = sum_of_due_amount[0].get("sum")

        return 0 if total is None else total


class AccountPayment(models.Model):
    _inherit = "account.payment"

    @api.model
    def get_deposit_amount(self, options):
        """
        Get deposit amount for this week, month, year.
        """
        year = date.today().year
        month = date.today().month
        week = date.today().isocalendar()[1]

        total = 0

        if options == "deposit_this_year":
            query = (
                """select SUM(amount) FROM account_payment
                WHERE account_payment.is_reconciled = 'true'
                AND account_payment.payment_type = 'inbound'"""
                + """ AND extract(year FROM create_date) = """
                + str(year)
            )
            self._cr.execute(query)
            sum_of_deposit_amount = self._cr.dictfetchall()
            total = sum_of_deposit_amount[0].get("sum")

        elif options == "deposit_this_month":
            query = (
                """select SUM(amount) FROM account_payment
                WHERE account_payment.is_reconciled = 'true'
                AND account_payment.payment_type = 'inbound'"""
                + """AND extract(month FROM create_date) = """
                + str(month)
                + """AND extract(year FROM create_date) = """
                + str(year)
            )
            self._cr.execute(query)
            sum_of_deposit_amount = self._cr.dictfetchall()
            total = sum_of_deposit_amount[0].get("sum")
        else:
            query = (
                """select SUM(amount) FROM account_payment
                WHERE account_payment.is_reconciled = 'true'
                AND account_payment.payment_type = 'inbound'"""
                + """AND extract(week FROM create_date) = """
                + str(week)
                + """AND extract(year FROM create_date) = """
                + str(year)
            )
            self._cr.execute(query)
            sum_of_deposit_amount = self._cr.dictfetchall()
            total = sum_of_deposit_amount[0].get("sum")

        return 0 if total is None else total
