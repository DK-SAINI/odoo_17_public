# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class PurchaseWizard(models.TransientModel):
    _name = "purchase.wizard"
    _description = "Purchase Wizard"


    @api.model
    def default_get(self, fields):
        res = super(PurchaseWizard, self).default_get(fields)
        po_id = self.env.context.get('active_id')
        if po_id:
            res.update({
                'po_id': po_id,
            })
        return res

    po_id = fields.Many2one('purchase.order', string='Purchase Order', required=True)
    po_lines = fields.Many2many('purchase.order.line', domain="[('order_id', '=', po_id)]")        


    def create_po(self):
        if not self.po_lines:
            raise UserError("Please select at least one line to create a new Purchase Order.")
        
        new_po = self.env['purchase.order'].create({
            'partner_id': self.po_id.partner_id.id,
            'order_line': [(0, 0, {
                'product_id': line.product_id.id,
                'name': line.name,
                'product_qty': line.product_qty,
                'product_uom': line.product_uom.id,
                'price_unit': line.price_unit,
                'taxes_id': [(6, 0, line.taxes_id.ids)],
                'date_planned': line.date_planned,
            }) for line in self.po_lines],
        })

        self.po_lines.unlink()

        return {
            'type': 'ir.actions.act_window',
            'name': 'New Purchase Order',
            'res_model': 'purchase.order',
            'res_id': new_po.id,
            'view_mode': 'form',
            'target': 'current',
        }