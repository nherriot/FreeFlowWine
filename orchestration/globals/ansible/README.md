Read Me for the setup of Ansible to create VM's and Live Servers for Freee Flow Wines
================


Author Nicholas Herriot
Created 27th Sep 2016

The scripts within this directory should be copied to your ansible directory.
Hence you should do the following:

## Install Ansible

Install the latest version of ansible to your machine:

/>  sudo pip install ansible )

## Copy To Directory

Copy the hosts and ansible.cfg file to /etc/ansible on your machine.
Please note that you will require root password to machines to run the initial setup.yml script.
If you are in this position go to your keepass file and look up your root password. In the file:

/> hosts

Change the line below to have the root passwords needed for the machies:

[ffw-prod:vars]
#ansible_ssh_pass=<insert real password here>

[ffw-test:vars]
ansible_ssh_user=root
ansible_ssh_pass=<insert real password here>


## Run Setup Scripts

From your /orchestration directory run your first scritp. You only ever need to run this scirpt once.

/> ansible-playbook  setup.yml

Now run your script to add your public key to the machine. This will allow you to talk to the machine
in a much more secure manner. But before you run this script ensure you comment out the variable in
the hosts file:  ansible_ssh_pass
This will force your machine to use ssh keys for installed hosts.
Or if you notice that you have never had any key added to this machine update the variable to hold
the root password of 'ffw_admin'. And again once you have finished comment out the line or remove
it from your hosts file.

/> ansible-playbook  addMyPublicKey.yml

You can now remove your root passwords from your host file if you like.

## Run Install Software Script

Now run the install software script. This is used to update and build a complete machine from scratch.
You should be able to run this script over and over with no ill effect. To run this do:

/> ansible-playbook playbook-install-ffw.yml

You can remove all software from the machine and start from scratch by running the  remove software script.
This will even reomve config files and stop installed services such as Nginx and Gunicorn.

/> ansible-playbook  playbook-remove-software-ffw.yml





