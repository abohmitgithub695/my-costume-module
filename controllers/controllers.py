# -*- coding: utf-8 -*-
# from odoo import http


# class CareCardApp(http.Controller):
#     @http.route('/care_card_app/care_card_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/care_card_app/care_card_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('care_card_app.listing', {
#             'root': '/care_card_app/care_card_app',
#             'objects': http.request.env['care_card_app.care_card_app'].search([]),
#         })

#     @http.route('/care_card_app/care_card_app/objects/<model("care_card_app.care_card_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('care_card_app.object', {
#             'object': obj
#         })
