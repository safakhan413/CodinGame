from datetime import datetime
def calcTime(l):
    print(l)
    first = l[0]
    dateTime = []
    # print(first[:2], first[3:5],first[6:8])
    # x = datetime.timedelta(hours=first[:2], minutes=first[3:5], seconds=first[6:8])
    x = datetime.strptime(first, '%H:%M:%S')
    for i in l:
        dateTime.append(datetime.strptime(i, '%H:%M:%S'))

    print(min(dateTime))
    minDate = str(min(dateTime))
    print(minDate[11:])
    

l = ['10:15:46','03:59:08', '04:00:08', '03:59:09']
calcTime(l)