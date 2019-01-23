# -*- coding: utf-8 -*-

{
    'name': 'InfoSaône - Module Odoo Pointeuse',
    'version': '1.0',
    'category': 'InfoSaône',

    'description': """
InfoSaône - Module Odoo Pointeuse 
===================================================

Ce module permet d'exploiter les données issues d'un lecteur de badges pour le pointage du personnel
""",

    'author': 'InfoSaône',
    'maintainer': 'InfoSaône',
    'website': 'http://www.infosaone.com',
    'depends': ['hr'],
    'data': [
        "assets.xml",            # Permet d'ajouter des css et des js
        "res_config_view.xml",
        "is_badge.xml",
        "is_pointage.xml",
        "is_pointage_commentaire.xml",
        "is_jour_ferie.xml",
        "hr_view.xml",
        "wizard/assistent_report_view.xml",
        "menu.xml",
        "security/ir.model.access.csv",
        "is_report.xml",
        "is_report_view.xml",
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'images': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
