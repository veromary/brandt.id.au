---
layout: default
title: Education
---

Ideas for homeschooling and general teaching/learning stuff

[The Catholic's Latin Instructor]({{ site.url }}/latin/) - a project to turn Fr Edward Caswall's book into an online course.

Here are two old pages:
[Home Education]({{ site.url }}/homeschool.html) and [Teaching]({{ site.url }}/teaching.html) resources, ideas, recommended reading and things like that. Lots of book reviews.

Here are the more recent posts:

{% for post in site.posts %}
{% if post.category contains 'Education' %}
* {{ post.date | date_to_string }} [{{ post.title }}]({{ post.url }})
{% endif %}
{% endfor %}

