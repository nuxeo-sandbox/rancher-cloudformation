# Rancher Cloudformation

This is a CloudFormation template suitable to install [Rancher](www.rancher.com) in a HA infrastructure hosted on AWS.


# Prerequisites

First, make sure your AWS credentials are ok in `~/.aws/credentials` so that boto can interract with AWS. 

After that you need a Python installation with `virtualenv`.

That's all.

## How to use

    # create a python virtual environment to not pollute your python installation
    virtualenv venv
    . ./venv/bin/activate

    # Install required python modules
    pip install -r requirements.txt

    # Install required ansible galaxy modules
    ansible-galaxy install -r ansible-requirements.txt

    # Launch the playbook 
    ansible-playbook -i inventory/rancher-dev deploy-infra.yml

If you don't use a `virtualenv`, you need ansible >= 2.2 otherwise, you'll have to run the script twice, since it doesn't know how to refresh it's inventory after the cloudformation call.

## Variables

