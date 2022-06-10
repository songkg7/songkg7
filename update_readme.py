import feedparser

blog_rss_url = "https://songkg7.github.io/feed.xml"
rss_feed = feedparser.parse(blog_rss_url)

MAX_POST_NUM = 5

latest_blog_post_list = ""

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"

markdown_text = """
### Hi there 👋

<h2 align="center">🛠 Skills</h2>

<br>

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

<!-- <h3 align="center">Frontend</h3> -->
<!-- <p align="center"> -->
<!--     <img src="https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=html5&logoColor=white"/> -->
<!--     <img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=css3&logoColor=white"/> -->
<!--     <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white"/> -->
<!--     <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white"/> -->
<!--     <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white"/> -->
<!-- </p> -->

<h3 align="center">Backend</h3>
<p align="center">
<!--     <img src="https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=java&logoColor=white"/> -->
<!--     <img src="https://img.shields.io/badge/Python-3766AB?style=for-the-badge&logo=Python&logoColor=white"/> -->
    <img src="https://img.shields.io/badge/Spring-6DB33F?style=flat-square&logo=spring&logoColor=white"/>
<!--     <img src="https://img.shields.io/badge/Hibernate-59666C?style=flat-square&logo=hibernate&logoColor=white"/> -->
<!--     <img src="https://img.shields.io/badge/Node.JS-339933?style=for-the-badge&logo=node.js&logoColor=white"/> -->
</p>

<h3 align="center">DevOps</h3>
<p align="center">
    <img src="https://img.shields.io/badge/Amazon&nbsp;AWS-232F32?style=flat-square&logo=amazon-aws&logoColor=white"/>
    <img src="https://img.shields.io/badge/Elastic-005571?style=flat-square&logo=elastic&logoColor=white"/>
<!--     <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white"/> -->
    <img src="https://img.shields.io/badge/postgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white"/>
    <img src="https://img.shields.io/badge/docker-2496ED?style=flat-square&logo=docker&logoColor=white"/>
<!--     <img src="https://img.shields.io/badge/Oracle-F80000?style=flat-square&logo=oracle&logoColor=white"/> -->
<!--     <img src="https://img.shields.io/badge/Apache&nbsp;Tomcat-F8DC75?style=flat-square&logo=apache-tomcat&logoColor=white"/> -->
</p>
<!-- 
<h3 align="center">Collaboration</h3>
<p align="center">
    <img src="https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=Jira-software&logoColor=white"/>
    <img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white"/>
</p> -->

<br>

---

<br>

<h3 align="center"> 📧 Contact & About Me</h3>

<p align="center">
    <a href="mailto:songkg7@gmail.com" target="_blank">
        <img src="https://img.shields.io/badge/Gmail-EA4335?style=flat-square&logo=gmail&logoColor=white"/>
    </a>
    <a href="https://www.notion.so/0377dd16e02d48cd82fa76394507382c" target="_blank">
        <img src="https://img.shields.io/badge/Notion-000000?style=flat-square&logo=notion&logoColor=white"/>
    </a>
    <a href="https://songkg7.github.io" target="_blank">
        <img src="https://img.shields.io/badge/Tech&nbsp;blog-54BBFF?style=flat-square&logo=github&logoColor=white"/>
    </a>
<!-- linkedin -->
</p>
<!-- 
<p align="center">
    <img src= "https://github-readme-stats.vercel.app/api/wakatime?username=Haril&layout"/>
</p> -->


<br>

___


### :octocat: My Github Stats

<!--
[![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=songkg7&count_private=true&show_icons=true&theme=highcontrast)](https://github.com/anuraghazra/github-readme-stats)

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=songkg7&layout=compact)](https://github.com/anuraghazra/github-readme-stats) -->
<!--
[![willianrod's wakatime stats](https://github-readme-stats.vercel.app/api/wakatime?username=Haril&layout=compact)](https://github.com/anuraghazra/github-readme-stats) -->

<table id="stats">
    <tr>
        <td valign="top" width="50%">
            <img src="https://github-readme-stats.vercel.app/api?username=songkg7&show_icons=true&count_private=true&hide_border=true" align="left" style="width: 100%" />
        </td>
        <td valign="top" width="50%">
            <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=songkg7&hide_border=true&layout=compact&hide=html" align="left" style="width: 100%" />
        </td>
    </tr>
</table>

<br>
<br>

<!-- 조회수 -->
<p align="right">
  <a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fsongkg7&count_bg=%238D7BF5&title_bg=%23252323&icon=github.svg&icon_color=%23FFFDFD&title=hits&edge_flat=false"/></a>
</p>

"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
