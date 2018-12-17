# Returns time information for contemporary or elecronic music composition.

sec_total = 0
hour = 0
minutes = 0
seconds = 0
pulses = 0
note_value = 4
tempo = 0
convert_tosec = 0
measure = 0

noquit = 1
checkquitvalues = 1


def main():

    quit = 1
    while quit:
        hour_str = input('hour (integer): ')
        try:
            if int(hour_str) >= 0:
                hour = int(hour_str)
                quit = 0
        except Exception as e:
            print(e, 'try again')

    quit = 1
    while quit:
        minutes_str = input ('minutes (integer): ')
        try:
            if int(minutes_str) >= 0:
                minutes = int(minutes_str)
                quit = 0
        except Exception as e:
            print(e, ', try again')

    quit = 1
    while quit:
        seconds_str = input ('seconds (integer): ')
        try:
            if int(seconds_str) >= 0:
                seconds = int(seconds_str)
                quit = 0
        except Exception as e:
            print(e, ', try again')

    quit = 1
    while quit:
        tempo_str = input ('tempo or bpm: ')
        try:
            if int(tempo_str) >= 1:
                tempo = int(tempo_str)
                quit = 0
        except Exception as e:
            print(e, ', try again')

    quit = 1
    while quit:
        pulses_str = input ('pulses or beats (for electronic, 1): ')
        try:
            if int(pulses_str) >= 1:
                pulses = int(pulses_str)
                quit = 0
        except Exception as e:
            print(e, ', try again')



    sec_total = hour * 60 ** 2 + minutes * 60 + seconds
    min_total = hour * 60 + minutes + seconds * 10 ** -1

    measure = sec_total / pulses

    print('total seconds: ', sec_total)
    print('measures:  {}, with {}, beats per measure'.format(measure, pulses))

    #fibonacci for the important beats:
    x = 0
    y =1
    z = 0
    sum = 0
    while y < sec_total:
        z = x + y
        x = y
        y = z
        sum += z
        if z > measure:
            measuref = (sum / pulses)
            print('measure: ', measuref)
        print(z)







while checkquitvalues:

    main()

    quit = 1
    while quit:
        noquit_str = input('Continue? 1 for yes, 0 for no: ')
        try:
            if int(noquit_str) == 1 or int(noquit_str) == 0:
                noquit =int(noquit_str)
                quit = 0
        except Exception as e:
            print(e, ', try again')

    if noquit == 0:
        checkquitvalues = 0
