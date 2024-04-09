Vagrant.Build-Base Box
======================

Brief
-----
1. Install Vagrant
2. Install VM Provider
3. Initialize VM Virtual Hardware
4. Install Guest Operating System
5. Install SSH Server on Guest VM
6. Test Host to Guest SSH Connection

Prerequisites
-------------
1. Goto: `Vagrant Downloads Page <https://developer.hashicorp.com/vagrant/downloads>`_ and install the latest version.
2. Install a Virtual Machine Provider (`ref <https://developer.hashicorp.com/vagrant/docs/providers>`_). This tutorial covers VirtualBox and VMWare, with Virtual box having the most support.

.. tab-set:: 

   .. tab-item:: Provider: VMWare
      :sync: vmware

      .. warning:: 
         
         For Vagrant boxes, GuestOS: Windows 11 and Provider: VMWare Workstation 17 are incompatible.
         Vagrant has no support for TPM 2.0 encryption yet, and VMWare Workstation 17 requires it for Windows 11.

      .. dropdown:: Install-Vagrant VMWare Utility [1]_
         :open:

         `Vagrant VMWare Utility Downloads Page <https://developer.hashicorp.com/vagrant/install/vmware>`_

      .. dropdown:: Install-Vagrant Plugin [2]_
         :open:
         
         .. code-block:: powershell
            :caption: PowerShell (Host Machine)

            vagrant plugin install vagrant-vmware-desktop 

   .. tab-item:: Provider: Parallels (HostOS: MacOS)

      .. code-block:: shell
         :caption: shell (Host Machine)

         # install vagrant 
         brew tap hashicorp/tap
         brew install hashicorp/tap/hashicorp-vagrant

         # install vagrant parallels plugin
         vagrant plugin install vagrant-parallels

      .. card:: create a macOS vm

         open parallels
         download macOS
      
      .. code-block:: 
         :caption: shell (Host Machine)

         VM=macos-14.4.1

         # copy vm to a new location
         cd ~/Parallels
         mkdir ~/vagrant
         mkdir ~/vagrant/base-boxes/
         mkdir ~/vagrant/base-boxes/$VM
         cp -r macOS.macvm ~/vagrant/base-boxes/$VM/macOS.macvm
         cd ~/vagrant/base-boxes/$VM/

      .. card:: register and auto rename the copied vm

         open and/or run ~/vagrant/base-boxes/$VM/macOS.macvm 
         parallels will automatically rename it and give it a new mac address.

      .. code-block:: 
         :caption: shell (Host Machine)

         # give the auto renamed vm a better name
         prlctl set 'macOS (1)' —name $VM

         # download metadata and vagrant file
         cd ~/vagrant/base-boxes/$VM
         curl -o metadata.json https://kb.parallels.com/Attachments/kcs-191881/metadata.json
         curl -o Vagrantfile https://kb.parallels.com/Attachments/kcs-191881/Vagrantfile

      .. card:: edit the vagrant file and meta data

         edit meta data "name" field
         remove private key logic in `Vagrantfile` if using the insecure public key (recommended — otherwise follow the steps outlined in https://kb.parallels.com/en/129720 to create and use private key)

      .. code-block:: 
         :caption: shell (Host Machine)

         # create vagrant box
         tar cvzf $VM.box ./$VM.macvm  ./Vagrantfile ./metadata.json
         vagrant box add $VM.box --name $VM

         # test vagrant file
         cd ~/vagrant
         mkdir ~/vagrant/test-$VM
         cd ~/vagrant/test-$VM
         vagrant init $VM
         vagrant up —provider=parallels

Procedure
---------
Initialize-VM Virtual Hardware
++++++++++++++++++++++++++++++
.. tab-set:: 

   .. tab-item:: GuestOS: MacOS
      :sync: macos
      
      - 1 Processor
      - 2048MB+ of RAM

   .. tab-item:: GuestOS: Windows
      :sync: windows

      - 1+ Processors
      - `4096MB+ of RAM <https://support.microsoft.com/en-us/windows/windows-11-system-requirements-86c11283-ea52-4782-9efd-7674389a7ba3>`_
   
   .. tab-item:: GuestOS: Ubuntu
      :sync: ubuntu

      - 1+ Processors
      - `512MB+ of RAM <https://developer.hashicorp.com/vagrant/docs/boxes/base#memory>`_

- `Dynamically Allocated 250GB HD <https://developer.hashicorp.com/vagrant/docs/boxes/base#disk-space>`_
- `Disable Audio and USB <https://developer.hashicorp.com/vagrant/docs/boxes/base#peripherals-audio-usb-etc>`_

.. tab-set:: 

   .. tab-item:: GuestOS: MacOS
      :sync: macos

      .. card::

         .. tab-set:: 

            .. tab-item:: Provider: VirtualBox
               :sync: virtualbox

               .. code-block:: powershell
                  :caption: PowerShell (Host Machine)

                  $VMName = 'virtualbox-vagrant-macos-12'
                  $VBoxManage = Join-Path ([Environment]::GetFolderPath('ProgramFiles')) Oracle VirtualBox VBoxManage.exe
                  & $VBoxManage modifyvm $VMName --cpuidset 00000001 000106e5 00100800 0098e3fd bfebfbff
                  & $VBoxManage setextradata $VMName "VBoxInternal/Devices/efi/0/Config/DmiSystemProduct" "iMac19,3"
                  & $VBoxManage setextradata $VMName "VBoxInternal/Devices/efi/0/Config/DmiSystemVersion" "1.0"
                  & $VBoxManage setextradata $VMName "VBoxInternal/Devices/efi/0/Config/DmiBoardProduct" "Iloveapple"
                  & $VBoxManage setextradata $VMName "VBoxInternal/Devices/smc/0/Config/DeviceKey" "ourhardworkbythesewordsguardedpleasedontsteal(c)AppleComputerInc"
                  & $VBoxManage setextradata $VMName "VBoxInternal/Devices/smc/0/Config/GetKeyFromRealSMC" 1
                  & $VBoxManage modifyvm $VMName --cpu-profile "Intel Core i7-2635QM"
               
Install-Guest Operating System
++++++++++++++++++++++++++++++
.. tab-set:: 

   .. tab-item:: GuestOS: MacOS
      :sync: macos

      Create a local user account with the username ``vagrant`` and password ``vagrant``
      
   .. tab-item:: GuestOS: Windows
      :sync: windows

      1. During installation, at "select a country" press ``Shift+F10`` to open command prompt, then enter  ``OOBE\BYPASSNRO``
      2. After restart, press ``Shift+F10`` to open command prompt, then enter ``ipconfig /release``
      3. Continue installation without internet connection
      4. Create a local user account with the username ``vagrant`` and password ``vagrant`` (`ref <https://developer.hashicorp.com/vagrant/docs/boxes/base#vagrant-user>`_)

   .. tab-item:: GuestOS: Ubuntu
      :sync: ubuntu

      Create a local user account with the username ``vagrant`` and password ``vagrant`` 

Install-SSH Server on Guest VM
++++++++++++++++++++++++++++++
.. tab-set::
   
   .. tab-item:: GuestOS: MacOS
      :sync: macos

      .. dropdown:: Edit-System Setup
         :open:   
         
         .. literalinclude:: /../src/sys-admin-scripts/agent/install-ssh-server/macos.sh
            :language: shell
            :caption: shell (Guest Machine)

      .. dropdown:: Initialize-Authorizied Keys Directory
         :open:   
         
         .. code-block:: shell
            :caption: shell (Guest Machine)
            
            sudo chmod go-w ~/
            sudo mkdir ~/.ssh
            sudo chmod 700 ~/.ssh
            sudo touch ~/.ssh/authorized_keys
            sudo chmod 600 ~/.ssh/authorized_keys

   .. tab-item:: GuestOS: Windows
      :sync: windows
      
      .. dropdown:: Install SSH Server
         :open:

         .. literalinclude:: /../src/sys-admin-scripts/agent/install-ssh-server/windows.ps1
            :language: powershell
            :caption: PowerShell (Guest Machine)  

         
         uncomment the following line in ``%ProgramData%/sshd_config``:

         .. code-block:: diff
            :caption: %ProgramData%/sshd_config (Guest Machine)

            - #PublickeyAuthentication yes
            + PublickeyAuthentication yes

      .. dropdown:: Install WinRM

         .. code-block:: powershell
            :caption: PowerShell (Guest Machine)

            Set-NetConnectionProfile -NetworkCategory Private
            Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "LocalAccountTokenFilterPolicy" -Value 1
            Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisablePwdCaching" -Value 0 -Type DWORD -Force
            Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Lsa" -Name "disabledomaincreds" -Value 0

            winrm quickconfig -q
            winrm set 'winrm/config/winrs' '@{MaxMemoryPerShellMB="512"}'
            winrm set 'winrm/config' '@{MaxTimeoutms="1800000"}'
            winrm set 'winrm/config/service' '@{AllowUnencrypted="true"}'
            winrm set 'winrm/config/service/auth' '@{Basic="true"}'
            Enable-PSRemoting -Force
            sc.exe config "WinRM" start= auto

   .. tab-item:: GuestOS: Ubuntu
      :sync: ubuntu

      .. dropdown:: Install SSH Server
         :open:
         
         .. literalinclude:: /../src/sys-admin-scripts/agent/install-ssh-server/ubuntu.sh
            :language: shell
            :caption: shell (Guest Machine)
         
Test-Host to Guest SSH Connection
++++++++++++++++++++++++++++++++++
.. tab-set::

   .. tab-item:: Provider: VirtualBox
      :sync: virtualbox

      .. dropdown:: Register-SSH Port Forwarding Rule
         :open:

         1. GoTo **VirtualBox** \| **Your Virtual Machine** \| **Settings** \| **Network** \| **Advanced** \| **Port Forwarding**

         2. Add-Rule

            .. list-table::
               :header-rows: 0
      
               * - **Name**
                 - SSH
               * - **Protocol**
                 - TCP
               * - **Host Port**
                 - 2222
               * - **Guest Port**
                 - 22
            
            .. note::

               - The Host Port can be any port you wish to use on your host machine. The Guest Port must be 22, as that is the port the SSH server on the guest machine is listening on.
               - The Name field is arbitrary, but it is recommended to use a name that describes the purpose of the rule.

      .. dropdown:: Test-SSH Connection
         :open:
         
         Make sure the VM is running, then invoke the following command on the Host machine:

         .. code-block:: shell 
            :caption: shell / cmd (Host Machine)
      
            ssh vagrant@localhost -p 2222

   .. tab-item:: Provider: VMWare
      :sync: vmware

      .. dropdown:: Find-Guest IP
         :open:

         1. On Guest Machine, Goto **VMWare** \| **Your Virtual Machine** \| **Settings** \| **Network Adapter** \| **Advanced** \| **MAC Address** 
         2. On Host Machine, invoke ``arp -a`` and look for the MAC Address of the Guest Machine. The IP Address associated with the MAC Address is the IP Address of the Guest Machine.
      
      .. dropdown:: Test-SSH Connection
         :open:

         Make sure the VM is running, then invoke the following command on the Host Machine:

         .. code-block:: shell
            :caption: shell / cmd (Host Machine)
      
            ssh vagrant@<Guest Machine IP Address>

Edit-Security Policies
+++++++++++++++++++++++++++++++++++++++
.. tab-set::
   
   .. tab-item:: GuestOS: Windows

      .. dropdown:: Edit-Windows Security Policies [4]_

         .. code-block:: powershell
            :caption: PowerShell (Guest Machine)

            # Disable UAC (User Account Control)
            Set-ItemProperty -Path 'HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System' -Name 'EnableLUA' -Value 0 -Type DWORD -ErrorAction SilentlyContinue

            # Disable Shutdown Tracker
            Set-ItemProperty -Path 'HKLM:\Software\Policies\Microsoft\Windows NT\Reliability' -Name 'ShutdownReasonOn' -Value 0 -ErrorAction SilentlyContinue

            # Disable Server Manager at Logon
            Set-ItemProperty -Path 'HKLM:\Software\Policies\Microsoft\Windows\Server\ServerManager' -Name 'DoNotOpenAtLogon' -Value 1 -ErrorAction SilentlyContinue

            # Disable Complex Passwords
            $ConfigFile = New-TemporaryFile
            $SecurityDatabseFile = Join-Path  $env:SystemDrive 'windows' 'security' 'local.sdb'
            secedit /export /cfg "$ConfigFile"
            (Get-Content $ConfigFile).replace("PasswordComplexity = 1", "PasswordComplexity = 0") | Out-File "$ConfigFile"
            secedit /configure /db $SecurityDatabseFile /cfg $ConfigFile /areas SECURITYPOLICY
            Remove-Item -Path $ConfigFile -Force -Confirm:$false

Install Additional Software
+++++++++++++++++++++++++++
Install any additional software you wish to have on your base box. For example, PowerShell Core, Python, etc.

Next steps
----------
:doc:`/Vagrant.Export-Base Box`

See Also
--------
.. card::

   **External Links**
   
   - `Vagrant Windows Base Box Configuration <https://developer.hashicorp.com/vagrant/docs/boxes/base#base-windows-configuration>`_
   - `Stack Overflow Edit Group Policy <https://serverfault.com/a/848519>`_
   - `Download List of Registry Keys <https://www.microsoft.com/en-us/download/confirmation.aspx?id=25250>`_
   - `Example: Using WSL Host with Windows Guest VM <https://discuss.hashicorp.com/t/winrm-port-does-not-work-in-vagrantfile/54601>`_
   - `Setup WinRM on Windows <https://github.com/AlbanAndrieu/ansible-windows/blob/master/files/ConfigureRemotingForAnsible.ps1>`_
   - https://woshub.com/using-psremoting-winrm-non-domain-workgroup/
   - https://kevrocks67.github.io/blog/powershell-remote-management-from-linux.html
   
   **Footnotes**
   
   .. [1] https://developer.hashicorp.com/vagrant/docs/providers/vmware/vagrant-vmware-utility
   .. [2] https://developer.hashicorp.com/vagrant/docs/providers/vmware/installation
   .. [3] https://developer.hashicorp.com/vagrant/docs/installation#windows-virtualbox-and-hyper-v
   .. [4] https://developer.hashicorp.com/vagrant/docs/boxes/base#base-windows-configuration