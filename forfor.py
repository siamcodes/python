#การวนลูปซ้อนกัน for ซ้อน for
#ให้แสดงตัวเลข 1- 100 เป็นแถวและคอลัมน์ (10 แถว 10 คอลัมน์)
x = y = 0
print("-------------------------------------")
for row in range(1,11):
    print(' ', end='')
    print('|', end=' ')
    for column in range(1,11):
        y=x+column
        print(end='')
        if y < 10 :
            print(end= ' ')
        print(y, end=' ')
    x = y
    if y == 100:
        print('|')
    else:
        print('|')

print("--------------------------------------")              

