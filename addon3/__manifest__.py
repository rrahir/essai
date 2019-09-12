# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'jeacnkev',
    'category': 'Tools',
    'summary': 'SMS Text Messaging',
    'description': """
This module gives a framework for SMS text messaging
----------------------------------------------------

The service is provided by the In App Purchase Odoo platform.
""",
    'depends': ['addonZ'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'qweb': [
    ],
    'price': 10000,
    'currency': 'EUR',
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
    'support': 'test@test.com',
}
