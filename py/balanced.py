with open("file.txt") as f:
    for line in f:
        arr = list(map(int, line.strip().split(",")))
        # print(arr)
        i = 0
        l = 0
        r = sum(arr)
        for i, v in enumerate(arr):
            if l == r:
                print([arr[0:i], arr[i:]])
            l += v
            r -= v
