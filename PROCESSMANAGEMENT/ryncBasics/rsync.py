#!/usr/bin/env python
import subprocess
import os
from multiprocessing import Pool

#------------------------------------------------VARIABLES

tasks = []
src = "/data/prod/"
dest = "/data/prod_backup/"

d = os.walk(src)

#------------------------------------------------RUN FUNCTION

def run(task):
  # Do something with task here
    subprocess.call(["rsync","-zvh", task, dest])
    print("Handling {}".format(task))
    
#------------------------------------------------TASK CREATOR

def task_Create(d):

  for  path, d ,file in d:
          if len(file) != 0:
                  for x in file:
                          task = (path + x)
                          tasks.append(task)
  return tasks
#----------------------------------------------------
if __name__ == "__main__":

#--------------------------------------------TAKSS CREATOR


  tasks = task_Create(d)
  # Create a pool of specific number of CPUs
  p  = Pool(len(tasks))
  print(p)
  # Start each task within the pool
#         p.map(run, tasks)

