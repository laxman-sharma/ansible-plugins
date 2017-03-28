# ansible-plugins

I'll store useful ansible plugins here.

Please feel free to add or reuse it.


Guide for using
-------------

1. Get the repository using following command:
~~~~
git clone https://github.com/laxman-sharma/ansible-plugins.git
~~~~

2. Add following line in your configuration file. Make sure you the  path of the directory is correct
~~~~
[defaults]
callback_plugins=<CLONE_DIRECTORY>/ansible-plugins
~~~~

3. Execute playbook normally.
