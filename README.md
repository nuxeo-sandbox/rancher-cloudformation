# Rancher Cloudformation

This is a CloudFormation template suitable to install [Rancher](www.rancher.com) in a HA infrastructure hosted on AWS.


## How to use

    virtualenv venv
    . ./venv/bin/activate
    pip install -r requirements.txt
    ansible-galaxy install -r ansible-requirements.txt
    ansible-playbook -i inventory/rancher-dev/ec2.py deploy-infra.yml