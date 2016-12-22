.. _hardware:

Hardware
========

Components
----------

(prices in USD and links as of spring 2016)

.. csv-table:: Part List
   :header: "Name", "Link", "Distributor", "Price", "Notes"

   "iRobot Create2","https://www.adafruit.com/products/2388","Adafruit",199.99,
   "Mini-DIN Connector Cable for iRobot Create 2 - 7 Pins - 6 feet","https://www.adafruit.com/products/2438","Adafruit",6.95,
   "4-channel I2C-safe Bi-directional Logic Level Converter - BSS138","https://www.adafruit.com/products/757","Adafruit",3.95,
   "UBEC DC/DC Step-Down (Buck) Converter - 5V @ 3A output","https://www.adafruit.com/products/1385","Adafruit",9.95,
   "Rugged Metal On/Off Switch with Green LED Ring - 16mm Green On/Off","https://www.adafruit.com/products/482","Adafruit",4.95,
   "Silicone Cover Stranded-Core Wire - 25ft 26AWG - Red","https://www.adafruit.com/products/2513","Adafruit",4.95,"For several Robots"
   "Silicone Cover Stranded-Core Wire - 25ft 26AWG - Black","https://www.adafruit.com/products/2517","Adafruit",4.95,"For several Robots"
   "Premium Female/Female Jumper Wires - 40 x 6""","https://www.adafruit.com/products/266","Adafruit",3.95,"For several Robots"
   "Multi-Colored Heat Shrink Pack - 3/32"" + 1/8"" + 3/16"" Diameters","https://www.adafruit.com/products/1649","Adafruit",4.95,"For several Robots"
   "Panel Mount USB Cable - A Male to A Female","https://www.adafruit.com/products/908","Adafruit",3.95,
   "Odroid C1+","http://ameridroid.com/products/odroid-c1","AmeriDroid",38.95,
   "WiFi Module 3","http://ameridroid.com/products/wifi-module-3","AmeriDroid",9.95,
   "DC Plug and Cable Assembly 2.5mm L-Type","http://ameridroid.com/products/dc-plug-and-cable-assembly-2-5mm-l-type","AmeriDroid",1.95,
   "Aluminum Standoff: 1/2"" Length, 4-40 Thread, F-F (4-Pack)","https://www.pololu.com/product/2091","Pololu",1.39,"For 2 robots each"
   "Machine Screw: #4-40, 1/4"" Length, Phillips (25-pack)","https://www.pololu.com/product/1960","Pololu",0.99,"For up to 12 robots each"
   "Machine Screw: #4-40, 5/16"" Length, Phillips (25-pack)","https://www.pololu.com/product/1961","Pololu",0.99,"For up to 12 robots each"
   "JST RCY Connector Pack, Female","https://www.pololu.com/product/1934","Pololu",1.75,"For up to 3 robots each"
   "JST RCY Connector Pack, Male","https://www.pololu.com/product/1935","Pololu",1.75,"For up to 3 robots each"
   "Parallax Standard Servo","https://www.parallax.com/product/900-00005","Parallax",12.99,"Optional"
   "PING))) Ultrasonic Distance Sensor ","https://www.parallax.com/product/28015","Parallax",29.99,"Optional"

Wiring
------

.. image:: wiring.png

Software
--------

Basic
^^^^^

* Download http://odroid.in/ubuntu_16.04lts/ubuntu-16.04-mate-odroid-c1-20160727.img.xz

* Extract::

    unxz ubuntu-16.04-mate-odroid-c1-20160727.img.xz

* Verify MD5::

    md5sum ubuntu-16.04-mate-odroid-c1-20160727.img
    f5dfee4a8ea919dd8afc4384431574e5  ubuntu-16.04-mate-odroid-c1-20160727.img

* Copy to SD-Card::

    sudo dd if=ubuntu-16.04-mate-odroid-c1-20160727.img of=</dev/path/of/card> bs=1M conv=fsync
    sync

Network
^^^^^^^

* Add `/etc/wpa_supplicant/wpa_supplicant.conf` with following content::

    network={
      ssid="<SSID>"
      psk="<password>"
      id_str="wifi"
    }

* Update `/etc/network/interfaces`::

    # interfaces(5) file used by ifup(8) and ifdown(8)
    # Include files from /etc/network/interfaces.d:
    source-directory /etc/network/interfaces.d

    auto lo
    iface lo inet loopback

    auto wlan0
    # allow-hotplug wlan0
    iface wlan0 inet manual
    wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
    iface wifi inet dhcp
    iface default inet dhcp

* Disable persistent network (so that SD-card can be used with any WiFi dongle)::

    sudo ln -s /dev/null /etc/udev/rules.d/80-net-setup-link.rules

PWM
^^^

* Update `/etc/modules`::

    # /etc/modules: kernel modules to load at boot time.
    #
    # This file contains the names of kernel modules that should be loaded
    # at boot time, one per line. Lines beginning with "#" are ignored.
    # Parameters can be specified after the module name.

    # ODROID HW PWM support (see http://odroid.com/dokuwiki/doku.php?id=en:c1_hardware_pwm)
    pwm-meson
    pwm-ctrl


GPIO Support
^^^^^^^^^^^^

* Add udev-rule: `/etc/udev/rules.d/90-gpio.rules`::

    SUBSYSTEM=="gpio", KERNEL=="gpiochip*", ACTION=="add", PROGRAM="/bin/sh -c 'chown root:gpio /sys/class/gpio/export /sys/class/gpio/unexport ; chmod 222 /sys/class/gpio/export /sys/class/gpio/unexport'"
    SUBSYSTEM=="gpio", KERNEL=="gpio*", ACTION=="add", PROGRAM="/bin/sh -c 'chown root:gpio /sys%p/active_low /sys%p/direction /sys%p/edge /sys%p/value ; chmod 660 /sys%p/active_low /sys%p/direction /sys%p/edge /sys%p/value'"

* Create GPIO group::

    sudo groupadd gpio

* Add user to group::

    sudo adduser odroid gpio

* Reboot


Additional Software
^^^^^^^^^^^^^^^^^^^

* Update the system::

    sudo apt update
    sudo apt upgrade

* Install additional packages::

    sudo apt install python3 python3-serial python3-scipy python3-numpy python3-matplotlib

Add User
^^^^^^^^

* Add user and assign groups::

    sudo adduser csci445
    sudo adduser csci445 gpio
    sudo adduser csci445 dialout

Debugging
---------

You can use the USB UART Kit for debugging, see http://odroid.com/dokuwiki/doku.php?id=en:usb_uart_kit for more details.
This will allow you to gain access to a shell using UART.

* On you host PC, add `/etc/udev/rules.d/99-odroiduart.rules` with the following content::

     SUBSYSTEM=="usb", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", MODE="0664", GROUP="plugdev"

  Make sure that your user is member of the `plugdev` group.

* To connect, use::

    picocom --baud 115200 /dev/ttyUSB0

  You can end the session by pressing Ctrl+A followed by Ctrl+X.
