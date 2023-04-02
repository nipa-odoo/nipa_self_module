from odoo import models,fields,api
from odoo.exceptions import UserError,ValidationError

class Supply_store(models.Model):
    _name="supply.store"
    _description="supply store"

    name=fields.Char()