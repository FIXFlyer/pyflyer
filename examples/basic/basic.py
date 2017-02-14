

import flyer
import pyuv
import signal
import socket



class PyuvAdaptor(object):
    """pyuv event loop adaptor."""

    def __init__(self, listener):
        self._listener = listener
        self._is_connected = False
        self._is_writable = False
        self._loop = pyuv.Loop.default_loop()
        return

    def connect(self, host, port):
        self._handle = pyuv.TCP(self._loop)
        self._handle.connect((host, int(port)), self._on_connected)
        self._handle.start_read(self._on_read)

        self._sigint_handler = pyuv.Signal(self._loop)
        self._sigint_handler.start(self._on_signal, signal.SIGINT)
        return

    def disconnect(self):
        self._handle.shutdown(self._on_disconnected)
        return

    def send(self, buf, buflen):
        self._handle.write(buf, self._on_written)
        return buflen

    def run(self):
        self._loop.run()
        return

    def stop(self):
        self._loop.stop()
        return

    def _on_connected(self, handle, error):
        print("_on_connected")
        self._listener.on_connected()
        return

    def _on_disconnected(self, handle, error):
        print("_on_disconnected")
        self._listener.on_disconnected()
        return

    def _on_read(self, handle, data, error):
        print("_on_read", len(data) if data else 0)
        self._listener.on_data(data)
        return

    def _on_written(self, handle, error):
        print("_on_written")
        return

    def _on_signal(self, handler, signal):
        print("_on_signal", int(signal))
        self.stop()
        return



class BasicExample(flyer.Listener):

    def __init__(self, username, password):
        self._username = username
        self._password = password

        self._manager = flyer.ApplicationManager(self, self)
        self._adaptor = PyuvAdaptor(self)
        return

    def start(self):
        self._adaptor.connect("127.0.0.1", 12917)
        self._adaptor.run()
        self._adaptor.disconnect()
        return


    # Flyer Sender interface.

    def send_bytes(self, buf, buflen):
        self._adaptor.send(buf, buflen)
        return

    def needs_flush(self):
        # Not needed for PyUV, because write() guarantees to send the
        # whole buffer.
        return


    # Flyer Listener interface
    #
    # Because we inherit from the interface, and because it provides a
    # default, do-nothing implementation of all functions, we only
    # need to implement those that we actually use.

    def on_logon(self, event):
        print("on_logon")
        return

    def on_disconnect(self):
        print("on_disconnect")
        self._adaptor.stop()
        return

    def on_heartbeat(self, event):
        print("on_heartbeat")
        return

    def on_error(self, event):
        print("on_error")
        return


    # Network adaptor callbacks

    def on_data(self, data):
        print("on_data")
        self._manager.receive_bytes(data, len(data) if data else 0)
        return

    def on_connected(self):
        print("TCP session connected.")
        self._manager.logon(self._username, self._password)
        return

    def on_disconnected(self):
        print("TCP session disconnected.")
        return



if __name__ == "__main__":

    example = BasicExample("guest", "guest")
    example.start()
