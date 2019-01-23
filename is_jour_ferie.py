# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
from openerp.tools.translate import _

class is_jour_ferie(osv.osv):
    _name='is.jour.ferie'
    _order='date'

    _columns={
        'name'     : fields.char("Intitulé",size=100,help='Intitulé du jour férié (ex : Pâques)', required=True, select=True),
        'date'     : fields.date("Date",required=True),
        'jour_fixe': fields.boolean('jour férié fixe',  help="Cocher pour préciser que ce jour férié est valable tous les ans"),
        'info_id'  : fields.many2one('is.heure.effective.info', 'Information'),
    }

is_jour_ferie()


