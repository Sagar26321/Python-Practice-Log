def f_to_c(f):
    return 5*(f - 32)/9

f = float(input("Enter temperature in Fahrenheit: "))
c = f_to_c(f)
print(f"{f} Fahrenheit is equal to {c} Celsius.")