from fs import loadConfig
from se import searchImagesForName


settings = loadConfig('settings')


searchImagesForName(name='Mary', settings= settings)
