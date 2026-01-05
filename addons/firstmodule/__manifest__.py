# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Module 1',
    'version': '1.0',
    'summary': 'first module',
    'sequence': 10,
    'description': """
    First module
    """,
    'category': 'Accounting/Accounting',
    'website': 'https://www.odoo.com',
    'depends': [],
    'data': [
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'post_init_hook': '_account_post_init',
    'assets': {
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
}
