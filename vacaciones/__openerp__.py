# -*- coding: utf-8 -*-
{
    'name': "vacaciones",

    'summary': """
        Gention de vacaciones de los empleados""",

    'description': """
        programa para organizar las vacaciones de empleados de la empresa Holidays
    """,

    'author': "Vacaciones",
    'website': "http://www.Vacaciones.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}