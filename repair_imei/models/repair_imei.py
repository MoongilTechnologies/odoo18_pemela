from odoo import models, fields

class RepairOrder(models.Model):
    _inherit = 'repair.order'

    imei = fields.Char(string="IMEI")
