# -*- coding: utf-8 -*-
# from odoo import http


# class OwlFramework(http.Controller):
#     @http.route('/owl_framework/owl_framework', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/owl_framework/owl_framework/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('owl_framework.listing', {
#             'root': '/owl_framework/owl_framework',
#             'objects': http.request.env['owl_framework.owl_framework'].search([]),
#         })

#     @http.route('/owl_framework/owl_framework/objects/<model("owl_framework.owl_framework"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('owl_framework.object', {
#             'object': obj
#         })

