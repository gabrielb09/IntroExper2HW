data = eval(input("input a list with format '[a,b,c,...]'\n"))
mean = sum(data)/len(data)
count = 1
devsqr = [(data[0]-mean)*(data[0]-mean)]
while count < len(data):
	devsqr = devsqr + [(data[count]-mean)*(data[count]-mean)]
	count += 1
stdv = (float(sum(devsqr))/float((len(data)-1)))**(0.5)
print (stdv)
