from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Url


# @registry.register_document
# class PostDocument(Document):
#     class Index:
#         name = 'posts'
#         settings = {'number_of_shards': 1,
#                     'number_of_replicas': 0}
#
#     class Django:
#         model = Post
#         fields = [
#             'title',
#             'content',
#             'date_posted',
#             'slug',
#         ]

@registry.register_document
class UrlDocument(Document):
    class Index:
        name = 'urls'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Url
        fields = [
            'original_url',
            'short_url',
            'date_created',
        ]
