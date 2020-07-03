"""
list / []

a[0:2] / 슬라이싱
len(a)
del a[1]
del a[1:]
a.append(a)
a.sort()
a.reverse()
a.index(1) / x의 위치, 없으면 오류
a.insert(0, '1')
a.remove(3) / 첫번째 3을 삭제
a.pop()
a.count(1)
a.extend(x) / x는 리스트만 가능
"""


"""
dictionary / {key:value}

a[key] = 'value'
del a[key]
*키에 리스트는 불가
list(a.keys()) / a.keys()가 리스트는 아님
a.values()
a.items()
a.clear()
a.get('key') / none 반환, 오류 아님, get 쓰자
'key' in a / True or False
"""

"""
set / set("hello")
- 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용

s1 & s2 / 교집합
s1.intersection(s2) / 교집합
s1 | s2 / 합집합
s1.union(s2) / 합집합
s1 - s2 / 차집합
s1.difference(s2) / 차집합

s1.add(4)
s1.update([1,2,3]) / 여러개 추가
s1.remove(4)

set에서 있는지 확인할 때?
'a' in list(s1)

"""

#continue

#result = [num * 3 for num in a]