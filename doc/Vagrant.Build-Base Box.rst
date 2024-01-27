Vagrant.Build-Base Box
======================

Prerequisites
-------------

.. tab-set:: 

   .. tab-item:: Provider: VMWare

      .. card::

         **Install:** `Vagrant VMWare Utility <https://developer.hashicorp.com/vagrant/docs/providers/vmware/vagrant-vmware-utility>`_

         **Install:** Vagrant Plugin [2]_

            .. code-block:: powershell

               vagrant plugin install vagrant-vmware-desktop 

   .. tab-item:: Provider: VirtualBox

      .. card::
         
         **Disable:** Hyper-V [3]_

            .. code-block:: powershell

               Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All

Install SSH Server on Guest VM
------------------------------

.. tab-set::
   
   .. tab-item:: GuestOS: Windows
      
      .. raw:: html

         <embed>
            <script src="https://gist.github.com/Liimurr/41f9192fd2cfb4249e7a84291ff5c7b5.js"></script>
         </embed>

   .. tab-item:: GuestOS: MacOS
      
      .. card::

         .. tab-set::

            .. tab-item:: Ventura

               .. list-table::
                  
                  * Enable **System Settings** \| **Sharing** \| **File Sharing**
                  * Enable **System Settings** \| **Sharing** \| **Remote Login**
                  * Disable **System Settings** \| **Display Energy** \| **Sleeping when the display is off**

            .. tab-item:: Monterey

               .. list-table::
                  
                  * - **Enable**
                    - ``System Prefferences`` → ``Sharing`` → ``Remote Login``
                  * - **Enable** 
                    - ``System Prefferences`` → ``Energy Saver`` → ``Prevent your Mac from automatically sleeping when the display is off``
                  * - **Enable**
                    - ``System Prefferences`` → ``File Sharing``
                  * - **Enable**
                    - ``System Prefferences`` → ``File Sharing`` → ``vagrant's Public Folder`` → ``Users`` → ``Everyone`` → ``Read & Write``

         .. code-block:: bash
            :linenos:

            sudo chmod go-w ~/
            sudo mkdir ~/.ssh
            sudo chmod 700 ~/.ssh
            sudo touch ~/.ssh/authorized_keys
            sudo chmod 600 ~/.ssh/authorized_keys

   .. tab-item:: GuestOS: Ubuntu

      .. raw:: html

         <embed>
            <script src="https://gist.github.com/Liimurr/454879c5f60ea31ea9e43c37acff0286.js"></script>
         </embed>
         
Test Host to Guest SSH Connection
---------------------------------

.. tab-set::

   .. tab-item:: Provider: VirtualBox

      .. card::

         GoTo
         ++++ 

         VirtualBox > Your Virtual Machine > Settings > Network > Advanced > Port Forwarding

         Add-Rule
         ++++++++

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

         Test-Connection
         +++++++++++++++

         .. code-block:: shell 
         
            ssh vagrant@localhost -p 2222

      .. note::

         - The Host Port can be any port you wish to use on your host machine. The Guest Port must be 22, as that is the port the SSH server on the guest machine is listening on.
         - The Name field is arbitrary, but it is recommended to use a name that describes the purpose of the rule.

.. [2] https://developer.hashicorp.com/vagrant/docs/providers/vmware/installation
.. [3] https://developer.hashicorp.com/vagrant/docs/installation#windows-virtualbox-and-hyper-v
