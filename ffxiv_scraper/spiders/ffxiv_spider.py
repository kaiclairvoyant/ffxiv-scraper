import scrapy
import json

class JobSkill:
    def __init__(self, name, level, img, type, cast, recast, cost, range, radius, effects):
        self.name = name
        self.level = level
        self.img = img
        self.type = type
        self.cast = cast
        self.recast = recast
        self.cost = cost
        self.range = range
        self.radius = radius
        self.effects = effects

    def __repr__(self):
        return "name:% s - level:% s - img:% s - type:% s - cast:% s - recast:% s - cost:% s - range:% s - radius:% s " \
               "- effects:% s" % (
                   self.name, self.level, self.img, self.type, self.cast, self.recast, self.cost, self.range,
                   self.radius,
                   self.effects)

    def format(self):
        description = ''

        for effect in self.effects:
            effect = effect.strip()
            description = description + effect + "\n"

        return {
            "name": self.name,
            "level": self.level,
            "image": self.img,
            "type": self.type,
            "cast": self.cast,
            "recast": self.recast,
            "cost": self.cost,
            "range": self.range,
            "radius": self.radius.strip(),
            "description": description
        }


class FfxivSpiderSpider(scrapy.Spider):
    def __init__(self, job=''):
        self.job = job
        self.name = 'ffxiv_spider'
        self.allowed_domains = ['na.finalfantasyxiv.com']
        self.start_urls = ["https://na.finalfantasyxiv.com/jobguide/% s/" % job]
        super().__init__()

    name = 'ffxiv_spider'

    def parse(self, response):
        jobBody = response.css('.job__tbody')

        pveActions = jobBody.css('[id*="pve_action"]')

        iconImageUrls = (pveActions.css('div.job__skill_icon')).css('img::attr(src)').getall()

        yield {
            'image_urls': iconImageUrls
        }

        jobData = []

        for pveAction in pveActions:
            skillName = (pveAction.css('.skill__wrapper').css('strong::text')).get()
            level = (pveAction.css('.jobclass__wrapper')).css('p::text').get()
            iconImage = (pveAction.css('div.job__skill_icon')).css('img::attr(src)').get().split('/')[-1]
            type = (pveAction.css('.classification::text')).get()
            cast = (pveAction.css('.cast::text')).get()
            recast = (pveAction.css('.recast::text')).get()
            cost = (pveAction.css('.cost::text')).get()
            range = (pveAction.css('.distant_range::text')).getall()[1]
            radius = (pveAction.css('.distant_range::text')).getall()[3]
            effects = (pveAction.css('.content::text')).getall()

            jobSkill = JobSkill(skillName, level, iconImage, type, cast, recast, cost, range, radius, effects)

            jobData.append(jobSkill.format())


        with open("jobs/% s.json" % self.job, 'w') as outputFile:
            json.dump(jobData, outputFile)

