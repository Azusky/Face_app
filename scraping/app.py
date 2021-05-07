from fs import loadConfig
from se import searchImagesForName
import names
# names.generateNames('en',5)
settingsY = loadConfig('settingsY')
settingsG = loadConfig('settingsG')

# tags = ['face', 'human', 'foto 3x4']
tag = loadConfig('tag')
names = names.generateNames_1(['ru',],2)


# searchImagesForName(names=names, settings=settingsY, tags=tags)

searchImagesForName(names=names, settings=settingsG, tags=tag)
