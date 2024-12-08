# class selectionsort():
#     n = 0

#     def sort(self,list):
#         if list[max] == nval:
#             print(list)
#         else: 
#             for i in range(0,len(list)-1):
#                 if nval < list[i]



list = [12,2,43,6,236,324,5,4,7,9]
nval = list[0]
nlist = []
for i in range(0,len(list)-1):
    if nval > list[i+1]:
        nlist.append(nval)
        nval = list[i]

print(nlist)