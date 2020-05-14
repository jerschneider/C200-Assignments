nq = 2
nd = 2
nn = 2

total = nq*.25 + nd*.10 + nn*.05
cost = 1.75

if total >= cost:
    print("soda dispensed with $", total-cost, "returned.")
else:
    print("Need $", cost - total, "more change.")
