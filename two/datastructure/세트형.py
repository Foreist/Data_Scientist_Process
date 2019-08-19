# 세트형은 중복되지 않는 것들부터 먼저 출력
a = set('abracadabra')
b = set('alacazam')

print('집합 a =', a);  print('집합 b =', b);
print('합집합, a | b =', a | b)
print('교집합, a & b =', a & b)
print('차집합, a - b =', a - b)
print('여집합, a ^ b =', a ^ b)

beast = ["lion", "tiger", "wolf", "tiger", "lion", "bear", "lion" ]
print(beast)

unique_beast = list(set(beast))
print(unique_beast)
sorted_beast = sorted(unique_beast)
print(sorted_beast)