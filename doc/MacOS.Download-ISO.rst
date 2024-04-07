MacOS.Download-ISO
==================
Prerequisites
-------------
Requires MacOS Operating System

Procedure
---------
.. code-block:: shell
   :caption: "List Available Installers (take not of the size)"

   # List all available MacOS versions
   softwareupdate --list-full-installer

Create Disk Image with enough space to hold the installer [1]_

See Also
--------
.. card::

   **External Links**
   
   - `Create Disk Image <https://support.apple.com/guide/disk-utility/create-a-disk-image-dskutl11888/mac>`_
   - `Create Bootable Installer <https://support.apple.com/en-us/101578>`_
   - `Software Update Man Page <https://ss64.com/mac/softwareupdate.html>`_
   - `Vagrant Windows Base Box Configuration <https://developer.hashicorp.com/vagrant/docs/boxes/base#base-windows-configuration>`_
   - `Stack Overflow Edit Group Policy <https://serverfault.com/a/848519>`_
   - `Download List of Registry Keys <https://www.microsoft.com/en-us/download/confirmation.aspx?id=25250>`_
   - `Example: Using WSL Host with Windows Guest VM <https://discuss.hashicorp.com/t/winrm-port-does-not-work-in-vagrantfile/54601>`_
   - `Setup WinRM on Windows <https://github.com/AlbanAndrieu/ansible-windows/blob/master/files/ConfigureRemotingForAnsible.ps1>`_
   - https://woshub.com/using-psremoting-winrm-non-domain-workgroup/
   - https://kevrocks67.github.io/blog/powershell-remote-management-from-linux.html
   
   **Footnotes**
   
   .. [1] `Create Disk Image <https://support.apple.com/guide/disk-utility/create-a-disk-image-dskutl11888/mac>`_
   .. [2] https://developer.hashicorp.com/vagrant/docs/providers/vmware/installation
   .. [3] https://developer.hashicorp.com/vagrant/docs/installation#windows-virtualbox-and-hyper-v
   .. [4] https://developer.hashicorp.com/vagrant/docs/boxes/base#base-windows-configuration

