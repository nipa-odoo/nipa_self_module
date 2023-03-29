from odoo import models,fields,api
from odoo.exceptions import UserError, ValidationError

class Supply_products(models.Model):
    _name="supply.products"
    _description="Supply Products"

    name=fields.Char()
    company_id = fields.Many2one('supply.chain')
    quantity = fields.Integer()
    stock = fields.Integer(compute="_quantity_num")

    @api.depends("quantity")
    def _quantity_num(self):
        for record in self:
            if record.quantity < 100 :
                record.company_id.quantity = record.quantity + 20
                