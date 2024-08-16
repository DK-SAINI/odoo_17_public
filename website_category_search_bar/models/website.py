# -*- coding: utf-8 -*-

from odoo import models


class Website(models.Model):
    _inherit = "website"

    def _search_get_details(self, search_type, order, options):
        result = super()._search_get_details(search_type, order, options)
        if search_type in ["category"]:
            category = True
            result.append(
                self.env["product.public.category"]._search_get_detail(
                    self, order, options, category
                )
            )
        return result
