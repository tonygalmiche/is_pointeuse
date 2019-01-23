# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

from openerp.osv import fields, osv

class res_company(osv.osv):
    _inherit = 'res.company'
    
    _columns = {
            'report_external_link': fields.char("Report External Link", size=128)
    }

class hr_config_settings(osv.osv_memory):
    _inherit = 'hr.config.settings'

    _columns = {
            'report_external_link': fields.char("Report External Link", size=128)
    }

    def _get_report_external_link(self, cr, uid, context):
        company = self.pool.get('res.users').browse(cr, uid, uid, context).company_id
        if company and company.report_external_link:
            return company.report_external_link
        return False
    
    _defaults= {
        'report_external_link': _get_report_external_link
    }

    def execute(self, cr, uid, ids, context=None):
        wizard = self.browse(cr, uid, ids, context)[0]
        if wizard.report_external_link:
            user = self.pool.get('res.users').browse(cr, uid, uid, context)
            user.company_id.write({'report_external_link': wizard.report_external_link})
        return super(hr_config_settings, self).execute(cr, uid, ids, context=context)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
