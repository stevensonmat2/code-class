import requests

package = {
    'APPID': "92486e93a8fd35ee17aeb60c1ac229ff",

}
x = True
while x == True:
    question = input("(C)ity name or (Z)ip?: ").lower()

    if question.isalpha():
        package['q'] = question
    else:
        package['zip'] = question


    r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)

    data = r.json()

    tempChoice = input("What unit of temperature? (F)ahrenheit or (C)elsius: ").lower()

    print('\n')

    if tempChoice in ('f', 'fahrenheit'):
        degrees = int(data['main']['temp'] / 3.96)
    else:
        degrees = int(data['main']['temp'] / 12.45)


    cityName = data['name']
    currentWeather = data['weather'][0]
    printWeather = currentWeather['description']
    tUnit = tempChoice.capitalize()

    print('The weather in {} is: {}.'.format(cityName, printWeather))
    print('The temperature is: {}{}'.format(degrees, tUnit))
    print('\n')
    again = input('Search another city? Yes or No: ').lower()
    # print(again)
    if again in ('n', 'no'):
        x = False
