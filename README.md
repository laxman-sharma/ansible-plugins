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


Example Output:
~~~~
**********Summary Of Execution**********

PLAYS
***************************************
Name:	localhost---------------------------------------------------------------------------------Execution Time:	0.31s

	TASKS
	*******************************
	Name:	TASK: setup-----------------------------------------------------------Execution Time:	0.28s

	Name:	TASK: debug message---------------------------------------------------Execution Time:	0.02s

	*******************************

***************************************
~~~~
