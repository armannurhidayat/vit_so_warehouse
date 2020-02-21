# -*- coding: utf-8 -*-
from odoo import http

# class VitSoWarehouse(http.Controller):
#     @http.route('/vit_so_warehouse/vit_so_warehouse/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_so_warehouse/vit_so_warehouse/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_so_warehouse.listing', {
#             'root': '/vit_so_warehouse/vit_so_warehouse',
#             'objects': http.request.env['vit_so_warehouse.vit_so_warehouse'].search([]),
#         })

#     @http.route('/vit_so_warehouse/vit_so_warehouse/objects/<model("vit_so_warehouse.vit_so_warehouse"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_so_warehouse.object', {
#             'object': obj
#         })