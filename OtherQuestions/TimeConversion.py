def timeConversion(s):
    if s[8:] == 'PM':
        hr = int(s[0:2])+12
        if hr == 24:
            hr = 12
        return str(hr).zfill(2) + s[2:-2]
    else:
        if int(s[0:2]) == 12:
            return '00' + s[2:-2]
        else:
            return s[:-2]


print timeConversion('12:00:45PM')
print timeConversion('12:40:00AM')
print timeConversion('10:13:45PM')
print timeConversion('11:45:45AM')