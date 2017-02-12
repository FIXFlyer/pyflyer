#! /usr/bin/env python
#-----------------------------------------------------------------------
# COPYRIGHT_BEGIN
# Copyright (C) 2017, FixFlyer, LLC.
# All rights reserved.
# COPYRIGHT_END
#-----------------------------------------------------------------------

class Event(object):
    """Base class for API events."""
    pass


class OnLogonEvent(Event):
    """Login response event.

    Sent by the Flyer Engine to an application in response to a call
    to ApplicationManager::logon()."""

    def __init__(self):
        self.success = False
        return


class OnSessionLogonEvent(Event):
    """Subscribed session logon event."""

    def __init__(self):
        self._session_id = ""
        self._connected = False
        self._current_trading_session_id = 0
        self._out_msg_seq_no = 0
        self._in_msg_seq_no = 0
        self._last_client_message_id = ""
        self._scheduled_down = False
        return


class OnSessionLogoutEvent(Event):
    """Subscribed session logout event."""

    def __init__(self):
        self._session_id = ""
        self._connected = False
        self._current_trading_session_id = 0
        self._out_msg_seq_no = 0
        self._in_msg_seq_no = 0
        self._last_client_message_id = ""
        self._scheduled_down = False
        return


class OnCommitEvent(Event):
    """Report confirming the engine has persisted the described message."""

    def __init__(self):
        self._session_id = ""
        self._client_message_id = ""
        self._last_outgoing_msg_seq_num = 0
        return


class OnResendEvent(Event):
    """Description of resent messages; response to restore() request."""

    def __init__(self):
        self._session_id = ""
        self._begin = 0
        self._end = 0
        self._complete = False
        return


class OnHeartbeatEvent(Event):
    """Report of heartbeat received request from Flyer Engine."""

    def __init__(self):
        self._id = ""
        return


class OnErrorEvent(Event):
    """Report of an asynchronous error from the engine or API."""

    def __init__(self):
        self._code = 0
        self._message = ""
        self._fix_message = ""
        self._client_message_id = ""
        return


class OnPayloadEvent(Event):
    """Delivery of an application protocol message from Flyer Engine."""
    def __init__(self):
        self._session_id = ""
        self._fix_message = ""
        return
