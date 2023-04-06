from odoo import models,fields,api,_
from odoo.exceptions import UserError,ValidationError

class Supply_wholesaler(models.Model):
    _name="supply.wholesaler"
    _description="Supply wholesaler"

    name = fields.Char()
    city = fields.Char()
    catagory = fields.Char()
    product_ids = fields.Many2many("supply.products")

    