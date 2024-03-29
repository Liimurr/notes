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
         :caption: PowerShell (Usage) (Host Machine)

         & (Join-Path '.' 'script.ps1') -VMDir (Join-Path 'E:' 'assets' 'vms' 'win-11') -BoxDir (Join-Path 'E:' 'assets' 'vagrant' 'boxes') -VMName 'win-11' -VMProvider 'vmware_desktop'

Next Steps
----------
:doc:`Vagrant.Initialize-VM`

See Also
--------
.. card::

   **External Links**
   
   - https://developer.hashicorp.com/vagrant/docs/providers/vmware/boxes#optimizing-box-size
   - https://developer.hashicorp.com/vagrant/docs/providers/vmware/boxes#contents