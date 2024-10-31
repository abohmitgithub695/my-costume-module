# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
class care_card_app(models.Model):
    _name = 'care_card_app.care_card_app'
    _description = 'care_card_app.care_card_app'
    card_no = fields.Integer(string="Card number", required=True)
    roll_number = fields.Char(string="roll number")    
    beneficiary = fields.Text(string="beneficiary name" ,required=True)
    validity_date = fields.Date(string='Validity Date', help='The date until which the care card is valid.')    
    card_status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
        ('expired', 'Expired'),
    ], string='Card Status', default='active')
    Card_Balance = fields.Float(string="Card Balance" , default=0.0)
    card_issue_date = fields.Date(string='Card Issue Date', help='The date when the care card was issued.')
    note = fields.Text(string='Notes', help='Additional information related to the care card.')
    _sql_constraints = [
        ('card_No_unique', 'unique(card_No)', 'The card_No must be unique!'),   
        ('beneficiary_unique', 'unique(beneficiary)', 'The beneficiary name must be unique!')
    ]
    @api.constrains('card_No')
    def _check_unique_card_number(self):
        for record in self:
            if self.search_count([('card_No', '=', record.card_No)]) > 1:
                raise ValidationError('The card number must be unique!')      
    @api.constrains('card_issue_date')
    def _check_issue_date(self):
        for record in self:
            if record.card_issue_date > fields.Date.today():
                raise ValidationError("The card issue date cannot be in the future!")         
    @api.constrains('card_No')
    def _check_Card_No(self):
        for record in self:
            if record.card_No < 0:
                raise ValidationError("The Card No  must be integer")
    @api.constrains('Card_Balance')
    def _check_Card_Balance(self):
        for record in self:
            if record.Card_Balance < 0:
                raise ValidationError("The Card Balance  must be integer")        
    @api.constrains('validity_date')
    def _validity_date(self):
        for record in self:
            if record.validity_date < fields.Date.today():
                raise ValidationError("The validity date must be in the future!")
    @api.model
    def _create_roll_number(self):
        for care in self.search([('roll_number','=',False)]):
            care.roll_number= "care" + str(care.id)
       
            






            
   # @api.constrains('card_No')
    # def _check_card_no_unique(self):
    #     for record in self:
    #         if self.search_count([('card_No', '=', record.card_No)]) > 1:
    #             raise ValidationError("The card number must be unique!")
