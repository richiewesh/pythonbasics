names = ['dan', 1, 'tim', True, False, 10.2]
print(names)
print(len(names))
print(names[-1])
print(names[-4])
print(names[2])
print(names[-2])
matrix=[ [1 ,2, 3], [4,5,6,['a','b','c','d',[11,12,13]]] ,[7,8,9]]
print(matrix[1][2])
print(matrix [1][3][-1])
print(matrix[-1])
print (matrix[1][3][4] [2])
numbers=[1,2,3,4,5,6,7,8,9,]
numbers[2]=11
# popping  removes the last element on a list
numbers.pop()
print(numbers)
empty=[2]
empty.append("orange")
print(empty)
months=('jan','feb','march','april')
print(months[3])
userName='mark zuckerberg'
passWord='pwd'

myDbValues=(1,'mark zuckerberg','password',38,'male')
un=myDbValues[1]
print(un)
pss=myDbValues[2]
print(pss)
#== srict equality sign
if un==userName:
    print('userName true')
else:
    print('userName false')
if pss==passWord:
    print('password true')
else:
    print('password false')
    dict = {'username':'mark  zuckerberg','password':'pwd','age':38,['money']}

    print(dict['username'])
    print(dict['password'])
    print(dict['age'])





