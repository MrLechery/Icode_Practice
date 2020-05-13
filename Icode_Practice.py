def ProblemA (x) :
    z = x.split(" ")
    print (int(z[0])+int(z[1]))

def ProblemB (x) :
    sum = 0
    for i in range (1,x+1,+2) :
        sum += i
    print(sum)

def ProblemD (x) :
    z = 1
    for i in range(x-1,-1,-1) :
        print(" "*i,end="")
        print("#"*z,end="")
        print("")
        z = z + 2
    z = z - 2
    for i in range(1,x+2):
        z = z - 2
        print(" "*i,end="")
        print("#"*z,end="")
        print("")

def Problem4 (x) :
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
    print(count)
    print(maximum)     


            
        


    
