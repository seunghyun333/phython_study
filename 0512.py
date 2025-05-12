#32 while
max =25
weight =0
item =3

while weight + item <= max:
    weight += item
    print(f'짐을 추가합니다.{weight}')
print(f'총 무게는 {weight} 입니다')

#33 break
drama = ['시즌1', '시즌2', '시즌3', '시즌4', '시즌5']
for x in drama:
    if x=='시즌3':
        print('재미없대 그만보자')
        break
    print(f'{x} 시청')