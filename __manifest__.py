{
    'name': "Odoo AutoDealer",
    'summary': """Gestión de concesionario: Vehículos, Mecánicos y Ventas""",
    'description': """
        Módulo para la administración de un concesionario de autos usados.
        Características:
        - Inventario de Vehículos (Marcas, Modelos, Placas).
        - Gestión de Mecánicos (Herencia de Contactos).
        - Control de Estados (Nuevo, Disponible, Vendido).
    """,
    'author': "Geraldo Jaramillo",
    'website': "https://www.tuhosting.com",
    'category': 'Sales',
    'version': '17.0.1.0.0',
    'depends': [
        'base',
        'contacts'],
    'data': [
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}