Vagrant Base Box (Ubuntu)
=========================

Prerequisites
-------------

.. card:: Vagrant

   https://developer.hashicorp.com/vagrant/install

.. card:: VMware Workstation Pro

   https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html

.. code-block:: shell
   :caption: Vagrant VMWare Plugin

   vagrant plugin install vagrant-vmware-desktop
   vagrant plugin update vagrant-vmware-desktop

Procedure
---------

.. card:: Build-VM (Host)

   1. maxmium disk size: 250GB
   2. store virtual disk as a single file: ✅
   
.. card:: Build-VM (Guest)
   
   1. install operating system
   3. username: `vagrant`
   4. password: `vagrant`

.. card:: Post-Install (Guest)
   
   .. card:: Passwordless Sudo
   
      1. run `sudo visudo`
      2. add the following line: `vagrant ALL=(ALL) NOPASSWD: ALL`

   .. code-block:: shell
      :caption: SSH Configuration

      # install ssh server
      sudo apt-get install openssh-server
      sudo systemctl enable ssh
      sudo systemctl start ssh

      # install vagrant ssh key
      sudo chmod go-w ~/
      sudo mkdir -p ~/.ssh
      sudo chmod 700 ~/.ssh
      sudo touch ~/.ssh/authorized_keys
      sudo chmod 600 ~/.ssh/authorized_keys
      VAGRANT_PUB_URL="https://raw.githubusercontent.com/hashicorp/vagrant/main/keys/vagrant.pub"
      wget -qO- "$VAGRANT_PUB_URL" | sudo tee -a ~/.ssh/authorized_keys >/dev/null

.. card:: Add-Files to VM Directory (Host):

   .. code-block:: json
      :caption: metadata.json

      {
         "provider": "vmware_desktop"
      }

   .. code-block:: ruby
      :caption: Vagrantfile

      Vagrant.configure("2") do |config|
         # Add default configuration options here
      end

.. code-block:: shell
   :caption: Export-Base Box (Host)

   VM='ubuntu-22'
   VMDir="~/development/assets/vms/vmware/$VM"
   BaseBoxDir='~/development/assets/vagrant/base-boxes'

   cd $VMDir
   vmware-vdiskmanager -d ./$VM.vmdk
   vmware-vdiskmanager -k ./$VM.vmdk
   cd $BaseBoxDir
   tar -v -z -f ./$VM.box -C $VMDir -c *.nvram *.vmsd *.vmx *.vmxf *.vmdk metadata.json Vagrantfile
   vagrant box add ./$VM.box --name=$VM