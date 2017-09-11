rain_chart = open('park_se_yard.rain', "r", encoding="utf8")
from operator import itemgetter

just_data = []
just_date = []

read_chart = rain_chart.readlines()

rain_chart.close()

for line in read_chart[11:]:
    just_data.append(line.split())

for line in just_data:
    just_date.append(line[0:2])

real_data = [i for i in just_date if i[1] != '-']


highest_date = sorted(just_date, key=itemgetter(1), reverse=True)[:1]


print('The date with the most rainfall was {}'.format(highest_date))


year_collections = {}


for tup in real_data:
    if tup[0][-4:] in year_collections:
        year_collections[tup[0][-4:]] += int(tup[1])
    else:
        year_collections[tup[0][-4:]] = int(tup[1])


def find_greatest_val_in_dict(dictionary):
    return sorted(dictionary.items(), key=itemgetter(1), reverse=True)[0]


highest_year = find_greatest_val_in_dict(year_collections)

print('{} had the most rain at {}'.format(highest_year[0], highest_year[1]))

