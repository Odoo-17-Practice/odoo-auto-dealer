from email.policy import default

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class DealerVehicle(models.Model):
    _name = 'dealer.vehicle'
    _description = 'Vehículo del concesionario'
    _rec_name = 'name'

    # Identificación
    name = fields.Char(string='Referencia', compute='_compute_name', store=True)
    license_plate = fields.Char(string='Placa', required=True)
    brand = fields.Char(string='Marca', required=True)
    model = fields.Char(string='Modelo', required=True)

    # Detalles técnicos
    year = fields.Integer(string='Año de fabricación', default=2024)
    mileage = fields.Integer(string='Kilometraje (km)')
    image = fields.Binary(string='Imagen')

    # Datos económicos
    price = fields.Monetary(string='Precio de venta', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Moneda', default=lambda self: self.env.company.currency_id)

    # Flujo de trabajo
    state = fields.Selection([
        ('new', 'Nuevo ingreso'),
        ('available', 'Disponible'),
        ('maintanance', 'En mantenimiento'),
        ('sold', 'Vendido')
    ], string='Estado', default='new', tracking=True)

    # Lógica de negocio
    # Generar el nombre automáticamente
    @api.depends('brand', 'model', 'license_plate')
    def _compute_name(self):
        for record in self:
            if record.brand and record.model and record.license_plate:
                record.name = f"{record.brand} {record.model} [{record.license_plate}]"
            else:
                record.name = record.license_plate or 'Nuevo vehículo'

    @api.constrains('year')
    def _check_year(self):
        for record in self:
            if record.year < 1980:
                raise ValidationError("Política de la empresa: No aceptamos vehículos anteriores a 1980.")