

class Logger(object):
    """ """

    def create_log(self, log):
        pass

    def set_log_level(self, log, level):
        pass

    def get_log_level(self, log, level_out):
        pass

    def log(self, log, level, message):
        pass

    def logf(self, log, level, format, ...):
        pass


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


class FixMessage(object):

    def clear(self):
        pass

    def size(self):
        pass

    def add(self, tag, value, index=-1):
        pass

    def add_tag_value(self, tag_value, index=-1):
        pass

    def add_utc_timestamp(self, tag, seconds, index=-1):
        pass

    def add_utc_timestamp_with_milliseconds(self, tag, seconds, milliseconds, index=-1):
        pass

    def remove(self, tag, nth=0):
        pass

    def remove_at(self, index):
        pass

    def get(self, tag, value_out, nth=0):
        pass

    def get_at(self, index, tag_out, value_out):
        pass

    def encode(self, buffer, buflen, length_out, raw=False):
        pass

    def decode(self, buffer, buflen):
        pass


class Sender(object):
    """ """

    def send_bytes(self, buffer, buflen, sent_out):
        pass

    def needs_flush(self):
        pass


class Listener(object):
    """ """

    def on_logon(self, logon):
        pass

    def on_disconnect(self):
        pass

    def on_session_logon(self, session_logon):
        pass

    def on_session_logout(self, session_logout):
        pass

    def on_commit(self, commit):
        pass

    def on_resend(self, resend):
        pass

    def on_heartbeat(self, heartbeat):
        pass

    def on_error(self, error):
        pass

    def on_payload(self, payload):
        pass


class ApplicationManager(object):
    """ """

    @staticmethod
    def create(sender, listener, logger, store):
        pass

    @staticmethod
    def destroy(manager):
        pass


    def register_fix_session(self, begin_string, sender_comp_id, target_comp_id, session_qualifier):
        pass

    def remove_fix_session_by_id(self, session_id):
        pass

    def remove_fix_session(self, begin_string, sender_comp_id, target_comp_id, session_qualifier):
        pass

    def is_fix_session_registered(self, begin_string, sender_comp_id, target_comp_id, session_qualifier, session_id_out):
        pass

    def load_all_fix_session_subscriptions(self):
        pass

    def is_ready(self):
        pass

    def set_auto_commit(self, auto_commit):
        pass

    def is_auto_commit(self):
        pass

    def commit(self, session_id, sequence_number):
        pass

    def logon(self, username, password):
        pass

    def logout(self):
        pass

    def heartbeat_ack(self, hbid):
        pass

    def restore(self, session_id, begin, end):
        pass

    def send(self, session_id, message_type, sequence_number, possible_duplicate, possible_resend, message, message_id):
        pass

    def send(self, session_id, message, message_id):
        pass

    def receive_bytes(self, buffer, buflen):
        pass

    def flush(self):
        pass


class Event(object):
    pass


class OnLogonEvent(Event):
    pass


class OnSessionLogonEvent(Event):
    pass


class OnSessionLogoutEvent(Event):
    pass


class OnCommitEvent(Event):
    pass


class OnResendEvent(Event):
    pass


class OnHeartbeatEvent(Event):
    pass


class OnErrorEvent(Event):
    pass

class OnPayloadEvent(Event):
    pass
