Jenkins.Install-Agent_Windows
=============================

Prerequisites
-------------

.. card:: Controller OS: Ubuntu

   Ubuntu Controller with Jenkins Docker Image Running

.. card:: Agent OS: Windows

.. code-block:: powershell
   :caption: Install OpenSSH Server (Windows Agent)

   # Install the OpenSSH Server
   Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
   # Start the sshd service
   Start-Service sshd

   # OPTIONAL but recommended:
   Set-Service -Name sshd -StartupType 'Automatic'

   # Confirm the Firewall rule is configured. It should be created automatically by setup. Run the following to verify
   if (!(Get-NetFirewallRule -Name "OpenSSH-Server-In-TCP" -ErrorAction SilentlyContinue | Select-Object Name, Enabled)) {
     Write-Output "Firewall Rule 'OpenSSH-Server-In-TCP' does not exist, creating it..."
     New-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
   } else {
     Write-Output "Firewall rule 'OpenSSH-Server-In-TCP' has been created and exists."
   }

Procedure
---------

.. code-block:: shell (Ubuntu Controller)
   :caption: List Running Containers

   docker ps

.. code-block::
   :caption: Check JDK Version

   # Data
   containerID='f3f3b3b3b3b3'

   # Code
   docker exec $containerID java --version

.. code-block::
   :caption: Install exact matching jdk version on Agent

.. code-block:: shell (Ubuntu Controller)
   :caption: Copy SSHKey to Agent

   # Data
   user='LiamR' # password will be the microsoft account password
   address='192.168.4.124'
   sshKeyFile="$HOME/.ssh/jenkins.pub"

   # Code
   remoteAlias="$user@$address"
   sshKey=$(cat $sshKeyFile)
   encodedSSHKey=$(echo -n "$sshKey" | iconv -t utf-16le | base64 -w 0)
   read -r -d '' data <<- EOM
     \$sshKey = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('$encodedSSHKey'))
   EOM
   read -r -d '' code <<- 'EOM'
     $authorizedKeysFile = "$env:ProgramData/ssh/administrators_authorized_keys"
     if (-not (Test-Path -Path $authorizedKeysFile))
     {
       New-Item -ItemType File -Path $authorizedKeysFile
     }
     $containsSSHKey = ((-not ((Get-Content -Path $authorizedKeysFile -Raw) -eq $null)) -and ((Get-Content -Path $authorizedKeysFile -Raw).Contains($sshKey)))
     if (-not $containsSSHKey)
     {
       # add ssh key to authorized_keys file
       Add-Content -Force -Path $authorizedKeysFile -Value $sshKey
       # grant remote admin rights
       icacls.exe $authorizedKeysFile /inheritance:r /grant "Administrators:F" /grant "SYSTEM:F"
     }
   EOM
   read -r -d '' command <<- EOM
     $data
     $code
   EOM
   encodedCommand=$(echo -n "$command" | iconv -t utf-16le | base64 -w 0)
   ssh $remoteAlias "powershell -encodedCommand $encodedCommand"