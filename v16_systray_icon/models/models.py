# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class v16_systray_icon(models.Model):
#     _name = 'v16_systray_icon.v16_systray_icon'
#     _description = 'v16_systray_icon.v16_systray_icon'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
