#Problem 1

totalpaid=0
x=1

while (x<13):

	print ('Month:' + str(x))

	minpayment= monthlyPaymentRate * balance
	roundminpay = round (minpayment, 2)
	print ('Minimum monthly payment:' + str(roundminpay))
	
	totalpaid= totalpaid+minpayment
	roundtot = round(totalpaid, 2)

	unpaidbalance= balance-minpayment
	balance= unpaidbalance * (1+annualInterestRate/12)
	roundbal= round(balance, 2)
	print ('Remaining balance:'+  str(roundbal))

	x=x+1

print ('Total paid:' + str(roundtot))
print ('Remaining balance:'+ str(roundbal))

#Problem 2

x=0
y=1
remainder=balance
inibalance=balance


while (remainder>=0):
	balance=inibalance
	y=1
	x=x+10
	while (y<13):
		unpaidbalance= balance-x
		balance= unpaidbalance * (1+annualInterestRate/12)
		y=y+1

	remainder= balance
	
print ('Lowest Payment:'+str(x))

#Problem 3

inibalance=balance
remainder=balance
monthlyrate=annualInterestRate/12
upper=(balance*(1+monthlyrate)**12)/12	

x= balance/12

while(abs(remainder)>0.001):

	if(remainder>0.001):
		lower=x
		balance=inibalance
		x=(upper+x)/2
		y=1

		while(y<13): 
			unpaidbalance=balance-x
			balance= unpaidbalance*(1+annualInterestRate/12)
			y=y+1

		remainder=balance

	elif(remainder<(-0.001)):
		upper=x
		balance=inibalance
		x=(lower+x)/2

		y=1

		while(y<13): 
			unpaidbalance=balance-x
			balance= unpaidbalance*(1+annualInterestRate/12)
			y=y+1

		remainder=balance
		

x=round(x,2)
print ('Lowest Payment:'+str(x))



