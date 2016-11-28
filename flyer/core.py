

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
    """TCP/IP socket adaptor interface.

    The Flyer Engine SDK does not deal directly with sockets.  This is
    to enable client applications to use their own socket libraries
    (eg. kernel bypass libraries), or to use a framework which hides
    sockets behind a richer abstraction, for example.

    Consequently, when it needs to send a message to the Flyer Engine,
    the API uses the function provided by this adaptor interface.

    The related function flyer::ApplicationManager::receive_bytes()
    should be invoked by the application code when it receives bytes
    from the Flyer Engine so that they can be processed by the API
    implementation, and delivered back to the application code via its
    Listener interface.
    """

    def send_bytes(self, buffer, buflen):
        """ Called by the API implementation to send a message to the
        Flyer Engine.

        This function should send the bytes in @p buffer using the
        TCP/IP socket that is connected to the Flyer Engine.  In the
        usual case, it's a simple wrapper for socket.send() function.

        @sa flyer::ApplicationManager::receive_bytes(), which
        should be called by the application when data is received
        from the TCP/IP socket.

        @param[in] buffer
           Buffer of bytes to be sent.  No more than @p buflen
           bytes from this buffer should be sent using the socket
           connected to the Flyer Engine.  The ownership of this
           buffer is retained by the caller: if your application
           needs to use it after returning from this function, it
           must make a copy.

        @param[in] buflen
           Maximum number of bytes to be sent from @p buffer.

        @returns
           The number of bytes actually sent.  This will be less than
           or equal to @p buflen.  The API will retry sending any
           unsent bytes; there's no need for the adaptor to do this
           (if it's better that way, copy the buffer and return @p
           buflen).
        """
        pass

    def needs_flush(self):
        """Inform the network adaptor that the library has unsent
        data.

        If send_bytes() reports a partial write (ie. @c written_out <
        @c buflen), the unsent data is queued within the API library,
        and this callback is invoked to inform the application that
        the socket is no longer writeable.

        The application should begin monitoring the socket's
        writeability, and once it becomes writeable again, should call
        ApplicationManager::flush() to drain any queued message data.
        """
        pass


class Listener(object):
    """Listener interface for delivery of Engine events.

    All asynchronous events in the Flyer Engine API are reported to
    the client application using this listener interface.  Each
    function has a single parameter, a reference to a structure
    containing all the details of the event.

    Events are either session level, or application level.  Session
    level events are things like logons, heartbeats, and lost message
    recovery; application level events deliver FIX messages from the
    Flyer Engine.
    """

    def on_logon(self, logon):
        """Response to Logon request from the Flyer Engine.

        Client applications initiate an engine connection by calling
        logon().  This function is invoked to return a result for that
        request.

        Clients must wait for this callback before sending other
        messages.

        @param[in] logon
           Details of the login response event.
        """
        pass

    def on_disconnect(self):
        """Report disconnection by the Flyer Engine.

        Client applications initiate disconnection from the engine by
        calling logout().  This function is invoked once the TCP/IP
        session is disconnected and the API's internal state is
        cleaned up.

        This callback is also called if the flyer engine disconnects
        for any other reason such as network failure.

        Once this function has been invoked, the API is in a stable,
        disconnected state.  The ApplicationManager can be deleted, or
        may reconnect and call logon() again.
        """
        pass

    def on_session_logon(self, session_logon):
        """A subscribed FIX session has logged on.

        @param[in] session_logon
           Details of the session logon event.
        """
        pass

    def on_session_logout(self, session_logout):
        """A subscribed FIX session has logged out.

        @param[in] session_logout
           Details of the session logout event.
        """
        pass

    def on_commit(self, commit):
        """Server has persisted a message from the application.

        This message should be used to flush application-side
        persistence of in-flight messages.

        @param[in] commit
           Details of the commit event.
        """
        pass

    def on_resend(self, resend):
        """Notification of replay event from Flyer engine.

        When a subscribed FIX session performs FIX recovery, and sends
        replayed messages, to the Flyer engine, those messages are
        preceded and followed by a Resend message.

        The Flyer Engine will send an initial on_resend() with the
        OnResendEvent::complete flag @c False.  The replayed messages
        are then delivered (via on_payload()), and then a second
        on_resend() with OnResendEvent::complete set @c to True.

        @param[in] resend
           Details of the resend event.
        """
        pass

    def on_heartbeat(self, heartbeat):
        """Heartbeat received from Flyer Engine.

        @param[in] heartbeat
           Details of the heartbeat event.
        """
        pass

    def on_error(self, error):
        """Engine reports an error.

        The @p error structure contains details of the problem.  Error
        codes include:

        <dl>
        <dt>11
        <dd>Unknown session requested in logon().
        </dl>

        @param[in] error
           Details of the error event.
        """
        pass

    def on_payload(self, payload):
        """A FIX payload message from a subscribed session.

        @param[in] payload
           Details of the payload event.
        """
        pass


class ApplicationManager(object):
    """Main interface for Flyer FIX Engine client applications."""

    @staticmethod
    def create(sender, listener, logger, store):
        """Create an ApplicationManager instance.

        This factory function returns a pointer to a newly created
        ApplicationManager.  The client application must supply a
        Sender and Listener, and may optionally specify a Logger and
        SessionStore.

        If not supplied, the Logger and SessionStore default to using
        an internal implementation.

        The internal logger implementation can be configured via two
        environment variables:
        <dl>
        <dt>FLYER_LOGDIR</dt>
        <dd>
            The full path name of a directory into which log files
            should be written.  This directory must already exist.
            The default directory is @c /tmp on Unix systems, and
            the user's @c AppData/Local/Temp on Windows.
        </dd>

        <dt>FLYER_LOGLEVEL</dt>
        <dd>
            The minimum priority of messages to be logged.  The
            value of this variable should be a string, one of @c
            DEBUG, @c INFO, @c NOTICE, @c WARNING, @c ERR, @c CRIT,
            @c ALERT, or @c EMERG.  The default level is @c
            WARNING.
        </dd>
        </dl>

        The internal session store implemenation can be configured
        using a single environment variable:

        <dl>
        <dt>FLYER_STOREDIR</dt>
        <dd>
            The full path name of a directory into which session
            sequence number files should be written.  This
            directory must already exist.  The default directory is
            @c /tmp on Unix systems, and the user's
            @c AppData/Local/Temp on Windows.
        </dd>
        </dl>

        @param[in] sender
            An implementation of the Sender interface, allowing the
            library to send messages on the socket connection to the
            Flyer Engine.

        @param[in] listener
            An implementation of the Listener interface, used by the
            library to call back into the client application when
            messages are received from the Flyer Engine.

        @param[in] logger
            An optional implementation of the Logger interface, used
            by the library to emit diagnostic information.  If @c
            nullptr, an internal implementation is used, and will
            write messages to a log file in the host system's
            temporary files directory.  The files are named like
            <tt>flyer-<i>user</i>-<i>executable</i>-API.log</tt>, and
            are never erased: messages are simply appended to any
            existing content.

        @param[in] store
            An optional implementation of the SessionStore interface,
            used by the library to maintain the last seen sequence
            number for subscribed FIX sessions.  If @c nullptr, an
            internal implementation is used, and will write sequence
            numbers to files in the host system's temporary files
            directory.  The files are named like
            <tt>sf-<i>begin_string</i>-<i>sender_comp_id</i>-<i>target_comp_id</i>.seq</tt>
            for sessions without a qualifier, or
            <tt>sf-<i>qualifier</i>-QUALIFIED.seq</tt> for qualified
            sessions.

        @returns
            A pointer to the newly created ApplicationManager if
            successful, or a null pointer otherwise.  Once no longer
            needed, the instance must be reclaimed using destroy()
            (ie. not @c delete)."""
        pass

    @staticmethod
    def destroy(manager):
        """Destroy an application manager instance.

        @param[in] manager
            Pointer to ApplicationManager instance to be destroyed.
            This pointer is invalid after the function returns."""
        pass

    def register_fix_session(self, begin_string, sender_comp_id, target_comp_id, session_qualifier):
        """Register a FIX session for processing by this application.

        A registered session that is not configured in the target
        server will cause an onError callback after logon, reporting
        the sender/target identifiers for the session.

        NOTE: FIX session registration only takes effect during logon.
        Any session registrations after logon() will be ignored until
        a future logout()/logon() cycle.

        @param[in] begin_string
            FIX begin string value (including version).

        @param[in] sender_comp_id
            FIX sender company identifier.

        @param[in] target_comp_id
            FIX target company identifier.

        @param[in] session_qualifier
            Session qualifier, used to distinguish sessions with the
            same sender and target.  This can happen for example if the
            engine is listening on two IPs, one for production traffic
            and one for UAT, and the FIX sessions use the same CompIDs.

        @returns
            Session identifier, or @c None if already registered."""
        pass

    def remove_fix_session_by_id(self, session_id):
        """Deregister a FIX session for processing by this application.

        NOTE: changes to FIX registration only take effect at logon.

        @param[in] session_id
            Session identifier.

        @retval 0
            Successful.

        @retval ENOENT
            No matching session is registered."""
        pass

    def remove_fix_session(self, begin_string, sender_comp_id, target_comp_id, session_qualifier):
        """Deregister a FIX session for processing by this application.

        NOTE: changes to FIX registration only take effect at logon.

        @param[in] begin_string
            FIX begin string value (including version).

        @param[in] sender_comp_id
            FIX sender company identifier.

        @param[in] target_comp_id
            FIX target company identifier.

        @param[in] session_qualifier
            session qualifier

        @retval 0
            Successful.

        @retval ENOENT
            No matching session is registered."""
        pass

    def is_fix_session_registered(self, begin_string, sender_comp_id, target_comp_id, session_qualifier, session_id_out):
        """Check whether a FIX session is registered for processing by
        this application.

        NOTE: changes to FIX registration only take effect at logon.

        @param[in] begin_string
            FIX begin string value (including version).

        @param[in] sender_comp_id
            FIX sender company identifier.

        @param[in] target_comp_id
            FIX target company identifier.

        @param[in] session_qualifier
            session qualifier

        @param[in] session_id_out
            If not @c NULL, points to registered session identifier on
            return.

        @returns
            @c True if registered, @c False otherwise."""
        pass

    def load_all_fix_session_subscriptions(self):
        """Register all sessions recorded in persistent session state.

        FIXME: TBD

        @returns
            0 on success."""
        pass

    def is_ready(self):
        """Returns whether the application manager is ready for operation.

        Must have sent logon request, and received successful logon
        response to become ready.

        @returns
            @c True if ready for operation, @c False otherwise."""
        pass

    def set_auto_commit(self, auto_commit):
        """Set whether the API automatically commits received messages.

        Received payload messages include a FIX sequence number.  This
        sequence number is recorded for each subscribed FIX session,
        so that if the client application is disconnected from the
        engine, it can request retransmission of missed messages.

        If @p auto_commit is @c True, the SDK will extract this
        sequence number and persist it once the on_payload() listener
        function returns.

        If @p auto_commit is @c False, the client application should
        call commit() directly for each message that it has received
        and processed.

        @sa is_auto_commit()
        @sa commit()

        @param[in] auto_commit
            If @c true, record the sequence number of received messages
            on arrival."""
        pass

    def is_auto_commit(self):
        """Check whether API is set to commit received messages automatically.

        @sa set_auto_commit()
        @sa commit()

        @returns
            @c True if automatic commit is enabled, @c False otherwise."""
        pass

    def commit(self, session_id, sequence_number):
        """Record the sequence number of a successfully processed message.

        If is_auto_commit() is @c False, the client application should
        invoke this function for each message it receives via the
        on_payload() listener callback.

        @sa set_auto_commit()
        @sa is_auto_commit()

        @param[in] session_id
            Identifier of session from which message was received.

        @param[in] sequence_number
            Sequence number of successfully processed message.

        @retval 0
            Successful."""
        pass

    def logon(self, username, password):
        """Initiate a logon to the Flyer Engine.

        Once a TCP/IP connection is established to the Flyer Engine
        (by the client application), and set_sender() has been called
        to enable the API to send data to the engine, this function
        should be invoked to initiate the application logon process.

        Prior to logging on, the client application must register a
        description of the FIX sessions from which it wants to receive
        messages using register_fix_session().  When logon() is
        invoked, all registered FIX session will be subscribed within
        the engine.

        The result of the attempt to log onto the engine is returned
        to the client application via the
        flyer::ApplicationManager::Listener::on_logon() function.

        @param[in] username
            Engine logon user name.

        @param[in] password
            Engine login password.

        @retval 0
            Successful."""
        pass

    def logout(self):
        """Initiate logout from the Flyer Engine.

        To commence disconnection from the Flyer Engine, the client
        application should first log out.  Once the logout process is
        complete, the engine will close the client's TCP/IP session.
        The client application should detect that the socket is
        readable, but read zero bytes (indicating a remote
        disconnection).  It should call receive_bytes() with zero
        length, which will clean up any internal state within the API,
        and then invoke the client's
        flyer::ApplicationManager::Listener::on_disconnect() function.

        @retval 0
            Successful."""
        pass

    def heartbeat_ack(self, hbid):
        """Send a heartbeat acknowledgement to the Flyer Engine.

        This should be called in response to a heartbeat in the
        on_heartbeat callback.

        @param[in] id
            Identifier for the heartbeat being acknowledged.

        @retval 0
            Successful."""
        pass

    def restore(self, session_id, begin, end):
        """Request the Flyer Engine resend a range of messages from a
        session.

        @param[in] session_id
            Identifier of session for requested messages.

        @param[in] begin
            Sequence number of first message requested.

        @param[in] end
            Sequence number of last message requested.

        @retval 0
            Successful.

        @retval ENOENT
            Session not found."""
        pass

    def send(self, session_id, message_type, sequence_number, possible_duplicate, possible_resend, message, message_id):
        """Send an application message to the Flyer Engine.

        @param[in] session_id
            Identifier for session to which message should be sent.

        @param[in] message_type
            FIX MsgType (35) value.

        @param[in] sequence_number
            FIX MsgSeqNum (34) value.

        @param[in] possible_duplicate
            FIX PossDupFlag (46) value.

        @param[in] possible_resend
            FIX PossResend (97) value.

        @param[in] message
            String contents of message.

        @param[in] message_id
            Optional identifier for this message.  Once the engine has
            received and processed this message, it will be confirmed
            via the on_commit listener callback's on_commit_event.

        @retval 0
            Successful."""
        pass

    def send(self, session_id, message, message_id):
        # FIXME: add default parameters to above.
        # FIXME: change C++ parameter order to match?
        pass

    def receive_bytes(self, buffer, buflen):
        """Pass data received from the Flyer Engine to the API.

        When the client application receives data from the TCP/IP
        socket connected to the Flyer Engine, it should be passed to
        the API implementation using this function.  The API will
        process the received data, and invoke the appropriate listener
        functions on the client application.

        Note that the API will consume all data provided for each
        call, internally buffering any incomplete messages, and thus
        this function does not return the number of bytes consumed: it
        always uses the entire buffer.

        @sa flyer::ApplicationManager::Sender::send_bytes(), which is
        used to pass data to the client application to be sent to the
        Flyer Engine.

        @param[in] buffer
            Buffer of received bytes.  The caller (the client
            application) retains ownership of this buffer: it can be
            overwritten or freed once this function returns.

        @param[in] buflen
            Number of bytes received and supplied in @p buffer.  Note
            that the application @em must report the disconnection of
            the TCP/IP session by the Flyer Engine by calling this
            function with @p buflen == 0.  This is consistent with the
            behaviour of the POSIX @em recv(2) system call, and the
            Winsock @em recv() function, both of which return zero to
            indicate the session peer's disconnection."""
        pass

    def flush(self):
        """Request that the libary attempt to send its queued data.

        When sending data to the Flyer Engine, in some cases the
        network adaptor code will complete a partial send: only some
        portion of the message is able to be sent.  In this
        circumstance, the libary will buffer the remainder of that
        message and call the Sender::needs_flush() call to inform the
        application.

        Once the application's network code detects that the outgoing
        buffers are no longer full (ie. the socket becomes writeable),
        it should call this function to send the remainder of the
        partially-sent message, and any other outgoing messages that
        have subsequently been queued.

        @returns
        Zero on success; any other value is an error code reported
        by Sender::send_bytes()."""
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
