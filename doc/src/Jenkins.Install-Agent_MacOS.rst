Jenkins.Install-Agent (MacOS)
=============================

Prerequisites
-------------

.. card:: Controller OS: Ubuntu

   Ubuntu Controller with Jenkins Docker Image Running

.. card:: Agent OS: MacOS

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

.. card:: Install Exact Matching JDK Version (MacOS Agent)

   https://www.openlogic.com/openjdk-downloads

.. card:: Enable SSH Server (MacOS Agent)

   System Settings > General > Sharing > Enable Remote Login: ✅, and set `Full disk access to users` to allow `All Users`.

.. card:: Disable UseDNS (MacOS Agent)
   
   This speeds up ssh connections by disabling DNS lookups.

   .. code-block:: shell
      :caption: uncomment the line: UseDNS no

      sudo nano /etc/ssh/sshd_config

.. code-block:: shell (Ubuntu Controller)
   :caption: Copy SSHKey to Agent

   # Data
   user='lm' # password will be the microsoft account password
   address='192.168.4.29'
   sshKeyFile="$HOME/.ssh/jenkins.pub"
   
   # Code
   ssh-copy-id -i $sshKeyFile $user@$address

.. card:: Create SSH Key Credential [1]_

   - Go to Jenkins Dashboard
   - Click on `Manage Jenkins`
   - Click on `Manage Credentials`
   - Click on `Jenkins`
   - Click on `Global credentials (unrestricted)`
   - Click on `Add Credentials`
   - Select `SSH Username with private key`
   - Fill in the following:
      - `Username`: `lm`
      - `Private Key`: `Enter directly`
      - `Key`: `Copy the contents of the private key file`
      - `Passphrase`: `(Leave empty)`
      - `ID`: `lm-ssh-key`
      - `Description`: `lm generic SSH Key`

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

      - `Node name`: `lm-macos-14`
      - `Remote root directory`: `/Users/lm/development/assets/jenkins`
      - `Labels`: `macos macos-14 vagrant`
      - `Host`: `192.168.4.29`

See Also
--------

.. card::

   **External Links**

   - https://www.jenkins.io/doc/book/using/using-agents/
   - https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell

   **Footnotes**

   .. [1] `New SSH Credential <https://www.jenkins.io/doc/book/using/using-agents/#create-a-jenkins-ssh-credential>`_
   .. [2] `New Agent Node <https://www.jenkins.io/doc/book/using/using-agents/#setup-up-the-agent1-on-jenkins>`_
