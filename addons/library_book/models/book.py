from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBook(models.Model):
    #the _name attribute is what we refer to in code
    _name = 'library.book'
    _description='Library Book'

    name = fields.Char(required=True)
    author = fields.Char(required=True)
    category_id = fields.Char(required=True)
    price = fields.Float()
    published_year = fields.Integer()

    is_expensive = fields.Boolean(
        compute='_compute_is_expensive',
        store=True
    )

    #Define a field called state.
    state = fields.Selection(
        #The state can only have two values: draft, and published
        [
            #left is what we refer to in code, right is what UI shows
            ('draft', 'Draft'),
            ('published', 'Published'),
        ],
        # The state defaults to draft.
        default='draft',
        #Every book should have a state
        required=True
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

    def action_publish(self):
        for record in self:
            if record.state=='published':
                continue
            if record.price <= 0:
                raise ValidationError(
                    "Can't publish a book with zero or negative price"
                )
            record.state='published'
