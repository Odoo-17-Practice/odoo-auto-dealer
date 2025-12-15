from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_mechanic = fields.Boolean(string='¿Es mecánico?', default=False)

    speciality = fields.Char(string='Especialidad Técnica')