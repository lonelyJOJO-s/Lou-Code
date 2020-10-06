# 基础解法 时间复杂度（m * n）
Min = -10000


def getmax(window_size, array):
    answer = []
    for i in range(len(array) - window_size + 1):
        Max = Min
        for j in range(window_size):
            if int(array[j + i]) > Max:
                Max = array[j + i]
        answer.append(Max)
    return answer


input = [4, 3, 5, 4, 3, 3, 6, 7]
print(getmax(3, input))
