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



TEST_DIR = "/tmp"



class FileLogTest(unittest.TestCase):
    def setUp(self):
        return

    def tearDown(self):
        return

    def test_del_no_close(self):
        log = flyer.FileLog("test", TEST_DIR)
        log.open()
        log = None
        return

    def test_double_close(self):
        log = flyer.FileLog("test", TEST_DIR)
        log.open()
        log.close()
        log.close()
        return

    def test_close_no_open(self):
        log = flyer.FileLog("test", TEST_DIR)
        log.close()
        return

    def test_get_set_level(self):
        log = flyer.FileLog("test", TEST_DIR)
        log.set_level(flyer.DEBUG)
        self.assertEqual(flyer.DEBUG, log.get_level())
        log.set_level(flyer.EMERG)
        self.assertEqual(flyer.EMERG, log.get_level())
        return

    def test_log_not_open(self):
        log = flyer.FileLog("test", TEST_DIR)
        log.log(flyer.EMERG, "i should not be here")
        return

    def test_log_filtered(self):
        log = flyer.FileLog("test", TEST_DIR)
        log.set_level(flyer.INFO)
        log.log(flyer.DEBUG, "debug message should be filtered")
        log.close()
        return



class FileLoggerTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_set_level(self):
        log = flyer.FileLogger(TEST_DIR)
        log.create_log("test")
        log.set_log_level("test", flyer.DEBUG)
        self.assertEqual(flyer.DEBUG, log.get_log_level("test"))
        return

    def test_log_simple(self):
        logger = flyer.FileLogger(TEST_DIR)
        logger.create_log("test")
        logger.log("test", flyer.DEBUG, "test_log_simple")
        return

    def test_log_with_format(self):
        logger = flyer.FileLogger(TEST_DIR)
        logger.create_log("test")
        logger.logf("test", flyer.DEBUG, "%s test #%u", "format", 1)
        return


if __name__ == "__main__":
    unittest.main() # pragma: no cover
