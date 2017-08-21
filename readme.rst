-------------------
Purpose
-------------------

The purpose of this code base is to provide an easy interface for
creating a Raspberry Pi-based coffee camera.  I found that there
were too many people walking back and forth to the empty coffee
pot and decided to make this little project with some parts that
I had mostly laying around.

-------------------
Equipment
-------------------

 - raspberry pi (all should work, but may need extra hardware)
 - compatible camera
 - wifi dongle (optional)
 - case (optional)
 - power adapter

-------------------
Setup
-------------------

===================
Installation
===================

At this time, you *must* be running this project on a Raspberry Pi
or the dependency ``picamera`` will not be runnable::

    pip install coffeecam

===================
Environment Setup
===================

How to set up your linux environment, RAM drive, etc.

-------------------
Running
-------------------

This package will serve up pages by simply starting it.  If you have
installed coffeecam into the path ``/home/myname/py3env``, then
you can simply::

    /home/myname/py3env/bin/coffeecam

to begin package execution.

===================
Dependencies
===================

Add dependencies are pip-installable:

 - flask
 - humanize
 - picamera
 - waitress

This has only been tested on Raspbian, though it may work with other
distributions.

-------------------
How it Works
-------------------

This package will run a flask instance which serves up a page containing
a screenshot.  A new camera picture is triggered by each client every
10s.  If the current image is less than 2s old, then the new image request
is ignored.