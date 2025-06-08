from odoo import api, models, fields, _
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    package_weights_input = fields.Char(string='Package weights')
    truck_packages = fields.Char(string='Truck', compute='_compute_weight_distribution', readonly=True)
    trailer_packages = fields.Char(string='Trailer', compute='_compute_weight_distribution', readonly=True)
    
    @api.depends('package_weights_input')
    def _compute_weight_distribution(self):
        for record in self:
            current_truck_result = _('Not possible')
            current_trailer_result = _('Not possible')
            
            package_weights_str = record.package_weights_input
            if not package_weights_str or not package_weights_str.strip():
                record.truck_packages = current_truck_result
                record.trailer_packages = current_trailer_result
                continue
            try:
                weights_str_list = [w.strip() for w in package_weights_str.split(',') if w.strip()]
                if not weights_str_list:
                    record.truck_packages = current_truck_result
                    record.trailer_packages = current_trailer_result
                    continue
                
                weights = [int(w) for w in weights_str_list]
                
                if any(w <= 0 for w in weights):
                    record.truck_packages = current_truck_result
                    record.trailer_packages = current_trailer_result
                    continue
            except ValueError:
                record.truck_packages = current_truck_result
                record.trailer_packages = current_trailer_result
                continue
            n = len(weights)
            found_solution = False
            if n >= 2:
                for i in range(1, n):
                    truck_load = weights[:i]
                    trailer_load = weights[i:]
                    if sum(truck_load) == sum(trailer_load):
                        current_truck_result = str(truck_load)
                        current_trailer_result = str(trailer_load)
                        found_solution = True
                        break
            
            if not found_solution and n >= 3:
                for i in range(1, n - 1): 
                    truck_load = weights[:i]
                    trailer_load = weights[i+1:]
                    if truck_load and trailer_load and sum(truck_load) == sum(trailer_load):
                        current_truck_result = str(truck_load)
                        current_trailer_result = str(trailer_load)
                        found_solution = True
                        break
            
            record.truck_packages = current_truck_result
            record.trailer_packages = current_trailer_result
