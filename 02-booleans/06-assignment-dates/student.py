# write your code here
def is_valid_month(month):
	if month >= 1 and month <= 12:
		return True
	return False


def is_leap_year(year):
	if year % 400 == 0:
		return True
	elif year % 100 == 0:
		return False
	elif year % 4 == 0:
		return True
	return False


def has_30_days(month):
	if is_valid_month(month):
		if month == 4 or month == 6 or month == 9 or month == 11:
			return True
	return False


def has_28_days(month, year):
	if is_leap_year(year):
		return False
	else:
		if month == 2:
			return True
	return False


def has_31_days(month):
	if is_valid_month(month):
		if has_30_days(month) == False:
			if month != 2:
				return True
	return False

def has_29_days(month, year):
	if is_leap_year(year):
		if month == 2:
			return True
	return False


def is_valid_date(day, month, year):
	if is_valid_month(month):
		if has_30_days(month):
			if 1 <= day <= 30:
				return True
		elif has_31_days(month):
			if 1 <= day <= 31:
				return True
		elif has_28_days(month, year):
			if 1 <= day <= 28:
				return True
		elif has_29_days(month, year):
			if 1 <= day <= 29:
				return True
	return False