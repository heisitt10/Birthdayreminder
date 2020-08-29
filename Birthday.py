import datetime


def print_header():

	print("---------------------------------")
	print("         Birthday Reminder")
	print("---------------------------------")
	print()


def get_birthday_from_user():
	print(" When You Were Born ??")
	year = int(input("year [YYYY]: "))
	month = int(input("Month [MM]: "))
	day = int(input("Day [DD]: "))

	birthday = datetime.date(year, month, day)

	return birthday 


def days_inbetween(original_date, target_date):
	this_year = datetime.date(target_date.year, original_date.month, original_date.day)

	dt = this_year - target_date

	return dt.days


def birth_info(days):

	if days < 0:
		print("you Had your BirthDay {}  days ago This Year".format(-days))
	elif days > 0:
		print("your BirthDay is in {}  days!!".format(days))

	else:
		print("Happy BirthDay!!!")


if __name__=="__main__":
	print_header()
	bday = get_birthday_from_user()
	today = datetime.date.today()
	number_of_days = days_inbetween(bday, today)
	birth_info(number_of_days)


		
