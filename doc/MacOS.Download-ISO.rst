MacOS.Download-ISO
==================
Prerequisites
-------------
Requires MacOS Operating System

Procedure
---------
.. code-block:: shell
   :caption: List Available Installers (take note of the size)

   # List all available MacOS versions
   softwareupdate --list-full-installer

Create Disk Image with enough space to hold the installer (Format: MacOS Extended Jorunal) [1]_

.. code-block:: shell
   SemanticVersion='14.4.1'
   softwareupdate --fetch-full-installer --full-installer-version $SemanticVersion

.. code-block:: shell

   Installer='Install macOS Sonoma.app'
   DMG='~/Desktop/macos-14.4.1.dmg'
   Output='~/Desktop/macos-14.4.1'
   Volume="macos-14.4.1"

   sudo /Applications/$Installer/Contents/Resources/createinstallmedia --volume /Volumes/$Volume
   diskutil eject /Volumes/$Volume
   # Convert the .dmg to .cdr
   hdiutil convert $DMG -format UDTO -o $Output
   # Rename the file to .iso
   mv $Output.cdr $Output.iso

See Also
--------
.. card::

   **External Links**
   
   - `Create Disk Image <https://support.apple.com/guide/disk-utility/create-a-disk-image-dskutl11888/mac>`_
   - `Create Bootable Installer <https://support.apple.com/en-us/101578>`_
   - `Software Update Man Page <https://ss64.com/mac/softwareupdate.html>`_
   - `Creating ISO Image On MacOS <https://macpaw.com/how-to/create-iso-file>`_
   
   **Footnotes**
   
   .. [1] `Create Disk Image <https://support.apple.com/guide/disk-utility/create-a-disk-image-dskutl11888/mac>`_

