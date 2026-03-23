odoo.define('crm_dashboard.suspect_prospect_ratio', function (require) {
    "use strict";

    const publicWidget = require('web.public.widget');

    publicWidget.registry.SuspectProspectRatio = publicWidget.Widget.extend({
        selector: '.lead_ratio',
        start: async function () {
            const filterValue = document.querySelector('.o_dashboard_filter select')?.value || 'this_month';
            const result = await this._rpc({
                route: '/crm_dashboard/suspect_prospect_ratio',
                params: { range: filterValue },
            });
            if (result) {
                this.el.querySelector('.suspect-prospect-ratio').textContent = result.ratio.toFixed(2);
            }
        },
    });

    return publicWidget.registry.SuspectProspectRatio;
});
