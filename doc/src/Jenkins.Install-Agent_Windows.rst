Jenkins.Install-Agent_Windows
=============================

Prerequisites
-------------

.. card:: Controller OS: Ubuntu

   Ubuntu Controller with Jenkins Docker Image Running

.. card:: Host OS: Windows

Procedure
---------

.. code-block:: shell (Ubuntu Controller)
   :caption: List Running Containers

   docker ps

.. code-block::
   :caption: Check JDK Version

   docker exec <container_id> java --version

.. code-block::
   :caption: Install exact matching jdk version on Agent