#Pascal Triangle
n = int(input("Give size of Pascal Triangle: "))
lstData = []

for i in range(n):
    if i == 0:
        arrData = [1]
        lstData.append(arrData)
    else:
        arrTemp = lstData[i-1]
        print(arrTemp)
        arrData = []
        for j in range(i+1):
            if j == 0:
                arrData.append(arrTemp[j])
                print(arrData)
            elif j == i:
                arrData.append(arrTemp[j-1])
            else:
                arrData.append(arrTemp[j-1]+arrTemp[j])
        
        lstData.append(arrData)
print(lstData)
