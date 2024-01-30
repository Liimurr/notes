Install-Vagrant
===============

Procedure
---------

.. tab-set:: 

   .. tab-item:: OS: MacOS

      .. code-block:: shell

         brew tap hashicorp/tap
         brew install hashicorp/tap/hashicorp-vagrant

   .. tab-item:: OS: Windows

      Goto `Vagrant Downloads Page <https://developer.hashicorp.com/vagrant/downloads>`_ and download the latest version of Vagrant for your platform.

   .. tab-item:: OS: Linux

      .. code-block:: shell

         wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
         echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
         sudo apt update && sudo apt install vagrant

See Also
--------

.. card::

   **External Links**

   - `Vagrant Downloads Page <https://developer.hashicorp.com/vagrant/downloads>`_ and download the latest version of Vagrant for your platform.