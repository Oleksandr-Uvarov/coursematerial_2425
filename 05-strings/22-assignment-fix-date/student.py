# write your code here
def fix_date(date):
    strings = date.split("/")

    fixed_date = f"{strings[2]}/{strings[0]}/{strings[1]}"
    return fixed_date

print(fix_date("2042/55/12"))