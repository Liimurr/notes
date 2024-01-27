🧰Vagrant.Build-Base Box
========================

Prerequisites
-------------

.. tab-set:: 

   .. tab-item:: Provider: VMWare

      .. dropdown:: Install-Vagrant VMWare Utility [1]_
         :open:

         `Downloads Page <https://developer.hashicorp.com/vagrant/install/vmware>`_

      .. dropdown:: Install-Vagrant Plugin [2]_
         :open:
         
         .. code-block:: powershell

            vagrant plugin install vagrant-vmware-desktop 

   .. tab-item:: Provider: VirtualBox

      .. dropdown:: Disable-HyperV [3]_
         :open:

         .. code-block:: powershell

            Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All

Initialize-VM Virtual Hardware
------------------------------

.. tab-set:: 

   .. tab-item:: GuestOS: MacOS
      
      - 1 Processor

   .. tab-item:: GuestOS: Windows

      - 1+ Processors

- `Dynamically Allocated 250GB HD <https://developer.hashicorp.com/vagrant/docs/boxes/base#disk-space>`_
- `512MB of RAM <https://developer.hashicorp.com/vagrant/docs/boxes/base#memory>`_
- `Disable Audio and USB <https://developer.hashicorp.com/vagrant/docs/boxes/base#peripherals-audio-usb-etc>`_


Install-SSH Server on Guest VM
------------------------------

.. tab-set::
   
   .. tab-item:: GuestOS: Windows
      
      .. code-block:: powershell

         # see: https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell#install-openssh-for-windows

         # Install the OpenSSH Server
         Add-WindowsCapability -Online -Name 'OpenSSH.Server~~~~0.0.1.0'

         # Start the sshd service
         Start-Service sshd

         # OPTIONAL but recommended:
         Set-Service -Name sshd -StartupType 'Automatic'

         # Confirm the Firewall rule is configured. It should be created automatically by setup. Run the following to verify
         if (!(Get-NetFirewallRule -Name "OpenSSH-Server-In-TCP" -ErrorAction SilentlyContinue | Select-Object Name, Enabled)) {
           Write-Output "Firewall Rule 'OpenSSH-Server-In-TCP' does not exist, creating it..."
           New-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
         } else {
           Write-Output "Firewall rule 'OpenSSH-Server-In-TCP' has been created and exists."
         }

   .. tab-item:: GuestOS: MacOS
   
      .. tab-set::   

         .. tab-item:: Ventura   

            .. dropdown:: Edit-System Settings
               :open:   

               .. tab-set::    

                  .. tab-item:: Manual   

                     - Enable **System Settings** \| **Sharing** \| **File Sharing**
                     - Enable **System Settings** \| **Sharing** \| **Remote Login**
                     - Disable **System Settings** \| **Display Energy** \| **Sleeping when the display is off**   

                  .. tab-item:: Script   

                     .. code-block:: bash
                        
                        sudo systemsetup -setremotelogin on
                        sudo systemsetup -setsleep off
                        sudo systemsetup -setwakeonnetworkaccess on   

         .. tab-item:: Monterey
            
            .. dropdown:: Edit-System Prefferences
               :open:   

               .. tab-set::    

                  .. tab-item:: Manual   

                     - Enable **System Prefferences** \| **Sharing** \| **Remote Login**
                     - Enable **System Prefferences** \| **Energy Saver** \| **Prevent your Mac from automatically sleeping when the display is off**
                     - Enable **System Prefferences** \| **File Sharing**
                     - Enable **System Prefferences** \| **File Sharing** \| **vagrant's Public Folder** \| **Users** \| **Everyone** \| **Read & Write**   

                  .. tab-item:: Script   

                     .. code-block:: bash
                        
                        sudo systemsetup -setremotelogin on
                        sudo systemsetup -setsleep off
                        sudo systemsetup -setwakeonnetworkaccess on   

      .. dropdown:: Initialize-Authorizied Keys
         :open:   
         
         .. code-block:: bash   
            
            sudo chmod go-w ~/
            sudo mkdir ~/.ssh
            sudo chmod 700 ~/.ssh
            sudo touch ~/.ssh/authorized_keys
            sudo chmod 600 ~/.ssh/authorized_keys

   .. tab-item:: GuestOS: Ubuntu

      .. code-block:: bash
            
         sudo apt-get install openssh-server
         sudo systemctl enable ssh
         sudo systemctl start ssh
         
Test Host to Guest SSH Connection
---------------------------------

.. tab-set::

   .. tab-item:: Provider: VirtualBox

      .. dropdown:: Register-SSH Port Forwarding Rule
         :open:

         1. GoTo **VirtualBox** \| **Your Virtual Machine** \| **Settings** \| **Network** \| **Advanced** \| **Port Forwarding**

         2. Add-Rule

            .. list-table::
               :header-rows: 0
      
               * - **Name**
                 - SSH
               * - **Protocol**
                 - TCP
               * - **Host Port**
                 - 2222
               * - **Guest Port**
                 - 22
            
            .. note::

               - The Host Port can be any port you wish to use on your host machine. The Guest Port must be 22, as that is the port the SSH server on the guest machine is listening on.
               - The Name field is arbitrary, but it is recommended to use a name that describes the purpose of the rule.

      .. dropdown:: Test-SSH Connection
         :open:

         .. code-block:: shell 
      
            ssh vagrant@localhost -p 2222


.. [1] https://developer.hashicorp.com/vagrant/docs/providers/vmware/vagrant-vmware-utility
.. [2] https://developer.hashicorp.com/vagrant/docs/providers/vmware/installation
.. [3] https://developer.hashicorp.com/vagrant/docs/installation#windows-virtualbox-and-hyper-v
