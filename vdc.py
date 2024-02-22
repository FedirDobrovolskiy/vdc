import datetime


def vdc(start, end, vacation_days_per_year):
    start_day, start_month, start_year = map(int, start.split('.'))
    end_day, end_month, end_year = map(int, end.split('.'))

    dates_list = [datetime.date(2021, 1, 1), datetime.date(2021, 1, 7), datetime.date(2021, 3, 8),
                  datetime.date(2021, 5, 1), datetime.date(2021, 5, 2), datetime.date(2021, 5, 9),
                  datetime.date(2021, 6, 20), datetime.date(2021, 6, 28), datetime.date(2021, 8, 24),
                  datetime.date(2021, 10, 14), datetime.date(2021, 12, 25), datetime.date(2022, 1, 1),
                  datetime.date(2022, 1, 7), datetime.date(2022, 3, 8)]

    date1 = datetime.date(start_year, start_month, start_day)
    date2 = datetime.date(end_year, end_month, end_day)

    periods = end_year - start_year + 1

    print('start:', date1)
    print('end:', date2)
    print('periods = ', periods)

    def days_between_dates(date1, date2):
        if date2 > date1:
            return (date2 - date1).days + 1
        else:
            return (date1 - date2).days + 1

    def holidays_between_dates(date1, date2):
        def is_between_dates(date, start_date, end_date):
            return start_date <= date <= end_date

        filtered_dates = [date for date in dates_list if is_between_dates(date, date1, date2)]
        return len(filtered_dates)

    if periods == 1:
        a = vacation_days_per_year
        b = days_between_dates(datetime.date(start_year, 1, 1), datetime.date(start_year, 12, 31))
        c = holidays_between_dates(datetime.date(start_year, 1, 1), datetime.date(start_year, 12, 31))
        d = days_between_dates(date1, date2)
        e = holidays_between_dates(date1, date2)
        print(a, b, c, d, e)
        return round(a / (b - c) * (d - e))
    else:
        a = vacation_days_per_year
        b = days_between_dates(datetime.date(start_year, 1, 1), datetime.date(start_year, 12, 31))
        c = holidays_between_dates(datetime.date(start_year, 1, 1), datetime.date(start_year, 12, 31))
        d = days_between_dates(date1, datetime.date(start_year, 12, 31))
        e = holidays_between_dates(date1, datetime.date(start_year, 12, 31))
        print(a, b, c, d, e)

        sp1 = round(a / (b - c) * (d - e))

        a = vacation_days_per_year
        b = days_between_dates(datetime.date(end_year, 1, 1), datetime.date(end_year, 12, 31))
        c = holidays_between_dates(datetime.date(end_year, 1, 1), datetime.date(end_year, 12, 31))
        d = days_between_dates(datetime.date(end_year, 1, 1), date2)
        e = holidays_between_dates(datetime.date(end_year, 1, 1), date2)
        print(a, b, c, d, e)
        sp2 = round(a / (b - c) * (d - e))

        return sp1 + sp2 + vacation_days_per_year * (periods - 2)
