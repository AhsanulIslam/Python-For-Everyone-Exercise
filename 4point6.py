def computepay(h,r):
    h = float(h)
    r = float(r)
    if h>40:
        p = 40*r + ((h-40)*1.5*r)
    return p
    

hrs = input("Enter Hours:")
rate = input("Enter rate per hour:")
p = computepay(hrs,rate)
print("Pay",p)
