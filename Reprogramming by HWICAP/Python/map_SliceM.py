
a=list(range(0,64))
for n in range(0,4):
	for m in range(0,4):
		a[16*n+2*m]    =  31-4*n-m
		a[16*n+1+2*m]  =  15-4*n-m
		a[16*n+8+2*m]  =  63-4*n-m
		a[16*n+9+2*m]  =  47-4*n-m

# print(a)



# x='0000000100100011010001010110011110001001101010111100110111101111' # 0123_4567_89AB_CDEF 通过测试
x='0110100110010110100101100110100110010110011010010110100110010110' # 6996966996696996 通过测试
y=list(range(0,64))


for i in range(0,64):
	if  x[63-i] == '1' :
		y[63-a[i]] = 1
	else :
		y[63-a[i]] = 0

print (y)