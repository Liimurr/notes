Build-Ansible Control Node
==========================

Prerequisites
-------------

.. tab-set:: 

   .. tab-item:: OS: Windows
      :sync: win
   
      :doc:`Install-WSL`

Procedure
---------

.. tab-set:: 

   .. tab-item:: OS: MacOS

      .. code-block:: shell
         :caption: shell

         yes | brew install ansible

   .. tab-item:: OS: Windows
      :sync: win

      .. card::

         1. Launch WSL Terminal

         2. On WSL, Install Ansible:

            .. code-block:: shell
               :caption: shell (WSL)

               sudo apt-get update 
               sudo apt-get -y install python3-pip git libffi-dev 
               libssl-dev -y 
               pip3 install --yes --user ansible

   .. tab-item:: OS: Linux

      .. code-block:: shell
         :caption: shell
         
         pip3 install --yes --user ansible

See Also
--------

- Ansible: Up and Running Ch. 2 - Installation and Setup
- https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#control-node-requirements