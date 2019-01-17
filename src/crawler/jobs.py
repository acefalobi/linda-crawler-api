import requests
from bs4 import BeautifulSoup
from django_cron import CronJobBase, Schedule

from crawler.models import Article


class CrawlerCronJob(CronJobBase):
    RUN_EVERY_MIN = 10

    schedule = Schedule(run_every_mins=RUN_EVERY_MIN)
    code = 'crawler.jobs.crawler_cron_job'

    @staticmethod
    def do():
        page = BeautifulSoup(requests.get("https://www.lindaikejisblog.com/").text, 'html.parser')
        html_articles = page.select(".main_board article")
        html_articles.reverse()

        for html_article in html_articles:
            title = html_article.select(".story_title a")[0].text.strip()
            url = html_article.select(".story_title a")[0].get('href')
            image_url = html_article.select("img")[0].get('src')
            snippet = html_article.select(".story_description")[0].text.strip()

            if not Article.objects.filter(url=url).exists():
                article = Article(title=title, url=url, image_url=image_url, snippet=snippet)
                try:
                    article.save()
                except Exception as e:
                    print(e)
