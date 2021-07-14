#การใช้ else ใน loop
phone = input('Enter phone number:')
for tel in phone:
    if tel == 7:
        print(tel , 'เลขไม่สวย')
        continue
else:
    print('not found')