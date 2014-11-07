# This file is part stock_supply_best_supplier module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.pool import Pool
from .purchase_request import *


def register():
    Pool.register(
        PurchaseRequest,
        module='stock_supply_best_supplier', type_='model')
