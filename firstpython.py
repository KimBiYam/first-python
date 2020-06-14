import datetime
import time
import random

print('hello world!')
print(1)
print([1, 2, 3])
print(1, 2)
print(1, 2, 3)
print('python')
print('My name is', 'Chang Hyun')

# print(input('이름을 입력하세요'))
# age = input('당신의 나이는?')

my_int = 1
my_int += 1
print(my_int)
my_float = 3.1
print(type(my_int))
print(type(my_float))

my_list = []
my_list = [1, 2, 3]
print(my_list)

students = ['홍길동', '강감찬', '아아아']

print(random.choice(students))
students[0] = '김창현'
print(students)

my_tuple = ('홍길동', '강감찬', '아아아')
# 튜플은 리스트와 다르게 값 변경이 불가
# my_tuple[0] = '김창현'

# 딕셔너리 : key : value로 구성되어있음(자바의 map과 유사)
my_dict = {'홍길동': '남', '강감찬': '남', '아아아': '여'}
print(my_dict['아아아'])
my_dict['아아아'] = '남'
print(my_dict['아아아'])

# 자료형 변환
print("float로 변환:", type(float(my_int)))
print("int로 변환:", type(int(my_float)))
print("str로 변환:", type(str(my_int)))

# list() 한글자씩 뽑아와 list 형태로 변환
my_str = "coding"
print(list(my_str))

# String은 큰 따옴표 작은따옴표 둘 다 가능
my_str = "김씨가족"
print(my_str)
my_str = '김씨가족'
print(my_str)

# """ , ''' : 따옴표 3개를 쓰면 여러줄의 String을 한 변수에 담을 수 있음
my_str = """김창현
홍길동
강감찬
"""
print(my_str)

# %s : 문자열을 대입할때 씀(Young Choi가 앞 문자열 %s에 들어감)
my_str = 'My name is %s' % 'Young Choi'
print(my_str)
# %d : 정수형 숫자를 대입할때 씀
my_int = '%d %d' % (1, 2)
print(my_int)
# %f : 실수형 숫자를 대입할때 씀
my_float = '%f' % 3.14
print(my_float)

# format( % 사용하지 않고 괄호와 뒤에 format 함수를 사용)
my_str = 'My name is {}'.format('홍길동')
print(my_str)

print('{} x {} = {}'.format(2, 3, 2*3))
# 괄호안에 숫자로 format함수의 값을 순서를 지정해서 대입 가능
print('{1} x {0} = {2}'.format(2, 3, 2*3))

# 인덱싱 : 문자열의 특정 위치의 값을 바로 추출 가능
my_name = "가나다라 마바사아"
print(my_name[3])
print(my_name[7])
print(my_name[-1])

# 슬라이싱 : 문자열의 지정한 위치의 여러개의 값을 바로 추출 가능
print(my_name[5:7])
print(my_name[:3])
print(my_name[2:])

# split 메소드
print(my_name.split())
fruit_str = '거봉 수박 포도 복숭아 망고 딸기 배 참외'
fruits = fruit_str.split()
print(fruits)
fruit_str = '거봉:수박:포도:복숭아:망고:딸기:배:참외'
fruits = fruit_str.split(":")
print(fruits)

# """(독스트링) : 함수 시작 부분에서 함수 인터페이스를 설명하는 문자열(주석의 역할)
""" 이 함수는 이런저런 역할을 합니다 """

# print 와 end : end 값을 입력하게되면 해당 문자열 출력 후 end의 값을 출력
# print 함수는 기본적으로 enter를 포함하는데 end값을 주면 enter를 출력하지 않는다
print('집단지성')
print('집단지성')
print('집단지성', end='')
print('집단지성', end='/')

# 이스케이프 코드
print('미운코딩새끼의 집단지성들')
print('미운코딩새끼의\n집단지성들')
print('미운코딩새끼의\t집단지성들')
print('미운', end='\t')
print('코딩')

# 리스트
my_list = []
print(type(my_list))
my_list = [1, 2, 3]
print(my_list)
# append() : 리스트 값 추가 함수
my_list.append(4)
print(my_list)

animals = []
animals.append('코알라')
animals.append('하이에나')
animals.append('바다소')
# insert() : 리스트의 원하는 위치에 해당 값 입력 가능
animals.insert(2, '다람쥐')
animals.append('스컹크')
animals.append('아나콘다')
animals.append('바다코끼리')
print(animals)


print(animals[3])
# del로 변수를 삭제
del fruit_str
# del로 리스트에 인덱스를 지정하면 리스트에서 해당 값 삭제
del animals[2]
print(animals)
# 리스트에서도 슬라이싱 마찬가지로 사용가능
print(animals[0:2])

# sort() : 리스트 정렬 가능
animals.sort()
print(animals)
# count() : 리스트에서 해당값과 같은 값의 수를 출력
print(animals.count('바다소'))
# len() : 해당 리스트, 문자열의 length 출력
print(len(animals))
print(len(my_str))


# 튜플 : 리스트와 같지만 값의 변경 불가능
my_tuple = ()
print(my_tuple)
print(type(my_tuple))
# 선언할때에 변수명에 괄호를 넣어도되고 그냥 , 로 구분지어주기만 해도 됨
my_tuple = (1, 2, 3)
print(my_tuple)
print(type(my_tuple))

my_tuple = 1, 2, 3
print(my_tuple)
print(type(my_tuple))

# 패킹과 언패킹
my_tuple = 1, 2, 3
print(my_tuple)
num1, num2, num3 = my_tuple
print(num1)
print(num2)
print(num3)

num1, num2 = num2, num1
print(num1)
print(num2)

# for문 : 파이썬에서는 for문 안에서 들여쓰기를 무조건 해줘야 함
# 한번 들여쓰기를 했으면 그 뒤로도 똑같이 띄워줘야함(탭으로 띄었으면 끝까지 탭으로)
for index, i in enumerate(my_tuple):
    print('인덱스:', index)
    print('for문:', i)

for animal in animals:
    print(animal)

for num in [1, 2, 3]:
    print(num)

for my_str in "김왼손의 왼손코딩":
    print(my_str)
    print(my_str)

# range : 숫자를 하나만 넣으면 0부터 해당값 까지 생성
# 두 개를 넣으면 앞의 숫자부터 뒤의 숫자까지 생성

print(range(3))
print(type(range(3)))

for n in [0, 1, 2]:
    print(n)

for n in range(0, 3):
    print(n)
# enumerate를 이용하면 리스트 range에서 index가 사용 가능
for index, n in enumerate(range(0, 100)):
    print('인덱스', index)
    print(n)
# 중복 반복문
for j in range(2, 10):
    for i in range(1, 10):
        print('{}x{}={}'.format(j, i, j*i))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = []

for number in numbers:
    if number % 2 == 1:
        odd_numbers.append(number)
print(odd_numbers)

# Comprehension
odd_numbers = [number for number in numbers if i % 2 == 1]
print(odd_numbers)


print(3 ** 2)
print(2 // 2, end="\n------------\n")

for num in range(1, 8):
    if num % 2 == 1:
        print(num)

for num in range(1, 8):
    if num % 2 == 1:
        print(num, end=" ")
        print("홀수!")
    else:
        print(num, end=" ")
        print("짝수!")

print('김왼손' + 'X' + '엘리스')
print('안녕' * 3)


def cls():
    print('\n'*100)


# 논리 연산자
print(True and True)
print(True and False)
print(False and False, end="\n---------\n")

print(True or False)
print(True or False)
print(False or False, end="\n---------\n")

print(not False)
print(not True, end="\n---------\n")

students = ['홍길동', '강감찬', '이성계', '김창현']

print('홍길동' in students)
print('이에스' in students)
print('홍길동' not in students)
print('이에스' not in students, end="\n---------\n")

input_name = input("이름을 입력하세요\n:")

# 조건문 파이썬에서는 else if 대신 elif 사용
if len(input_name) >= 3:
    print("Hello", input_name)
else:
    print("이름은 세글자 이상 입력해주세요")

name = input("이름을 입력하세요\n:")

if name == '김왼손':
    print('당신이 김왼손이군요!')
elif name == '호박':
    print('당신이 호박이군요!')
elif name == 'Meta':
    print('당신이 Meta군요!')
else:
    print('당신은!?')

count = 0
while count < 3:
    print('횟수:', count)
    count += 1

count = 0
while count < 10:
    count += 1
    if count < 4:
        continue
    print('횟수:', count)
    if count == 8:
        break

# 딕셔너리
my_dict = {}
print(type(my_dict))

my_dict[0] = 'a'
print(my_dict)
my_dict['b'] = 2
my_dict['학생1'] = '홍길동'
my_dict['학생2'] = '김창현'
print(my_dict)

print(my_dict['b'])

del my_dict['b']
del my_dict[0]
print(my_dict.values())

for std in my_dict.values():
    print(std)

for key, val in my_dict.items():
    print(key, val)


def add(num1, num2):
    return num1 + num2


print(add(1, 2))


def add_mul(num1, num2):
    return num1 + num2, num1 * num2


print(add_mul(1, 2))

my_add, my_mul = add_mul(1, 2)
print(my_add)
print(my_mul)

print(random.sample(range(1, 46), 6))

print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
print(datetime.datetime.now())
