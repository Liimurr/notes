Build-Ansible Control Node
==========================
Prerequisites
-------------
.. tab-set:: 

   .. tab-item:: OS: Windows
      :sync: win
   
      - :doc:`Install-WSL`
      - Install-VirtualBox (see `Downdloads Page <https://www.virtualbox.org/wiki/Downloads>`_)

Procedure [1]_
--------------

.. _Install Ansible:

Install Ansible
+++++++++++++++
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
               sudo apt-get -y install python3-pip git libffi-dev libssl-dev
               pip3 install --user ansible

   .. tab-item:: OS: Linux

      .. code-block:: shell
         :caption: shell
         
         pip3 install --user ansible

Next Steps
----------
:doc:`Test-Ansible`

See Also
--------
.. card::

   **External Links**
   
   - https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#control-node-requirements
   
   **Footnotes**
   
   .. [1] Ansible: Up and Running Ch. 2 - Installation and Setup