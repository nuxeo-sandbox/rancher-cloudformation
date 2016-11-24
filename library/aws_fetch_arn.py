#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import *
import boto.iam

DOCUMENTATION = '''
---
module: aws_fetch_arn
short_description: fetches the ARN of an SSL certificate
'''

def main():

    module = AnsibleModule(
        argument_spec=dict(
            region=dict(required=True),
            certificate_name=dict(required=True),
        )
    )

    region = module.params["region"]
    certificate = module.params["certificate_name"]

    iam = boto.iam.connect_to_region(region)
    arn = iam.get_server_certificate(certificate).arn

    module.exit_json(
        arn=arn,
        changed=True
    )


if __name__ == '__main__':
    main()
