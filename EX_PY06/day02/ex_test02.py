#연산자 실습

#실습] 문자열 데이터 2개에 대한 논리 연산 수행 후 출력
#data1='Hello'
#data2='hello'

data1='Hello'
data2='hello'

print(f'{data1}>{data2} and {data1}=={data2} : {data1>data2 and data1==data2}')
print(f'{data1}<{data2} or {data1}=={data2} : {data1<data2 or data1==data2}')

#실습] 정수 1개와 문자열 1개에 대한 논리 연산(not 연산자만 사용) 수행 후 출력
#num1=-3.2/0
#msg='원더우먼'/''

num1=-3.2
num2=0  #0: false
msg1='원더우먼'
msg2='' #'': false

print(f'not{num1} : {not num1}')
print(f'not{num2} : {not num2}')

print(f'not{msg1} : {not msg1}')
print(f'not{msg2} : {not msg2}')
