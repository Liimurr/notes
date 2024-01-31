Test-Ansible
============
Prerequisites
-------------
- Installed Vagrant (see :doc:`Install-Vagrant`)
- Installed Ansible
- Running on Ansible Control Node (see :doc:`Build-Ansible Control Node`)

.. tab-set:: 

   .. tab-item:: OS: Windows

      vagrant plugin install virtualbox_WSL2

Procedure
---------
.. dropdown:: Initialize-Vagrant VM
   :open:

   .. tab-set:: 
      
      .. tab-item:: OS: Windows

         .. code-block:: shell
            :caption: shell (WSL)

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

      $URI = 'https://raw.githubusercontent.com/hashicorp/vagrant/main/keys/vagrant.key.ed25519'
      $OutFile = '.vagrant/machines/default/virtualbox/vagrant.key.ed25519'
      Invoke-WebRequest -Uri $URI -OutFile $OutFile

      New-Item -Path ./inventory/vagrant.ini -ItemType File -Force -Value @"
      [webservers]
      testserver ansible_port=2222

      [webservers:vars]
      ansible_host=127.0.0.1
      ansible_user=vagrant
      ansible_private_key_file=$OutFile
      "@

   