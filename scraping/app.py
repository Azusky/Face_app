from fs import loadConfig
from se import searchImagesForName


settingsY = loadConfig('settingsY')
settingsG = loadConfig('settingsG')

names = ['Jessica', 'Kyra', 'Tanya', 'Nastya']


searchImagesForName(names=names, settings=settingsY)

searchImagesForName(names=names, settings=settingsG)
