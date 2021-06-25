regular_hourly_pay = 35
extra_hourly_pay = 45
year  = int(12)


def monthly_pay():
    regular_pay = regular_hours * regular_hourly_pay
    extra_pay = extra_hours * extra_hourly_pay
    final_pay = regular_pay + extra_pay
    yearly_estimate = year * regular_pay
    print('Your pay for the month is', final_pay)
    print('Yearly minimum with regular hours is',yearly_estimate)



regular_hours = float(input('Enter the regular hours of the month \n '))
extra_hours = float(input('Enter the extra hours of the month \n'))

monthly_pay()

