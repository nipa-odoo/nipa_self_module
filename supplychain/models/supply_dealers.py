from odoo import models,fields

class Supply_dealers(models.Model):
    _name = "supply.dealers"
    _description = "supply dealers"

    name = fields.Char()
    company_id = fields.Many2one("supply.chain",string="dealers")
