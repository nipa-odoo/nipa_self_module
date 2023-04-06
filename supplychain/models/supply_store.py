from odoo import models,fields,api
from odoo.exceptions import UserError,ValidationError

class Supply_store(models.Model):
    _name="supply.store"
    _description="supply store"
    _rec_name = "store_name"


    store_name=fields.Char()
    active = fields.Boolean(default = True)
    address = fields.Char()
    owner_name = fields.Char()
    registration_number = fields.Integer()
    establish_date = fields.Date()
    shop_catagory = fields.Char()
    wholesaler_ids = fields.Many2one("supply.store")
    product_ids = fields.One2many('supply.products','store_id',string="Products")
