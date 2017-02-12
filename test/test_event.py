#! /usr/bin/env python
#-----------------------------------------------------------------------
# COPYRIGHT_BEGIN
# Copyright (C) 2017, FixFlyer, LLC.
# All rights reserved.
# COPYRIGHT_END
#-----------------------------------------------------------------------

import flyer
import unittest

class EventTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_on_logon(self):
        event = flyer.OnLogonEvent()
        event.success = True
        self.assertEqual(True, event.success)
        event.success = False
        self.assertEqual(False, event.success)
        return


if __name__ == "__main__":
    unittest.main()
