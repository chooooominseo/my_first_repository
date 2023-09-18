my_var = 10
print(my_var)

my_list = {1, 2, 3}
print(*my_list)
"""
# 정수
my_int = 10
print(my_int)

# 부동 소수점
my_float = 3.14
print(my_float)

# 복소수
my_complex = 3 + 4j
print(my_complex)

# 문자
my_character = 'A'
print(my_character)

my_char = "@"
print(my_char)

# 문자열
my_string = 'Hello, World!'
print(my_string)

str_name = "python"
print(str_name)

# 불리언
my_bool = True
print(my_bool)

bFlag = False
print(bFlag)

#리스트
my_list = {1, 2, 'three', True}
print(my_list)

lsElement = {3.14, "b", 'two', False}
print(lsElement)

# 리스트 활용
my_list = [10, 3, 8, 9, 42, "hello"]

print(my_list)
print(*my_list)

# 크기
print(my_list.__len__())

# 인덱스
print(my_list[3])

list_el = my_list[2]
print(list_el)

# 엘레멘트 변경
my_list[3] = 11

print(my_list)

n_add = my_list[3] + my_list[2]
print(n_add)

# 슬라이딩
print(my_list[2:5])
print(my_list[:3])
print(my_list[0:3])
print(my_list[4:])

# 이중리스트

my_list = [10, 3, 8, 9, 42, "hello", [5, 4, 2, "world"]]

print(my_list)

# 이중 리스트 접근

print(my_list[6][1])

print(my_list[6][2:])

print(my_list[5][2])

# 메소드
my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)

my_list.insert(2, 4)
 
print(*my_list)

my_list = [10, 3, 8, 9, 42, "hello"]

print(my_list.index(3))

# append(value)
my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)

#
my_list.append(22)
print(*my_list)

#value와 동일한 요소, 갯수 출력
print(my_list.count(8))
print(my_list.count(5))

#마지막 요소 출력 후 삭제
my_list = [10, 3, 8, 9, 42, 8, "hello"]

print(my_list.pop())
print(*my_list)

#sort() 오름 차순

my_list = [10, 3, 8, 9, 42, 8]
print(my_list)
my_list.sort()

print(*my_list)

#error 뜨는 값
my_list = [10, 3, 8, 9, 42, 8, "hello"]

print(my_list)
my_list.sort()

print(*my_list)

#reserve(): 역순으로 정렬
my_list = [10, 3, 8, 9, 42, 8, "hello"]

print(my_list)
my_list.reserve()

print(*my_list)

my_list = [10, 3, 8, 9, 42, 8, "hello"]
list_tmp = [5, 7, "world"]

print(my_list, list_tmp)

my_list.extend(list_tmp)

print(*my_list)

list_tmp.clear()

print(list_tmp)

my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)

my_list.remove(3)

print(*my_list)

#del list[n]

print(my_list)

del my_list[2]

print(*my_list)

my_tup = (4, 2, 6, 1, "py", "w")

print(my_tup,*my_tup)

# 크기
print(my_tup.__len__())

#인덱스
print(my_tup)
print(my_tup[2])

my_tup[3] = 2
print(*my_tup)

print(my_tup[2] + my_tup[0])

n_add = my_tup[1] + my_tup[3]

print(n_add)

print(my_tup[2:5])
print(my_tup[1:4])
print(my_tup[:3])
print(my_tup[2:])

# 이중튜플
my_tup = (4, 2, 6, 1, "py", "w",("h", 8, 7, 3))
print(my_tup)
print(my_tup[6][0])

# 메소드
my_tup = (4, 2, 6, 1, "py", "w")
print(my_tup.index(2, 0, 3))

print(my_tup.index("py", 3, 5))

#print(my_tup.index(1, 0, 3))

# 딕셔너리
my_dict = {'key1': 'value1', 'key2': 'value2'}

my_item = my_dict.items()

print(my_item)

idx = ("key1","key2","key3")

dicts = dict.fromkeys(idx,"0")

print(dicts)

# 인덱싱
dicData = {"name" : "python", "number" : 23564897 }
print(my_dict["key1"])

my_str = my_dict.get("key2")

print(my_str)

print(my_dict.pop("key1"))

print(my_dict)

#복사
dicts = my_dict.copy()
print(dicts)
print(my_dict)

# 추가/변경
my_dict["key3"] = "value3"
print(my_dict)

my_dict.setdefault("key3")
print(my_dict)

my_dict.update({"key1" : "vs4"})
print(my_dict)

#삭제
del my_dict["key2"]
print(my_dict)

print("key2" in my_dict)
print("key3" in my_dict)

#변환
my_list = list(my_dict.keys())
print(my_list)

my_set = set(my_dict.keys())
print(my_set)

#삭제
my_dict.clear()
print(my_dict)
"""