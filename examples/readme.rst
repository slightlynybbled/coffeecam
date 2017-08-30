-------------------------
Configuration File Parameters
-------------------------

 1.  ``stats`` true/false, determines whether to show basic statistics or not
 2. ``host`` string, the host (probably you)
 3. ``framerate`` integer or float, determines the frame rate (higher creates more CPU load)
 4. ``resolution`` string, uses common values from the `pi resolutions <https://picamera.readthedocs.io/en/release-1.13/api_camera.html#piresolution>`_
 5. ``camera`` string, ``pi``, ``opencv``, or ``test`` in order to specify the camera to use

=====
Notes
=====

The ``framerate`` and ``resolution`` parameters are currently only supported
when using the pi camera.
