from datetime import datetime


def DateTimeUtils():
    print("Date Time")
    now = datetime.now()

    mm = str(now.month)

    dd = str(now.day)

    yyyy = str(now.year)

    hour = str(now.hour)

    mi = str(now.minute)

    ss = str(now.second)

    ms = str(now.microsecond)

    print (mm)
    print (dd)
    print (yyyy)
    print (hour)
    print (mi)
    print (ss)
    print (ms)


if __name__ == "__main__":    
    DateTimeUtils()


