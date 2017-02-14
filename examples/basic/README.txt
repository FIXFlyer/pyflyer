Basic Example
=============

This is close to being the most simple application using the Flyer
Engine Python API possible.

It connects to the engine's TCP application port, logs on, waits for a
heartbeat, and then logs off.  It demonstrates only the basic
framework for an SDK application.


Testing the Example
-------------------

The easiest way to test this application is to use the "basic" example
distributed with the Flyer Engine.

Follow the instructions in the engine's Install and Admin Guide to
unpack the engine and install your license file.  Then see the "Engine
Lab" chapter (page 419 for v6.1.1) for instructions in setting up the
basic example.

To test this program, you really only need to have "fbuy" running, but
crucially, you cannot have "appbuy" running -- this application will
take its place.

You need to edit the configuration for the fbuy engine, distributed in
example-engines/basic/buyside/buyside-conf.xml, and add the following
two lines to the

    <application-session>

tag with

    username = "guest"

(anywhere within the tag is fine):

    enable-heartbeats = "true"
    heartbeat-timeout = "1"

and then restart the engine.

If you do not change this configuration, the exaple application will
wait for a heartbeat packet forever.


Notes
-----

The main class in this example is derived from the ExampleBase class,
which can be found in examples/adaptor.  This base class implements
some basic cross-platform socket functionality and provides an adaptor
from the Flyer C++ API to a that thin wrapper of the basic Berkeley
sockets API.  It uses libevent (from http://libevent.org) to provide a
portable event loop for Linux, MacOS and Windows.
