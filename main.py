def hcf(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a==b:
        return a
    if a>b:
        return hcf(a-b,b)
    return hcf(a,b-a)
a=180
b=120
if hcf(a,b):
    print(hcf(a,b))
