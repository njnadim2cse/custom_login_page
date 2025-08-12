# -*- coding: utf-8 -*-
################################################################################
#
#
################################################################################

{
    'name': "Custom Login Page",
    'version': '17.0.1.0',
    'summary': """This module assists in configuring a background image for the login page and hide other odoo elements""",
    'description': """Module helps to set background image in Login page.""",
    'license': 'LGPL-3',
    'website': "",
    'author': 'Saiyedul Morsalin',
    'category': 'Tools',
    'depends': ['base', 'portal', 'web'],
    'data': [
        'views/res_company.xml',
        'views/web_login.xml',
    ],
    'images': ['static/description/banner.png'],
    'sequence': 1,
    "application": True,
    "installable": True
}
