


from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    bg_image = fields.Binary(string="Image")
