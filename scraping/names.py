from faker import Faker
from fs import loadConfig


def generateNames_1(locales, count):
    names = []
    for locale in locales:
        fake = Faker(locale)

        for _ in range(count):
            name = fake.name().split(' ').pop(0)
            if name not in names:
                names.append((locale, name))

    return names


# for name in n:
#     for t in tag[name[0]]:
#         print(t)
        # liter = list(name[1] + ' ' + tag)

        # print(liter)




# generateNames(locale, count)
#       return a list of unique names

# fix bug name = Mrs.

# def generateNames(locales, count):
#     locName = {}
#     for locale in locales:
#         fake = Faker(locale)
#         locName[locale] = []
#         names = []
#         for _ in range(count):
#             name = fake.name().split(' ').pop(0)
#             if name not in names:
#                 locName[locale].append(name)

#     return locName


# n = generateNames(['en','ru','fr'],5)
# print(n)

# names = {'en': ['David', 'Dustin', 'Ruth', 'Erin', 'Willie'],
#  'ru': ['Казаков', 'Фирс', 'Селиверстова', 'Василиса', 'Евдокимова'],
#  'fr': ['Monique', 'Lucas', 'Pierre', 'Gabriel', 'Pierre']}
