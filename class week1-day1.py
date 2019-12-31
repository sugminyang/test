
# coding: utf-8

# # Python class

# In[ ]:


123 + 321


# # 1. 기본 출력

# In[ ]:


print('my name is dean')


# In[ ]:


print('Hello python')


# In[ ]:


print(1, 2, 3)

print('Hello', 'Python')


# In[ ]:


print('my','name','is','dean')


# In[ ]:


print( 'i am' , 1 )


# # 2. 변수와 값 저장

# ## 2-0 주석(comment)

# In[ ]:


age = 10 # assign value 10 in age variable.
age = 20 
age = 10

print(age)


# ## 2-1 정수(int) 값 저장

# In[ ]:


10 == 10


# In[ ]:


age = 20
print(age)


# In[ ]:


age = 20

print('---- Result ----')
print(age)


# ### i.g 통장에 100만원이 있다. 변수이름은  myAccount로 설정하고 balance를 저장하시오.

# In[ ]:


myAccount = 1000000

print('---- Result ----')
print(myAccount)


# ## 2-2 실수(float) 값 저장

# In[ ]:


height = 175.6

print('---- Result ----')
print(height)


# In[ ]:


h1 = 123.2
h2 = 122.5

print(h1)

student = [123.2,122.5]
print(student[0])
print(type(student))

number = list(range(10))
print(student)

print(number)


# ## 2-3 문자열(string) 값 저장

# In[ ]:


name = 'dean'

print('---- Result ----')
print('my','name is',name)


# In[ ]:


city = "seoul"
print("I",'live','in',city)


# ## 2-4 논리형(boolean) 저장

# In[ ]:


isHuman = False #True or False


print('---- Result ----')
print(isHuman)


# ## 2-5 data type 확인 방법(type)

# In[ ]:


print(type(name))

number = 124215
print(type(number))

weight = 63.4456
print(type(weight))

print(type(False))

age = '20'
print(age)

print('age type:',type(age))

age + 20
print(age)


# # 3. 사칙연산
#  - ppt 참고(11p)

# In[ ]:


data1 = 3
data2 = 2

print ('---- Result ----')
print (data1 + data2)  # 더하기
print (data1 - data2)  # 빼기
print (data1 * data2)  # 곱하기
print (data1 / data2)  # 나누기
print (data1 ** data2) # 제곱
print (data1 % data2)  # 나머지


# ## 3-1 괄호 사용하기
#  - 우선 순위를 명시적으로 표현

# In[ ]:


print('1) 35 + 1 * 2')
print(35 + 1 * 2)

print('2) (35 + 1) * 2')
print((35 + 1) * 2)


# # 4. 여러 문자열들 연결하기
#  - +을 이용

# In[ ]:


str1 = "Hello"
str2 = "World"

print('---- Result ----')
print(str1 + ' ' + str2)  # 더하기
print(str1,str2)


result = str1 + ' ' + str2
print('result: ',result)


# In[ ]:


name = input('Enter a name: ')
base = 'your name is'
age = 10

print(base+name+str(age))


# In[ ]:


11:20 Nov 12, 2019 => 정수형 변환 or 문자열

시간 분 초 년 월 일 beginToContact
11 20 00 2019 11 12 M
11 22 32 2019 11 12 F


# # 5. 문자열 반복하기
#  - escape code ppt 참고(12p)

# In[ ]:


data = "Hello! \n" # \n은 줄을 바꾸라는 의미
print(data)
print(data)
print(data)
print(data)
print(data)

print('---- Result ----')
print(data * 5)


# # 6. 문자열 슬라이싱
#  - ppt 참고(13p)

# In[ ]:


data = "Hello World"


print ('---- Result ----')
print (data)
print (data[0])
print (data[3])
print (data[1:4])
print(data[1:7])
print(data[1:len(data)])
print(data[1:11])
print(data[1:])
len(data)


# In[ ]:


height = 172
print(type)


# ### i.g 문자열 슬라이싱 활용

# In[ ]:


data = "Hello World"

print('---- Result ----')
print(data[0:4]) # Hell
print(data[:5]) # Hello
print(data[6:]) #World
print(data[-1]) #"Hello Worl"


# # 7. 문자열 함수 예제
#  - ppt 참고(14p)

# In[ ]:


sample = " My favorite language is python "

print('---- Result ----')
print(len(sample))
print(sample.count('a'))
print(sample.index('y'))
print(sample.upper())
print(sample.lower())
print(sample.strip())
print(sample.replace("python", "java"))
print(sample.split())


# # 7- 파일 입출력

# In[ ]:


f = open('./sample.txt','r')
print(type(f))

header = f.readline()
header.split('\n')[0].split()
print(header.split('\n')[0])
print(header.split('\n')[0].split())

line = f.readline()
print(line)
print(line.split())

f.close()


# In[ ]:


f = open('./sample2.txt','w')

f.write('시간 분 초 년 월 일 beginToContact\n')
f.write('11:20 Nov 12, 2019 M')

f.close()


# # 8. 데이터 형변환(cast)

# ## 8-1 정수형, 실수형 -> 문자열 형변환

# In[ ]:


print('정수형 -> 문자열 (str()함수 사용)')
age = 20
print(age)
print(type(age)) #int

print("--- after casting ---")
aStr =str(age)
print(aStr)

#print(str(age),str(age),str(age),sep="\n")

aStr = aStr + "\n"

print(aStr*3)

for i in list(range(3)):
    print(str(age),sep="\n")
    
print(type(str(age)))
print(type(aStr))


# ## 8-2 문자열 -> 정수형 (int()) 형변환 , 실수형(float())

# In[ ]:


print('문자열 -> 정수형 형변환(int() 함수 사용)')
age = '20'
print(age)
print(type(age))

print("--- after casting ---")

print(int(age))
print(type(int(age)))

print("--- after casting ---")

print(float(age))
print(type(float(age)))


# In[ ]:


#list, tuple
#문자열 -> 리스트, 튜플
str = "abc"
print(tuple(str))
print(list(str))


# In[ ]:


temp = 20.0
print(temp)
aTemp = str(temp) + "00"
print(aTemp)

print(float(aTemp))


# ## 캐스팅이 필요한 이유

# ### 오류 상황

# In[ ]:


age = '20'
parentAge = age + 'num'
print(parentAge)


# ### 해결방안

# In[ ]:


age = '20'
parentAge = int(age) + 30
print(parentAge)


# # 9. 여러 타입 데이터 연결하기

# In[ ]:


age = 20        #정수형
name = 'dean'   #문자열
height = 175.6  #실수형

profile = 'my name is ' + name + '. I am ' + str(age) + ' years old and ' + str(height) + ' tall.'

print(profile)


# # 10. 논리 연산자

# In[ ]:


print('--- and operator ---')
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print('--- or operator ---')
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print('--- not operator ---')
print(not True)
print(not False)


# ### i.g complex logical expression

# In[ ]:


print('not True and False or not False')
print('(not True) and False or (not False)')
print('False and False or True')
print('(False and False) or True')
print('False or True')
print('True')


# # 11 비교 연산자
#  - ppt참고(15p)

# In[ ]:


print(10 > 20) #F
print(10 < 20) #T
print(10 == 20) #F
print(10 != 20) #t


# # 12 사용자 입력받기
#  - input() 사용

# In[ ]:


input()


# ## 12-1 사용자 입력 저장하기

# In[ ]:


x = input()
print(x)


# ### i.g 사용자에게 이름을 입력받아 출력하시오.

# In[ ]:


name = input()
print('oh, your name is ' + name)


# ### i.g 사용자에게 숫자를 입력받아 50을 덧셈하여 출력하시오.

# In[ ]:


num = input('Enter a number: ')
result = int(num) + 50
print(result)


# ### i.g 사용자에게 숫자 2개를 입력받아 더하는 프로그램을 작성하시오.

# ### 캐스팅이 필요한 이유2

# In[ ]:


num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
result = num1 + num2

print(result)


# In[ ]:


num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
result = int(num1) + int(num2)

print(result)


# # 두 변수가 담은 값를 변경해보시오. (변수 하나를 더 이용해서)

# In[ ]:


a = 10
b = 20


# In[ ]:


print(a) #10
print(b) #20


# In[ ]:


a,b = b,a
print(a)
print(b)


# In[ ]:


c = a
a = b
b = c

print(a)
print(b)

