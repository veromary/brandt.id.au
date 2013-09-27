LMS for a homeschool
####################
:date: 2013-07-17 11:58
:author: veronica
:category: Computers, Homeschooling
:slug: lms-for-a-homeschool

`|jumblelms|`_\ My project for the winter holidays was to make an online
course to go through the multiplication tables with my four sons, ages 6
- 11. It was meant to be an pleasant diversion from regular
homeschooling, but turned into an epic learning experience!

There are many options out there. My little collage of logos there
you'll see some open sources LMSs: `Moodle`_, `Chamilo`_ and
`Claroline`_; a couple of hosted services: `udemy`_ and `TalentLMS`_
and, lastly, some helpful tools `WordPress`_, `Hot Potatoes`_ and
`TinyLMS`_. There are more out there. Another open source LMS I
installed was `efront learning`_ - which may be related to TalentLMS
(see above).

Self-hosted LMS
---------------

At first (after my last look at the idea some years ago), I was settled
on `Chamilo`_, a very handsome Learning Management System (LMS). It
comes in two flavours right now, 1.9.6 and `LCMS Connect`_. They are
both great - 1.9.6 looks better for the K-6 age range, but Connect is a
bit more sophisticated.

It was all going well until I had a mysterious problem where one
computer would refuse to show any webpages from my webhosting. Other
websites would load fine. My home internet access is not the greatest,
so slow patches are par for the course, but sometimes it would be just
my webpages that were running slowly.

I learned about Shared Hosting vs VPS. Also that having several students
logged in at the same time on your average LMS requires hefty web
hosting - not your Economy class shared hosting. Most of the information
on this phenomenon refers to the Great `Moodle`_ of Western Australia,
but applies to Chamilo and other LMSs too. It might work if you
installed the LMS on your own network at home, but I have not networked
my home computers. Some estimate the server would need 2Gb RAM to be on
the safe side.

So, now I reluctantly turn my gaze from the beautiful, shiny,
self-hosted, open source LMSs. There seem to be two options: a) make do
with webpages with simple quiz things or b) sell out and use a
commercial service.

Webpages with quizzes
---------------------

This is a Wordpress blog, so it makes sense to explore what I already
have up and running. There are LMS plugins, like the free `Namaste!`_ or
many, many, many paid services. Namaste! has a catch, that it works with
an exam plugin, which has a basic free version and a range of paid
premium versions.

I can do my own "course" by making webpages, each ending with a quiz to
be passed to reveal the address of the next page plus a form to submit
the results to my email. This is fiddly, but gets the consistent looks
of this blog, plus it hopefully won't exceed the shared hosting limits
like Chamilo did. It's fiddly to set up, but it's cheap.

There are some tools for making this easier. `TinyLMS`_ takes a SCORM
package and formats it for web and/or printing. The resulting webpages
can be put online, on CD, or even zipped up and emailed to students. All
you need is a SCORM editor, like `eXe learning`_ from New Zealand and
`RELOAD`_ from the UK which both seem to be very quiet lately. The
RELOAD website displays a notice that they are undergoing an overhaul,
dated July 2008. There is a new one called `EXE Next Gen`_ from
Afghanistan which looks Great. They seem to have fixed up the NZ eXe and
enhanced it. It exports to several formats including one for mobiles.
Unfortunately my debian box doesn't seem to like the ubuntu packages,
but something to bear in mind. (**Update:** there is a current, working
version of eXe at `exelearning.net`_ based in Spain.)

And I should mention `Hot Potatoes`_ a Windows program that works on
Linux under wine. It makes javascript quizzes that you can export as
webpages and upload as they are or embed into blogs like this. Their
philosophy is not so much assessment, but doing exercises to help you
learn.

Going commercial
----------------

There are many companies only too willing to set up your LMS for a fee.
Some are particularly interesting to homeschoolers since they have a
free version for a limited number of students - which, depending on the
size of your family, might suit you right down to the ground. On the
other hand, if you want to share your courses with other families then
someone has to start paying.

I've started a site at `talentLMS`_ which is reminiscent of the free
`efront learning`_ and they both come from Greece. It is very slick. For
the time being `this is my multiplication course`_. We'll see how it
goes.

In conclusion
-------------

I would have liked to show off my Chamilo install here, but it would
bring down the rest of my webpages. I have learnt a bit about the limits
of what is possible on the internet. Maybe, as time goes by, the price
of strong hosting will come down, but then again, there will always be
fancier software available to tax the servers.

If you want to pay $30 per month for something, consider `Aid to the
Church in Need`_, `Family Life International`_ or `Australia Needs
Fatima`_.

.. _|image1|: http://brandt.id.au/wp-content/uploads/2013/07/jumblelms.png
.. _Moodle: http://moodle.org
.. _Chamilo: http://chamilo.org
.. _Claroline: http://claroline.net
.. _udemy: https://www.udemy.com/
.. _TalentLMS: http://www.talentlms.com/
.. _WordPress: http://wordpress.org
.. _Hot Potatoes: http://hotpot.uvic.ca/
.. _TinyLMS: http://www.randelshofer.ch/tinylms/
.. _efront learning: http://www.efrontlearning.net/
.. _LCMS Connect: http://lcms.chamilo.org/
.. _Namaste!: http://namaste-lms.org/
.. _eXe learning: http://exelearning.org/
.. _RELOAD: http://www.reload.ac.uk/
.. _EXE Next Gen: http://sourceforge.net/p/exe-nextgen/
.. _exelearning.net: http://exelearning.net/?lang=en
.. _Hot Potatoes: http://hotpot.uvic.ca
.. _talentLMS: http://talentlms.com
.. _efront learning: http://efrontlearning.org
.. _this is my multiplication course: http://brandt.talentlms.com/shared/start/key:GBKMFPJU
.. _Aid to the Church in Need: http://www.churchinneed.org/
.. _Family Life International: http://fli.org
.. _Australia Needs Fatima: http://fatima.org.au

.. |jumblelms| image:: http://brandt.id.au/wp-content/uploads/2013/07/jumblelms.png
.. |image1| image:: http://brandt.id.au/wp-content/uploads/2013/07/jumblelms.png
