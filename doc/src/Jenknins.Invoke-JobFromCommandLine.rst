Jenkins.Invoke-Job from Command Line
====================================

Prerequisites
-------------

.. card:: Jenkins Controller (Ubuntu)

.. card:: Jenkins Agent (Any)

Procedure
---------

.. card:: Create Token

   1. goto http://localhost:8080/
   2. goto User > Configure > API Token
   3. add new token
   4. select generate
   5. copy and save token somewhere for later use

.. card:: Create Job

   1. goto http://localhost:8080/
   2. select New Item > Freestyle project > OK
   3. enter name: Test.CommandLineTrigger (or any name)
   4. restrict where this project can be run: ✅ 
      - enter space delimited labels to restrict where this project can be run (optional)

.. code-block:: bash
   
   JOB_NAME='Test.CommandLineTrigger'
   API_TOKEN='1114e5b87bd94f533fef35f05b827f4b7e'
   USER='lm'
   URL='http://localhost:8080/'

   # 
   # https://www.jenkins.io/doc/book/system-administration/authenticating-scripted-clients/#shell-with-wget
   curl -X POST -L --user $USER:$API_TOKEN \
      $URL/job/$JOB_NAME/build

See Also
--------
.. card::

   **External Links**
   
   - `Invoke job with terminal <https://www.jenkins.io/doc/book/system-administration/authenticating-scripted-clients/>`_
   - `Invoke job with curl <https://www.jenkins.io/doc/book/system-administration/authenticating-scripted-clients/#shell-with-curl>`_
   - `Invoke job with wget <https://www.jenkins.io/doc/book/system-administration/authenticating-scripted-clients/#shell-with-wget>`_
