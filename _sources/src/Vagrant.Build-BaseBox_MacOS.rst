Vagrant.Build-Base Box (MacOS)
==============================

Prerequisites
-------------

.. card:: Host OS: MacOS

.. card:: Parallels 

   https://www.parallels.com/products/desktop/

.. card:: Vagrant
   
   .. code-block:: shell
      :caption: Install Vagrant

      brew tap hashicorp/tap
      brew install hashicorp/tap/hashicorp-vagrant

.. card:: Vagrant Parallels Plugin
   
   .. code-block:: shell
      :caption: Install Vagrant Parallels Plugin
      
      vagrant plugin install vagrant-parallels

Procedure
---------

.. card:: create a macos vm

   - open parallels
   - select download macos

.. code-block:: shell
   :caption: copy vm to a new location

   VM='macos-14'

   cd ~/Parallels
   mkdir ~/vagrant
   mkdir ~/vagrant/base-boxes/
   mkdir ~/vagrant/base-boxes/$VM
   cp -r macOS.macvm ~/vagrant/base-boxes/$VM/macOS.macvm
   cd ~/vagrant/base-boxes/$VM/

.. card:: register and auto rename the copied vm

   open and/or run ~/vagrant/base-boxes/<VM>/macOS.macvm 
   parallels will automatically rename it and give it a new mac address.

   .. code-block:: shell
      :caption: give the vm a better name
      
      VM='macos-14'

      prlctl set 'macOS (1)' —name $VM

.. card:: Build-VM 

   1. install operating system
   2. username: `vagrant`
   3. password: `vagrant`
   4. install Parallels Tools

.. card:: Post-Install (Guest)
   
   .. card:: Passwordless Sudo
   
      1. run `sudo visudo`
      2. add the following line: `vagrant ALL=(ALL) NOPASSWD: ALL`

   .. card:: Enable SSH server

      System Settings > General > Sharing > Enable Remote Login: ✅, and set `Full disk access to users` to allow `All Users`.

   .. code-block:: shell
      :caption: Install Vagrant SSH Key

      sudo chmod go-w ~/
      sudo mkdir -p ~/.ssh
      sudo chmod 700 ~/.ssh
      sudo touch ~/.ssh/authorized_keys
      sudo chmod 600 ~/.ssh/authorized_keys
      VAGRANT_PUB_URL="https://raw.githubusercontent.com/hashicorp/vagrant/main/keys/vagrant.pub"
      curl -sSL "$VAGRANT_PUB_URL" | sudo tee -a ~/.ssh/authorized_keys >/dev/null

.. card:: Add-Files to VM Directory (Windows Host):

   .. code-block:: json
      :caption: metadata.json

      {
         "provider": "parallels"
      }

   .. code-block:: ruby
      :caption: Vagrantfile

      Vagrant.configure("2") do |config|
         # Add default configuration options here
      end

.. code-block:: shell
   :caption: Export-Base Box (Host)

   VM='macos-14'

   tar cvzf $VM.box ./$VM.macvm  ./Vagrantfile ./metadata.json
   vagrant box add $VM.box --name $VM

.. code-block:: shell
   :caption: Test-Base Box (Host)

   VM='macos-14'

   vagrant init $VM
   vagrant up

See Also
--------
.. card::

   **External Links**

   - https://kb.parallels.com/en/129720
   - https://developer.hashicorp.com/vagrant/install
