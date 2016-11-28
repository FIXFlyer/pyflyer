#! /usr/bin/env python
#-----------------------------------------------------------------------
# COPYRIGHT_BEGIN
# Copyright (C) 2016, FixFlyer, LLC.
# All rights reserved.
# COPYRIGHT_END
#-----------------------------------------------------------------------

class Logger(object):
    """Logger interface.

    The API library logs informational messages describing its
    internal state and events.  By default, these messages are logged
    to a file in the host system's temporary directory.

    It's often desirable to redirect this logging to whatever facility
    is used by the client application.  The library's logging can be
    redirected by using an adaptor that implements this interface.
    """

    # Emergency message level.
    EMERG = 0

    # Alert message level.
    ALERT = 1

    # Critical message level.
    CRIT = 2

    # Error message level.
    ERR = 3

    # Warning message level.
    WARNING = 4

    # Notice message level.
    NOTICE = 5

    # Informational message level.
    INFO = 6

    # Debugging message level.
    DEBUG = 7

    def string_to_level(level):
        """Convert a string level name to its integer value.

        @param[in] level
            A level name, matching the constants defined above (EMERG, etc).

        @retval @c None
            No level name matched @p level.

        @returns
            Integer level value."""
        pass

    def level_to_string(level):
        """Convert an integer level into its string name.

        @param[in] level
            Integer level value.

        @retval None
            The supplied @p level value is invalid.

        @returns
            String name for the specified level."""
        pass

    def create_log(self, log):
        """Create a new log instance.

        @param[in] log
            Name of log instance.

        @retval 0
           Successful."""
        pass

    def set_log_level(self, log, level):
        """Set current minimum log level.

        @param[in] log
            Name of a log instance.

        @param[in] level
            Minimum log level of messages to be emitted.

        @retval 0
            Successful.

        @retval ENOENT
            @p log does not exist."""
        pass

    def get_log_level(self, log, level_out):
        """Get the current minimum log level.

        When logging a message, the caller specifies a level of
        importance, in the range of zero (most important) to 7 (least
        important).  Messages whose level is greater than the value
        returned from this function are not emitted.

        @param[in] log
            Name of a log instance.

        @param[out] level_out
            Minimum level of messages to be emitted for this log instance.
        @retval 0
            Successful.

        @retval ENOENT
            @p log does not exist."""
        pass

    def log(self, log, level, message):
        """Log a message.

        When implementing a Logger, providing this function is
        required.

        @param[in] log
            Name of a log instance.

        @param[in] level
            Level of importance of this message: 0 is most important,
            7 is least important.

        @param[in] message
            The string to be logged.

        @retval 0
            Successful."""
        pass

    def logf(self, log, level, format, ...):
        """Log a message, constructed printf()-style.

        When implementing a Logger, providing this function is
        optional.  The interface class provides an implementation
        which formats the string, and passes it to the single-string
        variant of log().

        @param[in] log
            Name of a log instance.

        @param[in] level
            Level of importance of this message: 0 is most important, 7
            is least important.

        @param[in] format
            printf()-style format string used to create the message.

        @param[in] ...
            Parameters to be substituted into the @p format string.

        @retval 0
            Successful."""
        pass
