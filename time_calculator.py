def add_time(start, duration, weekday=''):

    startHour = int(start.split()[0].split(':')[0])
    startMinutes = start.split()[0].split(':')[1]
    am_pm = start.split()[1].upper()

    durationHour = duration.split(':')[0]
    durationMinutes = duration.split(':')[1]

    if(am_pm == 'AM' and int(startHour) == 12):
        startHour = str(0)

    if(am_pm == 'PM'):
        newHours = 12
    else:
        newHours = 0

    newMinutes = int(startMinutes)+int(durationMinutes)
    newHours += int(startHour)+int(durationHour) + int(newMinutes/60)
    days = int(newHours/24)

    newMinutes %= 60
    newHours %= 24

    if(newHours > 12):
        newHours -= 12
        am_pm = 'PM'
    elif(newHours == 0):
        newHours = 12
        am_pm = 'AM'
    elif(newHours == 12):
        am_pm = 'PM'
    else:
        am_pm = 'AM'

    new_time = str(newHours)+':'+f"{newMinutes:0>2}"+' '+am_pm

    if(not weekday == ''):
        weekdays = ['Sunday', 'Monday', 'Tuesday',
                    'Wednesday', 'Thursday', 'Friday', 'Saturday']
        weekdaynumber = weekdays.index(weekday.capitalize())+days
        weekdaynumber %= 7
        new_time += ', '+str(weekdays[weekdaynumber])

    if(days > 0):
        if days == 1:
            new_time += ' (next day)'
        elif days > 1:
            new_time += ' ('+str(days)+' days later)'

    return new_time
