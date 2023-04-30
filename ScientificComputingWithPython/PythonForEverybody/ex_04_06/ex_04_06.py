print("PY4E - Exercise 4.6")
def computepay(hours, rate):
        if hours > 40:
            hours_above = hours - 40
            pay = (40 * rate) + (hours_above * rate * 1.5)
        else:
            pay = hours * rate
        return pay

try:
    h = float(input("Enter Hours: "))
    r = float(input("Enter Rate: "))
    payment = computepay(h, r)
    print("Pay: ", payment)
except:
    print("Error, please enter numeric input")
