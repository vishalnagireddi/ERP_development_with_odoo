from odoo import http
from odoo.http import request

class CrmDashboardUserController(http.Controller):
    @http.route('/crm_dashboard_for_sales_person_user_5/data', type='json', auth='user')
    def get_data(self, **kwargs):
        return request.env['crm.dashboard.for.sales.person.user.5'].sudo().get_dashboard_data()

    @http.route('/crm_dashboard_for_sales_person_user_5/is_manager', type='json', auth='user')
    def is_manager(self):
        user = request.env.user
        print("\n\n\nis_manager fun call......~~~~~~~~~~~~~user~~.........",user)
        is_manager = user.has_group(
            'crm_security.group_crm_normal_admin_2') or user.has_group(
            'crm_security.group_crm_sales_manager_3')
        print("\n\n\nis_manager fun call......~~~~~~~~~~~~is_manager~~~.........", is_manager)
        return {'is_manager': is_manager}

    @http.route('/crm_dashboard_for_sales_person_user_5/get_my_team_id', type='json', auth='user')
    def get_my_team_id(self):
        user_id = request.env.uid
        print("----@@@@@@@@@@@@@@@@@@@@----",user_id)
        team = request.env['crm.team'].sudo().search([('user_id', '=', user_id)], limit=1)
        print("----------::get_my_team_id:::---@@@--------",team)
        return {'team_id': team.id if team else False}

    @http.route('/crm_dashboard_for_sales_person_user_5/get_user_roles', type='json', auth='user')
    def get_user_roles(self):
        user = request.env.user
        print(f"Getting roles for user: {user.name}")

        roles = {
            'is_a_sales_person_user': user.has_group('crm_security.group_crm_sales_person_user_5'),
        }

        print("User roles:", roles)
        return roles
