<div align="center">
  <img src="odoo_auto_dealer/static/description/icon.png" alt="Odoo AutoDealer Logo" width="100" height="100">
  <h1>Odoo AutoDealer</h1>
  <p>
    <strong>Sistema de gestión de concesionario para Odoo 17: Inventario y Taller</strong>
  </p>

  <p>
    <a href="https://www.odoo.com/documentation/17.0/">
      <img src="https://img.shields.io/badge/Odoo-17.0-purple?style=for-the-badge&logo=odoo" alt="Odoo 17">
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/License-LGPL--3-green?style=for-the-badge" alt="License">
    </a>
  </p>
</div>

## 📖 Acerca de Odoo AutoDealer

Este es un módulo de **nivel intermedio** diseñado para aprender a extender la funcionalidad nativa de Odoo. Permite gestionar un concesionario de autos usados, incluyendo:

*   **Inventario:** Registro de vehículos con marca, modelo, año y kilometraje.
*   **Mecánicos:** Herencia del módulo de Contactos (`res.partner`) para gestionar personal técnico.
*   **Workflow:** Control de estados del vehículo (Nuevo, Disponible, Vendido) mediante barra de estado.
*   **Automatización:** Nombres computados y validaciones de año.

## 🛠️ Tecnologías Utilizadas

*   **Framework:** Odoo 17
*   **Python:** Herencia de clases (`_inherit`), campos computados y restricciones.
*   **XML:** Herencia de vistas (`xpath`), Vistas Kanban y Search.

## 📂 Estructura del Módulo

```text
odoo_auto_dealer/
├── models/         # Lógica (Vehículos y Herencia de Contactos)
├── views/          # Interfaz (Formularios, Kanban, Menús)
├── security/       # Reglas de acceso (CSV)
└── __manifest__.py # Metadatos del módulo
```
## 🚀 Instalación y Uso

1.  Clona el repositorio en tu carpeta de Odoo addons.
2.  Reinicia el servidor Odoo y actualiza la lista de aplicaciones.
3.  Busca **"Odoo AutoDealer"** e instálalo.
4.  ¡Empieza a registrar vehículos y asignar mecánicos!

