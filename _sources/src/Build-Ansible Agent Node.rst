Build-Ansible Agent Node
========================
Brief
-----
On a worker/slave/agent computer, create a node to be controlled by Ansible.

Procedure
---------
.. tab-set:: 

   .. tab-item:: OS: Windows

      No action required.

   .. tab-item:: OS: Linux

      .. code-block:: shell
         :caption: shell

         sudo apt update
         sudo apt install -y python3.12

   .. tab-item:: OS: MacOS

      .. code-block:: shell
         :caption: shell

         yes | brew install python@3.12

See Also
--------
.. card::

   **External Links**
   
   https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix