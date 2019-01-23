# -*- coding: utf-8 -*-
{
  "name" : "InfoSaône - Module Odoo 8 Pointeuse BSA",
  "version" : "0.1",
  "author" : "InfoSaône / Tony Galmiche",
  "category" : "InfoSaône\BSA",
  'description': """
InfoSaône - Module Odoo 8 Pointeuse BSA
===================================================

InfoSaône - Module Odoo 8 Pointeuse BSA
""",
  'maintainer': 'InfoSaône',
  'website': 'http://www.infosaone.com',
  "depends" : [
    "hr",
  ], 
  "init_xml" : [],
  "demo_xml" : [],
  "data" : [
        "assets.xml",
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
  "installable": True,
  "active": False,
  "application": True
}

