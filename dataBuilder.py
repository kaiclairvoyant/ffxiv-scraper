import json

templateFile = open("dataTemplate.json")

templates = json.load(templateFile)

jobs = ['reaper', 'sage', 'summoner', 'paladin', 'astrologian', 'warrior', 'gunbreaker', 'darkknight', 'dragoon', 'whitemage', 'blackmage', 'dancer', 'machinist', 'bard', 'redmage', 'ninja', 'monk', 'samurai', 'scholar']

dataOutput = {'data': []}

for job in jobs:
    jobSkillsJsonFile = open("jobs/% s.json" % job)

    skillsJson = json.load(jobSkillsJsonFile)

    templates[job]['skills'] = skillsJson

    dataOutput['data'].append(templates[job])

with open("data.json", 'w') as outputFile:
    json.dump(dataOutput, outputFile)

    print(
        "% s built successfully" % outputFile.name
    )
