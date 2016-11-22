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


