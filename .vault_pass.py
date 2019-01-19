#!/usr/bin/env python

"""
This file is for TravisCI to be able to submit the Ansible Vault password.
"""

import os
import sys
sys.stdout.write(os.environ['ANSIBLE_VAULT_PASSWORD'])
