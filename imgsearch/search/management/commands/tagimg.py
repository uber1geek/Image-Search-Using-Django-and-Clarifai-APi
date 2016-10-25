import os
import requests
from django.core.management.base import BaseCommand, CommandError
from search.models import Image
from django.conf import settings


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Testing Image Tagging"))

        apiurl = "https://api.clarifai.com/v1/tag?url={imageurl}&access_token=R9PRl6OCiMGJKDphBYbF65EAtfmGnX"

        with open(settings.IMAGEURLSFILE, 'r') as srcfile:
            urls = srcfile.readlines()
            for url in urls:
                callurl = apiurl.format(imageurl=url.strip())
                #TODO: Validate Urls
                self.stdout.write(self.style.SUCCESS(callurl))
                r = requests.get(callurl)
                response = r.json()
                self.stdout.write(self.style.SUCCESS(response))
                try:
                    if r.status_code == 200:
                        tags = response['results'][0]['result']['tag']['classes']
                        self.stdout.write(self.style.SUCCESS(tags))

                        img =  Image.objects.create(
                            image_url = url
                            )
                        img.tags.add(*tags)
                except IndexError:
                    self.stderr.write(self.style.ERROR("Something Went Wrong!"))
