# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
from openerp.tools.translate import _

from datetime import datetime
from pytz import timezone

from openerp import tools

class is_pointage(osv.osv):
    _name='is.pointage'
    _order='name desc'    #Ordre de tri par defaut des listes

    _columns={
        'name':fields.datetime("Date Heure",required=True),
        'employee': fields.many2one('hr.employee', 'Employé', required=True, ondelete='set null', help="Sélectionnez un employé", select=True),
        'entree_sortie': fields.selection([("E", "Entrée"), ("S", "Sortie")], "Entrée/Sortie", required=True),
        'pointeuse': fields.char('Pointeuse', help='Adresse IP du lecteur de badges', required=False),
        'commentaire': fields.text('Commentaire'),
    }
    _defaults = {
        'name': fields.datetime.now,
    }
    def write(self, cr, uid, ids, vals, context=None):
        now = datetime.now(timezone('Europe/Berlin'))
        user_obj = self.pool.get('res.users')
        user = user_obj.browse(cr, uid, uid, context=context)
        this = self.pool.get(str(self))
        doc = this.browse(cr, uid, ids, context=context)
        msg="\nPointage modifié manuellement "+now.strftime('le %d/%m/%Y à %H:%M:%S')+' par '+str(user.name)
        vals.update({'commentaire': msg})
        return super(is_pointage, self).write(cr, uid, ids, vals, context=context)



# Vue créée pour éssayer d'identifier les anomalies de pointage, mais c'est trop complexe à faire comme cela
# Je la conserve juste pour l'exemple (Menu Configuration / Configuration / Anomalies de pointage)
class is_pointage_anomalie(osv.osv):
    _name = "is.pointage.anomalie"
    _auto = False
    _columns = {
        'pointage_id': fields.many2one('is.pointage', 'Pointage', required=True, ondelete='set null', help="Pointage", select=True),
        'name':fields.datetime("Date Heure",required=True),
        'employee': fields.many2one('hr.employee', 'Employé', required=True, ondelete='set null', help="Sélectionnez un employé", select=True),
        'entree_sortie': fields.selection([("E", "Entrée"), ("S", "Sortie")], "Entrée/Sortie", required=True),
    }
    def init(self, cr):
        tools.drop_view_if_exists(cr, 'is_pointage_anomalie')
        cr.execute("""
                CREATE OR REPLACE view is_pointage_anomalie AS (
                    SELECT id as id, id as pointage_id, name, employee, entree_sortie
                    FROM is_pointage 
                    WHERE id>0
               )
        """)







class is_heure_effective(osv.osv):
    _name='is.heure.effective'
    _order='name desc'


#    def _balance_reelle(self, cr, uid, ids, field_name, arg, context=None):
#        res={}
#        for obj in self.browse(cr, uid, ids, dict(context, active_test=False)):
#            print obj
#            balance=obj.theorique=obj.effectif_reel
#            res[obj.id] = balance
#        return res


    _columns={
        'name':fields.date("Date",required=True),
        'employee_id': fields.many2one('hr.employee', 'Employé', required=True),
        'department_id': fields.many2one('hr.department', 'Département'),
        'theorique': fields.float(u'Heures théoriques'),
        'effectif_calcule': fields.float(u'Heures éffectives calculées'),
        'effectif_reel': fields.float(u'Heures éffectives réelles'),
        'balance_reelle': fields.float(u'Balance réelle'),
        'info_id': fields.many2one('is.heure.effective.info', 'Information'),
        'info_complementaire': fields.char('Information complémentaire'),
    }


    def write(self, cr, uid, ids, vals, context=None):
        if "effectif_reel" in vals:
            obj = self.browse(cr, uid, ids[0], context=context)
            vals["balance_reelle"]=vals["effectif_reel"]-obj.theorique
        res = super(is_heure_effective, self).write(cr, uid, ids, vals, context=context)
        return res




class is_heure_effective_info(osv.osv):
    _name='is.heure.effective.info'
    _order='name'

    _columns={
        'name':fields.char("Information",required=True),
    }







