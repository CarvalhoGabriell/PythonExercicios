
min = 10
seg = 59

print("10:00")
while min > 0:
    min -= 1
    seg = 59
    while seg >= 0:
        print(min,":",str(seg).zfill(2))
        seg -= 1
print("BOOOOOOOOMMMMMMMMMMMMMMM")