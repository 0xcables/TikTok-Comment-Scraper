import os
import requests
import shutil

try:
    import requests
except ImportError:
    os.system('pip install -q requests')
    import requests

print("TikTok Comment Scraper".center(shutil.get_terminal_size().columns))
print('\n')

videoid = input('          [?] TikTok link > ')

if "vm.tiktok.com" in videoid or "vt.tiktok.com" in videoid:
    videoid = requests.head(videoid, allow_redirects=True, timeout=5).url.split("/")[5].split("?", 1)[0]
else:
    videoid = videoid.split("/")[5].split("?", 1)[0]

t = 0
comm_num = 0

while True:
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'referer': f'https://www.tiktok.com/@x/video/{videoid}',
        }

        response = requests.get(f"https://www.tiktok.com/api/comment/list/?aid=1988&aweme_id={videoid}&count=9999999&cursor={t}", headers=headers)
        response.raise_for_status()

        comments = response.json()["comments"]
        if not comments:
            break

        for comment in comments:
            print(comment["text"])
            comm_num += 1

        t += 50

    except (requests.RequestException, KeyError, IndexError) as e:
        print(f"Error occurred: {e}")
        break

print(f"Total comments scraped: {comm_num}")
