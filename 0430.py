# 8.불리안
# bool(?) 값이 있으면 True, 없으면 False
a="안녕"
b=" "
c=""
print(bool(a))
print(bool(b))
print(bool(c)) #False

a=1
b=-2
c=0
print(bool(a))
print(bool(b))
print(bool(c)) #False

print(bool(None)) #False

#9 주석
# 한줄주석
'''여러 줄 주석 '''

#10 인덱스와 슬라이싱 
lang ='PYTHON'
print(lang[0]) #첫 번째 값 
print(lang[-1]) #마지막 값 

print(lang[1:6]) #1부터 6직전까지(=5까지)
print(lang[1:])  #1부터 끝까지 
print(lang[:4])  #처음부터 3까지 
print(lang)
print(lang[:])

#11 문자열 처리
num = 3
num += 2
num -= 1
num *=2
print(num)

snack ='꿀꽈배기'
print(len(snack))

snack = '''꿀꽈배기는
너무
맛있어요'''
print(snack)

#12 문자열 메서드  
# 클래스 내에 정의된 어떤 동작, 기증을 하는 코드들의 묶음 

letter = 'how are YOU?'
print(letter.lower())
print(letter.upper())

#첫글자만 대문자로
print(letter.capitalize())

#각 단어들의 첫 글자만 대문자로
print(letter.title())

#대문자를 뒤바꾸려면
print(letter.swapcase())

#문자열을 나누려면
print(letter.split()) #리스트형태

#몇번쓰였는지
print(letter.count('how'))

#13. 문자열 메서드 2

s='나도고등학교'
#나도로 시작하는지
print(s.startswith('나도'))

#어떤 문자로 끝나는지
print(s.endswith('학교'))

#앞뒤로 불필요한 부분 제거
s='....나도고등학..교...'
print(s.strip('.')) #나도고등학..교, 값을 넣지 않으면 앞뒤 공백 제거 됨 

#문자열 변경 
s='나도고등학교'
print(s.replace('고등학교', '고교'))

#특정 글자 위치 찾기
print(s.find('학교'))

#다른 문자들 사이에 넣기
print(s.center(10,'-')) #--나도고등학교--
print(s.center(11,'-')) #---나도고등학교--