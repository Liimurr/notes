Install-Vagrant_VMWare (Ubuntu)
===============================

.. card::

   .. code-block:: shell
      :caption: install linux headers

      sudo apt install linux-headers-`uname -r`

   .. code-block:: shell
      :caption: install vmware workstation

      LICENSE_KEY=XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
      sudo mkdir /opt/vmware/datastore
      yes '' | ./vmware-installer.bundle \
         -s vmware-player-app softwareUpdateEnabled no \
         -s vmware-player-app dataCollectionEnabled no \
         -s vmware-workstation-server hostdUser ${USERNAME} \
         -s vmware-workstation-server datastore /opt/vmware/datastore \
         -s vmware-workstation-server httpsPort 443 \
         -s vmware-workstation serialNumber ${LICENSE_KEY}

   .. code-block:: shell
      curl https://releases.hashicorp.com/vagrant-vmware-utility/1.0.22/vagrant-vmware-utility_1.0.22-1_amd64.deb -o vagrant-vmware-utility.deb
      sudo dpkg -i vagrant-vmware-utility.deb
      rm vagrant-vmware-utility.deb
      sudo /opt/vagrant-vmware-desktop/bin/vagrant-vmware-utility certificate generate
      sudo /opt/vagrant-vmware-desktop/bin/vagrant-vmware-utility service install
      
See Also
--------
.. card::

   **External Links**
   
   - `Troubleshooting VMWare on Ubuntu 22.04 <https://communities.vmware.com/t5/VMware-Workstation-Pro/Workstation-17-5-not-working-on-Ubuntu-22-04-or-23-10/td-p/3011934>`_
   - `VMWare Silent Install <https://communities.vmware.com/t5/vSphere-Storage-Discussions/Adding-Storage-via-VMware-Workstation-VM/td-p/2642187>`_
   - `Vagrant VMWare Utility Installation <https://developer.hashicorp.com/vagrant/docs/providers/vmware/vagrant-vmware-utility>`_