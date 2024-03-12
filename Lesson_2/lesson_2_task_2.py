def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
    
if is_year_leap(2004):
    print(2004, "True")
else:
    print(2021, "False")
        
is_year_leap(2004)

is_year_leap(2021)
             