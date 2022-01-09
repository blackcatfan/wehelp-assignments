#task1
def calculate(min, max):
    sum=0
    for i in range (min,max+1):
        sum=sum+i
    print(sum)

calculate(1,3)
calculate(4,8)

# task2 要求二：Python 字典與列表、JavaScript 物件與陣列
#完成以下函式，正確計算出員工的平均薪資，請考慮員工數量會變動的情況。
#提醒：請勿更動題目中任何已經寫好的程式。

def avg(data):
# 請用你的程式補完這個函式的區塊
    data={"counts":3, "employees":[{"name":"John","salary":30000},{"name":"Bob","salary":60000},{"name":"Jenny","salary":50000}]}
    W2=data["employees"]
    W3=data["counts"]
    g=0
    for i in range(W3):
        g+=W2[i]["salary"]
    print(g/W3)

avg({
"count":3,
"employees":[
                {
                "name":"John",
                "salary":30000
                },
             
                {
                "name":"Bob",
                "salary":60000
                },
                
                {
                "name":"Jenny",
                "salary":50000
                }
                
                ]
}) # 呼叫 avg 函式

#task3 -修正

def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    maxnum=nums[0]*nums[1]

    if len(nums)==2:
        product=nums[0]*nums[1]
        print(product)
    else:
        for i in list(nums):
            for j in list (nums):
                if i !=j:
                    product=i*j
                    maxnum=max(product,maxnum)
        print(maxnum)
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0

#task 4 陣列和演算 作業實練

def twoSum(nums, target):
    k=len(nums)
    for i in range (0,k-1):
        for j in range(i+1,k):
            if nums[i]+nums[j] == target:
                return([i,j])

result=twoSum([2, 11, 7, 15], 9)
print(result)

#task 5 給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大長度。
def maxZeros(nums):
# 請用你的程式補完這個函式的區塊
    NumZero=0
    c_count=0
    max_count=0
    for i in list(nums):
        if i == NumZero:
            c_count=c_count+1
            max_count=max(c_count,max_count)
     
        else:
            i !=NumZero
            c_count=0

    print(max_count)

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3