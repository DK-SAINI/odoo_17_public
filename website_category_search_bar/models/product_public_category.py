# -*- coding: utf-8 -*-

from odoo import models, api


class ProductPublicCategory(models.Model):
    _inherit = "product.public.category"

    @api.model
    def _search_get_detail(self, website, order, options, category=None):
        results_data = super()._search_get_detail(website, order, options)
        if category:
            results_data["search_fields"].extend(
                ["parent_id.name", "parent_id.parent_id.name"]
            )
            results_data["fetch_fields"].append("parent_id")

        return results_data

    def _search_render_results(self, fetch_fields, mapping, icon, limit):
        results_data = super()._search_render_results(
            fetch_fields, mapping, icon, limit
        )
        if "parent_id" in fetch_fields:
            for data in results_data:
                if data.get("id"):
                    category = self.browse(data.get("id"))

                    def get_full_category_path(category):
                        if category.parent_id:
                            return f"{get_full_category_path(category.parent_id)} / {category.name}"
                        else:
                            return category.name

                data["name"] = get_full_category_path(category)

            results_data = sorted(results_data, key=lambda x: x["id"])
        return results_data
