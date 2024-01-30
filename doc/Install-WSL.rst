Install-WSL
===========
Prerequisites
-------------
Running on Windows Operating System

Procedure
---------
.. code-block:: powershell
   :caption: PowerShell

   $Features = @( 'VirtualMachinePlatform', 'Microsoft-Windows-Subsystem-Linux' )
   $RequiresRestart = $false

   $Features | ForEach-Object {
     if ((Get-WindowsOptionalFeature -Online -FeatureName $_).State -ne 'Enabled') {
        Write-Host "Install feature $_"
        Enable-WindowsOptionalFeature -Online -NoRestart -FeatureName $_
        $RequiresRestart = $true
     }
     else {
        Write-Host "Feature already installed $_"
     }
   }

   if ((bcdedit /enum | findstr -i hypervisorlaunchtype) -like '*Auto*') {
     Write-Host "hypervisorlaunchtype already setup"
   }
   else {
     Write-Host "setting hypervisorlaunchtype"
     bcdedit /set hypervisorlaunchtype Auto
     $RequiresRestart = $true
   }

   if ($RequiresRestart) {
     Restart-Computer
   }