import datetime

d_now = datetime.datetime.now()

print("Corrent date:" , d_now)
num_y = input()
num_d = input()

print("Given years:", num_y)
print("Given days:" , num_d)

t_delta = datetime.timedelta(days =int(num_y) * 365 + int(num_d) )

print("Final date:", d_now + t_delta)
