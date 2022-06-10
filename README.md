# Todo app
Usage: todo-app.py [-h] [-a TASK [TASK ...]] [-d DELETE [DELETE ...]]
                   [-D DELETE_COMPLETED [DELETE_COMPLETED ...]] [-m NUM [NUM ...]] [-c NUM "TASK"]
                   [-l] [-w]

To-do list application that allows you to add, edit, and mark tasks as completed. Default output
without arguments: contents of todo-list. Default path to save list is /home/zairtalk/.local/todo-app

options:
  -h, --help            show this help message and exit
  -a TASK [TASK ...], --add TASK [TASK ...]
                        add a new task
  -d DELETE [DELETE ...], --delete DELETE [DELETE ...]
                        delete an existing tasks
  -D DELETE_COMPLETED [DELETE_COMPLETED ...], --delete-completed DELETE_COMPLETED [DELETE_COMPLETED ...]
                        delete an existing completed tasks
  -m NUM [NUM ...], --mark NUM [NUM ...]
                        mark task as completed
  -c NUM "TASK", --change NUM "TASK"
                        change an existing tasks
  -l, --list-completed  list completed tasks
  -w, --wipe            -w - wipe completed list, -ww wipe all
