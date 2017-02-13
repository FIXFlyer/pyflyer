#! /usr/bin/env python
#-----------------------------------------------------------------------
# COPYRIGHT_BEGIN
# Copyright (C) 2017, FixFlyer, LLC.
# All rights reserved.
# COPYRIGHT_END
#-----------------------------------------------------------------------

import flyer
import unittest


class LoggerTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_string_to_level(self):
        self.assertEqual(flyer.DEBUG, flyer.Logger.string_to_level("DEBUG"))
        self.assertEqual(flyer.INFO, flyer.Logger.string_to_level("INFO"))
        self.assertEqual(flyer.NOTICE, flyer.Logger.string_to_level("NOTICE"))
        self.assertEqual(flyer.WARNING, flyer.Logger.string_to_level("WARNING"))
        self.assertEqual(flyer.ERR, flyer.Logger.string_to_level("ERR"))
        self.assertEqual(flyer.CRIT, flyer.Logger.string_to_level("CRIT"))
        self.assertEqual(flyer.ALERT, flyer.Logger.string_to_level("ALERT"))
        self.assertEqual(flyer.EMERG, flyer.Logger.string_to_level("EMERG"))
        return

    def test_level_to_string(self):
        self.assertEqual("DEBUG", flyer.Logger.level_to_string(flyer.DEBUG))
        self.assertEqual("INFO", flyer.Logger.level_to_string(flyer.INFO))
        self.assertEqual("NOTICE", flyer.Logger.level_to_string(flyer.NOTICE))
        self.assertEqual("WARNING", flyer.Logger.level_to_string(flyer.WARNING))
        self.assertEqual("ERR", flyer.Logger.level_to_string(flyer.ERR))
        self.assertEqual("CRIT", flyer.Logger.level_to_string(flyer.CRIT))
        self.assertEqual("ALERT", flyer.Logger.level_to_string(flyer.ALERT))
        self.assertEqual("EMERG", flyer.Logger.level_to_string(flyer.EMERG))
        return

    def test_string_to_level_bad(self):
        self.assertIsNone(flyer.Logger.string_to_level("BADNAME"))
        return

    def test_level_to_string_bad(self):
        self.assertIsNone(flyer.Logger.level_to_string(-1))
        self.assertIsNone(flyer.Logger.level_to_string(8))
        return

class FileLoggerTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass



if __name__ == "__main__":
    unittest.main()
