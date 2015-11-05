from openerp import models, fields

class product_template(models.Model):
    _inherit = ['product.template']
    
    planned_hours = fields.Float(string='Initial Planned Hours')