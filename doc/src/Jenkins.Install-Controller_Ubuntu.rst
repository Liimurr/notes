Jenkins.Install-Controller (Ubuntu)
===================================

Prerequisites
-------------

.. card:: Host OS: Ubuntu

Procedure
---------

.. code-block:: shell
   :caption: install-bridged network

   sudo docker network create jenkins

.. code-block:: shell
   :caption: install-jenkins docker image

   sudo docker run \
     --name jenkins-docker \
     --rm \
     --detach \
     --privileged \
     --network jenkins \
     --network-alias docker \
     --env DOCKER_TLS_CERTDIR=/certs \
     --volume jenkins-docker-certs:/certs/client \
     --volume jenkins-data:/var/jenkins_home \
     --publish 2376:2376 \
     docker:dind \
     --storage-driver overlay2

.. card:: Create docker file:

   .. code-block:: Dockerfile
      :caption: Dockerfile

      FROM jenkins/jenkins:2.440.2-jdk17
      USER root
      RUN apt-get update && apt-get install -y lsb-release
      RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
      https://download.docker.com/linux/debian/gpg
      RUN echo "deb [arch=$(dpkg --print-architecture) \
      signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
      https://download.docker.com/linux/debian \
      $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
      RUN apt-get update && apt-get install -y docker-ce-cli
      USER jenkins
      RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"

.. code-block:: shell
   :caption: build jenkins image
   
   sudo docker build -t jenkins-blueocean-0.1.0:2.440.2-1 .

.. code-block:: shell
   :caption: run jenkins image

   sudo docker run \
      --name jenkins-blueocean \
      --restart=on-failure \
      --detach \
      --network jenkins \
      --env DOCKER_HOST=tcp://docker:2376 \
      --env DOCKER_CERT_PATH=/certs/client \
      --env DOCKER_TLS_VERIFY=1 \
      --publish 8080:8080 \
      --publish 50000:50000 \
      --volume jenkins-data:/var/jenkins_home \
      --volume jenkins-docker-certs:/certs/client:ro \
      jenkins-blueocean-0.1.0:2.440.2-1

See Also
--------

.. card::

   **External Links**

   - https://www.jenkins.io/doc/book/installing/docker/#setup-wizard
