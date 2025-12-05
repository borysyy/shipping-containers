#!/bin/bash

ansible-playbook deploy.yml -i inventory.ini  --vault-password-file ./vault_password.txt -vvv
