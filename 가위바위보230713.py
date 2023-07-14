# user = input() # 입력


#조건문을 사용해서
#누가 이겼는지 판별하 ㄴ후에
# 승자를 출력
# 게임의 결과도 출력
# 내가 가위를 내고 컴퓨터가 바위를 내서 패배하였습니다.


i = input()
a = ["가위","바위","보"]
import random
rcp = random.choice(a)

if i == rcp:
    print(f"내가{i}를 내고 컴퓨터가{rcp}를 내서 비겼습니다.")
elif i == "가위" and rcp =="보":
    print(f"내가{i}를 내고 컴퓨터가{rcp}를 내서 이겼습니다.")
elif i == "바위" and rcp =="가위":
    print(f"내가{i}를 내고 컴퓨터가{rcp}를 내서 이겼습니다.")
elif i == "보" and rcp =="바위":
    print(f"내가{i}를 내고 컴퓨터가{rcp}를 내서 이겼습니다.")
elif i == "가위" and rcp =="바위":
    print(f"내가{i}를 내고 컴퓨터가{rcp}를 내서 졌습니다.")
elif i == "바위" and rcp =="보":
    print(f"내가{i}를 내고 컴퓨터가{rcp}를 내서 졌습니다.")
elif i == "보" and rcp =="가위":
    print(f"내가{i}를 내고 컴퓨터가{rcp}를 내서 졌습니다.")
