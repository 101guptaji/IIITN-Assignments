from collections import Counter
def freqQuery(queries):

    freq = Counter()
    cnt = Counter()
    res = []

    for a,b in queries:
        if a==1:
            cnt[freq[b]]-=1
            freq[b]+=1
            cnt[freq[b]]+=1

        elif a==2:
            if freq[b]>0:
                cnt[freq[b]]-=1
                freq[b]-=1
                cnt[freq[b]]+=1

        else:
            if cnt[b]>0:
                res.append(1)
            else:
                res.append(0)

    return res


q = int(input().strip())

queries = []
for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

ans = freqQuery(queries)
print('\n'.join(map(str,ans)))
