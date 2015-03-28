---
layout: default
title: Food
---

# Food

I wanted to post a recipe, so now I have a new category for the webpage.  Back in 2007 we started doing the [FAILSAFE](http://fedup.com.au) diet, so I had to cook lots of stuff from scratch.  Since then we have not kept to the diet but it still influences my choices - Carob and beetroot cake anyone?

##Recent posts

{% for post in site.posts %}
{% if post.category contains 'Food' %}
* {{ post.date | date_to_string }} [{{ post.title }}]({{ site.url }}{{ post.url }})
{% endif %}
{% endfor %}


