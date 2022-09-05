# 贪心算法
## 简介
在问题求解时，总是做出在当前来说最好的选择。需要保证问题具有最优子结构性质，即问题的最优解包含其子问题的最优解
## 常见应用
1. 选择排序算法
   ```py
   def select_sort(data:list):
    n = len(data)
    for i in range(0,n):
        minIdx = i
        for j in range(i+1,n):
            if data[j] < data[minIdx]:
                minIdx = j
        temp = data[i]
        data[i] = data[minIdx]
        data[minIdx] = temp
    return data


   print(select_sort([2,3,1,0,4,5]))
   ```
2. 买股票的最佳时机
