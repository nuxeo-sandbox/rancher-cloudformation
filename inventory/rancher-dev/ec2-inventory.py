#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from posix import putenv

lib_path = os.path.abspath("library")
sys.path.append(lib_path)

from nx_ec2 import Ec2Inventory
