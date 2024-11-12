heroes = {
    'Dürrenmatt': '05.01.1921',
    'Lincoln' : '12.02.1809',
    'Pavlov' : '26.09.1849',
    'Dali' : '11.05.1904',
    'Rostand' : '01.04.1868',
    'Chebyshov' : '04.05.1821',
    'Euler' : '15.04.1707',
    'Monteverdi' : '09.05.1567',
    'Casanova' : '02.04.1725',
    'Priestley' : '13.09.1894'
}

days = {
    '01' : 'first',
    '02' : 'second',
    '03' : 'third',
    '04' : 'fourth',
    '05' : 'fifth',
    '06' : 'sixth',
    '07' : 'seventh',
    '08' : 'eighth',
    '09' : 'nineth',
    '10' : 'tenth',
    '11' : 'eleventh',
    '12' : 'twelfth',
    '13' : 'thirteenth',
    '14' : 'fourteenth',
    '15' : 'fifteenth',
    '16' : 'sixteenth',
    '17' : 'seventeenth',
    '18' : 'eighteenth',
    '19' : 'nineteenth',
    '20' : 'twentieth',
    '21' : 'twenty first',
    '22' : 'twenty second',
    '23' : 'twenty third',
    '24' : 'twenty fourth',
    '25' : 'twenty fifth',
    '26' : 'twenty sixth',
    '27' : 'twenty seventh',
    '28' : 'twenty eighth',
    '29' : 'twenty nineth',
    '30' : 'thirtieth',
    '31' : 'thirty first'
}

months = {
    '01' : 'January',
    '02' : 'February',
    '03' : 'March',
    '04' : 'April',
    '05' : 'May',
    '06' : 'June',
    '07' : 'July',
    '08' : 'August',
    '09' : 'September',
    '10' : 'October',
    '11' : 'November',
    '12' : 'December',
}

heroes_keys = list(heroes.keys())
game = 'y'

while game == 'y':
    print('(If you decide to exit the game print "N" any time)')
    import random
    chosen_keys = random.sample(heroes_keys,5)
    n=1    

    right_answeres = 0
    for key in chosen_keys:
        answer = input(f"{n}. Print the {key}'s birthdate in 'dd.mm.yyyy' format: ")
        if answer == 'N':
            break
        elif answer == heroes[key]:
            print('You are right!')
            right_answeres += 1
        else:
            date = heroes[key]
            list_date = date.split('.')
            day = days[list_date[0]]
            month = months[list_date[1]]
            year = list_date[2]
            print(f'No, you are wrong. It is the {day} of {month} in the year of {year}.')
        n += 1

    wrong_answeres = 5 - right_answeres

    print(f'\nRight answeres count is {right_answeres}')
    print(f'Wrong answeres count is {wrong_answeres}')
    game = input('Do you want to play again? Print Y or N.  ')
    game = game.lower()