from odoo import models, fields, _
from odoo.exceptions import UserError, ValidationError


class Supply_dealers(models.Model):
    _name = "supply.dealers"
    _description = "supply dealers"

    name = fields.Char()
    state = fields.Char()
    catagory = fields.Char()
    quantity = fields.Integer()
    company_id = fields.Many2one('supply.chain')
    product_ids = fields.Many2many("supply.products")
    dealer_ids = fields.Many2one("supply.chain", string="dealers")

    # def action_confirm(self) :
            
    #     self.product_ids.quantity = self.product_ids.quantity - self.product_ids.quantity


    # if self.quantity > self.product_ids.quantity:
    #     raise ValidationError(_("Quanntity Error"))
    # else:
    #     self.product_ids.quantity = self.product_ids.quantity - self.quantit

    # def action_Accepted(self):
    #     for self in self.property_id.offer_ids:
    #         self.status = 'rejected'

    #     if self.status != 'accepted':
    #         self.status = 'accepted'
    #         self.property_id.state = 'offered_accepted'
    #         self.property_id.buyer_id = self. partner_id
    #         self.property_id.selling_price = self.price
