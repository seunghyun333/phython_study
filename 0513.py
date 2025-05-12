# 34. Continue
drama = ['시즌1', '시즌2', '시즌3', '시즌4', '시즌5']

for x in drama:
    if x =='시즌3':
        print('재미없대 스킵')
        continue
    print(f'{x} 시청')


#35 들여쓰기
'''
들여쓰기 적용되면 하나의 문단으로 보기 

if, for, while, def, try, class:
:으로 끝나는 다음 줄은 들여쓰기 해야함 
'''

#36 리스트 컴프리헨션
products = ['JOA-2020', 'JOA-2021', 'SIRO-2021', 'SIRO-2022']
recall = []
for p in products:
    if p.startswith('SIRO'):
        recall.append(p)

my_list = [1,2,3,4,5]
new_list = [x*10 for x in my_list if x>3]
new_list2 = [str(x)+'번째' for x in my_list if x>3]
print(new_list2)


recall2 = [x for x in products if x.startswith('SIRO')]
print(recall2)

prod_se = [p +'SE' for p in products]
prod_lower = [p.lower() for p in products]
prod_new = [p+'(최신형)' for p in products if p.endswith('2022')]

print(prod_se)
print(prod_lower)
print(prod_new)


#37 함수
def show_price():
    print('커트가격은 10000원입니다')

show_price()