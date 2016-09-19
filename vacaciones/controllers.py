# -*- coding: utf-8 -*-
from openerp import http

# class Vacaciones(http.Controller):
#     @http.route('/vacaciones/vacaciones/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vacaciones/vacaciones/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vacaciones.listing', {
#             'root': '/vacaciones/vacaciones',
#             'objects': http.request.env['vacaciones.vacaciones'].search([]),
#         })

#     @http.route('/vacaciones/vacaciones/objects/<model("vacaciones.vacaciones"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vacaciones.object', {
#             'object': obj
#         })