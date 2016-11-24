#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

DOCUMENTATION = '''
---
module: nx_mvn_copy
short_description: executes a maven dependency copy on a remote node
'''

OPTIONS = {
    'maven': 'mvn'
}

def main():

    module = AnsibleModule(
        argument_spec=dict(
            maven=dict(default='mvn'),
            connect_pom=dict(required=True),
            use_cache=dict(default=False),
            group_id=dict(required=True),
            artifact_id=dict(required=True),
            version=dict(required=True),
            classifier=dict(default=None),
            packaging=dict(required=True),
            dest=dict(default=None),
        )
    )

    maven = module.params["maven"]
    connect_pom = module.params["connect_pom"]
    use_cache = module.params["use_cache"]
    group_id = module.params["group_id"]
    artifact_id = module.params["artifact_id"]
    version = module.params["version"]
    classifier = module.params["classifier"]
    packaging = module.params["packaging"]
    dest = module.params["dest"]

    args = [maven, '-f', connect_pom]

    if use_cache:
        args.append('-nsu')

    artifact = '{group_id}:{artifact_id}:{version}:{packaging}'.format(
        group_id=group_id,
        artifact_id=artifact_id,
        version=version,
        packaging=packaging
    )

    if classifier is not None and len(classifier.strip()):
        artifact += ':' + classifier

    args.extend([
        'dependency:copy',
        '-Dartifact=' + artifact,
        '-Dmdep.useBaseVersion=true'
    ])

    if dest is not None and len(dest.strip()):
        args.append('-DoutputDirectory=' + dest)

    startd = datetime.datetime.now()

    rc, out, err = module.run_command(args)

    endd = datetime.datetime.now()
    delta = endd - startd

    if out is None:
        out = ''
    if err is None:
        err = ''

    module.exit_json(
        cmd=args,
        stdout=out.rstrip("\r\n"),
        stderr=err.rstrip("\r\n"),
        rc=rc,
        start=str(startd),
        end=str(endd),
        delta=str(delta),
        changed=True
    )

# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
