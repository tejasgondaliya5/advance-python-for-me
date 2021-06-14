import os

'''
cwd = current working directory
'''
print(os.getcwd())

'''
chdir = change directory loction 
'''
# os.chdir('mynewdir')
# print(os.getcwd())

'''
rename = used to change name to directory
'''
# os.rename('parentdir', 'fatherdir')

'''
rmdir = remove directory
'''
# os.rmdir('mynewdir')
os.rmdir('fatherdir/childdir/granddir')  # delete only granddir
os.removedirs('fatherdir/childdir/granddir')  # delete all folder
