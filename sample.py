
hour = 3
min = 20

hour_angle = (360 / 12)*hour
min_angle = (360 / 60)*min

hour_plus = (30/60)*min

print(hour_angle)
print(min_angle)
print(min_angle-(hour_angle+hour_plus))
