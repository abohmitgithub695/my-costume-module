from odoo import models, fields

class ResPartner(models.Model):
    # _name ='event.res.partner'
    _inherit = 'res.partner'
    
    partner_type = fields.Selection(
        selection=[
            ('individual', 'Individual'),
            ('organization', 'Organization'),
            ('customer', 'Customer'),
        ],
        string='partner_type'
    )

