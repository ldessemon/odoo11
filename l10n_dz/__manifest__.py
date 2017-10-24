# -*- coding: utf-8 -*-
{
    'name': 'Algeria - Regions',
    'version': '11.0.1.0.0',
    'description': """Adds extra functionality and configuration to Odoo """,
    'summary': '',
    'author': 'version 10.0 d''OSI, modifié par Ludovic Dessemon pour Odoo 11.0',
    'website': '',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'depends': ['account','l10n_dz_region'],
    'data': [
        'data/wizard_data.xml',
        'data/plan_comptable_data.xml',
        'views/l10n_dz_view.xml',
        'data/account_tax_data.xml',
        'data/account_fiscal_position_template_data.xml',
        'data/account_chart_template_data.yml'
    ]
}
