mi_km =  1.60934
mi_ft = 5280
mi_m = 1609.34
km_mi = 0.621371
km_ft = 3280.84
km_m = 1000
m_km = 0.001
m_mi = 0.000621371
m_ft = 3.28084
ft_mi = 0.000189394
ft_km = 0.0003048
ft_m = 0.3048

playing = True

while playing:
    distance = input("Distance:")

    unit = input("Unit of Measure:")

    query = input("Convert To:")
    if query == 'mi' and unit == 'km':
        print(float(distance) * km_mi)
    if query == 'mi' and unit == 'ft':
        print(float(distance) * ft_mi)
    if query == 'mi' and unit == 'm':
        print(float(distance) * m_mi)
    if query == 'km' and unit == 'mi':
        print(float(distance) * mi_km)
    if query == 'km' and unit == 'ft':
        print(float(distance) * ft_km)
    if query == 'km' and unit == 'm':
        print(float(distance) * m_km)
    if query == 'm' and unit == 'mi':
        print(float(distance) * mi_m)
    if query == 'm' and unit == 'km':
        print(float(distance) * km_m)
    if query == 'm' and unit == 'ft':
        print(float(distance) * ft_m)
    if query == 'ft' and unit == 'mi':
        print(float(distance) * mi_ft)
    if query == 'ft' and unit == 'km':
        print(float(distance) * km_ft)
    if query == 'ft' and unit == 'm':
        print(float(distance) * m_ft)
    else:
        query = input('Unit not recognized, try again? Type Yes or No')
        if query == 'No':
            print('Goodbye')
            break
        if query == 'no':
            print('Goodbye')
            break
        if query == 'Yes':
            continue
        if query == 'yes':
            continue

        # query = input('Try another?')
        # if query == 'No':
        #     print('Goodbye')
        #     break
        # if query == 'no':
        #     print('Goodbye')
        #      break
        # if query == 'Yes':
        #     continue
        # if query == 'yes':
        #     continue
