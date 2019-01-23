# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
from openerp.tools.translate import _

from datetime import datetime
from pytz import timezone

from openerp import tools

class is_pointage_commentaire(osv.osv):
    _name='is.pointage.commentaire'
    _order='name desc'    #Ordre de tri par defaut des listes

    _columns={
        'name':fields.date("Date",required=True),
        'employee': fields.many2one('hr.employee', 'Employé', required=True, ondelete='set null', help="Sélectionnez un employé", select=True),
        'commentaire': fields.char('Commentaire', size=15, help="Mettre un commentaire court sur 15 caractères maximum"),
    }
    _defaults = {
        'name': fields.datetime.now,
    }
is_pointage_commentaire()



