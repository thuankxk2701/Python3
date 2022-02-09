#!/usr/bin/env python
import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GLib  # noqa


def hello_world(widget, data=None):
    print("Hello World")


def close_request_cb(widget, data=None):
    global running
    running = False


running = True
window = Gtk.Window()
window.connect("close-request", close_request_cb)
button = Gtk.Button(label="Hello World")
button.connect("clicked", hello_world, None)

window.set_child(button)
window.show()

context = GLib.MainContext.default()
while running:
    context.iteration(True)