def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    name_of_week_days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

    if type(day_of_week) is int and 1 <= day_of_week <= 7:
        # print(day_of_week)
        # print(name_of_week_days[day_of_week - 1])
        return name_of_week_days[day_of_week - 1]
    else:
        # print('Enter the day as an integer between 1(Sunday) and 7(Saturday)')
        return None
    
# Some More Tests
# print(weekday_name(3.5))
# print(weekday_name('hi'))
# print(weekday_name(4))