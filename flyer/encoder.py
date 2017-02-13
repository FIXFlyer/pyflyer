#! /usr/bin/env python
#-----------------------------------------------------------------------
# COPYRIGHT_BEGIN
# Copyright (C) 2017, FixFlyer, LLC.
# All rights reserved.
# COPYRIGHT_END
#-----------------------------------------------------------------------

"""Protocol encoder."""

import time
import md5
import flyer


def get_event_timestamp():
    """Return current timestamp string."""
    now = time.time()
    bits = time.localtime(now)
    flyer_time = "#" + time.strftime("%a %b %d %H:%M:%S %Z %Y", bits)
    return flyer_time


class Encoder(object):
    """Protocol encoder."""

    @staticmethod
    def encode_logon_request(user, password, subs):
        """Encode LogonRequest message."""

        hasher = md5.md5(password)

        buf = "50001=%u\0x1" % flyer.protocol.COMMON_MESSAGE_TYPE
        buf += "50011=%u\x01" % flyer.protocol.LOGON_REQUEST_EVENT_ID
        buf += "50013=#Logon\r\n"
        buf += "%s\r\n" % get_event_timestamp()
        buf += "Username=%s\r\n" % user
        buf += "SessionSubscriptions="

        for name in subs:
            sub = subs[name]
            buf += "%s\\:" % sub.get_begin_string()
            buf += "%s\\:" % sub.get_sender_comp_id()
            buf += "%s\\:" % sub.get_target_comp_id()
            buf += "%s\\:" % sub.get_last_sequence()
            buf += "%s\\n" % sub.get_trading_session()
        buf += "\n"

        buf += "Password=%s\r\n" % hasher.hexdigest()
        buf += "ApiMessageType=%u\x01" % flyer.protocol.LOGON_REQUEST_EVENT_ID
        buf += "50015=EOF\x01"
        return buf


    @staticmethod
    def encode_logout_request(user, password):
        """Encode LogoutRequest message."""

        hasher = md5.md5(password)

        buf = "50001=%u\0x1" % flyer.protocol.COMMON_MESSAGE_TYPE
        buf += "50011=%u\x01" % flyer.protocol.LOGOUT_REQUEST_EVENT_ID
        buf += "50013=#Logout\r\n"
        buf += "%s\r\n" % get_event_timestamp()
        buf += "Username=%s\r\n" % user
        buf += "Password=%s\r\n" % hasher.hexdigest()
        buf += "ApiMessageType=%u\x01" % flyer.protocol.LOGOUT_REQUEST_EVENT_ID
        buf += "50015=EOF\x01"
        return buf


    @staticmethod
    def encode_restore(begin, sender, target, first, last):
        """Encode Restore message."""

        buf = "50001=%u\0x1" % flyer.protocol.COMMON_MESSAGE_TYPE
        buf += "50011=%u\x01" % flyer.protocol.RESTORE_EVENT_ID
        buf += "50013=#Restore\r\n"
        buf += "%s\r\n" % get_event_timestamp()
        buf += "BeginString=%s\r\n" % begin
        buf += "SenderCompID=%s\r\n" % sender
        buf += "TargetCompID=%s\r\b" % target
        buf += "Begin=%u\r\n" % first
        buf += "End=%s\r\n" % last
        buf += "ApiMessageType=%u\x01" % flyer.protocol.RESTORE_EVENT_ID
        buf += "50015=EOF\x01"
        return buf


    @staticmethod
    def encode_heartbeat_ack(identifier):
        """Encode HeartbeatAck message."""

        buf = "50001=%u\x01" % flyer.protocol.HEARTBEAT_ACK_MESSAGE_TYPE
        buf += "50002=%s\x01" % identifier
        buf += "50015=EOF\x01"
        return buf


    @staticmethod
    def encode_payload(message_type,
                       sequence_number,
                       possible_duplicate,
                       possible_resend,
                       source,
                       destination,
                       client_message_id,
                       fix_message):
        """Encode Payload message."""

        buf = "50001=%u\0x1" % flyer.protocol.PAYLOAD_MESSAGE_TYPE
        buf += "50003=%u\x01" % message_type
        buf += "50004=%u\x01" % sequence_number
        buf += "50008=%s\x01" % "Y" if possible_duplicate else "N"
        buf += "50009=%s\x01" % "Y" if possible_resend else "N"
        buf += "50005=%s\x01" % source
        buf += "50006=%s\x01" % destination
        buf += "50016=%s\x01" % client_message_id
        buf += "50007=%u\x01" % len(fix_message)
        buf += fix_message
        if buf[-1] != "\x01":
            buf += "\x01"
        buf += "50015=EOF\x01"
        return buf
