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
