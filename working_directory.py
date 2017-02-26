#current working directory

import os

#determine
os.getcwd()

#the canonical path of the specified filename, eliminating any symbolic links encountered in the path
os.path.realpath('c:\\data\\repos\\some_other_dir')

#change
os.chdir('c:\\data\\repos\\some_other_dir')