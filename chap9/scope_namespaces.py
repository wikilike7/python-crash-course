# def scope_test():
#     def do_local():
#         spam = 'local spam'

#     def do_nonlocal():
#         nonlocal spam
#         spam = 'nonlocal spam'

#     def do_global():
#         global spam
#         spam = 'global spam'

#     spam = 'test spam'
#     do_local()
#     print('Afer local assignment:', spam)
#     do_nonlocal()
#     print('After nonlocal assignment:', spam)
#     do_global()
#     print('After global assignment:', spam)

# scope_test()
# print('In global scope:', spam)

money = 2000

def addmoney():
    global money
    #money = 10
    money += 1
    print(money)

print(money)
addmoney()
#print(money)
    