#count rabbits
def cr(n,k):
	#print n,k
	if n<=0:
		print '**************'
		return 0
	elif n==1 or n==2:
		return 1
	elif n<k+1:
		return ((cr(n-1,k)+cr(n-2,k)))
	elif n==k+1 or n==k+2:
		return (cr(n-1,k)+cr(n-2,k))- 1		
	elif n>k+2:
		return cr(n-1,k)+cr(n-2,k)-cr((n-(k+1)),k)		

print "counting rabbits"
n=15
k=4
print 'k=',k,': '
for i in range (1,n+1):
	print i,cr(i,k)


