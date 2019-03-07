from scrapy.loader import ItemLoader, Identity


class ArtworksLoader(ItemLoader):
    """
    Item loader for ArtworksItem
    """
    url_in = Identity()
    artist_in = Identity()
    title_in = Identity()
    height_in = Identity()
    width_in = Identity()
    description_in = Identity()
    path_in = Identity()
