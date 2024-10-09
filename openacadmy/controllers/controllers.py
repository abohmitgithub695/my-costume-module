# -*- coding: utf-8 -*-
# from odoo import http


# class Openacadmy(http.Controller):
#     @http.route('/openacadmy/openacadmy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openacadmy/openacadmy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('openacadmy.listing', {
#             'root': '/openacadmy/openacadmy',
#             'objects': http.request.env['openacadmy.openacadmy'].search([]),
#         })

#     @http.route('/openacadmy/openacadmy/objects/<model("openacadmy.openacadmy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openacadmy.object', {
#             'object': obj
#         })
