#-----
#내장함수
#-----

#숫자 데이터 절대값 계산 내장함수 abs(n)
print(abs(-9))

#최댓값, 최소값 찾아주는 내장함수 max(), min()
print(max(10,3), min(10,3))
print(max(10,3,91), min(10,3,-2))

#제곱근 계산 내장함수 pow()
print('연산자 ** : ', 2**4)
print('내장함수 pow() :', pow(2,4))

#파일관련 내장함수 open(파일명, 동작모드, 인코딩)
#기본값: 동작모드_읽기(r)
#        인코딩_시스템 따라서  

FILE_PATH='0628.txt'

#1. 파일열기-쓰기모드
file=open(FILE_PATH, mode='w', encoding='utf-8')
#2. 데이터 쓰기
file.write('Hello\n')
file.write('안녕~ 좋은 아침이야')
#3. 파일 닫기
file.close()