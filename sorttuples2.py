sample=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
length=len(sample)
for i in range(length):
    for j in range(i+1,length):
        if sample[i][1]>sample[j][1]:
            temp=sample[i]
            sample[i]=sample[j]
            sample[j]=temp
print("The sorted list :")
print(sample)