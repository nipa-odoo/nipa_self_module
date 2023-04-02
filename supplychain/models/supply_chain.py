from odoo import models,fields
from odoo.exceptions import UserError , ValidationError

class Supply_chain(models.Model):
    _name = "supply.chain"
    _description = "Supply Chain"
    _rec_name = "company_name"

    company_name = fields.Char()
    address = fields.Char()
    owner_name = fields.Char()
    registration_number = fields.Integer()
    establish_date = fields.Date()
    product_catagory = fields.Char()
    product_ids = fields.One2many('supply.products','company_id',string="Products")
    quantity = fields.Integer()
    dealer_ids = fields.One2many("supply.dealers",'company_id',string="dealers")

