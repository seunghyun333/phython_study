#14. 문자열포맷
python ='파이썬'
java='자바'

print(python + java)
print(python + ' '+ java)
print(python,java) #띄어쓰기 자동

print('1. 개발 언어에는 ' + python +', '+java+' 등이 있어요')

print('2. 개발 언어에는 {}, {} 등이 있어요'.format(python,java))
print('3. 개발 언어에는 {1}, {0} 등이 있어요'.format(python,java))
print(f'4. 개발 언어에는 {python}, {java} 등이 있어요')

#15. 탈출문자 \
print('나는 "마라탕을" 생각했다')
print("나는 '마라탕을' 생각했다")
print('하지만 \'나만 당할 순 없지\'라는 생각에 \"엄청 쉽지\"라고 했다.')

snack = '꿀꽈배기는 \n너무 \n맛있어요'
print(snack)

#16. 리스트1
my_list =['오예스','몽쉘','초코파이','초코파이']
print(my_list)
your_list=[1,2,True,False,'아무거나']
print(your_list)
empty_list = []
print(empty_list)

#17. 리스트2
print(my_list[0])
print(my_list[:2])
print('몽쉘' in my_list)
print(len(my_list))

my_list[1] = '수정' 
print(my_list)

my_list.append('추가')
print(my_list)

my_list.remove('수정')
print(my_list)

my_list.extend(your_list)
print(my_list)



'''
insert() 원하는 위치에 값 추가
pop() 원하는 위치 또는 마지막의 값 삭제
clear() 모든 값 삭제
sort() 값 정렬
reverse() 순서 뒤집기
copy() 리스트 복사
count() 어떤 값이 몇개 있는지
index() 어떤 값이 어디에 있는지 

---
add는 없음 
'''

print(my_list.index('추가')) #3
print(my_list.count('초코파이')) #2

my_list.insert(1, 'orange')  # 인덱스 1 위치에 'orange' 삽입
print(my_list)

my_list2 = ['초코파이', '초코파이']
print(my_list2) #['초코파이', '초코파이']