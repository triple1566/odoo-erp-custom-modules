from odoo import models, fields, api

class LibraryBookCategory(models.Model):
    _name="library.book.category"
    _description="Library Book Category"

    name=fields.Char(required=True)

    # Maps to multiple rows in the LibraryBook model
    book_ids = fields.One2many(
        'library.book',
        'category_id',
        string='Books'
    )

    book_count = fields.Integer(
        string='Book Count',
        compute='_compute_book_stats',
        store=True
    )

    total_value = fields.Monetary(
        string='Total Value',
        compute='_compute_book_stats',
        currency_field = "currency_id",
        store=True
    )

    currency_id = fields.Many2one(
        'res.currency',
        default=lambda self: self.env.company.currency_id,
        readonly=True,
    )

    @api.depends('book_ids.price')
    def _compute_book_stats(self):
        for category in self:
            books=category.book_ids
            category.book_count=len(books)
            category.total_value=sum(books.mapped('price'))

