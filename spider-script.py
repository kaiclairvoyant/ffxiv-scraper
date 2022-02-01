import os
from datetime import datetime

startTime = datetime.now()

jobsFolderExists = os.path.isdir('jobs/')

if not jobsFolderExists:
    os.mkdir('jobs/')

jobs = ['reaper', 'sage', 'summoner', 'paladin', 'astrologian', 'warrior', 'gunbreaker', 'darkknight', 'dragoon',
        'whitemage', 'blackmage', 'dancer', 'machinist', 'bard', 'redmage', 'ninja', 'monk', 'samurai', 'scholar']

for job in jobs:
    print("Running ffxiv_spider for % s" % job)
    os.system("scrapy crawl ffxiv_spider -a job=% s" % job + " -s LOG_ENABLED=False")

print("Finished in " + str((datetime.now() - startTime).total_seconds()) + " seconds")

print("Building data with dataBuilder.py")

os.system("py dataBuilder.py")
