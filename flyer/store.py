#! /usr/bin/env python
#-----------------------------------------------------------------------
# COPYRIGHT_BEGIN
# Copyright (C) 2016, FixFlyer, LLC.
# All rights reserved.
# COPYRIGHT_END
#-----------------------------------------------------------------------

class SessionStore(object):
    """ """

    class Listener(object):
        """ """
        def on_session(self, session_id, begin_string, sender_comp_id, target_comp_id, session_qualifier, trading_Session_id, last_seq):
            pass

    def add_session(self, session_id):
        pass

    def remove_session(self, session_id):
        pass

    def has_session(self, session_id):
        pass

    def get_session(self, session_id, trading_session_id_out, last_seq_out):
        pass

    def update_session(self, session_id, trasing_session_id, last_seq):
        pass

    def for_each_session(self, listener):
        pass
