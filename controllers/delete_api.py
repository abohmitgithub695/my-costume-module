# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request
class DeleteApi(http.Controller):
        @http.route("/delete/care_card_app.care_card_app/<int:card_No>", methods=["DELETE"], type="http", auth="none", csrf=False)
        def delete_cardno(self,card_No):
                try:
                    card_No = request.env['care_card_app.care_card_app'].sudo().search([('card_No','=',card_No)])
                    if not card_No:
                        return "card number does not exist"                
                    card_No.unlink()
                    return  "card number has been deleted"             
                except Exception as error:
                        return{
                              "error":error  
                        }
                