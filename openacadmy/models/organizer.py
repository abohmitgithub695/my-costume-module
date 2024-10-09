# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Organizer(models.Model):
    _name = 'event.organizer'  
    _description = 'Event Organizer'
    
    first_name = fields.Char(string='First Name', required=True,index=True)
    last_name = fields.Char(string='Last Name', required=True)
    phone = fields.Char(string='Phone', required=True)
    email = fields.Char(string='Email')
    title = fields.Selection([
        ('mr', 'Mr.'),
        ('mrs', 'Mrs.'),
    ], string='Title', required=True)

   
    _sql_constraints = [
         ('_check_first_name_unique', 'unique(first_name)', 'The first name must be unique!'),
         ('_check_phone_unique', 'unique(phone)', 'The phone number must be unique!'),
         ('_check_email_unique', 'unique(email)', 'The email must be unique!')
    ]

    @api.constrains('first_name','last_name')
    def _check_first_name_last_name_not_equal(self):
        for record in self:
            if record.first_name ==record.last_name:
                raise ValidationError("The first name should not be the same as the last name!")
            
    @api.constrains('phone')
    def _check_phone_length_isdigit(self):
        for record in self:
            if len(record.phone) != 9:
                raise ValidationError("The phone number must be exactly 9 digits long!")
            if not record.phone.isdigit():
                raise ValidationError('The phone number must contain only digits!')

            
    @api.constrains('email')
    def _check_email_constraints(self):
        for record in self:
            # Check if email is in valid format
            email_regex = r'^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)$'
            if not re.match(email_regex, record.email):
                raise ValidationError("The email address is not valid!")
   











   
    # @api.constrains('first_name')
    # def _check_unique_card_number(self):
    #     for record in self:
    #         if self.search_count([('first_name', '=', record.first_name)]) > 1:
    #             raise ValidationError('The first_name must be unique!')
      



    # _sql_constraints = [
    #     ('first_name_unique', 'unique(first_name)', 'The first name must be unique!'),

        
    #     ('first_name_last_name_unique', 'CHECK(first_name != last_name)', 'The first name should not be the  last_name!'),
    
    # ]
    # _sql_constraints = [
    #     ('first_name_last_name_unique', 'CHECK(first_name != last_name)', 'The first name should not be the  last_name!')
    # ]
    
    # name = fields.Char(string='event organizer', required=True)