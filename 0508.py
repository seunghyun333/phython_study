#23 딕셔너리2
person = {
    '이름':'나귀욤',
    '나이':7,
    '키':120
}

print(person.get('별명')) #없는 키 접근 시 None 출력 

#새로운 키 추가
person['최종학력'] ='유치원'

#키 바꾸기
person['나이'] = 8

#여러 개 수정
person.update({'키':130, '몸무게':120})
print(person) #{'이름': '나귀욤', '나이': 8, '키': 130, '최종학력': '유치원', '몸무게': 120}

#특정 키 삭제 -- 딕셔너리는 중복허용 x 
person.pop('몸무게')

#모든 자료형 삭제
#person.clear()
print(person)

#어떤 key들이 있는지 확인
print(person.keys()) #dict_keys(['이름', '나이', '키', '최종학력'])
#어떤 value들이 있는지 확인
print(person.values()) #dict_values(['나귀욤', 8, 130, '유치원'])

print(person) #{'이름': '나귀욤', '나이': 8, '키': 130, '최종학력': '유치원'}
print(person.items()) #dict_items([('이름', '나귀욤'), ('나이', 8), ('키', 130), ('최종학력', '유치원')])  콤마로 구분된 모든 데이터 

'''
fromkeys() 제공된 keys를 통해 새로운 딕셔너리 생성 및 반환
popitem() 마지막으로 추가된 데이터 삭제
setdefault() key에 해당하는 value 반환, key가 없다면 새로 만들고 default vlaue 설정 및 반환
'''
print(person.setdefault('이름'))
print(person.setdefault('지역'))


#24 자료형 비교
'''
리스트/ lst =[], 순서보장, 중복허용, 접근 lst[idx], tnwjdrksmd, 추가 append(), insert(), extend(), 삭제 remove(), pop() clear()
튜플/ t= (), 순서보장, 중복허용, 접근 t[idx], 수정x, 추가x, 삭제x
세트/ s={}, 순서 x, 중복 x, 접근x, 수정x, 추가 add(), update(), 삭제 remove(),discard(),pop(),clear()
딕셔너리/ d={key:value}, 순서보장, 중복x, 접근 d[key], d.get(key), 수정 가능(value),  추가 d[key]=val, update(), 삭제 pop(), popitem(), clear()

여러값들을 순서대로 관리: 리스트
값이 바뀔일 없고 안된다: 튜플
값의 존재여부 중요, 중복 안됨 :세트
key를 통해 효율적으로 관리: 딕셔너리 

'''