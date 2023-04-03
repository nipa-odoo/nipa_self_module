from odoo import models,fields,_
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

    def action_confirm(self):
        for record in self.quantity:
            if record.quantity < record.product_ids.quantity:
                record.product_ids.quantity = record.product_ids.quantity - record.quantity
            else:
                raise ValidationError(_("Quanntity Error"))            

        # if self.quantity > self.product_ids.quantity:
        #     raise ValidationError(_("Quanntity Error"))
        # else:
        #     self.product_ids.quantity = self.product_ids.quantity - self.quantit


    # def action_Accepted(self):
    #     for record in self.property_id.offer_ids:
    #         record.status = 'rejected'

    #     if self.status != 'accepted':
    #         self.status = 'accepted'
    #         self.property_id.state = 'offer accepted'
    #         self.property_id.buyer_id = self. partner_id
    #         self.property_id.selling_price = self.price