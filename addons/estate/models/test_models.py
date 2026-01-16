from odoo import models, fields

class test_model(models.Model):
    _name = "test_model"
    _description = "test estate model"

    name = fields.Char(required = True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facade = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(string='Orientation',
        selection=[('north','North'), ('south','South'), ('east','East'), ('west','West')],
        help="Oreintation is used to separate garden"
        )