import feedparser

blog_rss_url = "https://songkg7.github.io/feed.xml"
rss_feed = feedparser.parse(blog_rss_url)

MAX_POST_NUM = 5

latest_blog_post_list = "## 📄 Blog <br>\n"

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"- [{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"

markdown_text = """

# Hi there 👋

I'm haril song(in short, haril 하릴), a software engineer from South Korea. I'm interested in web development, infrastructure, and more.
 I'm currently working at startup company as a backend developer.

## 🛠 Skills

### BE

![Java](https://img.shields.io/badge/Java-007396?style=flat-square&logo=java&logoColor=white)
![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white)
![Spring](https://img.shields.io/badge/Spring-6DB33F?style=flat-square&logo=spring&logoColor=white)

### Infra

![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=flat-square&logo=amazon-aws&logoColor=white)
![GCP](https://img.shields.io/badge/Google%20Cloud-%234285F4.svg?style=flat-square&logo=google-cloud&logoColor=white)
![Elastic](https://img.shields.io/badge/Elastic-005571?style=flat-square&logo=elastic&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-000?style=flat-square&logo=apachekafka)
![Jenkins](https://img.shields.io/badge/Jenkins-%232C5263.svg?style=flat-square&logo=jenkins&logoColor=white)

## 🏆 Contribution

- Google : [java-logging-logback](https://github.com/googleapis/java-logging-logback/pull/969)
- Obsidian : [O2 plugin](https://github.com/songkg7/o2)
- Naver : [Fixture Monkey](https://github.com/naver/fixture-monkey)

## 📫 Contact

<a href="mailto:songkg7@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Gmail-EA4335?style=flat-square&logo=gmail&logoColor=white"/>
</a>
<a href="https://www.linkedin.com/in/경근-송-b63216210/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white"/>
</a>
<a href="https://songkg7.github.io" target="_blank">
    <img src="https://img.shields.io/badge/Tech&nbsp;blog-0A2647?style=flat-square&logo=github&logoColor=white"/>
</a>

## :octocat: My Github Stats

<!--START_SECTION:waka-->
<!--END_SECTION:waka-->

<p>
  <img height="180em" src="https://github-readme-stats-liart-gamma.vercel.app/api?username=songkg7&show_icons=true&include_all_commits=true&bg_color=30,e96443,904e95&title_color=fff&text_color=fff">
</p>

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
