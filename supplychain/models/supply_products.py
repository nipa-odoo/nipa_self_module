from odoo import models,fields

class Supply_products(models.Model):
    _name="supply.products"
    _description="Supply Products"

    name=fields.Char()
    company_id = fields.Many2one('supply.chain')
    quantity = fields.Integer()
