---
layout: default
title: Lessons from the Tokens
permalink: /lessons/
---

<section class="container lessons-list" style="max-width: 45em; margin: 0 auto; padding: 3em 1.5em;">
  <h1>Lessons from the Tokens</h1>
  <p class="lessons-intro">Lessons from the Tokens: short notes on AI, data science, machine learning, and research software. These are small lessons, observations, and patterns I want to keep track of and share.</p>

  {% if site.posts.size == 0 %}
    <p>No lessons yet.</p>
  {% else %}
    {% for post in site.posts %}
      <article class="post-preview">
        <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
        <p class="post-meta">{{ post.date | date: "%B %-d, %Y" }}</p>
        {% if post.excerpt %}
          <p class="post-excerpt">{{ post.excerpt | strip_html | truncate: 200 }}</p>
        {% endif %}
        {% if post.tags and post.tags.size > 0 %}
          <p class="post-tags">
            Tags: {% for tag in post.tags %}<span class="tag">{{ tag }}</span>{% unless forloop.last %} {% endunless %}{% endfor %}
          </p>
        {% endif %}
      </article>
    {% endfor %}
  {% endif %}

  <p class="rss-link"><a href="{{ '/feed.xml' | relative_url }}">RSS feed</a></p>
</section>
