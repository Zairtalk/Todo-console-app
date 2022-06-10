# Todo app

Usage: **todo-app.py** [-h] [-a TASK [TASK ...]] [-d DELETE [DELETE ...]] [-D DELETE_COMPLETED [DELETE_COMPLETED ...]]
                   [-m NUM [NUM ...]] [-u NUM [NUM ...]] [-c NUM "TASK"] [-l] [-w]

<p>To-do list application that allows you to add, edit, and mark tasks as completed. Default output without arguments:</p>
contents of todo-list. Default path to save list is $HOME/.local/todo-app
<br>  
options:
<br>  
  -h, --help            show this help message and exit
<br>  
  -a TASK [TASK ...], --add TASK [TASK ...]
                        add a new task
<br>  
  -d DELETE [DELETE ...], --delete DELETE [DELETE ...]
                        delete an existing tasks
<br>  
  -D DELETE_COMPLETED [DELETE_COMPLETED ...], --delete-completed DELETE_COMPLETED [DELETE_COMPLETED ...]
                        delete an existing completed tasks
<br>  
  -m NUM [NUM ...], --mark NUM [NUM ...]
                        mark tasks as completed
<br>  
  -u NUM [NUM ...], --unmark NUM [NUM ...]
                        return tasks to to-do list
<br>  
  -c NUM "TASK", --change NUM "TASK"
                        change an existing tasks
<br>  
  -l, --list-completed  list completed tasks
<br>  
  -w, --wipe            -w - wipe completed list, -ww wipe all
