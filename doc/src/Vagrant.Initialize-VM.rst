Vagrant.Initialize-VM
=====================
Prerequisites
-------------
Configure WSL on Windows
+++++++++++++++++++++++++
.. tab-set:: 

   .. tab-item:: HostOS: Windows

      .. dropdown:: In WSL, Add-Content to ``~/.profile``
         :open:

         .. code-block:: shell
            :caption: ~/profile (WSL)

            export VAGRANT_WSL_ENABLE_WINDOWS_ACCESS="1"
            export PATH="$PATH:/mnt/c/Program Files/Oracle/VirtualBox"

      .. dropdown:: In WSL, set restrictive file permissions for windows mounted Files
         :open:

         1. 
            .. code-block:: shell
               :caption: shell (WSL)

               sudo nano /etc/wsl.conf

         2.
         
            .. code-block:: ini
               :caption: add lines to /etc/wsl.conf

               [automount]
               options = "umask=077"
         
         3. Press ``Ctrl+O`` to save and ``Ctrl+X`` to exit

         4. Shutdown WSL 

         5. Wait 8 Seconds for the changes to take effect [1]_

         6. Start WSL

      .. dropdown:: In Windows, set restrictive file permissions for ssh key file
         :open:

         .. code-block:: powershell
            :caption: PowerShell

            cd E:/path/to/vagrant/project
            icacls ./.vagrant.d/insecure_private_key /remove "NT AUTHORITY\Authenticated Users"

Procedure
---------
Initialize-Vagrant
++++++++++++++++++++++
.. code-block:: shell
   :caption: shell / cmd (Host Machine)
   
   vagrant box add --name my-box /path/to/the/new.box
   vagrant init my-box

Edit-Vatgrantfile
+++++++++++++++++
.. tab-set:: 

   .. tab-item:: GuestOS: Windows

      .. dropdown:: Add-Content to ``Vagrantfile`` [2]_ [3]_
         :open:

         .. code-block:: ruby
            :caption: Vagrantfile (Host Machine)
         
            config.ssh.shell = "powershell"
            config.vm.guest = :windows
            config.ssh.insert_key = false # can't insert ssh on windows
            config.vm.synced_folder '.', '/vagrant', disabled: true # can't sync folders on wsl to windows virtualbox

Next Steps
----------
:doc:`Vagrant.Up-VM`

See Also
--------
.. card::

   **Footnotes**

   .. [1] `can't insert ssh on windows <https://github.com/hashicorp/vagrant/issues/12344#issuecomment-845065364>`_
   .. [2] `windows required setting: config-vm-guest <https://developer.hashicorp.com/vagrant/docs/vagrantfile/machine_settings#config-vm-guest>`_
   .. [3] `remove synced folders <https://superuser.com/a/757031>`_