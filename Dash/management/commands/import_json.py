import json 
from django.core.management.base import BaseCommand
from Dash.models import User 

class Command(BaseCommand):
    help = 'Import external json file into Django Database.'
    
    def handle(self, *args, **kwargs):
        with open(r'C:\Users\DELL\Downloads\Dashboard_DjangoF\Dashboard\jsondata.json', 'r',encoding='utf8') as file:
            data = json.load(file)
            print(data)
            for item in data:
                User.objects.create(
                    intensity = item['intensity'],
                    likelihood = item['likelihood'],
                    relevance = item['relevance'],
                    year = item['end_year'],
                    country = item['country'],
                    sector = item['sector'],
                    insight = item['insight'],
                    impact = item['impact'],
                    pestle = item['pestle'],
                    source = item['source'],
                    topics = item['topic'],
                    region = item['region'],
                    url =  item['url'],
                    title = item['title'],
                    
                )
        self.stdout.write(self.style.SUCCESS('Done'))