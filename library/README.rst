https://shop.pimoroni.com/products/button-shim

Five tactile push buttons and one super-bright RGB LED indicator, ideal
for adding extra input and visual notifications to your Raspberry Pi
alongside most other HATs and pHATs!

Installing
----------

Full install (recommended):
~~~~~~~~~~~~~~~~~~~~~~~~~~~

We've created an easy installation script that will install all
pre-requisites and get your Buttom SHIM. up and running with minimal
efforts. To run it, fire up Terminal which you'll find in Menu ->
Accessories -> Terminal on your Raspberry Pi desktop, as illustrated
below:

.. figure:: http://get.pimoroni.com/resources/github-repo-terminal.png
   :alt: Finding the terminal

In the new terminal window type the command exactly as it appears below
(check for typos) and follow the on-screen instructions:

.. code:: bash

    curl https://get.pimoroni.com/buttonshim | bash

Alternatively, on Raspbian, you can download the ``pimoroni-dashboard``
and install your product by browsing to the relevant entry:

.. code:: bash

    sudo apt-get install pimoroni

(you will find the Dashboard under 'Accessories' too, in the Pi menu -
or just run ``pimoroni-dashboard`` at the command line)

If you choose to download examples you'll find them in
``/home/pi/Pimoroni/buttonshim/``.

Manual install:
~~~~~~~~~~~~~~~

Library install for Python 3:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

on Raspbian:

.. code:: bash

    sudo apt-get install python3-buttonshim

other environments:

.. code:: bash

    sudo pip3 install buttonshim

Library install for Python 2:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

on Raspbian:

.. code:: bash

    sudo apt-get install python-buttonshim

other environments:

.. code:: bash

    sudo pip2 install buttonshim

Development:
~~~~~~~~~~~~

If you want to contribute, or like living on the edge of your seat by
having the latest code, you should clone this repository, ``cd`` to the
library directory, and run:

.. code:: bash

    sudo python3 setup.py install

(or ``sudo python setup.py install`` whichever your primary Python
environment may be)

Documentation & Support
-----------------------

-  Guides and tutorials - https://learn.pimoroni.com/button-shim
-  Function reference - http://docs.pimoroni.com/buttonshim/
-  GPIO Pinout - https://pinout.xyz/pinout/buttonshim
-  Get help - http://forums.pimoroni.com/c/support

Unofficial / Third-party libraries
----------------------------------

-  Go library by Tom Mitchell - https://github.com/tomnz/button-shim-go
