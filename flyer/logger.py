#! /usr/bin/env python
#-----------------------------------------------------------------------
# COPYRIGHT_BEGIN
# Copyright (C) 2016-2017, FixFlyer, LLC.
# All rights reserved.
# COPYRIGHT_END
#-----------------------------------------------------------------------

import os
import psutil
import time


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

# Level names.
NAMES = ["EMERG", "ALERT", "CRIT", "ERR", "WARNING", "NOTICE", "INFO", "DEBUG"]

# Level numbers.
LEVELS = {"EMERG": EMERG,
          "ALERT": ALERT,
          "CRIT": CRIT,
          "ERR": ERR,
          "WARNING": WARNING,
          "NOTICE": NOTICE,
          "INFO": INFO,
          "DEBUG": DEBUG}



class Logger(object):
    """Logger interface.

    The API library logs informational messages describing its
    internal state and events.  By default, these messages are logged
    to a file in the host system's temporary directory.

    It's often desirable to redirect this logging to whatever facility
    is used by the client application.  The library's logging can be
    redirected by using an adaptor that implements this interface.
    """

    @staticmethod
    def string_to_level(level):
        """Convert a string level name to its integer value.

        @param[in] level
            A level name, matching the constants defined above (EMERG, etc).

        @retval @c None
            No level name matched @p level.

        @returns
            Integer level value."""

        return LEVELS.get(level)


    @staticmethod
    def level_to_string(level):
        """Convert an integer level into its string name.

        @param[in] level
            Integer level value.

        @retval None
            The supplied @p level value is invalid.

        @returns
            String name for the specified level."""

        if level < 0 or level >= len(NAMES):
            return None
        return NAMES[level]


    def create_log(self, log):
        """Create a new log instance.

        @param[in] log
            Name of log instance.

        @retval 0
           Successful."""
        return


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
        return


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
        return


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
        return


    def logf(self, log, level, format, *params):
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

        @param[in] params
            Parameters to be substituted into the @p format string.

        @retval 0
            Successful."""

        return self.log(log, level, format % params)



class FileLog(object):
    def __init__(self, name, directory):
        self._name = name
        self._directory = directory
        self._level = DEBUG
        self._file = None
        return

    def __del__(self):
        self.close()
        return

    def set_level(self, level):
        self._level = level
        return

    def get_level(self):
        return self._level

    def open(self):
        proc = psutil.Process(os.getpid()).name()
        filename = "flyer-%s-%s-%s.log" % (os.getlogin(), proc, self._name)
        path = os.path.join(self._directory, filename)

        self._file = open(path, "a")

        self.raw_write("SYSTEM",
                       "Opened log %s for %s (pid %u)." % (self._name,
                                                           proc,
                                                           os.getpid()))
        return

    def close(self):
        self.raw_write("SYSTEM", "Closing log")
        self._file.close()
        self._file = None
        return

    def log(self, level, message):
        if level > self._level:
            return

        return self.raw_write(NAMES[level], message)

    def raw_write(self, level, message):
        if not self._file:
            return

        now = time.time()
        ts = time.strftime("%Y-%m-%d %H:%M:%S.", now)
        ts += "%06u" % (now - int(now)) * 1000000
        file.write("%s %-7s %s\n" % (ts, level, message))
        file.flush()
        return


class FileLogger(Logger):
    """Default logging implementation."""

    def __init__(self, directory):
        """Constructor."""
        self._directory = directory
        self._logs = {}
        return

    def __del__(self):
        """Destructor."""
        for log in self._logs.values():
            log.close()
        return

    def create_log(self, name):
        """Create a new log instance.

        @param[in] name
            Name of log instance.

        @returns
           None Successful."""

        self._logs[name] = FileLog(name, self._directory)
        return

    def set_log_level(self, name, level):
        """Set current minimum log level.

        @param[in] name
            Name of a log instance.

        @param[in] level
            Minimum log level of messages to be emitted.

        @retval 0
            Successful.

        @retval ENOENT
            @p log does not exist."""

        log = self._logs[name]
        return log.set_level(level)

    def get_log_level(self, name, level_out):
        """Get the current minimum log level.

        When logging a message, the caller specifies a level of
        importance, in the range of zero (most important) to 7 (least
        important).  Messages whose level is greater than the value
        returned from this function are not emitted.

        @param[in] name
            Name of a log instance.

        @param[out] level_out
            Minimum level of messages to be emitted for this log instance.
        @retval 0
            Successful.

        @retval ENOENT
            @p log does not exist."""

        log = self._logs[name]
        return log.get_level()

    def log(self, name, level, message):
        """Log a message.

        When implementing a Logger, providing this function is
        required.

        @param[in] name
            Name of a log instance.

        @param[in] level
            Level of importance of this message: 0 is most important,
            7 is least important.

        @param[in] message
            The string to be logged.

        @retval 0
            Successful."""

        log = self._logs[name]
        return log.log(level, message)
