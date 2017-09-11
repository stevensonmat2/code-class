# breakfast

# input = ('When are you eating?: ')
# if input == >= 7 and <= 9:
#     print('you should eat breakfast')

# Breakfast: 7AM - 9AM
# Lunch: 12PM - 2PM
# Dinner: 7PM - 9PM
# Hammer: 10PM - 4AM

# time
current_time = input('what time is it?: ')

meridian = current_time[-2:]
time = int(current_time[:-2])

if meridian.lower() == 'am':
    if 7 <= time <=9:
        print('eat breakfast'.format(current_time))
    elif time == 12 or time >= 1 and time <= 4:
        print('hammer time')
    else:
        print('wrong')
elif meridian.lower() == 'pm':
    if time == 12 or time == 1 or time ==2:
        print('eat lunch'.format(current_time))
    elif time >= 7 and time <= 9:
        print('dinner')
    elif time >= 10 and time <= 11:
        print('hammer')
    else:
        print('wrong')
else:
    print('This doesn\'t work')


# if time >= 7 and time <= 9:
#     print('You should eat Breakfast')
# elif time >= 12 and time <= 2:
#     print('You should eat Lunch')
# elif time >= 7 and time <= 9:
#     print('You should eat Dinner')
# elif time >= 10 and time <= 4:
#     print('Hammer Time')
