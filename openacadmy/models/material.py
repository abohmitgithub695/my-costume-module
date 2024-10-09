from odoo import models, fields

class Material(models.Model):
    _name = 'event.material'
    _description = 'Event Material'

    material_name = fields.Char(string='material name', required=True, index=True)

  
    material_type = fields.Selection([
        ('raw', 'Raw Material'),
        ('semi_finished', 'Semi-Finished Product'),
        ('finished', 'Finished Product'),
        ('packaging', 'Packaging Material'),
    ], string='Material Type', required=True, help='Type of material being managed.')

    characteristics = fields.Text(string='Characteristics',help='Describe the characteristics of the material.')

    event_ids = fields.Many2one(
        'event.event',
        string='Events'
    )

  
    _sql_constraints = [
        ('material_name_unique', 'unique(material_name)', 'The Material name must be unique!')
    ]