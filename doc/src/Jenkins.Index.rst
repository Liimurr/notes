Jenkins.Overview
==================

Overview
--------

Controller
++++++++++
A jenkins-controller (originally called a jenkins "master"): a computer with jenkins installed on it. 
The jenkins installation allows it to control other computers through ssh. 
The computers that are controlled through ssh are termed "agents" (newer term) or "slaves" (older term) 

Agent
+++++
A jenkins-agent: a computer that can be used by jenkins to perform jobs. 
Does not require jenkins to be installed (jenkins is only needed to control other nodes). 
Requires an ssh-server installed and enabled for the jenkins-controller computer to perform actions on it. 

Install-Jenkins Controller
--------------------------

Bare Metal
++++++++++
1. install java 17
2. install jenkins
   
   recommended: when installing, setup jenkins as a service that is initialized on startup

Docker
++++++
1. install docker
2. install jenkins docker image


Install-Jenkins Agent
---------------------
1. install java 17
2. install and enable ssh ssh-server
3. on the jenkins controller:
   i. generate an ssh key specifically for this agent
      (recommended: use the agent's name as the ssh-key file-name)
   ii. copy ssh key into the jenkin agent's authorized keys file
   iii. add generated ssh key to jenkin controller's ssh config
      - use the agent's network device id as the host
      - use the agent's user name you want to ssh into as the user-name
   iv. verify ssh works from the jenkins-controller to the ssh jenkins-agent

Invoke-Git Repo Scripts on Jenkins
----------------------------------
A typical use case when beginning with jenkins involves running scripts (.bat, .sh, .ps1 etc.) that reside on a git repository. 
In order to run a script through ssh ( in this case jenkins which uses ssh ) a flag must be set on the script file to mark it as executable.
1. create a script
2. add the script to the repo with the executable flag set
