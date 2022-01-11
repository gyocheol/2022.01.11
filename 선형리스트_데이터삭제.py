# 함수 선언부
def add_data(friend):
    katok.append(None)
    klen = len(katok)
    katok[klen-1] = friend

# 전역 변수부
katok = []

# 메인  코드부
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
add_data('모모')
add_data('나연')

def insert_data(position, friend): # 3, '미나', 원하는 곳에 데이터 추가
    katok.append(None)
    klen = len(katok)
    for i in range(klen-1, 3, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

insert_data(3, '미나')

# 데이터 삭제
def delete_data(position):
    katok[position] = None
    klen = len(katok)
    for i in range(position+1, klen, 1):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[klen-1])

delete_data(4)

print(katok)