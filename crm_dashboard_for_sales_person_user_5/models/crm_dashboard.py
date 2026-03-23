from odoo import models, api, fields

class CrmDashboard(models.Model):
    _name = 'crm.dashboard.for.sales.person.user.5'
    _description = 'CRM Dashboard Logic'

    @api.model
    def get_dashboard_data(self, period='this_month'):
        user = self.env.user
        domain = []

        # Admin: All leads
        if user.has_group('crm_security.group_crm_sales_person_user_5'):
            domain = []

        # # Team Lead: Own and team
        # elif user.has_group('crm_dashboard.group_crm_team_lead'):
        #     domain = ['|', ('user_id', '=', user.id), ('team_id.user_id', '=', user.id)]
        #
        # # Team User: Own leads only
        # elif user.has_group('crm_dashboard.group_crm_team_user'):
        #     domain = [('user_id', '=', user.id)]

        leads = self.env['crm.lead'].search(domain)
        total = sum(leads.mapped('expected_revenue'))

        return {
            'lead_count': len(leads),
            'total_revenue': total,
        }


