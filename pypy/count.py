def counting_sort_asc(A,B,K):
    # A : 정렬 대상
    # B : 정렬 결과
    # K : 정렬 대상 중 최댓값
    C = [0] * (K+1)
    # C : 카운트 배열(원소의 개수를 세주고, 자리를 정해준다.)
    # C[i] = i의 등장 횟수
    # C[1] => A 안에 1이 몇개 있는지??


    # 1. 각 원소의 등장 횟수를 세준다.
    for i in range(len(A)):
        # A[i]의 등장 횟수를 하나씩 증가 시켜 주면 된다.
        C[A[i]] += 1

    # 2. 각 원소의 등장횟수를 계산해서 각 원소가 들어갈 자리의 위치를 구해 준다.
    for i in range(1, len(C)):
        # i는 i보다 작은수가 몇 개 있는지를 알면 그 뒤부터 나온다는 것을 알기 때문에
        C[i] += C[i-1]

    # 뒤에서부터 A를 확인하면서 자리를 채워준다.
    # 뒤에서부터 확인하는 이유는 안전 정렬(원래 배열의 순서를 보장)
    # 자리를 채워 줄때마다 1씩 감소시켜줘야 한다.(자리 중복을 피하기 위해)

    for i in range(len(B) - 1, -1, -1):
        # C[A[i]] => A[i]가 들어갈 자리를 가르키고 있다.(들어가기 전에 1 빼고)
        C[A[i]] -= 1
        # 자리에 A[i}를 넣어주면 된다.

        B[C[A[i]]] = A[i]

    nums = [0, 4, 1, 3, 1, 2, 4, 1]

    result_asc = []*8
    counting_sort_asc(nums, result_asc, max(nums))

    print(result_asc)
#
#
# def counting_sort_asc(A,B,K):
#     # A : 정렬 대상
#     # B : 정렬 결과
#     # K : 정렬 대상 중 최댓값
#     C = [0] * (K+1)
#     # C : 카운트 배열(원소의 개수를 세주고, 자리를 정해준다.)
#     # C[i] = i의 등장 횟수
#     # C[1] => A 안에 1이 몇개 있는지??
#
#
#     # 1. 각 원소의 등장 횟수를 세준다.
#     for i in range(len(A)):
#         # A[i]의 등장 횟수를 하나씩 증가 시켜 주면 된다.
#         C[A[i]]["num"] += 1
#
#     # 2. 각 원소의 등장횟수를 계산해서 각 원소가 들어갈 자리의 위치를 구해 준다.
#     for i in range(1, len(C)):
#         # i는 i보다 작은수가 몇 개 있는지를 알면 그 뒤부터 나온다는 것을 알기 때문에
#         C[i] += C[i-1]
#
#     # 뒤에서부터 A를 확인하면서 자리를 채워준다.
#     # 뒤에서부터 확인하는 이유는 안전 정렬(원래 배열의 순서를 보장)
#     # 자리를 채워 줄때마다 1씩 감소시켜줘야 한다.(자리 중복을 피하기 위해)
#
#     for i in range(len(B) - 1, -1, -1):
#         # C[A[i]] => A[i]가 들어갈 자리를 가르키고 있다.(들어가기 전에 1 빼고)
#         C[A[i]["num"]] -= 1
#         # 자리에 A[i}를 넣어주면 된다.
#
#         B[C[A[i]["num"]]] = A[i]
#
#     nums_dict = [
#         {"name": "김", "num": 3},
#         {"name": "tmd", "num": 2},
#         {"name": "d", "num": 53},
#         {"name": "3", "num": 41},
#         {"name": "4", "num": 44},
#         {"name": "5", "num": 55},
#         {"name": "8", "num": 1},
#     ]
#
#     result_asc = []*8
#     counting_sort_asc(nums_dict, result_asc, max(nums_dict))
#
#     print(result_asc)
#