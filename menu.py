print('1.20mb')
print('2.50mb')
print('3.100mb')
choice= int(input('enter selection: '))
print(type(choice))

if choice==1:
    print('you have bought 20mb')
elif choice==2:
    print('you have bought 50 mb')
elif choice==3:
    print('you have bought 100 mb')
else:
    print('invalid')