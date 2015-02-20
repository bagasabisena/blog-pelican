Title: Rumpy, a (Supposedly) Multiplatform Chat App
Date: 2015-1-30
Category: Blog
<<<<<<< HEAD
Tags: android, java, programming
og_image: images/rumpy/screenshot3.png
=======
Slug: rumpy
Tags: android, java, programming

>>>>>>> gallery

Rumpy is a hobby project that I developed as an escape from a boring on-the-job training back in 2012. The name Rumpy was chosen from Indonesian word 'rumpi' which means chit-chat. It was my first programming project that I did while I was learning to code. I always wanted to know how to program, so it was the perfect time to start. 

2012 was a time where Blackberry and its Messenger app took reign in Indonesia. It got me thinking for some time, why don't we roll-out our own version of chat service? Why should we rely on others infrastructure and pay monthly cost to them? Those naive idealistic thoughts drove me to the idea of a multiplatform chat service for my first coding project, and so Rumpy was born.

In order to make chat service, you need to develop three things:

* First, of course the app. The idea is multiplatform, so, client application for Android and iOS are mandatory.
* Second, the server. It has to be able to pass message between users.
* Lastly, the protocol. The client and server have to talk with a mutual understanding.

It sounds simple in my head but when it comes to actual implementation, it is a whole different level. 

Building a good Android app alone is delicate enough especially when you are still scratching your head from learning data structure, OOP, design pattern, and so on while fixing the error on syntax. Then you have to design and develop the server which is far more complex than the app. 

At the end the project was, well.. unfinished. No, it is not worth [$20 billion like WhatsApp](http://time.com/3477028/facebook-whatsapp-19-billion-dollar-deal/). The app didn't even arrive at Google Play. But wait, wait! Don't leave my blog just yet. At least it is not for nothing, okay.

Rumpy did work at some level. Through the android app I could send message back and forth (as long as the server is up). And it also had delivered and read receipt which was a big deal at the time. Don't believe me? I have the screenshots (and the code) below.

![](/images/rumpy/splash.jpg)
![](/images/rumpy/screenshot2.png)
![](/images/rumpy/screenshot3.png)

Then I took Rumpy to the national startup competition [iMULAI 4.0](https://www.techinasia.com/imulai-4-jakarta/) with my friend [Mohammad Anggasta](http://www.twitter.com/stanggasta). We thought maybe the idea and the prototype was not bad. And turned out we got into the [best 50 ideas](https://twitter.com/IMULAI/status/205503584291397634). 

So, in the end, I gained so much from Rumpy. My TU Delft Professor always put this sentence at the cover of exam paper.
> Make clear in your answer how you reach the final result; the road to the answer is very important.

Learning is not always about result. Process is also important. Rumpy not only given me the experience (and taught me the [DRY](http://en.wikipedia.org/wiki/Don%27t_repeat_yourself) principle), but also the satisfaction you get when you do something meaningful.

The take home message for myself: 
>Creating something is fun. So let's start making the idea into reality. The worst thing I can get from it is that I learn.

Thank you for reading!

----------
BTW i have uploaded the source code to github. For those who interested feel free to check from links below.

* [Server](https://github.com/bagasabisena/RumpyServerWS)
* [Android client](https://github.com/bagasabisena/RumpyClient)
* [Protocol](https://github.com/bagasabisena/Stanza)
