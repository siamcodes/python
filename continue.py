#continue เป็นการข้ามคำสั่ง โดยไม่ทำคำสั่งที่เหลือในลูปปัจจุบัน แล้วกลับไปเริ่มต้นทำงานกับคำสั่งในรอบถัดไป
phone = input('Enter Telepone: ')
for tel in phone:
    if tel == '4':
        break
    print(tel , end= ' ')
