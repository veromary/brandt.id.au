---
layout: post
title: Hot Potatoes in Wordpress
date: 2014-04-07 14:50:00 +1100
---

This page started life as an incoherent test post, but turns out to be one of the most popular articles, so here goes making it coherent.

The first thing to do to get your hotpotato up on your Wordpress blog is to upload it.  Now, Wordpress.com doesn't let you upload html files.  You could upload your html file to [Dropbox](http://dropbox.com) and make a link to that file [like this](https://dl-web.dropbox.com/get/Public/pater1m.htm?_subject_uid=48278710&w=AAB2Sj6w2YdFKj1aRYMg3a0J5n0L34MA3xR6wNoO6_yk4w).

Wordpress.com is also fussy about what it embeds, so you can't embed it in a page, but people can click on your link to reach the hot potato.  Dropbox mixes up the addresses, so the Masher sets of hotpotato quizzes won't work.  Unless you have a self-hosted Wordpress.org site.

###The Self Hosted Wordpress Way

Self hosted Wordpress *does* let you upload and embed html files.  First upload using the Media Library, then get the link address.

In the page you want to embed your quiz, go to edit the page/post, switch from Visual to Text mode, use this code:

```
  <iframe src="http://yourwebsite.com/path-to-your.htm" height="400" width="400"></iframe>
```

Which should give something like this:

<iframe src="test.htm" height="400" width="400"></iframe>

You may need to adjust the width and height according to your quiz.

I hope that helps,

Veronica

