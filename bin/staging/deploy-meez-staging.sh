ansible-playbook --ssh-extra-args=-A -i staging webservers.yml -K --tags="deploy" --ask-vault-pass
