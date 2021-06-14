import os


'''
mkdir = make a new directory
'''

os.mkdir('mynewdir')

#  make directory inside directory but first directory is present so create child directory
os.mkdir('mynewdir/childdir')

# create many directory using this method.
os.makedirs('parentdir/childdir/granddir')