#! /usr/bin/env python
#-----------------------------------------------------------------------
# COPYRIGHT_BEGIN
# Copyright (C) 2016, FixFlyer, LLC.
# All rights reserved.
# COPYRIGHT_END
#-----------------------------------------------------------------------

class Message(object):

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
