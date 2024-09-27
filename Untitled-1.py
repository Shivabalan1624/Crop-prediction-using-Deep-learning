def countingValleys(steps,path):
    sea_level = 0
    valleys = 0
    for step in path:
    if step == 'U':
        sea_level +=1
    else:
        sea_level -=1
        
        if step =='U' and sea_level ==0:
            valleys +=1
            return valleys
        
    steps = int(input("enter the number of stes :"))
    path = input("enter the path taken :")
    result=countingValleys(steps ,path)
    print(result)