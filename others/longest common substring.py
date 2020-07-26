MaxLen=0
def LCS(str1,str2):
	global MaxLen
	if len(str1)==0 or len(str2)==0:
		return 0
	if MaxLen[len(str1)-1][len(str2)-1]!=-1:
		pass
	elif str1[-1]==str2[-1]:
		MaxLen[len(str1)-1][len(str2)-1]=LCS(str1[:-1],str2[:-1])+1
	else:
		MaxLen[len(str1)-1][len(str2)-1]=max(LCS(str1,str2[:-1]),LCS(str1[:-1],str2))
	return MaxLen[len(str1)-1][len(str2)-1];

def init(str1,str2):
	global MaxLen
	MaxLen = len(str1)*[[]]
	for i in range(len(str1)):
		MaxLen[i] = len(str2)*[-1]

def track(str1,str2):
	global MaxLen
	l1 = len(str1)-1
	l2 = len(str2)-1
	rtn = ''
	while l1>=0 and l2>=0:
		if MaxLen[l1][l2]==0:
			return rtn
		if str1[l1]==str2[l2]:
			rtn = str1[l1]+rtn
			l1=l1-1
			l2=l2-1
		elif MaxLen[l1][l2]==MaxLen[l1-1][l2]:
			l1=l1-1
		elif MaxLen[l1][l2]==MaxLen[l1][l2-1]:
			l2=l2-1
	return rtn

def Do(str1,str2):
	global MaxLen
	init(str1,str2)
	LCS(str1,str2)
	print "".join(track(str1,str2))

str1='thisisatest'
str2='testing123testing'
Do(str1,str2)


	
