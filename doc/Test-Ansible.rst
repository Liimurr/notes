Test-Ansible
============
Brief
-----

1. Install-Prerequisites
2. Initialize-Vagrant VM
3. Initialize-Ansible Inventory

Prerequisites
-------------
- Installed Vagrant (see :doc:`Install-Vagrant`)
- Installed Ansible (see :ref:`Install Ansible`)
- Running on Ansible Control Node (see :doc:`Build-Ansible Control Node`)

.. tab-set:: 

   .. tab-item:: OS: Windows

      Installed Vagrant on WSL

      .. tab-set:: 

         .. tab-item:: VirtualBox

            .. code-block:: shell
               :caption: shell (WSL)
            
               vagrant plugin install virtualbox_WSL2

Procedure
---------
.. dropdown:: Initialize-Vagrant VM
   :open:

   .. tab-set:: 
      
      .. tab-item:: OS: Windows

         .. code-block:: shell
            :caption: shell (WSL)

            ANSIBLE_PLAYBOOKS=$(wslpath -u 'E:\assets\ansible-playbooks')
            VAGRANT_BOX=win-11
            # ------------------------------
            cd $ANSIBLE_PLAYBOOKS
            vagrant init $VAGRANT_BOX
            vagrant up --provider virtualbox

      .. tab-item:: OS: Other

         .. code-block:: shell
            :caption: shell (WSL)

            vagrant init win-11
            vagrant up --provider virtualbox
   
.. dropdown:: Initialize-Ansible Inventory
   :open:

   .. code-block:: powershell
      :caption: PowerShell

      $PrivateKeyFile = '.vagrant.d/insecure_private_key'
      
      New-Item -Path ./inventory/vagrant.ini -ItemType File -Force -Value @"
      [webservers]
      testserver ansible_port=2222

      [webservers:vars]
      ansible_host=127.0.0.1
      ansible_user=vagrant
      ansible_private_key_file=$PrivateKeyFile
      "@
      ---
      $remoteip=ip route | grep default | awk '{print $3}'
      $port=55986
      $user=vagrant
      New-Item -Path ./inventory/vagrant.ini -ItemType File -Force -Value @"
      [webservers]
      testserver ansible_port=$port

      [webservers:vars]
      ansible_host=$remoteip
      ansible_user=$user
      "@


   