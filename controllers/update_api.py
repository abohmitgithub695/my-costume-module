# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request
class UpdateApi(http.Controller):
        @http.route("/update/care_card_app.care_card_app/<int:card_No>", methods=["PUT"], type="json", auth="none", csrf=False)
        def update_cardno(self,card_No):
            try:
                card_No = request.env['care_card_app.care_card_app'].sudo().search([('card_No','=',card_No)])
                if not card_No:
                       return {
                     "error":"Crad number does not exist"
                     }                 
                print(card_No)
                args = request.httprequest.data.decode()
                vals = json.loads(args)
                print(vals)
                res = card_No.write(vals)
                if res:
                   return {
                         "The care card has been updated successfully"
                     }
                print(card_No.beneficiary)
            except Exception as error:
                return {
                     "message":error
                     }






