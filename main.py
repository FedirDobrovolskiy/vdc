import datetime

from vdc import vdc


# while True:
#     print('################################################################################')
#     print('dd.mm.yyyy')
#     start = input('Enter start date: ')
#     end = input('Enter end date: ')
#     vacation_days_per_year = input('Enter vacation days per year: ')
#
#     print(vdc(start, end, vacation_days_per_year))

start = '01.01.2021'
end = '30.06.2021'
vacation_days_per_year = 24

print(vdc(start, end, vacation_days_per_year))
