# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleWizard(models.TransientModel):
    _name = "sale.wizard"
    _description = "sale excel report"

    user_id = fields.Many2many('res.users', string='Sales Person')
    start_date = fields.Date("Start Date")
    end_date = fields.Date("End Date")

    def get_excel_report(self):
        # redirect to /sale/excel_report controller to generate the excel file
        return {
            'type': 'ir.actions.act_url',
            'url': '/sale/excel_report/%s' % (self.id),
            'target': 'new',
        }
