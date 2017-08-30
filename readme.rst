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


-------------------
Running
-------------------

===================
From the Command Line
===================

This package will serve up pages by simply starting it.  If you have
installed coffeecam into the path ``/home/myname/py3env``, then
you can simply::

    $ sudo /home/myname/py3env/bin/coffeecam

Or, if you wish to specify a configuration file::

    $ sudo /home/myname/py3env/bin/coffeecam -c /my/config/file.json

The configuration file is not required to begin execution.  If a configuration
file is not supplied, defaults will be assumed.

An example configuration file may be found in the `examples directory <https://github.com/slightlynybbled/coffeecam/tree/master/examples>`_.

===================
At Reboot
===================

From Raspbian, you may wish to add to the crontab in order to start up at boot::

    $ sudo su
    $ crontab -e

Then append the line::

    @reboot /home/myname/py3env/bin/coffeecam

===================
Dependencies
===================

All dependencies are pip-installable:

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
a series of screenshots.  This originally had a different structure, but after
coming across `a blog post <https://blog.miguelgrinberg.com/post/video-streaming-with-flask>`_,
I decided to template the project after that.

-------------------
Contributions
-------------------

All contributions are welcome!  I could use some particular focus on adding tests
and documentation, but features are always welcome as well!

-------------------
Screenshots
-------------------

    .. image:: https://github.com/slightlynybbled/coffeecam/blob/master/docs/img/coffeecam-full.png
    .. image:: https://github.com/slightlynybbled/coffeecam/blob/master/docs/img/coffeecam-small.png
