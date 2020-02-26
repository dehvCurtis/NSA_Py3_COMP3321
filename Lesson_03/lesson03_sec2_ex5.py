import datetime

now = datetime.datetime.now()

print(now)

if now.hour in range(1,12):
    print('Morning Time')
elif now.hour in range(10,17):
    print('Afternoon time')
elif now.hour in range(17,24):
    print('Evening time')
