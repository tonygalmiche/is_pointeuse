# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import datetime
import time

class assistent_report1(osv.osv_memory):
    _name = "assistent.report1"


    def date_debut_mois():
        now = datetime.date.today()                               # Date du jour
        date_debut_mois = datetime.datetime( now.year, now.month, 1 )   # Premier jour du mois
        return date_debut_mois.strftime('%Y-%m-%d')                     # Formatage


    def date_hier():
        now = datetime.date.today()                               # Date du jour
        date_hier = now + datetime.timedelta(days=-1)
        return date_hier.strftime('%Y-%m-%d')                     # Formatage



    _columns = {
        #'site': fields.selection([
        #    ("1", "Gray"), 
        #    ("4", "ST-Brice"), 
        #], "Site", required=False),
        'type_rapport': fields.selection([
            ("rapport_a_date", "Liste à date"),
            ("rapport_date_a_date", "Liste de date à date"),  
            ("rapport_mois", "Liste mensuelle"), 
        ], "Modèle de rapport", required=True),
        'date_jour': fields.date("Date", required=False),
        'date_mois': fields.date("Date dans le mois", required=False),
        'date_debut': fields.date("Date de début", required=False),
        'date_fin': fields.date("Date de fin", required=False),
        'department_id': fields.many2one('hr.department', 'Service', help="Sélectionnez un service"),
        'employee': fields.many2one('hr.employee', 'Employé', required=False, ondelete='set null', help="Sélectionnez un employé"),
        'interimaire': fields.boolean('Intérimaire',  help="Cocher pour sélectionner uniquement les intérimaires"),
        'saut_page': fields.boolean('Saut de page',  help="Cocher pour avoir un saut de page pour chaque employé"),
        'detail': fields.boolean("Vue détaillée"),
    }

    _defaults = {
        #'date_jour':  time.strftime('%Y-%m-%d'),
        'date_jour':  date_hier(),
        'date_mois':  date_debut_mois(),
        'date_debut': date_debut_mois(),
        'date_fin':   time.strftime('%Y-%m-%d'),
        'type_rapport': 'rapport_mois',
    }






    def assistent_report1(self, cr, uid, ids, context=None):
        report_data = self.browse(cr, uid, ids[0])

        
        #hr_setting_obj = self.pool.get("hr.config.settings")
        #hr_config_ids = hr_setting_obj.search(cr, uid, [], limit=1, order='id DESC', context=context)
        #url = False
        #if hr_config_ids:
        #    hr_settings = hr_setting_obj.browse(cr, uid, hr_config_ids[0], context=context)
        #    report_link = hr_settings.report_external_link

        #En dur en attendant que le bug soit corrigé
        report_link = "http://odoo-rh.bsa-inox.fr/rapport1.php"
        #start_date = datetime.datetime.strptime(report_data.start_date, '%Y-%m-%d').strftime('%d/%m/%Y')
        #end_date = datetime.datetime.strptime(report_data.end_date, '%Y-%m-%d').strftime('%d/%m/%Y')
        #date_mois = datetime.datetime.strptime(report_data.end_date, '%Y-%m-%d').strftime('%d/%m/%Y')

        url = str(report_link)  + '?' \
            + '&dbname='        + str(cr.dbname) \
            + '&type_rapport='  + str(report_data.type_rapport) \
            + '&date_jour='     + str(report_data.date_jour) \
            + '&date_mois='     + str(report_data.date_mois) \
            + '&detail='        + str(report_data.detail) \
            + '&department_id=' + str(report_data.department_id.id) \
            + '&employee='      + str(report_data.employee.id) \
            + '&interimaire='   + str(report_data.interimaire) \
            + '&saut_page='     + str(report_data.saut_page) \
            + '&date_debut='    + str(report_data.date_debut) \
            + '&date_fin='      + str(report_data.date_fin)

        print cr.dbname, url


        return {
            'name'     : 'Go to website',
            'res_model': 'ir.actions.act_url',
            'type'     : 'ir.actions.act_url',
            'target'   : 'current',
            'url'      : url
        }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
