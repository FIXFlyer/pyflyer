#! /usr/bin/env python
#
# create a session
# parameterise it with a policy class which controls the protocol
# open the session
# send order(s)
# get responses
# etc.

# session = Session(FIX44)
# order =


# Validation of the order occurs when it's submitted to the session.
# How is modification and cancel/replace supported?
# - Do you create a new order, and call replace with it?
#   - Cloning it first?
# - Can you queue up changes to an existing order?



class Persistence(object):
    pass


class Logger(object):
    pass


class SessionListener(object):
    """Listener for events on the Flyer Engine session."""
    pass


class Session(object):
    """Flyer Engine session."""

    def __init__(self):
        pass

    def subscribe(self):
        pass

    def connect(self):
        pass

    def disconnect(self):
        pass


#---------------------------------------------------------------

class OrderIdGenerator(object):
    pass


class Trade(object):

    def __init__(self):
        self._price = 0
        self._amount = 0
        self._match_id = 0
        self._timestamp = 0
        return


class OrderListener(object):

    def pending(self):
        pass

    def accepted(self):
        pass

    def rejected(self):
        pass

    def canceled(self):
        pass

    def fill(self):
        pass

    def replaced(self):
        pass


class Order(object):

    def __init__(self, session):
        return

    def set_tag(self, tag, value):
        """Set the value of a FIX tag for this order.

        tag -- FIX tag number.
        value -- This value will be converted to the appropriate type for the FIX field.
        """
        pass

    def submit(self):
        """Submit this order for execution via the specified session."""
        pass

    def cancel(self):
        """Request cancelation of this order."""
        pass

    def modify(self):
        """Request modification of this order."""
        pass

    def state(self):
        """Return the current state of this order."""
        pass

    def next_in_chain(self):
        """Return this order's replacement, if any."""
        pass

    def previous_in_chain(self):
        """Return the order this order replaced, if any."""
        pass

    def fills(self):
        """Return an iterator for the fills received for this order."""
        pass

    def leaves(self):
        pass

    def amount(self):
        pass

    def average_price(self):
        pass



def main():

    o1 = Order()

    pass


if __name__ == "__main__":
    main()
