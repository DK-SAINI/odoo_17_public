# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class split_po_line(models.Model):
#     _name = 'split_po_line.split_po_line'
#     _description = 'split_po_line.split_po_line'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

