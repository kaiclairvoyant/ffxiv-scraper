import os
from datetime import datetime

startTime = datetime.now()

jobs = ['reaper', 'sage', 'summoner', 'paladin', 'astrologian', 'warrior', 'gunbreaker', 'darkknight', 'dragoon', 'whitemage', 'blackmage', 'dancer', 'machinist', 'bard', 'redmage', 'ninja', 'monk', 'samurai', 'scholar']

for job in jobs:
    os.system("scrapy crawl ffxiv_spider -a job=% s" % job)

print("Finished in: " + str((datetime.now() - startTime).total_seconds()) + " seconds")
