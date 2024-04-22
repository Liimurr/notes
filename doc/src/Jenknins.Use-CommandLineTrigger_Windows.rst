
https://www.jenkins.io/doc/book/system-administration/authenticating-scripted-clients/

# Prerequisites

## Jenkins Powershell Plugin

# Procedure

## Create Token
goto http://localhost:8080/
goto User > Configure > API Token
add new token
select generate
copy and save token somewhere

## Create Job
goto http://localhost:8080/
select New Item
enter a name

restrict where this project can be run: ✅ 
enter space delimited labels

# jenkins job name
# jenkins job api token
# jenkins user name
# jenkins url


JOB_NAME='Test.CommandLineTrigger'
API_TOKEN='1114e5b87bd94f533fef35f05b827f4b7e'
USER='lm'
URL='http://localhost:8080/'

# https://www.jenkins.io/doc/book/system-administration/authenticating-scripted-clients/#shell-with-curl
# https://www.jenkins.io/doc/book/system-administration/authenticating-scripted-clients/#shell-with-wget
curl -X POST -L --user $USER:$API_TOKEN \
    $URL/job/$JOB_NAME/build

