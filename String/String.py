# 문자열 - 문자, 단어 등으로 구성된 문자들의 집합

print("Life is too short, You need Python")
print("a")
print("123")

# 1. 큰따옴표(")로 양쪽 둘러싸기
print("Hello World")

# 2. 작은따옴표(')로 양쪽 둘러싸기

print('Python is fun')

# 3. 큰따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기
print("""Life is too short, You need python""")

# 4. 작은따옴표 3개를 연속(''')으로 써서 양쪽 둘러싸기
print('''Life is too short, You need python''')

# 1-1 문자열에 작은따옴표 (')포함시키기
food = "Python's favorite food is perl"

# 2-2 문자열에 큰따옴표(")포함시키기
say = '"Python is very easy." he says.'

# 3-3 백슬래시(\)를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기

abc = 'Python\'s favorite food is perl'
qwe = "\"Python is very easy.\" he says."


# 여러 줄인 문자열을 변수에 대입하기

# 1. 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
multiline = "Life is too short\nYou need python"

# 2. 연속된 작은따옴표 3개(''') 또는 큰따옴표 3개(""") 사용하기

multiline='''
Life is too short
You need python
'''

# 이스케이프 코드란? - 프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 "문자 조합"이다.

# Concatenation.py
# multistring.py

# 문자열 길이 구하기 - len 함수는 파이썬의 기본 내장 함수다.

a = "Life is too short"
len(a)

### 문자열 인덱싱과 슬라이싱
## 인덱싱(Indexing) - "가리킨다"
## 슬라이싱(Slicing) - "잘라낸다"

### 문자열 인덱싱이란?
a = "Life is too short, You need Python"
a[3]
# 'e'

## "파이썬은 0부터 숫자를 센다."
## a[0]:'L', a[1]:'i', a[2]:'f', a[3]:'e', a[4]:' ', ...
## a[번호] - 문자열 안의 특정한 값을 뽑아내는 역할

### 문자열 인덱싱 활용하기
a[-1]
# 'n'

## 문자열을 뒤에서부터 읽기 위해 마이너스(-) 기호를 붙이는 것

### 문자열 슬라이싱이란? - 단어를 뽑아내는 방법
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
b
# 'Life'

## 위 방법처럼 단순하게 접근할 수도 있지만 파이썬에서는 더 좋은 방법을 제공한다.

a = "Life is too short, You need Python"
a[0:4]
# 'Life'

## 자리 번호 0부터 4까지의 문자를 뽑아낸다.

## 하지만 다음과 같은 의문이 생길 것이다. a[0]은 L, a[1]은 i, a[2]는 f, a[3]은 e니까 a[0:3]으로도 Life라는 단어를 뽑아낼 수 있지 않을까? 다음 예로 확인해 보자.
a[0:3]
# 'Lif'

## 슬라이싱 기법으로 a[시작 번호:끝 번호]를 지정할 때 끝 번호에 해당하는 것은 포함하지 않기 때문이다.

## a[0:3] 수식 - 0 <= a < 3

### 문자열을 슬라이싱하는 방법
a[0:5]
# 'Life '
## a[4]는 공백 문자이기 때문이다.

## 슬라이싱할 때 항상 시작 번호가 0일 필요는 없다.

a[5:7]
# 'is'

## a[시작 번호:끝 번호]에서 끝 번호 부분을 생략하면 시작 번호부터 그 문자열의 끝까지 뽑아낸다.

a[19:]
# 'You need Python'

## a[시작 번호:끝 번호]에서 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지 뽑아낸다.

a[:17]
# 'Life is too short'

## a[시작 번호:끝 번호]에서 시작 번호와 끝 번호를 생략하면 문자열의 처음부터 끝까지를 뽑아낸다.

a[:]
# 'Life is too short, You need Python'

## 슬라이싱에서도 인덱싱과 마찬가지로 마이너스(-) 기호를 사용할 수 있다.
a[19:-7]
# 'You need'

### 슬라이싱으로 문자열 나누기