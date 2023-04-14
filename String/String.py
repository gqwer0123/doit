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

a = "20010331Rainy"
date = a[:8]
weather = a[8:]
date
# '20010331'
weather
# 'Rainy'

### "Pithon"이라는 문자열을 "Python"으로 바꾸려면?
a = "Pithon"
a[1]
# 'i'
a [1] = 'y'

"""

오류가 발생한다. 왜냐하면 문자열의 요솟값은 바꿀 수 있는 값이 아니기 때문이다.
문자열 자료형은 그 요솟값을 변경할 수 없다.
(immutable한 자료형이라고도 부른다.)

"""

a = "Pithon"
a[:1]
# 'P'
a[2:]
# 'thon'
a[:1] + 'y' + a[2:]
# 'Python'


### 문자열 포매팅
## 문자열 포매팅(Formatting)이 있다.

## "현재 온도는 18도입니다."
## "현재 온도는 20도입니다."

## 위 두 문자열은 모두 같은데 숫자만 다르다. 이렇게 문자열 안의 특정한 값을 바꿔야 할 경우가  있을 때 문자열 포매팅 기법을 이용한다.

### 문자열 포매팅 따라 하기

## 1.숫자 바로 대입

"I eat %d apples." % 3
# 'I eat 3 apples.'

## 여기에서 %d는 문자열 포맷 코드라고 부른다.

## 2. 문자열 바로 대입

" I eat %s apples." %"five"
# 'I eat five apples.'

## 문자열을 대입할 때는 앞에서 배운 것처럼 큰따옴표나 작은따옴표를 반드시 써주어야 한다.

## 3.숫자 값을 나타내는 변수로 대입
number = 3
"I eat %d apples." % number
# 'I eat 3 apples.'

## 4.2개 이상의 값 넣기
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)
# 'I ate 10 apples. so I was sick for three days.'

## 위 예문처럼 2개 이상의 값을 넣으려면 마지막 % 다음 괄호 안에 콤마(,)로 구분하여 각각의 값을 넣어준다.

## %s 포맷 코드 - 어떤 형태의 값이든 변환해 넣을 수 있다.

### [포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다.]

## 문자열 포맷 코드인 %d와 %가 같은 문자열 안에 존재하는 경우, %를 나타내려면 반드시 %%로 사용하는 법칙이 있다.
"Error is %d%%" % 98
#'Error is 98%.'

### 포맷 코드와 숫자 함께 사용하기
## 1. 정렬과 공백
"%10s" % "hi"
# '          hi'

## 앞의 예문에서 %10는 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 남겨 두라는 의미이다.

## 2.소수점 표현하기
"%0.4f" % 3.42134234
# '3.4213'

### format 함수를 사용한 포매팅
## 문자열의 format 함수를 사용하면 좀 더 발전된 스타일로 문자열 포맷을 지정할 수 있다.

## 숫자 바로 대입하기
"I eat {0} apples.".format(3)
'I eat 3 apples'

## 문자열 바로 대입하기
"I eat {0} apples".format("five")
'I eat five apples'

## 2개 이상의 값 넣기

number = 10
day = "three"

"I ate {0} apples. so I was sick for {1} days.".format(number, day)

#'I ate 10 apples. so I was sick for three days.'

## 이름으로 넣기
