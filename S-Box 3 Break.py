#   S-Box 3 Collision finder
#   By Michael Gugino

s3 = [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,13,
      6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
x1b = 111111
x1d = 63
x1f = 13
x2b = 0
x2d = 0
x2f = 0
xl = 0
x3b = 0
x3d = 0
xr = 0
check = 0
matches = []

while check != 64:
    x2d = check
    x2b = "{0:06b}".format(check)
    x2f = s3[int(x2b[1:5],2) + (int(x2b[0] + x2b[5], 2) * 16)]
    xl = x1f ^ x2f
    x3d = x1d ^ x2d
    x3b = "{0:06b}".format(x3d)
    xr = s3[int(x3b[1:5], 2) + (int(x3b[0] + x3b[5], 2) * 16)]
    if xl == xr:
        matches.append(x2b)
    check += 1

print(matches)
