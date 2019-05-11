# This function returns century code.
def cent_code(yr):
    val = [0,6,4,2]
    yr = yr // 100
    return val[(abs(yr-19))%4]

# This function returns number of leap year upto the inserted year of that century.
def num_of_leap(yr):
    yr = (yr % 100)-1
    return (yr // 4)

# This function check wheather a year is leap year or not.
def leap_year(yr):
    if yr % 400 == 0:
        return True
    elif yr % 100 != 0 and yr % 4 == 0:
        return True
    else : return False

# This function calculates the weekday.
def day_find(date):
    date = date.split('/')
    dt = []
    for i in date:
        dt.append(int(i))
        
    if dt[0] > 31 or dt[1] > 12 or (dt[0] > 30 and (dt[1] == 4 or dt[1] == 6 or dt[1] == 9 or dt[1] == 11)) or (dt[1] == 2 and dt[0] > 29):
        return "Not possible"
    
    days = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
    month_code = [0,1,4,4,0,2,5,0,3,6,1,4,6]
    sm = dt[0] + month_code[dt[1]] + (dt[2]%100) + cent_code(dt[2]) + num_of_leap(dt[2])
    if leap_year(dt[2]):
        if dt[1] > 2 :
            sm += 1
    else :
        if dt[1] == 2 and dt[0] > 28:
            return "Not possible"
    return days[(sm % 7)]

# Main program

s = input("Insert the date (format : dd/mm/yyyy) :---->  ")
print("The week-day is : ",day_find(s))
s = input("......Thank You for using.......")
