from scrapy.loader import ItemLoader, Identity
from scrapy.loader.processors import TakeFirst, MapCompose


def add_base_url(value, loader_context):
    return loader_context['base_url'] + value


class ArtworksLoader(ItemLoader):
    """
    Item loader for ArtworksItem
    """
    default_output_processor = TakeFirst()
    url_in = Identity()
    artist_in = Identity()
    title_in = TakeFirst()
    image_in = MapCompose(add_base_url)
    height_in = Identity()
    width_in = Identity()
    description_in = Identity()
    path_in = Identity()
    path_out = Identity()
