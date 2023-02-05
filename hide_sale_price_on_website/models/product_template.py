# -*- coding: utf-8 -*-

from odoo import models, fields


class hide_sale_price_on_website(models.Model):
    _inherit = "product.template"

    # Add New Fields
    hide_sale_price = fields.Boolean(help="Product price hide on shop when you set true its value.")

    def _get_combination_info(
        self,
        combination=False,
        product_id=False,
        add_qty=1,
        pricelist=False,
        parent_combination=False,
        only_template=False,
    ):
        # override _get_combination_info function for updte
        # hide_sale_price
        combination = super()._get_combination_info(
            combination=combination,
            product_id=product_id,
            add_qty=add_qty,
            pricelist=pricelist,
            parent_combination=parent_combination,
            only_template=only_template,
        )
        combination.update(
            {
                "hide_sale_price": self.hide_sale_price,
            }
        )
        return combination
