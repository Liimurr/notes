Vagrant Base Box (MacOS)
==========================

Prerequisites
-------------
- Parallels

.. card:: Vagrant
   
   .. code-block::shell
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

   VM=macos-14.4.1

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
      
      VM=macos-14.4.1

      prlctl set 'macOS (1)' —name $VM

.. card:: Build-VM 

   1. install operating system
   3. username: `vagrant`
   4. password: `vagrant`
   5. install Parallels Tools
   6. `sudo visudo` and add the following line: `vagrant ALL=(ALL) NOPASSWD: ALL`
   7. System Settings > General > Sharing > Enable Remote Login: ✅, and set `Full disk access to users` to allow `All Users`.

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
   :caption: Package the VM

   VM=macos-14.4.1

   tar cvzf $VM.box ./$VM.macvm  ./Vagrantfile ./metadata.json
   vagrant box add $VM.box --name $VM

.. code-block:: shell
   :caption: test the vagrant box

   VM=macos-14.4.1
   
   vagrant init $VM
   vagrant up

See Also
--------
.. card::

   **External Links**

   - https://kb.parallels.com/en/129720
   - https://developer.hashicorp.com/vagrant/install
