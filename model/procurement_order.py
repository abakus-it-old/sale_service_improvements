from openerp import models, fields, api
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class procurement_order(models.Model):
    _inherit = ['procurement.order']

    def _create_service_task(self, cr, uid, procurement, context=None):
        #original code
        """
        project_task = self.pool.get('project.task')
        project = self._get_project(cr, uid, procurement, context=context)
        planned_hours = self._convert_qty_company_hours(cr, uid, procurement, context=context)
        task_id = project_task.create(cr, uid, {
            'name': '%s:%s' % (procurement.origin or '', procurement.product_id.name),
            'date_deadline': procurement.date_planned,
            'planned_hours': planned_hours,
            'remaining_hours': planned_hours,
            'partner_id': procurement.sale_line_id and procurement.sale_line_id.order_id.partner_id.id or procurement.partner_dest_id.id,
            'user_id': procurement.product_id.product_manager.id,
            'procurement_id': procurement.id,
            'description': procurement.name + '\n',
            'project_id': project and project.id or False,
            'company_id': procurement.company_id.id,
        },context=context)
        self.write(cr, uid, [procurement.id], {'task_id': task_id}, context=context)
        self.project_task_create_note(cr, uid, [procurement.id], context=context)
        return task_id
        """
        #modified code
        project_task = self.pool.get('project.task')
        
        sale_order_description = ''
        sale_order_obj = self.pool.get('sale.order')
        sale_order_ids = sale_order_obj.search(cr, uid, [('name','=',procurement.origin)])
        if sale_order_ids:
            sale_order = sale_order_obj.browse(cr, uid, sale_order_ids[0])
            sale_order_description = sale_order.client_order_ref
        
        project = self._get_project(cr, uid, procurement, context=context)
        planned_hours = self._convert_qty_company_hours(cr, uid, procurement, context=context) * procurement.product_id.planned_hours
        task_id = project_task.create(cr, uid, {
            'name': '%s: %s (%s)' % (procurement.product_id.name, sale_order_description, procurement.origin or ''),
            'date_deadline': procurement.date_planned,
            'planned_hours': planned_hours,
            'remaining_hours': planned_hours,
            'partner_id': procurement.sale_line_id and procurement.sale_line_id.order_id.partner_id.id or procurement.partner_dest_id.id,
            'user_id': procurement.product_id.product_manager.id,
            'procurement_id': procurement.id,
            'description': procurement.name + '\n',
            'project_id': project and project.id or False,
            'company_id': procurement.company_id.id,
        },context=context)
        self.write(cr, uid, [procurement.id], {'task_id': task_id}, context=context)
        self.project_task_create_note(cr, uid, [procurement.id], context=context)
        return task_id
        