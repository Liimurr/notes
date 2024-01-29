Build-Ansible Control Node
==========================

Prerequisites
-------------

.. tab-set:: 

   .. tab-item:: GuestOS: Windows
      :sync: win
   
      :doc:`Install-WSL`

Procedure
---------

.. tab-set:: 

   .. tab-item:: GuestOS: MacOS

      .. code-block:: shell
         :caption: shell

         brew install ansible

   .. tab-item:: GuestOS: Windows
      :sync: win

      .. card::

         1. Launch WSL Terminal

         2. On WSL, Install Ansible:

            .. code-block:: shell
               :caption: shell (WSL)

               sudo apt-get update 
               sudo apt-get install python3-pip git libffi-dev 
               libssl-dev -y 
               pip3 install --user ansible

   .. tab-item:: GuestOS: Linux

      .. code-block:: shell
         :caption: shell
         
         pip3 install --user ansible

See Also
--------

- Ansible: up and running Ch. 2 - Installation and Setup