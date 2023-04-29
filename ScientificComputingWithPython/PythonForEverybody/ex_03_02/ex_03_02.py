print("PY4E")
try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    if hours > 40:
        hours_above = hours - 40
        pay = (40 * rate) + (hours_above * rate * 1.5)
    else:
        pay = hours * rate
    print("Pay :", pay)
except:
    print("Error, please enter numeric input")