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

def insert_data(position, friend): # 3, '미나', 원하는 곳에 데이터 추가
    katok.append(None)
    klen = len(katok)
    for i in range(klen-1, 3, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

insert_data(3, '미나')
# katok.append(None) # 1단계
#
# katok[6] = katok[5] # 2단계
# katok[5] = None
# katok[5] = katok[4]
# katok[4] = None
# katok[4] = katok[3]
# katok[3] = None
#
# katok[3] = '미나'  # 3단계


# katok.append(None) # 빈칸 추가
# katok[0] = '다현'
#
# katok.append(None) # 빈칸 추가
# katok[1] = '정연'
#
# katok.append(None) # 빈칸 추가
# katok[2] = '쯔위'
#
# katok.append(None) # 빈칸 추가
# katok[3] = '사나'
#
# katok.append(None) # 빈칸 추가
# katok[4] = '지효'
#
#
print(katok)