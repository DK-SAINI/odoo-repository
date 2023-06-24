# -*- coding: utf-8 -*-
# from odoo import http


# class V16SystrayIcon(http.Controller):
#     @http.route('/v16_systray_icon/v16_systray_icon', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/v16_systray_icon/v16_systray_icon/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('v16_systray_icon.listing', {
#             'root': '/v16_systray_icon/v16_systray_icon',
#             'objects': http.request.env['v16_systray_icon.v16_systray_icon'].search([]),
#         })

#     @http.route('/v16_systray_icon/v16_systray_icon/objects/<model("v16_systray_icon.v16_systray_icon"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('v16_systray_icon.object', {
#             'object': obj
#         })
