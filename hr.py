# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
from openerp.tools.translate import _



class hr_employee(osv.osv):
    _name = "hr.employee"
    _inherit = "hr.employee"

    def _badge_count(self, cr, uid, ids, field_name, arg, context=None):
        obj = self.pool('is.badge')
        res = {}
        for id in ids:
            nb = obj.search_count(cr, uid, [('employee', '=', id)], context=context)
            res[id] = {
                'is_badge_count': nb,
            }
        return res


    def _pointage_count(self, cr, uid, ids, field_name, arg, context=None):
        obj = self.pool('is.pointage')
        res = {}
        for id in ids:
            nb = obj.search_count(cr, uid, [('employee', '=', id)], context=context)
            res[id] = {
                'is_pointage_count': nb,
            }
        return res




    def action_view_badge(self, cr, uid, ids, context=None):
        print "test"

        #employee = self._get_products(cr, uid, ids, context=context)
        #obj = self.pool('is.badge')
        #nb = obj.search_count(cr, uid, [('employee', '=', id)], context=context)
        #result = self._get_act_window_dict(cr, uid, 'is.badge', context=context)

        #if len(ids) == 1:
        res = {}
        res['context'] = "{'employee': " + str(ids[0]) + "}"
        #else:
        #    result['domain'] = "[('product_id','in',[" + ','.join(map(str, products)) + "])]"
        #    result['context'] = "{}"
        return res





    _columns = {
        #'is_site': fields.selection([
        #    ("1", "Gray"), 
        #    ("4", "ST-Brice"), 
        #], "Site", required=False),
        'is_matricule': fields.char('Matricule', help='N° de matricule du logiciel de paye', required=False),
        'is_categorie': fields.selection([
            ("2x8" , "Équipe en 2x8"), 
            ("2x8r", "Équipe en 2x8 avec recouvrement"), 
            ("nuit", "Équipe de nuit"),
            ("3x8" , "en 3x8"),
            ("jour", "Personnel de journée"),
        ], "Catégorie de personnel", required=False),
        'is_interimaire': fields.boolean('Intérimaire',  help="Cocher pour indiquer que c'est un intérimaire"),
        'is_badge_count': fields.function(_badge_count, string='# Badges', type='integer', multi="_badge_count"),
        'is_pointage_count': fields.function(_pointage_count, string='# Pointages', type='integer', multi="_pointage_count"),

        'is_jour1': fields.float('Lundi'),
        'is_jour2': fields.float('Mardi'),
        'is_jour3': fields.float('Mercredi'),
        'is_jour4': fields.float('Jeudi'),
        'is_jour5': fields.float('Vendredi'),
        'is_jour6': fields.float('Samedi'),
        'is_jour7': fields.float('Dimanche'),

    }

hr_employee()



# 
#-> 
#-> 
#-> 


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
