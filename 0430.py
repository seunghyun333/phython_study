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

#12