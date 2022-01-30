import os
from datetime import datetime

startTime = datetime.now()

jobs = ['reaper', 'sage', 'summoner', 'paladin', 'astrologian', 'warrior', 'gunbreaker', 'darkknight', 'dragoon', 'whitemage', 'blackmage', 'dancer', 'machinist', 'bard', 'redmage', 'ninja', 'monk', 'samurai', 'scholar']

for job in jobs:
    print("Running ffxiv_spider for % s" % job)
    os.system("scrapy crawl ffxiv_spider -a job=% s" % job + " -s LOG_ENABLED=False")

print("Downloads were completed in " + str((datetime.now() - startTime).total_seconds()) + " seconds")

print("Building data with dataBuilder.py")

os.system("py dataBuilder.py")