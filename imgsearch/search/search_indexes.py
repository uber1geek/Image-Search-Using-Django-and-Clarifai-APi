from haystack import indexes
from .models import Image


class ImageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    image_url = indexes.CharField(model_attr='image_url')
    tags = indexes.MultiValueField()

    def get_model(self):
        return Image

    def index_queryset(self, using=None):
    	return Image.objects.all()

    def prepare_tags(self, instance):
    	tags = []
    	for tag in instance.tags.all():
    		tags.append(tag.name)

    	return tags
