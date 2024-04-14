Vagrant.Export-Base Box
=======================

Brief
-----
1. Convert the VM to a vagrant ``.box`` file
2. Add the box file to vagrant
3. Test the box file with vagrant by provisioning it in a new directory

Prerequisites
-------------

:doc:`Vagrant.Build-Base Box`

Procedure
---------
VM.ConvertTo-Box File
+++++++++++++++++++++

.. tab-set:: 

   .. tab-item:: VirtualBox
      :sync: virtualbox

      .. dropdown:: Ensure-NAT is Configured Correctly
         :open:

         .. image:: /images/20240120165626.png
      
      .. dropdown:: Install-Guest Additions
         :open:

         .. image:: /images/20240120181640.png
      
      .. dropdown:: Invoke-Vagrant Package Command

         .. code-block:: shell
            :caption: cmd / shell
         
            vagrant package --base virtualbox-vagrant-win-11 --output win-11

   .. tab-item:: VMWare
      :sync: vmware
         
      .. code-block:: powershell
         :caption: PowerShell (Script) (Host Machine)

         $VM='windows-10'
         $VMDir="C:/development/assets/vms/$VM"
         $BaseBoxDir='C:/development/assets/vagrant/base-boxes'
         Set-Alias 'vmware-vdiskmanager' 'C:/Program Files (x86)/VMware/VMware Workstation/vmware-vdiskmanager.exe'
         Set-Location $VMDir
         vmware-vdiskmanager -d ./$VM.vmdk
         vmware-vdiskmanager -d ./$VM.vmdk
         Set-Location $BaseBoxDir
         $content = @"
         {
           "provider": "vmware-desktop"
         }
         "@
         Set-Content -Path "$VMDir/metadata.json" -Value $content
         tar -v -z -f ./$VM.box -C $VMDir -c *.nvram *.vmsd *.vmx *.vmxf *.vmdk metadata.json 

Next Steps
----------
:doc:`Vagrant.Initialize-VM`

See Also
--------
.. card::

   **External Links**
   
   - https://developer.hashicorp.com/vagrant/docs/providers/vmware/boxes#optimizing-box-size
   - https://developer.hashicorp.com/vagrant/docs/providers/vmware/boxes#contents
