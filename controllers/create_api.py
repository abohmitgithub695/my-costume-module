# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request
class CareCardApi(http.Controller):
    @http.route("/create/care_card_app.care_card_app", methods=["POST"], type="json", auth="none", csrf=False)
    def post_carecard(self):
      try:
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        if not vals.get('card_No'):
             return {
          "message":"card_No is required"
        }
        if not vals.get('beneficiary'):
             return {
          "message":"beneficiary name is required"
        }
        res=request.env['care_card_app.care_card_app'].sudo().create(vals)
        if res:
         return {
           "The care card has been created successfully"
         }
      except Exception as error:
        return {
          "message":error
        }

              
    
          
