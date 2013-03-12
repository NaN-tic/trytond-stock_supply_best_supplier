#This file is part stock_supply_best_supplier module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.

from trytond.pool import PoolMeta

__all__ = ['PurchaseRequest']
__metaclass__ = PoolMeta


class PurchaseRequest:
    'Purchase Request'
    __name__ = 'purchase.request'

    @classmethod
    def find_best_supplier(cls, product, date):
        '''
        Return a supplier if we have any best supplier
        '''
        supplier, purchase_date = super(PurchaseRequest, cls).find_best_supplier(product, date)

        if not supplier and product.product_suppliers:
            supplier = product.product_suppliers[0].party
        return supplier, purchase_date
