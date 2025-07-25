from twisted.internet import defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from scrapy.utils.reactor import install_reactor
from scraping.spiders.spider_category import CategorySpider
from scraping.spiders.spider_product import ProductSpider
import csv


install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
settings = get_project_settings()
configure_logging(settings)
runner = CrawlerRunner(settings)

@defer.inlineCallbacks
def crawl():
    """Scrape les catégories. Puis à partir de celles ci, scrape les listings de produits associés."""
    # on récupère toutes les catégories 
    yield runner.crawl(CategorySpider) 
    
    # elles devraient être stocké dans un fichier nommé comme la spider
    csv_file = open(f'{CategorySpider.name}.csv')
    reader = csv.reader(csv_file)
    _ = next(reader) # on saute l'entête
    page_list_index = 2
    
    # on récupère l'url de tous les listings de produits
    categories_to_explore = []
    for category in reader:
        if category[page_list_index]:
            categories_to_explore.append(category[page_list_index])
    
    # on récupère tous les produits à partir de ces listings
    yield runner.crawl(ProductSpider, urls=categories_to_explore)
            
    csv_file.close()
    reactor.stop()

from twisted.internet import reactor

crawl()
reactor.run()  # the script will block here until the last crawl call is finished