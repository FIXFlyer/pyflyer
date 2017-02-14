#! /usr/bin/env python
#-----------------------------------------------------------------------
# COPYRIGHT_BEGIN
# Copyright (C) 2017, FixFlyer, LLC.
# All rights reserved.
# COPYRIGHT_END
#-----------------------------------------------------------------------

"""Protocol decoder."""

import flyer


MARKER = "50015=EOF\x01"
MARKER_LEN = len(MARKER)


class Decoder(object):
    """Protocol decoder."""

    def __init__(self):
        self._listener = None
        self._buf = ""
        return


    def set_listener(self, listener):
        self._listener = listener
        return


    def receive_bytes(self, buf, buflen):
        self._buf += buf[:buflen]
        return


    def get_message(self):
        pos = self._buf.find(MARKER)
        if pos < 0:
            return

        msg = self._buf[0:pos + MARKER_LEN]
        self._buf = self._buf[pos + MARKER_LEN:]

        return msg


    def dispatch(self, msg):

        msg_type = getInt32("50001=", msg, "\x01")
        if msg_type < 0:
            #FIXME: log
            return

        if msg_type == flyer.protocol.PAYLOAD_MESSAGE_TYPE:
            return self.decode_payload_message(msg)

        elif msg_type == flyer.protocol.HEARTBEAT_MESSAGE_TYPE:
            return self.decode_heartbeat_message(msg)

        elif msg_type == flyer.protocol.COMMIT_MESSAGE_TYPE:
            return self.decode_commit_message(msg)

        elif msg_type == flyer.protocol.COMMON_MESSAGE_TYPE:
            event_type = getInt32("50011=", msg, "\x01")
            if event_type < 0:
                #FIXME: log
                return

            if event_type == flyer.protocol.LOGON_RESPONSE_EVENT_ID:
                return self.decode_logon_response_message(msg)

            elif event_type == flyer.protocol.SESSION_LOGON_EVENT_ID:
                return self.decode_session_logon_message(msg)

            elif event_type == flyer.protocol.SESSION_LOGOUT_EVENT_ID:
                return self.decode_session_logout_message(msg)

            elif event_type == flyer.protocol.RESEND_EVENT_ID:
                return self.decode_resend_message(msg)

            elif event_type == flyer.protocol.ERROR_EVENT_ID:
                return self.decode_error_message(msg)

            else:
                #FIXME: log
                return
        else:
            #FIXME: log
            return


    def decode_payload_message(self, msg):
        return


    def decode_heartbeat_message(self, msg):
        event = OnHeartbeatEvent()
        event.id = getString("50002=", msg, "\x01")
        self._listener.on_heartbeat(event)
        return


    def decode_commit_message(self, msg):
        return


    def decode_logon_response_message(self, msg):
        event = OnLogonEvent()
        result = getString("Success=", msg, "\r\n")
        event.success = (result == "true")
        self._listener.on_logon(event)
        return


    def decode_session_logon_message(self, msg):
        return


    def decode_session_logout_message(self, msg):
        return


    def decode_resend_message(self, msg):
        return


    def decode_error_message(self, msg):
        return
