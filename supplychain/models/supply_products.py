from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Supply_products(models.Model):
    _name = "supply.products"
    _description = "Supply Products"

    name = fields.Char()
    company_id = fields.Many2one('supply.chain')
    store_id = fields.Many2one('supply.store')
    create_for = fields.Selection(
        selection=[
            ('company', 'Company'),
            ('store', 'Store'),
        ]
    )
    quantity = fields.Integer()
    required_quantity = fields.Integer()