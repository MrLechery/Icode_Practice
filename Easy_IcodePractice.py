def problem1(x1,x2) :
    time = []
    for i in x1.split(":") :
        time.append(int(i))
    for i in x2.split(":") :
        time.append(int(i))
    print(time[2]-time[0])
    
def problem2 (word_list) : #Clear
    new_word = word_list.split() #แยกออกจากกัน

    for i in range (len(new_word),0,-1) :
        print(new_word[i-1],end=" ")# print(new_word[::-1])

def problem3 (word) :
    z = word[::-1]
    print("true") if z == word else print("False")

def problem4 (x) :
    count = []
    maximum = 0
    for i in x.upper() :
        if i not in count :
            count.append(i)
            count.append(1)
        if i in count :
            k = count.index(i)
            count[k+1] = count[k+1]+1
    for i in count :
        if type(i) == int :
            if (i) > maximum :
                maximum = i
              
 def problem6(x1,x2) :
    time = []
    for i in x1.split(":"):
        time.append(int(i))
    for i in x2.split(":"):
        time.append(int(i))
    time[1] += time[3]
    time[3] -= time[3]
    time[0] += time[2]
    time[2] -= time[2]
    if time[1] >= 60 :
        time[1] -= 60
        time[0] += 1
    print(str(time[0]).zfill(2),":",str(time[1]).zfill(2))

    print(count)
    print(maximum)
    
def problem7 (x):
    num = []
    sum = 0
    tar = False

    num = list(map(int, str(x)))
    for i in num :
        sum += i
    num = list(map(int,str(sum)))
    sum = 0
    for i in num :
        sum += i
    if sum == 4 :
         print(9-sum,end="")
         print(x)
    else :
        print(x)
 
def problem8 (x1,x2) #NotFinish :
    sum = 0
    for i in range (x1,x2+1) :
        if 100 // i == 0 :
            sum += 365
        elif 400 // i == 0 :
            sum += 366
        else :
            sum += 365
        print(sum)
        
