-------------------------
Configuration File Parameters
-------------------------

 1. ``title`` string, the page title and window title (defaults to "coffeeCam")
 2. ``stats`` true/false, determines whether to show basic statistics or not (defaults to True)
 3. ``host`` string, the host (probably you, defaults to "coffeeCam")
 4. ``framerate`` integer or float, determines the frame rate (higher creates more CPU load, default to 2)
 5. ``resolution`` string, uses common values from the `pi resolutions <https://picamera.readthedocs.io/en/release-1.13/api_camera.html#piresolution>`_
 6. ``camera`` string, ``pi``, ``opencv``, or ``test`` in order to specify the camera to use (defaults to "pi")
 7. ``client time`` true/false, determines whether to set the system time based on the client time (defaults to False)
 8. ``port`` integer, the port number to serve on (defaults to 80)
 9. ``messages`` integer, the maximum number of messages to support (defaults to 0)

=====
Notes
=====

The ``framerate`` and ``resolution`` parameters are currently only supported
when using the pi camera.
