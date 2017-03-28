import datetime
import os
import time
from ansible.plugins.callback import CallbackBase

class CallbackModule(CallbackBase):
    def __init__(self):
        super(CallbackModule, self).__init__()
        self.stats = {}
        self.currentPlay = None
        self.playIndex = 0
        self.currentTask = None
        self.taskIndex = 0
        self.Plays = []
import datetime
import os
import time
from ansible.plugins.callback import CallbackBase

class CallbackModule(CallbackBase):
    def __init__(self):
        super(CallbackModule, self).__init__()
        self.stats = {}
        self.currentPlay = None
        self.playIndex = 0
        self.currentTask = None
        self.taskIndex = 0
        self.Plays = []

    def playbook_on_play_start(self, name):
        if self.currentPlay is not None:
            if self.currentTask is not None:
                self.stats[self.playIndex]['tasks'][self.taskIndex]['time'] = time.time() - self.stats[self.playIndex]['tasks'][self.taskIndex]['time']
            self.stats[self.playIndex]['time'] = time.time() - self.stats[self.playIndex]['time']

        self.taskIndex = 0
        self.currentTask = None
        self.playIndex += 1
        self.currentPlay = name
        self.stats[self.playIndex] = {}
        self.stats[self.playIndex]['name'] = self.currentPlay
        self.stats[self.playIndex]['time'] = time.time()
        self.stats[self.playIndex]['tasks'] = {}

    def playbook_on_task_start(self, name, condition):
        if self.currentTask is not None:
             self.stats[self.playIndex]['tasks'][self.taskIndex]['time'] = time.time() - self.stats[self.playIndex]['tasks'][self.taskIndex]['time']

        if not name:
            name = 'Setup'

        self.taskIndex += 1
        self.currentTask = name
        self.stats[self.playIndex]['tasks'][self.taskIndex] = {}
        self.stats[self.playIndex]['tasks'][self.taskIndex]['name'] = self.currentTask
        self.stats[self.playIndex]['tasks'][self.taskIndex]['time'] = time.time()

    def playbook_on_stats(self, stats):

        if self.currentTask is not None:
            self.stats[self.playIndex]['tasks'][self.taskIndex]['time'] = time.time() - self.stats[self.playIndex]['tasks'][self.taskIndex]['time']
        if self.currentPlay is not None:
            self.stats[self.playIndex]['time'] = time.time() - self.stats[self.playIndex]['time']

        print("\n\n**********Summary Of Execution**********\n\nPLAYS")
        for play in self.stats:
            print("***************************************")
            print("Name:\t{0:-<90}Execution Time:\t{1:.02f}s\n\n\tTASKS".format(self.stats[play]['name'], self.stats[play]['time']))

            print("\t*******************************")
            for task in self.stats[play]['tasks']:
                print("\tName:\t{0:-<70}Execution Time:\t{1:.02f}s\n".format(self.stats[play]['tasks'][task]['name'], self.stats[play]['tasks'][task]['time']))
            print("\t*******************************\n")
            print("***************************************\n\n\n")
