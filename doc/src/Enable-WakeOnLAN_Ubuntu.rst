Enable Wake-On-LAN (Ubuntu)
===========================

Prerequisites
-------------

.. card:: Ubuntu Machine

   An Ubuntu machine with network access and sudo privileges.

.. card:: Wake-on-LAN enabled in BIOS

   Ensure Wake-on-LAN (WoL) is enabled in the BIOS or UEFI settings of the machine.

Procedure
---------

.. code-block:: shell
   :caption: Install `ethtool` to manage Wake-on-LAN settings

   sudo apt install ethtool

.. code-block:: shell
   :caption: Check if Wake-on-LAN is enabled on your network interface

   # Replace 'enp36s0f1' with your actual network interface name
   sudo ethtool enp36s0f1

   # Look for the 'Wake-on' field. 'g' means WoL is enabled, 'd' means it is disabled.

.. card:: Enable Wake-on-LAN

   If Wake-on-LAN is disabled (Wake-on: d), run the following command:

   .. code-block:: shell
      :caption: Enable Wake-on-LAN

      sudo ethtool -s enp36s0f1 wol g

.. code-block:: shell
   :caption: Make Wake-on-LAN persistent across reboots using a systemd service

   # Create a systemd service file
   sudo nano /etc/systemd/system/wol.service

   # Add the following content:
   [Unit]
   Description=Enable Wake-on-LAN
   After=network-online.target
   Wants=network-online.target

   [Service]
   Type=oneshot
   ExecStart=/sbin/ethtool -s enp36s0f1 wol g

   [Install]
   WantedBy=multi-user.target

   # Reload systemd to apply the changes
   sudo systemctl daemon-reload

   # Enable the service to run at boot
   sudo systemctl enable wol.service

   # Start the service manually to test
   sudo systemctl start wol.service

.. code-block:: shell
   :caption: Check the status of the Wake-on-LAN service

   sudo systemctl status wol.service

   # Ensure the service is active and executed successfully.

.. code-block:: shell
   :caption: Verify Wake-on-LAN is enabled after reboot

   sudo reboot
   sudo ethtool enp36s0f1

   # After reboot, the 'Wake-on' field should show 'g'.

.. card:: Troubleshooting NetworkManager Reset

   If NetworkManager resets WoL settings after reboot:

   .. code-block:: shell
      :caption: Disable NetworkManager power management

      sudo nano /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf

      # Add the following line to disable power management:
      [connection]
      wifi.powersave = 2

      # Restart NetworkManager
      sudo systemctl restart NetworkManager

   .. card:: Reboot the system to test if Wake-on-LAN persists after applying these changes.

See Also
--------

.. card::

   **External Links**

   - https://linux.die.net/man/8/ethtool
   - https://www.freedesktop.org/wiki/Software/systemd/
