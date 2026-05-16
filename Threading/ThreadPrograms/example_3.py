import threading
import requests


def fetch_url(url):
    res = requests.get(url)
    print(f"{url}: {len(res.content)} bytes")


urls = ["https://google.com", "https://python.org", "https://demoblaze.com"]
threads = [threading.Thread(target=fetch_url, args=(u,)) for u in urls]

for t in threads:
    t.start()
for t in threads:
    t.join()
