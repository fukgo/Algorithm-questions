while True:
    s1 = list(input())
    s2 = list(input())
    cnt = 0
    try:

        for i in range(len(s1) - 1):
            if s1[i] == s2[i]:
                continue
            else:
                if s1[i + 1] == 'o':
                    s2[i], s1[i + 1] = s1[i], '*'
                else:
                    s2[i], s1[i + 1] = s1[i], 'o'
                cnt += 1
        print(cnt)
    except:
        break

