

def bank(a,time):
    for each_year in range(time):
        a = (a * 1.1)
    return a

a=float(input("Сколько денег вкладываем? "))

time=int(input("На сколько лет? "))

print(bank(a,time))