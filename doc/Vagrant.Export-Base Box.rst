Vagrant.Export-Base Box
=======================

Brief
-----
1. Convert the VM to a vagrant ``.box`` file
2. Add the box file to vagrant
3. Test the box file with vagrant by provisioning it in a new directory

Procedure
---------

.. _Test:

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

   .. tab-item:: VMWare
      :sync: vmware
         
      .. code-block:: powershell
         :caption: PowerShell (Script)

         param ( 
           # Path to the virtual machine
           [Parameter(Mandatory=$true)] 
           [string]$VMDir,
         
           [Parameter(Mandatory=$true)]
           [string]$BoxDir,
         
           # Name of the virtual machine
           [Parameter(Mandatory=$true)] 
           [string]$VMName,
         
           # Name of the virtual machine provider
           [Parameter(Mandatory=$true)] 
           [string]$VMProvider
         )
         
         function Get-VMWarePath {
           @( 
             [System.Environment]::GetFolderPath('ProgramFiles'),
             [System.Environment]::GetFolderPath('ProgramFilesX86') 
           ) | ForEach-Object { 
             $ConditionalReturnValue = Join-Path $_ 'VMware' 'VMware Workstation'
             if ($ConditionalReturnValue | Test-Path -ErrorAction SilentlyContinue) { return $ConditionalReturnValue }
           }
         }
         $VMWarePath = Get-VMWarePath
         $VMDiskManager = ($VMWarePath) ? $(Join-Path $VMWarePath 'vmware-vdiskmanager.exe') : $null
         $VMDK = "$VMDir/$VMName.vmdk"
         & "$VMDiskManager" -d "$VMDK"
         & "$VMDiskManager" -k "$VMDK"
         
         $MetaData = @"
         {
           "provider": "$VMProvider"
         }
         "@
         
         $Files = Get-ChildItem -Path $VMDir
         $FilesToArchive = @()
         foreach ($File in $Files) {
           $Extension = $File.Extension.TrimStart('.')
           if ($Extension -in @('nvram', 'vmsd', 'vmx', 'vmxf', 'vmdk') -or  $File.Name -eq 'metadata.json') {
             $FilesToArchive += (Resolve-Path -Path $File.FullName -RelativeBasePath $VMDir -Relative).Substring(2)
           }
         }
         Set-Content -Path (Join-Path $VMDir 'metadata.json') -Value $MetaData -Force
         tar cvzf (Join-Path $BoxDir "$VMName.box") --directory=$VMDir $FilesToArchive

      .. code-block:: powershell
         :caption: PowerShell (Usage)

         & (Join-Path '.' 'script.ps1') -VMDir (Join-Path 'E:' 'assets' 'vms' 'win-11') -BoxDir (Join-Path 'E:' 'assets' 'vagrant' 'boxes') -VMName 'win-11' -VMProvider 'vmware_desktop'

Box.Initialize-Vagrant
++++++++++++++++++++++

.. code-block:: shell
   :caption: shell / cmd
   
   vagrant box add --name my-box /path/to/the/new.box
   vagrant init my-box

.. tab-set::

   .. tab-item:: VirtualBox
      :sync: virtualbox

      .. dropdown:: Add-Content to Vagrantfile
         :open:

         1. Copy **VirtualBox** \| <**Your VM**> \| **Settings** \| **Network** \| **Adapter 1** \| **Advanced** \| **MAC Address**
         2. Add the following to the Vagrantfile in the directory you called ``vagrant init`` in:
            
            .. code-block:: ini
               :caption: Vagrantfile
            
               config.vm.base_mac=<mac address>

      .. dropdown:: Provision the Vagrant Box
         :open:

         .. code-block:: shell
            :caption: shell / cmd

            vagrant up --provider virtualbox

   .. tab-item:: VMWare
      :sync: vmware
      
      .. dropdown:: Provision the Vagrant Box
         :open:

         .. code-block:: shell
               :caption: shell / cmd

               vagrant up --provider vmware_desktop

See Also
--------

- https://developer.hashicorp.com/vagrant/docs/providers/vmware/boxes#optimizing-box-size
- https://developer.hashicorp.com/vagrant/docs/providers/vmware/boxes#contents