#18 튜플 - 읽기 전용
'''
리스트 = [값1, 값2]
튜플 = (값1, 값2)  => 소괄호, 수정불가, 읽기 전용, 중복 허용, 아무 자료형 가능, , 순서 보정, 슬라이싱 가능, in, 
'''

#19 튜플2
my_tuple = ('오예스', '몽쉘', '초코파이') #패킹 
(pie1, pie2, pie3) = my_tuple #언패킹 my_tuple을 풀어서 각 pie에 값 넣기 

print(pie1) #오예스 

numbers =(1,2,3,4,5,6,7,8,9,10)
(one, two, *others) = numbers
print(others) #튜플이 아닌 리스트 형태임  [3, 4, 5, 6, 7, 8, 9, 10]

#20 세트 - 순서x, 중복x
A = {'돈까스','보쌈', '제육덮밥'}
B = {'짬뽕', '초밥', '제육덮밥'}
print(A.intersection(B)) #교집합
print(A.union(B)) #합집합 {'보쌈', '짬뽕', '제육덮밥', '돈까스', '초밥'} 중복허용 x , 순서 보장 x 할때마다 다르게 나올 수 있음 
print(A.difference(B)) #교집합 

set2={1,2,3,4,4,5}
print(set2) #출력결과 : {1, 2, 3, 4, 5}

#21 세트2
my_set = {'돈까스', '보쌈', '제육덮밥'}
my_set.add('닭갈비')
print(my_set)

my_set.remove('제육덮밥')
print(my_set)

my_set.clear() #내용 삭제 
print(my_set) #출력결과 : set()

del my_set #완전 삭제
#print(my_set) #NameError: name 'my_set' is not defined

'''
copy() 세트 복사
discard() 값 삭제(해당 값이 없어도 에러발생 x)
isdisjoint() 두 세트에 겹치는 값이 없는지 여부
issubset() 다른 세트의 부분집합인지 여부 
issuperset() 다른 세트의 상위집합인지 여부
update() 다른 세트의 값들을 더함 
'''

'''
리스트 : [] - 순서 보장, 슬라이싱, 인덱스 , 중복허용 
튜플 : () - 읽기전용, 집합으로 출력, 삭제만 가능, 중복 허용
세트: {} - 순서 보장 x, 중복허용 x 
'''

#22 딕셔너리1 - key,value / key 중복허용x, 여러자료형 사용 가능 
'''
딕셔너리 = {key1:value1, key2:value2}
'''

person = {
    '이름':'나귀욤',
    '나이':7,
    '키':120
}

print(person['이름'])

#23 딕셔너리2 33:16