# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

### 문제
# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
#
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
#
# ### 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
#
# 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
#
# ### 출력
# 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

# ### 해결책
# K를 동전의 가치 Ai로 나눈 몫을 동전개수값에 더하고
# 나머지를 K로 다시 설정하고 for문을 연산하면 된다.
#
# K = 5600원 Ai = 1000원
# 몫 : 5 , 나머지 : 600
# 600원 100원
# 몫 : 6  나머지 :0 -> break!

N,K = map(int, input().split())
coin_val = []
for i in range(N):
    coin_val.append(int(input()))

res = 0
coin_val.sort(reverse=True)
for idx in range(N):
    res += (K//coin_val[idx])
    K %=coin_val[idx]
    if K <=0:
        break
print(res)

