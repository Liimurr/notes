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
   2. username: `vagrant`
   3. password: `vagrant`

.. card:: Post-Install (Guest)
   
   .. card:: Passwordless Sudo
   
      1. run `sudo visudo`
      2. add the following line: `vagrant ALL=(ALL) NOPASSWD: ALL`
      3. remove any line that contains `requiretty`

   .. code-block:: shell
      :caption: SSH Configuration

      # install ssh server
      sudo apt-get install openssh-server
      sudo systemctl enable ssh
      sudo systemctl start ssh

      # install vagrant ssh key
      sudo chmod go-w ~/
      sudo mkdir -p ~/.ssh
      sudo chown -R vagrant:vagrant ~/.ssh
      sudo chmod 700 ~/.ssh
      sudo touch ~/.ssh/authorized_keys
      sudo chmod 600 ~/.ssh/authorized_keys
      VAGRANT_PUB_URL="https://raw.githubusercontent.com/hashicorp/vagrant/main/keys/vagrant.pub"
      wget -qO- "$VAGRANT_PUB_URL" | sudo tee -a ~/.ssh/authorized_keys >/dev/null

   .. card:: Remove UseDNS

      1. edit `/etc/ssh/sshd_config` (`sudo nano /etc/ssh/sshd_config`)
      2. set `UseDNS` to `no`

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
   VMDir="$HOME/development/assets/vms/vmware/$VM"
   BaseBoxDir="$HOME/development/assets/vagrant/base-boxes"

   cd $VMDir
   vmware-vdiskmanager -d ./$VM.vmdk
   vmware-vdiskmanager -k ./$VM.vmdk
   tar -v -z -f "$BaseBoxDir/$VM.box" -c $(find . -type f \( -name "*.nvram" -o -name "*.vmsd" -o -name "*.vmx" -o -name "*.vmxf" -o -name "*.vmdk" \)) metadata.json Vagrantfile
   vagrant box add "$BaseBoxDir/$VM.box" --name=$VM

.. code-block:: shell
   :caption: Test-Base Box (Host)

   VM='ubuntu-22'

   vagrant init $VM
   vagrant up