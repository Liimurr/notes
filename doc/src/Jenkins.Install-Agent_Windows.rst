Jenkins.Install-Agent (Windows)
===============================

Prerequisites
-------------

.. card:: Controller OS: Ubuntu

   Ubuntu Controller with Jenkins Docker Image Running

.. card:: Agent OS: Windows

Procedure
---------

.. code-block:: shell (Ubuntu Controller)
   :caption: List Running Containers

   sudo docker ps

.. code-block::
   :caption: Check JDK Version (Ubuntu Controller)

   # Data
   containerID='11bf7d89b5d9'

   # Code
   sudo docker exec $containerID java --version

.. card:: Install exact matching jdk version (Windows Agent)

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

.. card:: Disable UseDNS (Windows Agent)
   
   This speeds up ssh connections by disabling DNS lookups.

   .. code-block:: cmd
      :caption: uncomment the line: UseDNS no
      
      notepad.exe `%ProgramData%/ssh/sshd_config`

.. code-block:: shell (Ubuntu Controller)
   :caption: Copy SSHKey to Agent

   # Data
   user='LiamR' # password will be the microsoft account password
   address='192.168.4.124'
   sshKeyFile="$HOME/.ssh/jenkins.pub"
   
   # Code
   remoteAlias="$user@$address"
   sshKey=$(cat $sshKeyFile)
   encodedSSHKey=$(echo -n "$sshKey" | base64 -w 0)
   read -r -d '' data <<- EOM
     \$sshKey = [System.Text.Encoding]::Utf8.GetString([System.Convert]::FromBase64String('$encodedSSHKey'))
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
   encodedCommand=$(printf "$command" | iconv -f UTF-8 -t UTF-16LE | base64 -w 0)
   ssh $remoteAlias "powershell -encodedCommand $encodedCommand"

.. card:: Create SSH Key Credential [1]_

   - Go to Jenkins Dashboard
   - Click on `Manage Jenkins`
   - Click on `Manage Credentials`
   - Click on `Jenkins`
   - Click on `Global credentials (unrestricted)`
   - Click on `Add Credentials`
   - Select `SSH Username with private key`
   - Fill in the following:
      - `Username`: `LiamR`
      - `Private Key`: `Enter directly`
      - `Key`: `Copy the contents of the private key file`
      - `Passphrase`: `Leave empty`
      - `ID`: `LiamR`
      - `Description`: `LiamR SSH Key`

.. card:: Create Agent Node [2]_

   - Go to Jenkins Dashboard
   - Click on `Manage Jenkins`
   - Click on `Manage Nodes and Clouds`
   - Click on `New Node`
   - Fill in the following:
      - `Node name`: `< node name >`
      - `Permanent Agent`: ✅
      - `Remote root directory`: `< jenkins directory >`
      - `Labels`: `< space delimited labels >`
      - `Usage`: `Only build jobs with label expressions matching this node`
      - `Launch method`: `Launch agent via SSH`
      - `Host Key verification Strategy`: `Manually trusted key verification`
      - `Host`: `< agent computer's ip address >`
   
   .. card:: Example

      - `Node name`: `lm-windows-10`
      - `Remote root directory`: `c:/development/assets/jenkins`
      - `Labels`: `windows windows-10 vagrant`
      - `Host`: `192.168.4.124`

See Also
--------

.. card::

   **External Links**

   - https://www.jenkins.io/doc/book/using/using-agents/
   - https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell

   **Footnotes**

   .. [1] `New SSH Credential <https://www.jenkins.io/doc/book/using/using-agents/#create-a-jenkins-ssh-credential>`_
   .. [2] `New Agent Node <https://www.jenkins.io/doc/book/using/using-agents/#setup-up-the-agent1-on-jenkins>`_
