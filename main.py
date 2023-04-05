from Assignment3_exeercise3 import Crawler

if __name__ == '__main__':
    crawler = Crawler("https://sport050.nl/sportaanbieders/alle-aanbieders/")
    crawler.crawl_site()