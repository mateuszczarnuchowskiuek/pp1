#8. The speed limit on a motorway in Poland is 140 km/h. Write a program that checks whether a car exceeded the speed limit. If so, a warning is displayed. Sample result:
#speed_limit = 140
#car_speed = int( input('Enter car speed km/h: ') )
#
#if car_speed > speed_limit:
#    print('Warning: speed limit exceeded!!')

maxSpeed = 140
carSpeed = int( input('Enter car speed km/h: ') )

if carSpeed > maxSpeed:
    print('Speed limit exceeded!')