#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    kanban todo <name>...
    kanban doing <task_id>
    kanban done <task_id>
    kanban list <command>
    kanban (-i | --interactive)
    kanban (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""
import sys
import cmd
from docopt import docopt, DocoptExit
from model import KanBan

def docopt_cmd(func):
	 """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
    	try:
    		opt=docopt(fn.__doc__,arg)
    	except DocoptExit as e:
    		 # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.
            print('Invalid Command! Try Another one.')
            print(e)

            return
        except SystemExit:
        	  # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.
            return
         return finc(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn
class MyInteractive(cmd.Cmd):
	"""docstring for MyInteractive"""
	intro='\n\t++++++++++++++++++++++++++++++++++++++++++++++\n\n' \
            '\tWelcome to KanBan Console Application!\n\n' \
            '\tAdd, organize and view your tasks\n\n' \
            '\tThe Commands For Any Action Are Listed Below\n\n' \
            '\t---------------------------------------------\n'\
            '\ttodo task_name : Create A todo Task \n' \
            '\tdoing task_id  : Start Doing Task \n' \
            '\tdone task_id   : Mark Task Done \n' \
            '\tlist todo      : View Task You Supposed To Do\n' \
            '\tlist doing     : View Task You Are Doing \n' \
            '\tlist done      : View Task You Have Finished\n' \
            '\tlist all       : View All Your Tasks In All Sections\n' \
            '\tquit           : To Exit\n' \
            '\t---------------------------------------------\n\n' \
            '\t+++++++++++++++++++++++++++++++++++++++++++++++++\n'

	




