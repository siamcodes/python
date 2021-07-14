#break หลุดและออกจากวนรอบทันที โดยไม้ต้อกระทำคำสั่งที่เหลือ
num,sum = 1,0
while num < 10 :
    sum += num
    if num > 8 :
        break
    print('ค่าของ sum', num ,'=', sum )
    num +=1
print("จบการทำงาน")

