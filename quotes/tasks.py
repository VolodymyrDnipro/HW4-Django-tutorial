import requests
import bs4
from quotes.models import Author, Quotes
from django.db import transaction

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


def send_email_no_quotes_left():
    subject = "Empty"
    message = "no quotes"
    recipient_list = ["example@mail.com"]

    send_mail(subject, message, settings.NOREPLY_EMAIL, recipient_list)


def get_author_id(author_name):
    try:
        author = Author.objects.get(fullname=author_name)
        author_id = author.id
    except Author.DoesNotExist:
        author = Author.objects.create(fullname=author_name)
        author_id = author.id

    return author_id


@shared_task
def scrape_quotes():
    page_number = 1
    quotes_count = 0
    quotes_on_page = 0

    while True:
        url = f"http://quotes.toscrape.com/page/{page_number}/"
        print(page_number)
        response = requests.get(url)
        if response.status_code != 200:
            break
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        quotes = soup.find_all("div", class_="quote")
        quotes_on_page = len(quotes)
        print(quotes_on_page)
        if not quotes:
            send_email_no_quotes_left()
            break

        with transaction.atomic():
            for quote in quotes:
                quote_text = quote.find("span", class_="text").get_text()
                author_name = quote.find("small", class_="author").get_text()

                author_id = get_author_id(author_name)

                bio_link = "http://quotes.toscrape.com" + quote.find("a", href=True)["href"]

                bio_response = requests.get(bio_link)
                if bio_response.status_code == 200:
                    bio_soup = bs4.BeautifulSoup(bio_response.content, "html.parser")
                    birth_date = bio_soup.find("span", class_="author-born-date").get_text()
                    biography = bio_soup.find("div", class_="author-description").get_text()

                    author = Author.objects.get(pk=author_id)
                    author.birth_day = birth_date
                    author.bio = biography
                    author.save()

                Quotes.objects.create(quote=quote_text, author_id=author_id)
                quotes_count += 1

                if quotes_count == 5 and quotes_on_page > 5:
                    quotes_on_page -= quotes_count
                    quotes_count = 0

                elif quotes_count == 5 and quotes_on_page >= 0:
                    quotes_count = 0
                    page_number += 1

                elif quotes_count < 5 and quotes_on_page < 5:
                    # Проверяем наличие элемента li с классом next
                    next_button = soup.find("li", class_="next")
                    if next_button is None:
                        send_email_no_quotes_left()
                        break

    print("Данные успешно записаны в базу данных.")
