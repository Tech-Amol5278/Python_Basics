# generaete the list ranging 0-100 step 2
# find the midian of list check if it is mathcing with the users given no, if matched brak  the loop
# if not matched sepaate the list into two sl1,sl2
# check both the lists and ignore the list which doesnt have the element
# repeat the same steps from 2





import random

for x in range(1):
  winning_no = random.randint(1,100)

ml = [i for i in range(0,101,2)]
# ml_med = int(len(ml)/2) + 1
# print(ml_med)
# print(ml[int(len(ml)/2)])
# sl1 = ml[0:ml_med -1]
# sl2 = ml[ml_med:len(ml)]
# print(sl1)
# print(sl2)


#################### Sol #########################################
sl = ml
i = 1
while True:
    user_no = int(input("Enter a user number: "))
    sl_med_pos = int(len(sl)/2) + 1
    sl_med_elmnt = sl[int(len(sl)/2)]
    sl1 = ml[0:sl_med_pos -1]
    sl2 = ml[sl_med_pos:len(sl)]

    if user_no == sl_med_elmnt:
        print(f"Congrats, You searched the binary in {i} attempts")
        break
    elif sl_med_elmnt in sl1:
        sl = sl1 
    else :
        sl = sl2 

    i += 1    






