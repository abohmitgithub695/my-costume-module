# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import organizer

class OpenAcadmy(models.Model):
    # _name = 'openacadmy.event'  # Define a new model name
    _inherit = 'event.event'      # Inherit from the event model
    _description="this is my custome model"

    theme_event=fields.Char(string="theme event")
    # theme_event2=fields.Char(string="theme_event2")

    
    organizer_event = fields.Many2one(
        'event.organizer',  
        string='event organizer',  
        required=True  
    )


    material_ids = fields.One2many(
        'event.material',
        'event_ids',
        string='Materials'
    )

    organization= fields.Many2one(
        'res.partner',
        string='organization',
        required=True
    )






















    # material_field_1 = fields.Char(string='Material Field 1')
    # material_field_2 = fields.Text(string='Material Field 2')

    # check_field_1 = fields.Boolean(string="Check Field 1")
    # check_field_2 = fields.Boolean(string="Check Field 2")

    # Add your custom fields here

    # You can also add methods or other business logic as needed
    # name = fields.Char()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

######################################################33333
########################################################


# from odoo import models, fields

# class MyEvent(models.Model):
#     _inherit = 'event.event'

#     # Add your custom fields here
#     my_custom_field = fields.Char(string='My Custom Field')


