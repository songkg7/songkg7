import feedparser

blog_rss_url = "https://songkg7.github.io/feed.xml"
rss_feed = feedparser.parse(blog_rss_url)

MAX_POST_NUM = 5

latest_blog_post_list = "### 📄 Blog <br>\n"

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"- [{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"

markdown_text = """

## 🛠 Skills

<!--
**songkg7/songkg7** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->

### Backend

![Java](https://img.shields.io/badge/Java-007396?style=flat-square&logo=java&logoColor=white)
![Spring](https://img.shields.io/badge/Spring-6DB33F?style=flat-square&logo=spring&logoColor=white)

### DevOps

![Aws](https://img.shields.io/badge/Amazon&nbsp;AWS-232F32?style=flat-square&logo=amazon-aws&logoColor=white)
![Elastic](https://img.shields.io/badge/Elastic-005571?style=flat-square&logo=elastic&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

### 📧 Contact & About Me

<a href="mailto:songkg7@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Gmail-EA4335?style=flat-square&logo=gmail&logoColor=white"/>
</a>
<a href="https://www.notion.so/0377dd16e02d48cd82fa76394507382c" target="_blank">
    <img src="https://img.shields.io/badge/Notion-000000?style=flat-square&logo=notion&logoColor=white"/>
</a>
<a href="https://songkg7.github.io" target="_blank">
    <img src="https://img.shields.io/badge/Tech&nbsp;blog-54BBFF?style=flat-square&logo=github&logoColor=white"/>
</a>

### :octocat: My Github Stats

<!--
[![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=songkg7&count_private=true&show_icons=true&theme=highcontrast)](https://github.com/anuraghazra/github-readme-stats)
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=songkg7&layout=compact)](https://github.com/anuraghazra/github-readme-stats) -->

![wakatime](https://github-readme-stats.vercel.app/api/wakatime?username=Haril&layout=compact)
![stat](https://github-readme-stats.vercel.app/api?username=songkg7&show_icons=true&count_private=true&hide_border=true)

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
