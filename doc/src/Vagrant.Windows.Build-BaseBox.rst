Build Windows Base Box for Vagrant
==================================

Prerequisites
-------------
- VMWare Workstation Pro
- Windows Pro or Enterprise (Windows Home does not support Hyper-V)
- Vagrant

.. code-block:: powershell
   :caption: Enable Hyper-V

   Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All

Procedure
---------

.. dropdown:: Build-VM (Host):
   :open:

   1. maxmium disk size: 250GB
   2. store virtual disk as a single file: ✅
   3. settings > options > advanced > Disable side channel mitigations for Hyper-V enabled hosts: ✅
   
.. dropdown:: Build-VM (Guest):
   :open:
   
   1. install operating system
   2. use offline account
   3. username: `vagrant`
   4. password: `vagrant`
   5. install vmware tools

.. code-block:: powershell
   :caption: Post-Install Script (Guest)

   # misc
   Set-NetConnectionProfile -NetworkCategory Private
   Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "LocalAccountTokenFilterPolicy" -Value 1
   Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Name "DisablePwdCaching" -Value 0 -Type DWORD -Force
   Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Lsa" -Name "disabledomaincreds" -Value 0
   # setup winrm
   winrm quickconfig -q
   winrm set 'winrm/config/winrs' '@{MaxMemoryPerShellMB="512"}'
   winrm set 'winrm/config' '@{MaxTimeoutms="1800000"}'
   winrm set 'winrm/config/service' '@{AllowUnencrypted="true"}'
   winrm set 'winrm/config/client/auth' '@{Basic="true"}'
   winrm set 'winrm/config/service/auth' '@{Basic="true"}'
   Enable-PSRemoting -Force
   sc.exe config "WinRM" start= auto

.. dropdown:: Add-Files to VM Directory (Host):
   :open:

   .. code-block:: json
      :caption: metadata.json

      {
         "provider": "vmware_desktop"
      }

   .. code-block:: ruby
      :caption: Vagrantfile

      Vagrant.configure("2") do |config|
      config.vm.guest = :windows
      config.vm.communicator = "winrm"
      end


.. code-block:: powershell
   :caption: Export-Base Box (Host):

   $VM='windows-10'
   $VMDir="C:/development/assets/vms/$VM"
   $BaseBoxDir='C:/development/assets/vagrant/base-boxes'

   Set-Alias 'vmware-vdiskmanager' 'C:/Program Files (x86)/VMware/VMware Workstation/vmware-vdiskmanager.exe'
   Set-Location $VMDir
   vmware-vdiskmanager -d ./$VM.vmdk
   vmware-vdiskmanager -k ./$VM.vmdk
   Set-Location $BaseBoxDir
   tar -v -z -f ./$VM.box -C $VMDir -c *.nvram *.vmsd *.vmx *.vmxf *.vmdk metadata.json Vagrantfile
   vagrant box add ./$VM.box --name=$VM

.. code-block:: powershell
   :caption: Test-Base Box (Host)

   $VM='windows-10'
   $VagrantDir="C:/development/assets/vagrant/vms/$VM"

   Set-Location $VagrantDir
   vagrant init $VM
   vagrant up
   vagrant winrm --Command 'Write-Host $env:USERPROFILE'

.. code-block:: powershell
   :caption: Test-Base Box (Agent - Host-Windows)

   # open port 55985 for WinRM testing
   $VagrantDir="C:/development/assets/vagrant/vms/$VM"
   Set-Location $VagrantDir
   vagrant up
   New-NetFirewallRule -DisplayName "Vagrant WinRM" -Direction Inbound -LocalPort 55985 -Protocol TCP -Action Allow

.. dropdown:: Test-Base Box (Controller - Host-Ubuntu):
   :open:

   .. code-block:: shell
      :caption: install pywinrm

      pip install pywinrm

   .. code-block:: shell
      :caption: test winrm

      import winrm;
      
      agent_ip = '192.168.4.124'
      vagrant_port = '55985'
      session = winrm.Session("$agent_ip:$vagrant_port", auth=('vagrant', 'vagrant'))
      result = session.run_ps('echo "Hello, World!"')
      print(result.std_out.decode('utf-8'))