import feedparser
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(connect=5, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

blog_rss_url = "https://haril.dev/blog/rss.xml"
response = session.get(blog_rss_url, verify=True)
rss_feed = feedparser.parse(response.content)

MAX_POST_NUM = 5

latest_blog_post_list = "## 📄 Blog <br>\n"

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"- [{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"

# print latest_blog_post_list
print(latest_blog_post_list)

markdown_text = """

# Hi there 👋

I'm haril song(in short, haril 하릴), a software engineer from South Korea.

I'm interested in web development, infrastructure, and more.
I'm currently working at 42dot.

## 🏆 Contribution

### Logback

- https://github.com/googleapis/java-logging-logback/pull/969

### Obsidian

- https://github.com/obsidianmd/obsidian-releases/pull/1678

### Fixture Monkey

- Add 'InnerSpec.keys()' Method with Collection Parameter Support https://github.com/naver/fixture-monkey/pull/934

"""

view_count = """
<!-- 조회수 -->
<p align="right">
  <a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fsongkg7&count_bg=%238D7BF5&title_bg=%23252323&icon=github.svg&icon_color=%23FFFDFD&title=hits&edge_flat=false"/></a>
</p>
"""

readme_text = f"{markdown_text}{latest_blog_post_list}{view_count}"

with open("README.md", 'w') as f:
    f.write(readme_text)
