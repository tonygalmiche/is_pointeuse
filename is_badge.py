# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
from openerp.tools.translate import _

class is_badge(osv.osv):
    _name='is.badge'
    _order='employee'    #Ordre de tri par defaut des listes


    _sql_constraints = [('name_uniq','UNIQUE(name)', 'Ce badge existe deja')] #ATTENTION : Ne pas mettre d'accent dans le message


    #ATTENTION : Pour que la relation many2one affiche le code du moule, le champ doit être nommé 'name' sinon il faut surcharger la méthode name_get
    _columns={
        'name':fields.char("Code",size=20,required=True, select=True),
        'employee': fields.many2one('hr.employee', 'Employé', required=False, ondelete='set null', help="Sélectionnez un employé"),
    }

is_badge()

