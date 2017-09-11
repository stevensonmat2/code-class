cities = {
  'Boston': ['New York', 'Albany', 'Portland'],
  'New York': ['Boston', 'Albany', 'Philadelphia'],
  'Albany': ['Boston', 'New York', 'Portland'],
  'Portland': ['Boston', 'Albany'],
  'Philadelphia': ['New York']}

accessibleCities = []
secondHop = []
visitedCities = []
unvisitedCities = []
currentCity = 'n'

x = True

while x == True:




    destination = input("where to? ").title()
    # accessibleCities = (cities[destination])
    # visitedCities.append([destination])

    if destination in visitedCities:
        print("you've already been there!")
        print(currentCity)

    else:
        currentCity = destination
        print('you are in {}'.format(currentCity))
        accessibleCities = cities[currentCity]
        # print(accessibleCities)
        for city in accessibleCities:
            print('you can go to {} in one hop.'.format(city))
            for c in cities[city]:

                if c != destination:

                    secondHop.append(c)
            # secondHop.remove(destination)
        # print(secondHop)
        # print(accessibleCities)
        secondHop = set(secondHop)
        for city in secondHop:
            if city not in cities[currentCity]:
                print('And to {} in two hops.' .format(city))

    again = input('Search another city? Yes or No: ').lower()
    if again in ('n', 'no'):
        x = False

    currentCity = destination
    visitedCities.append([destination])
