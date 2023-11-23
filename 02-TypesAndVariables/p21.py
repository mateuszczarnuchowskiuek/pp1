#height in cm
height = 170

#total height in inches
inches = height / 2.54

feet = inches // 12

inch = round(inches % 12)

print(f"I am {height}cm tall, i.e. {feet} feet and {inch} inches.")

