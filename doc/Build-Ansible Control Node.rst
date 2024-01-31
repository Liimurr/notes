Build-Ansible Control Node
==========================
Prerequisites
-------------
.. tab-set:: 

   .. tab-item:: OS: Windows
      :sync: win
   
      - :doc:`Install-WSL`
      - Install-VirtualBox (see `Downdloads Page <https://www.virtualbox.org/wiki/Downloads>`_)

Procedure [2]_
--------------
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

         3. On WSL, Enable windows access [1]_

            .. code-block:: shell
               :caption: shell (WSL)
               
               export VAGRANT_WSL_ENABLE_WINDOWS_ACCESS="1"
               export PATH="$PATH:/mnt/c/Program Files/Oracle/VirtualBox"
               export VAGRANT_WSL_WINDOWS_ACCESS_USER_HOME_PATH="/mnt/e/assets/ansible-playbooks"
      
         4. On PowerShell, set restrictive file permissions

            cd E:\assets\ansible-playbooks\
            icacls ./.vagrant.d/insecure_private_key /remove "NT AUTHORITY\Authenticated Users"

         4. On WSL, set restrictive file permissions for windows Files

            .. code-block:: shell
               :caption: shell (WSL)

               sudo nano /etc/wsl.conf

            .. code-block:: ini
               :caption: add lines to /etc/wsl.conf

               [automount]
               options = "umask=077"
            
            Press ``Ctrl+O`` to save and ``Ctrl+X`` to exit

            Shutdown WSL 

            Wait 8 Seconds for the changes to take effect [3]_

            Start WSL
         

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
   
   .. [1] https://developer.hashicorp.com/vagrant/tutorials/getting-started/getting-started-boxes
   .. [2] Ansible: Up and Running Ch. 2 - Installation and Setup
   .. [3] https://learn.microsoft.com/en-us/windows/wsl/wsl-config#the-8-second-rule-for-configuration-changes