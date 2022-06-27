#!/usr/bin/env python3

import json as j
import argparse as ap
from pathlib import Path as p
import os

class Entry:

    def __init__(self, num:int, task:str):
        self.__task = task
        self.__num = num

    def correct_task(self,task):
        self.__task = task

    def __str__(self) -> str:
        return str(self.__num) + ". " + self.__task

    def num(self):
        return self.__num

    def task(self):
        return self.__task

    def subtract_num(self):
        self.__num = int(self.__num) - 1

    def change_num(self,num):
        self.__num = num

class EntryEncoder(j.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,Entry):
            return {'Num':obj.num(),'Task':obj.task()}
        else:
            return super().default(obj)

TODO_LIST = []
COMPLETED_LIST = []
DATA_DIR = p.home().joinpath('.local','todo-app')

def delete_entry(num):
    try:
        del TODO_LIST[num-1]
        for i in TODO_LIST:
            if i.num() < num:
                continue
            else:
                i.subtract_num()
    except IndexError:
        print(f"There isn't task # {num}")

def delete_entry_completed(num):
    try:
        del COMPLETED_LIST[num-1]
        for i in COMPLETED_LIST:
            if i.num() < num:
                continue
            else:
                i.subtract_num()
    except IndexError:
        print(f"There isn't task # {num}")

def mark_entry_as_completed(num):
    try:
        task = TODO_LIST[num-1]
        task.change_num(len(COMPLETED_LIST)+1)
        COMPLETED_LIST.append(task)
        del task
        delete_entry(num)
    except IndexError:
        print(f"There isn't task # {num}")

def mark_entry_as_incomplete(num):
    try:
        task = COMPLETED_LIST[num-1]
        task.change_num(len(TODO_LIST)+1)
        TODO_LIST.append(task)
        del task
        delete_entry_completed(num)
    except IndexError:
        print(f"There isn't task # {num}")

def add_entry(task):
    TODO_LIST.append(Entry(len(TODO_LIST)+1,task))

def change_entry(num,task):
    TODO_LIST[num-1].correct_task(task)

def print_list(TODO_LIST):
    if TODO_LIST:
        for i in TODO_LIST:
            print("  ",i,end='\n\n')

def save_to_json(todolist,completed=False):
    if not DATA_DIR.exists():
        os.mkdir(DATA_DIR,mode=0o766)
    if completed:
        todolist_name = 'completed'
    else:
        todolist_name = 'todolist'
    with open(DATA_DIR.joinpath(todolist_name + ".json"),'wt') as f:
        j.dump(todolist,f,cls=EntryEncoder)

def read_from_json(todolist,completed=False):
    if completed:
        todolist_name = 'completed'
    else:
        todolist_name = 'todolist'
    if not DATA_DIR.joinpath(todolist_name + ".json").exists():
        return
    else:
        with open(DATA_DIR.joinpath(todolist_name + ".json"),'rt') as f:
            tasks = j.load(f)
            for i in tasks:
                todolist.append(Entry(i['Num'],i['Task']))

def wipe():
        COMPLETED_LIST = []
        save_to_json(COMPLETED_LIST,True)

def wipe_all():
        TODO_LIST = []
        COMPLETED_LIST = []
        save_to_json(TODO_LIST)
        save_to_json(COMPLETED_LIST,True)

if __name__ == "__main__":
    read_from_json(TODO_LIST)
    read_from_json(COMPLETED_LIST,True)
    parser = ap.ArgumentParser(description="To-do list application that allows you to add, edit, and mark tasks as completed. Default output without arguments: contents of todo-list." \
    f" Default path to save list is {DATA_DIR}")
    parser.add_argument('-a','--add',dest='task',help='add a new task',type=str,nargs='+')
    parser.add_argument('-d','--delete',dest='delete',help='delete an existing tasks',type=int,nargs='+')
    parser.add_argument('-D','--delete-completed',dest='delete_completed',help='delete an existing completed tasks',type=int,nargs='+')
    parser.add_argument('-m','--mark',dest='mark',help='mark tasks as completed',type=int,nargs='+',metavar='NUM')
    parser.add_argument('-u','--unmark',dest='unmark',help='return tasks to to-do list',type=int,nargs='+',metavar='NUM')
    parser.add_argument('-c','--change',dest='change',help='change an existing tasks',nargs=2,metavar=('NUM','"TASK"'))
    parser.add_argument('-l','--list-completed',dest='completed',help='list completed tasks',action='store_true')
    parser.add_argument('-w','--wipe',dest='wipe',help='-w - wipe completed list, -ww wipe all',action='count',default=0)
    args = parser.parse_args()
    if args.task:
        task = ' '.join(x for x in args.task)
        add_entry(task)
        save_to_json(TODO_LIST)
    if args.delete:
        if not TODO_LIST:
            print("Nothing to delete")
            parser.exit()
        for i in sorted(args.delete,reverse=True):
            delete_entry(int(i))
        save_to_json(TODO_LIST)
    if args.delete_completed:
        if not COMPLETED_LIST:
            print("Nothing to delete")
            parser.exit()
        for i in sorted(args.delete_completed,reverse=True):
            delete_entry_completed(int(i))
        save_to_json(COMPLETED_LIST,True)
    if args.change:
        if not TODO_LIST:
            print("Nothing to change")
            parser.exit()
        try: 
            change_entry(int(args.change[0]),args.change[1])
        except:
            print('Incorrect format. -c/--change NUM "TASK"')
            parser.exit()
    if args.mark:
        if not TODO_LIST:
            print("Nothing to mark as completed")
            parser.exit()
        for i in sorted(args.mark,reverse=True):
            mark_entry_as_completed(int(i))
        save_to_json(COMPLETED_LIST,True)
        save_to_json(TODO_LIST)
    if args.unmark:
        if not COMPLETED_LIST:
            print("Nothing to return")
            parser.exit()
        for i in sorted(args.unmark,reverse=True):
            mark_entry_as_incomplete(int(i))
        save_to_json(TODO_LIST)
        save_to_json(COMPLETED_LIST,True)
    if args.completed:
        if COMPLETED_LIST:
            print(f'#{"=".center(25,"=")}#')
            print(f'''{"COMPLETED LIST".center(25)}''')
            print(f'#{"=".center(25,"=")}#\n')
            print_list(COMPLETED_LIST)
        else:
            print('Saved data not found')
    if int(args.wipe) >= 2:
            wipe_all()
    elif int(args.wipe) == 1:
        if COMPLETED_LIST:
            wipe()
        else:
            print('Nothing to wipe')
    if not sum((bool(x) for x in vars(args).values())):
        if TODO_LIST:
            print(f'#{"=".center(25,"=")}#')
            print(''' ╔╦╗┌─┐┌┬┐┌─┐   ╦  ┬┌─┐┌┬┐
  ║ │ │ │││ │───║  │└─┐ │ 
  ╩ └─┘─┴┘└─┘   ╩═╝┴└─┘ ┴ ''')
            print(f'#{"=".center(25,"=")}#\n')
            print_list(TODO_LIST)
        else:
            print('Saved data not found')
