from odoo import models, fields
from odoo.exceptions import UserError, ValidationError

class Supply_dealers(models.Model):
    _name = "supply.dealers"
    _description = "supply dealers"

    name = fields.Char()
    state = fields.Char()
    catagory = fields.Char()
    quantity = fields.Integer()
    product_ids = fields.Many2one("supply.products")
    dealer_ids = fields.Many2one("supply.chain", string="dealers")

    def action_Accepted(self):
        for record in self.dealer_ids.

    def action_Rejected(self):
        for record in self:
            record.status = "rejected"

 
    def action_Accepted(self):
        for record in self.property_id.offer_ids:
            record.status = 'rejected'

        if self.status != 'accepted':
            self.status = 'accepted'
            self.property_id.state = 'offer accepted'
            self.property_id.buyer_id = self. partner_id
            self.property_id.selling_price = self.price