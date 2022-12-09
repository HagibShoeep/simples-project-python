

#for store values row in tower
tower=[]
# for display values row in tower as lines 
def showList(array):
    for list in array:
        s=""
        for k in list:
            s+=" "+str(k)
        print(s,"\n")
        
# insert the number petween tow numbers in row 
def insertToRowList(maxlement,minelments,count):
    row=[]
    while count>0:
        x= int(input())
        if x> maxlement:
            print("number less of or equal ",maxlement)
            continue
        elif x<=minelments:
            print("number larger of ",minelments)
            continue    
        if x  in row:
            print("number is found enter anther number ",minelments)
            continue
        row.append(x)
        count-=1
    row.append(minelments)
    row.sort(reverse = True)
    return     row

print("insert number\n")
total=input()
total=int(total)
curentmax=total
if total>0 and  total<1000000:
    while True:
        num=int(input())
        if num>curentmax or num<1:
               print("insert number less then or equal ",curentmax,"and positive ")
               continue
        elif num==curentmax:
            tower.append([num])
        else:    
            array=insertToRowList(curentmax,num,curentmax-num)
            if len(array)==0:
                continue
            tower.append(array)
        curentmax=num-1
        if curentmax==0:
            break

print("\n\n")
showList(tower)
