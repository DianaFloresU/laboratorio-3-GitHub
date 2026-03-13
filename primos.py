MAX = 10**7

primo = [True] * (MAX + 1)
primo[0] = primo[1] = False

for i in range(2, int(MAX**0.5) + 1):
    if primo[i]:
        for j in range(i*i, MAX + 1, i):
            primo[j] = False

pref = [0] * (MAX + 1)
contador = 0
for i in range(MAX + 1):
    if primo[i]:
        contador += 1
    pref[i] = contador

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    if a == 0:
        print(pref[b])
    else:
        print(pref[b] - pref[a-1])