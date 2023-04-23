import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
import argparse

parser = argparse.ArgumentParser(description='Описание что делает программа')

parser.add_argument('name', help='Ваше имя')
args = parser.parse_args()
print(args.name)

load_dotenv()

BITLY_API = "https://api-ssl.bitly.com/v4/"


def link_shorter(link, token):
  url = f"{BITLY_API}bitlinks"
  headers = {"Authorization": f"Bearer {token}"}
  body = {"long_url": link}
  response = requests.post(url, headers=headers, json=body)
  response.raise_for_status()
  return f"\nБитлинк: {response.json()['link']}"


def click_counter(link, token):
  url = f"{BITLY_API}/bitlinks/{link}/clicks/summary"
  headers = {"Authorization": f"Bearer {token}"}
  payload = {"unit": "day", "units": -1}
  response = requests.get(url, headers=headers, params=payload)
  response.raise_for_status()
  return f"Всего переходов: {response.json()['total_clicks']}\n\n"


def is_bitlink(url):
  return requests.get(f"{BITLY_API}bitlinks/{url}",
                      headers={
                        "Authorization": f"Bearer {os.environ['BITLY_TOKEN']}"
                      }).ok


def main():
  url = args.name
  parsed_url = f"{urlparse(url).netloc}{urlparse(url).path}"
  if (is_bitlink(parsed_url)):
    try:
      out = click_counter(f"{parsed_url}", os.environ['BITLY_TOKEN'])
    except requests.exceptions.HTTPError:
      out = "Некорректный Bit.ly\n\n"
  else:
    try:
      out = link_shorter(url, os.environ['BITLY_TOKEN'])
    except requests.exceptions.HTTPError:
      out = "Некорректный URL\n\n"
  print(out)


if __name__ == '__main__':
  main()
