# 한 번의 이동 = 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것
# 같은 값을 가진 두 블록의 충돌 -> 하나로 합쳐짐

# 입력 : 보드의 크기 N(1<=N<=20)
#       둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어짐
#       0 : 빈칸, 이외의 값 : 모두 블록(블록에 쓰여진 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴)

# 출력 : 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력

# 필요 기능 1: 게임판을 상하좌우로 기울이기
# 필요 기능 2: 조합...?



import sys
input = sys.stdin.readline

n = int(input())


def 