from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBook(models.Model):
    #the _name attribute is what we refer to in code
    _name = 'library.book'
    _description='Library Book'

    name = fields.Char(required=True)
    author = fields.Char(reqired=True)
    price = fields.Float()
    published_year = fields.Integer()

    is_expensive = fields.Boolean(
        compute='_compute_is_expensive',
        store=True
    )

    @api.depends('price')
    def _compute_is_expensive(self):
        for record in self:
            record.is_expensive = record.price > 60

    @api.constrains('published_year')
    def _check_published_year(self):
        for record in self:
            if record.published_year and record.published_year < 1500:
                raise ValidationError(
                    'published_year must be greater than 1500'
                )
