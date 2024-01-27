Vagrant.Build-Base Box
========================

Prerequisites
-------------

.. tab-set:: 

   .. tab-item:: Provider: VirtualBox
      :sync: virtualbox

      .. dropdown:: Disable-HyperV [3]_
         :open:

         .. code-block:: powershell

            Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All

   .. tab-item:: Provider: VMWare
      :sync: vmware

      .. warning:: 
         
         For Vagrant boxes, GuestOS: Windows 11 and Provider: VMWare Workstation 17 are incompatible.
         Vagrant has no support for TPM 2.0 encryption yet, and VMWare Workstation 17 requires it for Windows 11.

      .. dropdown:: Install-Vagrant VMWare Utility [1]_
         :open:

         `Downloads Page <https://developer.hashicorp.com/vagrant/install/vmware>`_

      .. dropdown:: Install-Vagrant Plugin [2]_
         :open:
         
         .. code-block:: powershell

            vagrant plugin install vagrant-vmware-desktop 

Initialize-VM Virtual Hardware
------------------------------

.. tab-set:: 

   .. tab-item:: GuestOS: MacOS
      :sync: macos
      
      - 1 Processor
      - 2048MB+ of RAM

   .. tab-item:: GuestOS: Windows
      :sync: windows

      - 1+ Processors
      - `4096MB+ of RAM <https://support.microsoft.com/en-us/windows/windows-11-system-requirements-86c11283-ea52-4782-9efd-7674389a7ba3>`_
   
   .. tab-item:: GuestOS: Ubuntu
      :sync: ubuntu

      - 1+ Processors
      - `512MB+ of RAM <https://developer.hashicorp.com/vagrant/docs/boxes/base#memory>`_

- `Dynamically Allocated 250GB HD <https://developer.hashicorp.com/vagrant/docs/boxes/base#disk-space>`_
- `Disable Audio and USB <https://developer.hashicorp.com/vagrant/docs/boxes/base#peripherals-audio-usb-etc>`_

Install-Operating System
------------------------

.. tab-set:: 

   .. tab-item:: GuestOS: MacOS
      :sync: macos

      Create a local user account with the username ``vagrant`` and password ``vagrant``
      
   .. tab-item:: GuestOS: Windows
      :sync: windows

      1. During installation, at "select a country" press ``Shift+F10`` to open command prompt, then enter  ``OOBE\BYPASSNRO``
      2. After restart, press ``Shift+F10`` to open command prompt, then enter ``ipconfig /release``
      3. Continue installation without internet connection
      4. Create a local user account with the username ``vagrant`` and password ``vagrant`` (`ref <https://developer.hashicorp.com/vagrant/docs/boxes/base#vagrant-user>`_)

   .. tab-item:: GuestOS: Ubuntu
      :sync: ubuntu

      Create a local user account with the username ``vagrant`` and password ``vagrant`` 

Install-SSH Server on Guest VM
------------------------------

.. tab-set::
   
   .. tab-item:: GuestOS: MacOS
      :sync: macos

      .. tab-set::   

         .. tab-item:: Ventura   
            :sync: ventura

            .. dropdown:: Edit-System Settings
               :open:   

               .. tab-set::    

                  .. tab-item:: Manual   

                     - Enable **System Settings** \| **Sharing** \| **File Sharing**
                     - Enable **System Settings** \| **Sharing** \| **Remote Login**
                     - Disable **System Settings** \| **Display Energy** \| **Sleeping when the display is off**   

                  .. tab-item:: Script   

                     .. literalinclude:: /../src/sys-admin-scripts/agent/install-ssh-server/macos.sh
                        :language: bash

         .. tab-item:: Monterey
            :sync: monterey
            
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

   .. tab-item:: GuestOS: Windows
      :sync: windows
      
      .. literalinclude:: /../src/sys-admin-scripts/agent/install-ssh-server/windows.ps1
         :language: powershell

   .. tab-item:: GuestOS: Ubuntu
      :sync: ubuntu

      .. literalinclude:: /../src/sys-admin-scripts/agent/install-ssh-server/ubuntu.sh
         :language: bash
         
Test-Host to Guest SSH Connection
---------------------------------

.. tab-set::

   .. tab-item:: Provider: VirtualBox
      :sync: virtualbox

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

   .. tab-item:: Provider: VMWare
      :sync: vmware

      TODO

.. [1] https://developer.hashicorp.com/vagrant/docs/providers/vmware/vagrant-vmware-utility
.. [2] https://developer.hashicorp.com/vagrant/docs/providers/vmware/installation
.. [3] https://developer.hashicorp.com/vagrant/docs/installation#windows-virtualbox-and-hyper-v
