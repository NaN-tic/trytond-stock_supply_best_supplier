# This file is part of the stock_supply_best_supplier module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class StockSupplyBestSupplierTestCase(ModuleTestCase):
    'Test Stock Supply Best Supplier module'
    module = 'stock_supply_best_supplier'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockSupplyBestSupplierTestCase))
    return suite