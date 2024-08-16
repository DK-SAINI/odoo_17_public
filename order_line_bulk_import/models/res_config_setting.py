from odoo import models, fields, api


class CustomSettings(models.TransientModel):
    _inherit = "res.config.settings"

    responsible_user_id = fields.Many2one("res.users", string="Merge Notification")

    @api.model
    def get_values(self):
        res = super(CustomSettings, self).get_values()
        responsible_user_id = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("order_line_bulk_import.responsible_user_id", default=False)
        )
        res["responsible_user_id"] = (
            int(responsible_user_id) if responsible_user_id else False
        )
        return res

    def set_values(self):
        super(CustomSettings, self).set_values()

        self.env["ir.config_parameter"].sudo().set_param(
            "order_line_bulk_import.responsible_user_id", self.responsible_user_id.id
        )
