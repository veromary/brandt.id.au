---
layout: default
title: Computers
---

#Computers

[Hotpotatoes in Wordpress]({{ site.url }}/computers/hot-potatoes-in-wordpress.html)

Here are the more recent posts:

{% for post in site.posts %}
{% if post.category contains 'Computers' %}
* {{ post.date | date_to_string }} [{{ post.title }}]({{ site.url }}{{ post.url }})
{% endif %}
{% endfor %}

