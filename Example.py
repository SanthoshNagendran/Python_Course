

import First
print(First.c)

from First import b
print(b)

a = 345
L = ['san', 123, a]
print(len(L))
print(L[2])
L + [1, 2, 3]
print(L)

L.append('Kala')
L.pop(1)
print(L)

X = ['CC' , 'BB' , 'AA']
X.sort()
print(X)

X.reverse()
print(X)

X.append('SS')
print(X)

X.pop(1)
X.sort()
print(X)

D = [3,45,22,1,43,66]
D.pop(2)
D.append(100)
D.sort()
print(D)

c = D + X + [['venky','sangee','monkey'],['mathake']]
print(c)

c.reverse()
print(c)

print(c[0])

print(c[1][0])

M = [[1,2,3],[2,4,6],[3,6,9]]
col = [row[2] for row in M]
print(col)
diag = [M[i][i] for i in [2,1,0]]
print(diag)
row = [col[0] for col in M]
print(row)

doubles = [i*2 for i in 'suresh']
print(doubles)

f = {x: ord(x) for x in 'santhosh'}
print(f)

D = {'Day': 'Friday', 'Time': 14.46, 'Year': 2019}
print(D['Time'])
D['Time'] += 4.00
print(D)

K={}
K[5] = 4
K[2] = 1
K[0] = 2
print(K)

Rec = {'Name': {'First': 'Santhosh', 'Last': 'Nagendran'}, 'Job': {'PT': 'MOTEL','FT': 'Engieer'}, 'Age': [23,1]}
print(Rec['Name'])
Rec['Age'].append('I meant years and months')
print(Rec)


Ks = list(K.keys())
Ks.sort()
print(Ks)
for Key in Ks:
    print(Key, '=>', K[Key])

for x in 'santhosh':
    print(x.upper())

for x in 'RAMESH':
    print(x.lower())

x = 0
while x <= 5:
    print('Sandy' * x)
    x+=1

D['Deadline'] = 'Infinity'
print(D)

if not 'DeadTime' in D:
    print('DeadTime not found so its going to be taken care of')
    D['DeadTime'] = 'Fixed'
    print(D)

T = (1,2,3,4)
print(T+(5,6))

#f = open('SampleFile.txt', 'w')
#f.write('Hello World\n')
#f.close()

f = open('SampleFile.txt')
text = f.read()
x = text.split()
print(x)

x = set('spam')
y = {'h','a','m'}
print(x,y)

#nam = input('who are you?')
#print('Welcome', nam)

#while 1:
 #   inp = input('0 or 1')
  #  usf = int(inp) + 1
   # if usf == 2:
    #    print('two')
   # else:
    #    print(usf)
     #   usf = input('type inn new data')
      #  if  type(usf) == str:
       #     print('thanks for entering a string')
        #else:
         #   print(usf)
          #  usf = input('please enter a string')
       # break
S = 'Santhosh'
S.find('th')

def Exp (x,y):
    z = x*y
    return(z)

x= 5; y=11
m = Exp(x,y)
print("value of m is",m)
#print(m)
x = input ('enter a value to multiply with m\n')
z = int(x)
y = Exp(z,m)
print(y)

a = Exp(1,2)

def Sandy(s1,s2):
    print("\nStart of Sandy s1 is",s1)
    print("Start of Sandy s2 is",s2)
    s1=[1,2,3,]
    s2=[4,5,6]
    print("\nEnd of Sandy s1 is ",s1)
    print("End of Sandy s2 is ",s2)
    return(s1,s2)

s1="Spam"
s2={1:"s","p":"a"}

b=Sandy(s1,s2)
print("\nreturned values for s1 & s2 ",b)

print("\ns1 is ",s1)
print("s2 is ",s2)

def Fun1 (x=1,y=2,z=3):
    return(x+y-z)

def concat_strings(a,b):
    str_type = type('')
    if type(a)==str_type and type(b)==str_type:
        return(a+''+b)
    if type(a)==int and type(b)==int:
        return(a*b)
    else:
        return(a*b)

print("strings:", concat_strings('first','second'))
print("Integers:", concat_strings(1,2))


import random
x=0;
a={}
while x<10:
    y = random.randint(0,9)
    a[x]=y
    #print("Dictionary key is ",x)
    #print("the value of this key is ",y)
    #print('Sandy' * x)
    x+=1

print(a)

for n in range(2,13):
    print("the value of n is",n)
    if n == 5:
        break
    n+=1

    

print('\nThat is %d %s bird!' %(1, 'dead'))

a='santhosh'
b=a.replace('a','EE')
print("\n",b)

S = 'spray'
L = list(S)

S=''.join(L)
print(S)

