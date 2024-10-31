# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request
class ReadApi(http.Controller):
    @http.route("/read/care_card_app.care_card_app/<int:card_No>", methods=["GET"], type="http", auth="none", csrf=False)
    def read_cardno(self, card_No):
        try:
            card_record = request.env['care_card_app.care_card_app'].sudo().search([('card_No', '=', card_No)])   
            if not card_record:
                return http.Response(json.dumps({"error": "Crad number does not exist"}))       
            response_data = {
                "card_No": card_record.card_No,
                "roll_number": card_record.roll_number,
                "beneficiary": card_record.beneficiary,
                "card_status": card_record.card_status,
                "Card_Balance": card_record.Card_Balance,
                "note": card_record.note
            }      
            return http.Response(json.dumps(response_data))      
        except Exception as error:
            return http.Response(json.dumps({"error": str(error)}))