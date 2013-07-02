import urlparse
from django.db import models


class YouTubeEmbedField(models.URLField):
    description = 'YouTube embed field'

    def to_python(self, value):
        youtube_embed_url = 'https://youtube.com/embed/'

        if value and value.startswith(youtube_embed_url):
            parsed_url = urlparse.urlparse(value)
            parse_qs = urlparse.parse_qs(parsed_url.query)
            youtube_id = parse_qs['v'][0]
            return '%s%s' % (youtube_embed_url, youtube_id)

        return value


try:
    from south.modelsinspector import add_introspection_rules

    add_introspection_rules([],
        [
            "youtubeembedfield\.fields\.YouTubeEmbedField"
        ])
except ImportError:
    pass