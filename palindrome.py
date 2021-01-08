def palindrome1():
	i = input("enter the number to be checked: ")
	check=i.isdigit()
	while not check:
		print("you have entered a string. Please enter a number.")
		i=input("enter the number to be checked: ")
		if i.isdigit():
			break
	if i==i[::-1]:
		return"The entered number is a pallindrome number."
	else:
		return"The entered number is not a pallindrome number."

def palindrome2():
	def run():
		num=int(input("enter the number to be checked: "))
		print(" ")
		original_num=num
		last_digit=0
		reversed_digit=0
		while num>0:
			last_digit=int(num%10)
			reversed_digit=int((reversed_digit*10)+last_digit)
			num=int(num/10)
		if original_num==reversed_digit:
			return "The entered number is a palindrome number."
		else:
			return "The entered number is not a palindrome number."
	try:
		print(run())
	except ValueError:
		print("You have done something wrong.")
		print(" ")
		print("Plese rerun the program and try again. ") 
	finally :
		print(" ")
		print("Thanks for testing our code. ")

print(palindrome1())
print(palindrome2())


