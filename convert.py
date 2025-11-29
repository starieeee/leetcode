def convertDate(date):
    month_abbrev = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    day = date[:2]
    month = date[2:4]
    year = date[4:]
    
    monthIndex = int(month)
    day = int(day)
    return f'{month_abbrev[monthIndex]} {day}, {year}'
