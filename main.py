# Case-study #2
# Developers:   Grishaev G. (50%),
#               Abrarova V. (30%),
#               Zlobinskaya L. (35%)

import os
import local as lc

import os
def main():
  '''The main program that outputs thenpath to the current directory and menu.
    Calls the command execution function.'''
  while True:
    print(lc.current_directory, os.getcwd())
    print(lc.menu)
    command = acceptCommand()
    if command == 7:
      print(lc.exit)
      break


def acceptCommand():
  '''Requests the command number and displays an error message
   if the command number is specified incorrectly'.
  Commands are requested until the correct command number is entered.
  Returns the correct command number'''
  command = int(input (lc.menu_selecting))
  list = [1,2,3,4,5,6,7]
  c = list.count(command)
  while c <= 0:
    command = int(input (lc.menu_selecting))
    list = [1,2,3,4,5,6,7]
    c = list.count(command)
  runCommand(command)


def moveUp():
  '''Makes the parent directory current.'''
  os.chdir('..')
  print(os.getcwd())


def moveDown(currentDir):
  '''Requests the name of the subdirectory.
  If the name is specified correctly, it makes the directory
  located in currentDir the current one,
  otherwise it displays an error message.'''
  try:
    os.chdir('./' + currentDir)
  except:
    print(lc.directory_error)


def countFiles(path, list_num):
  '''A recursive function that counts the number of files
  in the specified path directory. All files located in subdirectories
  are included in the calculation. Returns the number of files.'''
  a = 0
  l = os.listdir(path)
  for i in l:
    name = str(i)
    dir_1 = str(path) + chr(92) + name

    if not os.path.isdir(dir_1):
      a += 1
    else:
      try:
        if countFiles(dir_1, list_num) is None:
          a += 0
        else:
          a += countFiles(dir_1, list_num)
      except PermissionError:
        a += 0
  return list_num.append(a)


def findFiles(target, path):
  '''A recursive function that forms a list of paths to files
  whose name contains target.
  All subdirectories of the path directory are included in the search.
  If the files are not found, it displays the corresponding message.'''
  k = []
  dirs = o.listdir(path)
  for f in dirs:
    if o.path.isdir(path + '/' + f):
      k.extend(findFiles(target, path + '/' + f))
    elif o.path.isfile(path + '/' + f):
      if f.find(target) != -1:
        k.append(path + '/' + f)
  return k


def countBytes(path):

    file_stats = os.stat(file)
    bytes = os.stat(file).st_size

def runCommand(command):
  '''Determines by the command number which function should be performed.'''
  if command == 1:
    print(os.listdir())
  elif command == 2:
    moveUp()
  elif command == 3:
    moveDown(currentDir)
  elif command == 4:
    path = os.getcwd()
    list_num = []
    countFiles(path, list_num)
    for d in list_num:
      s += int(d)
    print(lc.files_num + str(s))
  elif command == 5:

  elif command == 6:
    findFiles(target, path)


main()