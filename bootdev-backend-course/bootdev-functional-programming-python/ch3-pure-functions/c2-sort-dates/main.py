# code before changes:

# def sort_dates(dates):
#     dates.sort()
#     return dates

# actual code:

# "MONTH-DAY-YEAR"
# we have to somehow compare years at least
# .sort() by itself sort only by months?

# so to do a proper work we have to sort 1) years 2) months 3) days

# create a variables?

# how to take only years?
# make a dictionary of each block in date?

def sort_dates(dates):
    split_dates = list(map(lambda date: date.split("-"), dates))
    sorted_list = sorted(split_dates, key=lambda parts: (int(parts[2]), int(parts[0]), int(parts[1])))
    sorted_dates = list(map(lambda date: "-".join(date), sorted_list))
    return sorted_dates

# it was really hard and solution quite simpler:

# def sort_dates(dates):
#     return sorted(dates, key=format_date)


# def format_date(date):
#     month, day, year = date.split("-")
#     return year + month + day
