i = int(input('Nomer mesiaca: '))
def month_to_season(i):
    season = {12:'Winter', 1:'Winter', 2:'Winter', 3:'Spring', 4:'Spring' ,5:'Spring',
     6:'Summer', 7:'Summer', 8:'Summer', 9: 'autumn', 10: 'autumn', 11: 'autumn'}
    i = season.get(i)
    return i


print(month_to_season(i))
print(i)