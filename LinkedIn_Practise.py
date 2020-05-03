def Function1():
    print("i am a function")
    return 1

Function1()
print(Function1())

def func2(arg1,arg2):
    print(arg1+arg2)

func2(1,3)

def power(num, x=1):
    result =1
    return num*x

print(power(3))
print(power(x=4,num=3))

def Mul_Add(*x):
    result = 0
    for i in x:
        result+=i
    return result

print(Mul_Add(2,3,4,5,6))

for n in range(0,10):
    if(n==5):break
    print(n)


class myClass():
    def mySample():
        print("Inside the first sample class")
    def Sample_2(x):
        print("Inside the second sample class", x, "elsemore")


class InheritedClass():
    def mySample():
        myClass.Sample_2("testing func inside base class from inherited class")
        print("Inside the first ingerited class")
    def Sample_2():
        print("Inside the second inherited class")

c = myClass
c2=InheritedClass


c.mySample()
c.Sample_2("eeeeeee")
c2.mySample()
c2.Sample_2()

f = open("SampleFile.txt","r")
if f.mode == 'r':
    print("file open success")
    contents = f.read()
    print(contents)


def files_sample():
    print("added")
    f = open("newTextFile.txt","w+")
    for a in range(0,10):
        print("added")
        f.write("I just wanted to test the appending of a file is working 10 times" + str(i) + "\r\n")
    print("added")
    f.close()
files_sample()
