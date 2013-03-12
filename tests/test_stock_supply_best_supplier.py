#!/usr/bin/env python
#This file is part stock_supply_best_supplier module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.

import sys
import os
DIR = os.path.abspath(os.path.normpath(os.path.join(__file__,
    '..', '..', '..', '..', '..', 'trytond')))
if os.path.isdir(DIR):
    sys.path.insert(0, os.path.dirname(DIR))

import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import POOL, DB_NAME, USER, CONTEXT, test_view,\
    test_depends
from trytond.transaction import Transaction


class StockSupplyBestSupplierTestCase(unittest.TestCase):
    '''
    Test Stock Supply Best Supplier module.
    '''

    def setUp(self):
        trytond.tests.test_tryton.install_module('stock_supply_best_supplier')

    def test0006depends(self):
        '''
        Test depends.
        '''
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockSupplyBestSupplierTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
