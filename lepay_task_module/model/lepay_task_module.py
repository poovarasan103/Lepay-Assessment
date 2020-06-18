# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2018-Today Ascetic Business Solution <www.asceticbs.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################

from odoo import api,fields,models,_
from odoo import exceptions

class LepayTask(models.Model):
    _name = "lepay.task"

    name = fields.Char('Input Numbers',help="Integer values with comma separated.",required=True)  
    odd_values = fields.Char('Odd Number',compute='get_odd_val')
    adjacent_val = fields.Char('Adjacent Values',compute='get_adjacent_val')

    @api.depends('name')
    def get_odd_val(self):
        for record in self:
            if record.name:
               fval = record.name
               lists = list(fval.split(","))
               list_int = [int(num) for num in lists]
               for elem in list_int:
                   if list_int.count(elem) > 1:
                      raise exceptions.Warning("Please don't repeat the values")                   
                   else:                   
                      record['odd_values'] = [num for num in list_int if num % 2 == 1]


    @api.depends('name')
    def get_adjacent_val(self):
        for record in self:
            if record.name:
               fval = record.name
               lists = list(fval.split(","))
               list_int = [int(num) for num in lists]
               count = 0
               n = len(list_int)
               adj_list = []
               for i in range(0, n): 
                   for j in range(i + 1, n): 
                       if list_int[i] + list_int[j] == 20: 
                          adj_list.append((list_int[i],list_int[j]))
               record['adjacent_val'] = adj_list

            
