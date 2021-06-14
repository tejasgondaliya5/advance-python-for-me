'''
- an Exception is a runtime error which can be handled by the programmer.
- all exception are represented as classes in python.

- TWO TYPES OF EXCEPTION:-
  -- Built-in Exception :- Exception which are already available in python language.
                           The base class for all built-in exception is baseException class.

  -- User Defined Exception :- a programmer can create his own Exceptions, called user-defined exception.`

(1)  try:- the try block contains code which may cause exceptions.

    syntax:-
              try:
                  statements

(2) Except:- The except block is used to catch an exception that is raised in the try block. There can be multiple except
              block for try block.

    syntax:-
            except ExceptionName:
                statements

(3) Else:- This block will get executed when no exception is raised. Else block is executed after try block.
    syntax:-
            else:
                statement

(4) Finally:- This block will get executed irrespective of whether there is an exception or not.
     syntax:-
            finally:
                statement

Example:-

    try:
        statement

    except Exception class name:
        statement
    else:
        statement         # try block ma error na ave tyare else chale.   or  except run nathay tyare else run thay.
    finally:
        statement         # try block ma error ave ke na ve pan finally to run thay j.


'''

a = 10
b = 5
try:
    d = a/b
    print(d)

except ZeroDivisionError:
    print('divide by zero is not allowed')

print('rest of the code')


print()
print('.......................................')
print()


a = 10
b = 0
try:
    d = a/b
    print(d)

except ZeroDivisionError:
    print('divide by zero is not allowed')

print('rest of the code')


