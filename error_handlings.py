
'''we can handle minor errors only. using the try and ecxcept blocks'''
'''----------------------------------------------'''
# print('hello python')
# print('5')
# a=10
# try:
#     print(a/0)
# except:
#     print('anything by zero is not defined' )
# print('hi my name is chitti')

'''output'''
# hello python
# 5
# anything by zero is not defined
# hi my name is chitti
'''-------------------------------------------------------'''
# print('HELLO GOUTHAM')
# print('WELCOME TO PYTHON WORLD')
# a=10
# try:
#     print(a/0)
# except NameError:
#     print('value is not defined' )
# print('MY NAME IS CHITTI')
# it is zero division error so it will not goes to the except block it stop at line 30.
# if it is name error then only goes to the except blockbecause we are metioned type of error in except block
'''----------------------------------------------------------------------------------------------------------------'''  
# print('HELLO GOUTHAM.....')
# print('WELCOME TO PYTHON WORLD')
# a=10
# try:
#     print(a/0)
# except ZeroDivisionError:
#     print('value is not defined' )
# print('MY NAME IS CHITTI')
'''output'''
# HELLO GOUTHAM
# WELCOME TO PYTHON WORLD
# value is not defined   
# MY NAME IS CHITTI      
'''-------------------------------------------'''
# print("Python")
# print("Core Python")
# try:
#     print(10/5)
# except: 
#     print('Not Ok Divided by Zero')
# print("Advance Python")
# print("Python Analytics")
'''output'''
# Python
# Core Python
# 2.0
# Advance Python
# Python Analytics
'''==========================================================='''
# print('HELLO GOUTHAM.....')
# print('WELCOME TO PYTHON WORLD')
# a=10
# try:
#     print(a/2)
#     print(a/0)
# except ZeroDivisionError:
#     print('value is not defined' )
# print('MY NAME IS CHITTI')
# '''output'''
# HELLO GOUTHAM.....
# WELCOME TO PYTHON WORLD
# 5.0
# value is not defined   
# MY NAME IS CHITTI      
'''==========================================='''
# print('HELLO GOUTHAM.....')
# print('WELCOME TO PYTHON WORLD')
# a=10
# try:
#     print(a/0)
#     print(a/2)  
# except ZeroDivisionError:
#     print('value is not defined' )
# print('MY NAME IS CHITTI')
'''output'''
# HELLO GOUTHAM.....
# WELCOME TO PYTHON WORLD
# value is not defined   
# MY NAME IS CHITTI     
'''-----------------------------------------------------'''
# print('HELLO GOUTHAM.....')
# print('WELCOME TO PYTHON WORLD')
# a=10
# try:
#     print(a/2)  
#     print(a/0)
# except ZeroDivisionError:
#     print('value is not defined' )
# except NameError:
#     print('value not defined')
# print('MY NAME IS CHITTI')

'''output'''
# HELLO GOUTHAM.....
# WELCOME TO PYTHON WORLD
# 5.0
# value is not defined   
# MY NAME IS CHITTI  
'''==================================================================='''
# print('HELLO GOUTHAM.....')
# print('WELCOME TO PYTHON WORLD')
# a=10
# try:
#     print(b)
#     print(a/2)  
#     print(a/0)
# except ZeroDivisionError:
#     print('value is not defined' )
# except NameError:
#     print('value not defined')
# print('MY NAME IS CHITTI')
'''output'''
# ELLO GOUTHAM.....
# WELCOME TO PYTHON WORLD
# value not defined      
# MY NAME IS CHITTI  
'''---------------------------------------------------------------------------------'''
#In the program we can give the multiple except block and only one try block whatever error happend first that corresponding except block excecuted
'''------------------------------------------------------------------------------'''
# print("Python")
# print("Core Python")
# a=5
# b='6'
# try:
#     print(a/5)
#     print(a/0)
#     print(,)   
# except SyntaxError: 
#     print('Not Ok Divided by Zero')
# print("Advance Python")
# print("Python Analytics")

#this program will not excectue because it contains major error that is
'''# SyntaxError: invalid syntax it is major error sowe can not handle by the try and exception method'''

#######################################################################################################
'''==================================================================================================='''

# print("Python")
# print("Core Python")
# a=5
# b='6'
# try:
#     print(a/5)  
# except ZeroDivisionError: 
#     print('Not Ok Divided by Zero')
# finally:
#     print("Its ok next time don't divide by zero")  
# print("Advance Python")
# print("Python Analytics")

'''output'''
# Python
# Core Python
# 1.0
# Its ok next time don't divide by zero
# Advance Python
# Python Analytics
'''-----------------------------------------------'''

# print("Python")
# print("Core Python")
# a=5
# b='6'
# try:
#     print(a/0)  
# except ZeroDivisionError: 
#     print('Not Ok Divided by Zero')
# finally:
#     print("Its ok next time don't divide by zero")  
# print("Advance Python")
# print("Python Analytics")

'''output'''
# Python
# Core Python
# Not Ok Divided by Zero
# Its ok next time don't divide by zero
# Advance Python
# Python Analytics
'''--------------------------------------'''
# print("Python")
# print("Core Python")
# a=5
# b='6'
# try:
#     print(a/0)  
# finally:
#     print("Its ok next time don't divide by zero")  
# print("Advance Python")
# print("Python Analytics")
# '''ouput'''
# Python
# Core Python
# Its ok next time don't divide by zero
# ZeroDivisionError: division by zero
'''here it execute upto 205 line then gives Zerodivisionerror'''
'''it is not mandatory to have exception block when finally block exsits '''
#finally block will excectue always irrespective of eroor
'''====================================================================='''
# print('welcome to python world')
# a=22
# b='b'
# try:
#     print(b+'hello')
#     print(a+'hello')
# except TypeError:
#     print('it is type error not repeat again')
# finally:
#     print('i am always free to excecute')
# print('bye')

'''output'''
#welcome to python world
# bhello
# it is type error not repeat again
# i am always free to excecute
# bye
'''============================================================================='''
# print('hello chitti')
# a=5
# b='jkl'
# try:
#     print(b+ ' is wrong sentence')
#     print(a/0)
# except TypeError:
#     print( 'it is type error')
# else:
#     print('it not a type error')
# print('bye chitti')
#output gives that is zero division error 
'''because else excecute when the except is false '''

'''===================================================='''
# print("Python")
# print("Core Python")
# a=5
# b='6'
# c=1
# try:
#     print(a/5)
#     print(c)  
# except NameError: 
#     print('Not Ok Divided by Zero')
# else:
#     print("Its ok next time don't divide by zero")   
# print("Advance Python")
# print("Python Analytics")

'''output'''
# Python
# Core Python
# 1.0        
# 1
# Its ok next time don't divide by zero
# Advance Python
# Python Analytics
'''---------------------------------------------------------------------'''

""" AssertionError"""

# n=int(input('Enter any value:'))
# if n<17:
#     assert print("You are not eligible to vote")


'''output'''
# Enter any value:16
# You are not eligible to vote
#     assert print("You are not eligible to vote")
# AssertionError

'''assertion error is user defined error it will excecute when it satisfy the statement (use keyword= assert) writing before print statement'''
'''==============================================================================================================='''

""" Making your own errors with exception"""

n=int(input('Enter the value more than 40:'))
if (n>40):
    raise Exception ('Your Eligible')

'''output'''
# Enter the value more than 40:45
# Exception: Your Eligible
''' exception error is also a user defined error using key word as( raise exception) here we not use print'''