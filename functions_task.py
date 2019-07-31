import datetime

def check_birthdate(year, month, day):
	datetime_object = datetime.datetime.now()
	if int(datetime_object.year) > year:
		return True
	elif int(datetime_object.year) == year and int(datetime_object.month) > month:
		return True
	elif int(datetime_object.year) == year and int(datetime_object.month) == month and int(datetime_object.day) > day :
		return True
	else:
		return False
def calculate_age(year, month, day):
    datetime_object = datetime.datetime.now()
    Ayear = int(datetime_object.year) - year
    if int(datetime_object.month) < month:
        Ayear -=1
        Amonth = int(datetime_object.month) - month
        if Amonth < 0:
            Amonth = Amonth + 12
        Aday= datetime_object.day - day
    elif int(datetime_object.month) == month:
        if int(datetime_object.day) < day:
            Ayear -= 1
            Amonth = 0
            Aday = day - int(datetime_object.day)
        else:
        	Amonth = 0
        	Aday= datetime_object.day - day
    else:
        Amonth = int(datetime_object.month) - month
        Aday= datetime_object.day - day

    print("You are {} years, {} months, and {} days".format(Ayear, Amonth, Aday))

birthyear = int(input("Enter year of birth: "))
birthmonth = int(input("Enter month of birth: "))
birthday = int(input("Enter day of birth: "))

if check_birthdate(birthyear, birthmonth, birthday) == True:
	if birthmonth <= 12 and birthday <=31:
		calculate_age(birthyear, birthmonth, birthday)
	else:
		print("Invalid birthdate input.")
else:
	print("Invalid birthdate input.")


