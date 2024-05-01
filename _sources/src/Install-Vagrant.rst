Install-Vagrant
===============

Brief
-----

Install the latest version of Vagrant on your system.

Procedure
---------

.. tab-set:: 

   .. tab-item:: OS: MacOS

      .. code-block:: shell
         :caption: shell

         brew tap hashicorp/tap
         brew install hashicorp/tap/hashicorp-vagrant

   .. tab-item:: OS: Windows

      .. warning:: 
         If installing vagrant on WSL, it is recommended to install vagrant on the WSL environment only (using the Linux installation instructions) and not on the Windows environment.
         Otherwise, you will need to install the same version of vagrant on both environments and may still run into other issues when trying to use the WSL vagrant binary. [1]_

      .. code-block:: powershell
         :caption: PowerShell

         $Version = Invoke-WebRequest -Uri 'https://releases.hashicorp.com/vagrant/' | Select-Object -ExpandProperty Links | Where-Object { $_.href -match '/vagrant/[0-9]+\.[0-9]+\.[0-9]+/' } | Select-Object -First 1 -ExpandProperty href | Split-Path -Leaf
         $Arch = if ($env:PROCESSOR_ARCHITECTURE -eq 'AMD64') { 'amd64' } else { 'i686' }
         $URL = "https://releases.hashicorp.com/vagrant/$Version/vagrant_${Version}_windows_${Arch}.msi"
         $Dest = Join-Path ([System.IO.Path]::GetTempPath()) 'vagrant.msi'
         Invoke-WebRequest -Uri $URL -OutFile $Dest
         Start-Process -FilePath msiexec -ArgumentList "/i $Dest /qn /passive /norestart" -Wait
         Remove-Item -Path $Dest
         
   .. tab-item:: OS: Linux

      .. code-block:: shell
         :caption: shell

         wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
         echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
         sudo apt update && sudo apt install vagrant

See Also
--------

.. card::

   **External Links**

   `Vagrant Downloads Page <https://developer.hashicorp.com/vagrant/downloads>`_
   
   **Footnotes**

   .. [1] `Vagrant Installation on WSL <https://developer.hashicorp.com/vagrant/docs/other/wsl#vagrant-installation>`_