---
layout: page
title: The 2016 Contest
permalink: /2016/
redirect_from: /2016/getting-started/
---

* Show the table of contents here
{:toc}

Results
---------------

| Placement | Team | Total Score | Sources |
| -- |
| 1 | PUCRS | 33 | [PUCRS.tar.gz](/2016/sources/PUCRS.tar.gz) |
| 2 | Flisvos-2016 | 30 | [Flisvos-2016.zip](/2016/sources/Flisvos-2016.zip) |
| 3 | lampe | 12 | [lampe.zip](/2016/sources/lampe.zip) |
| 4 | Python-DTU | 6 | [Python-DTU.zip](/2016/sources/Python-DTU.zip) |
| 5 | BathTUB | 5 | [BathTUB.zip](/2016/sources/BathTUB.zip) |

| Match | Sim1 | Sim2 | Sim3 | Score | Replay xmls |
| -- |
| BathTUB vs. Python-DTU | -640,533:**49,725** | -111,406:**39,123** | **50,000**:38,919 | 2:4 | [ZIP](/2016/day1match1.zip) |
| BathTUB vs. PUCRS | -1039:**851268** | 50000:**102345** | 36921:**227144** | 0:9 | [ZIP](/2016/day1match2.zip) |
| lampe vs. PUCRS | 63776:**73549** | 55518:**159922** | 50000:**61728** | 0:9 | [ZIP](/2016/day1match3.zip) |
| Flisvos-2016 vs. lampe | **117,353**:54,555 | **288,760**:47422 | **485,984**:-3,022 | 9:0 | [ZIP](/2016/day1match4.zip) |
| Flisvos-2016 vs. Python-DTU | **2,610,354**:36,764 | **1,156,322**:48,404 | **138,718**:43,968 | 9:0 | [ZIP](/2016/day1match5.zip) |
|  |
| BathTUB vs. Flisvos-2016 | 184763:**657500** | -508096:**977580** | 37258:**164839** | 0:9 | [ZIP](/2016/day2match1.zip) |
| Flisvos-2016 vs. PUCRS | **109387**:86775 | 140856:**150358** | 350240:**761920** | 3:6 | [ZIP](/2016/day2match2.zip) |
| PUCRS vs. Python-DTU | **136401**:42882 | **3517745**:47897 | **374010**:47671 | 9:0 | [ZIP](/2016/day2match3.zip) |
| lampe vs. Python-DTU | 38280:**40863** | **172963**:47410 | **321791**:49088 | 6:2 | [ZIP](/2016/day2match4.zip) |
| BathTUB vs. lampe | **64875**:50710 | 38638:**85114** | 173379:**383046** | 3:6 | [ZIP](/2016/day2match5.zip) |

Matchup Schedule
----------------

Finally, the schedule is fixed. The contest will take place on 2 consecutive days: **September 12th and 13th**.

* Each day is divided into **3 slots** and we play on **2 servers** simultaneously.
* A slot ends once its matches on both servers have finished so that no team has to play 2 matches in parallel.
* Each team plays **2 matches a day**.
* All times are **Berlin time** (CEST/UTC+2).
* Servers will be **started around 12:45** on each day, so you have enough time to connect your agents.
* The servers will be started in "manual-mode" (i.e. "tournamentmode=2"), that is, all agents can connect at any time to the simulation server.
* Matches can take up to ~3 hours in the worst case, however, qualification matches indicate somwhere around 1-2 hours per match.
* The **earliest times are guaranteed**. If a match ends even sooner, we will not continue with the following match until the given time.
* Please check back right before the contest to see if **times might have changed**.
* If there is an unforeseen technical issue on our side, we will reschedule the affected matches.

| Slot | Matches Day 1 || Earliest time | Latest time |
| -- |
| | [agentcontest1](http://agentcontest1.in.tu-clausthal.de) | [agentcontest2](http://agentcontest2.in.tu-clausthal.de) |||
| -- |
| 1 | BathTUB vs.<br> Python-DTU | Flisvos 2016 vs.<br> lampe | 13:00 | 13:00 |
| 2 | BathTUB vs.<br> PUCRS | Flisvos 2016 vs.<br> Python-DTU | 14:00 | 16:00 |
| 3 | lampe vs.<br> PUCRS  | none | 15:00 | 19:00 |

| Slot | Matches Day 2 || Earliest time | Latest time |
| -- |
| | [agentcontest1](http://agentcontest1.in.tu-clausthal.de) | [agentcontest2](http://agentcontest2.in.tu-clausthal.de) |||
| -- |
| 1 | BathTUB vs.<br> Flisvos 2016 | lampe vs.<br> Python-DTU | 13:00 | 13:00 |
| 2 | Flisvos 2016 vs.<br> PUCRS | BathTUB vs.<br> lampe | 14:00 | 16:00 |
| 3 | PUCRS vs.<br> Python-DTU  | none | 15:00 | 19:00 |

Maps
------------

| Sim | Map | Download | Coordinates |
| -- |
| 1 | London | [OSM.PBF](../maps/london.osm.pbf) | minLon="-0.1978"<br> maxLon="-0.0354"<br> minLat="51.4647"<br> maxLat="51.5223"<br> mapCenterLat="51.4885438"<br> mapCenterLon="-0.1112036"|
| 2 | Hannover | [OSM.PBF](../maps/hannover.osm.pbf) | minLon="9.68"<br> maxLon="9.81"<br> minLat="52.33"<br> maxLat="52.39"<br> mapCenterLat="52.362967"<br> mapCenterLon="9.712156" |
| 3 | San Francisco | [OSM.PBF](../maps/sanfrancisco.osm.pbf) | minLon="-122.495"<br> maxLon="-122.365"<br> minLat="37.695"<br> maxLat="37.795"<br> mapCenterLat="37.73"<br> mapCenterLon="-122.43" |

All maps are © OpenStreetMap contributors ([terms](http://www.openstreetmap.org/copyright)).

Qualification details
---------------------

1. **Parameters**:
  * Sim: 200 steps (=> max. 14 minutes)
  * Map: standard London
  * Goal: <20% timeouts ("noAction")
  * Start: Thu, 1st of September 2016, 14:00 (CEST)
  * Chat: irc.quakenet.org #agentcontest2016
2. **Results**:

| Match | Team | Timeouts |
| -- |
| 1 | Flisvos-2016 | 0 |
| 2 | BathTUB | 0 |
| 3 | lampe | 0 |
| 4 | Python-DTU | 0 |
| 5 | LTI-USP | withdrawn |
| 6 | PUCRS | 0 |

<div class="actions">
  <a href="/2016/qualification-results.tar.gz" title="qualification-results.tar.gz">
    <span class="title">Qualification results</span>
    <br>
    <span class="filename">qualification-results.tar.gz</span>
  </a>
</div>

Registrants
-----------

| Team | Affiliation | Members | Language/<br>Platform | Details |
| -- |
| BathTUB | Technische<br> Universität<br> Berlin<br> (Germany) | Christian Brandt <br> Marc Schmidt <br> Holger Schuh <br> Julian Böhm <br> Robin Schmied <br> Oguz Serbetci <br> Axel Heßler | JIAC |
| Flisvos 2016 |  | Evangelos I. Sarmas | Python | [PDF](../registration/flisvos-2016.pdf) |
| lampe | Technische<br> Universität<br> Clausthal<br> (Germany) | Philipp Czerner <br> Jonathan Pieper | C++ | [PDF](../registration/lampe.pdf) |
| LTI-USP | University<br> of São Paulo<br> (Brazil) | Arthur Casals <br> Igor Conrado Alves de Lima <br> Jaime Simão Sichman <br> Luís Gustavo Ludescher | JaCaMo |
| PUCRS | Pontifícia<br> Universidade<br> Católica<br> do Rio Grande<br> do Sul (Brazil) | Rafael Cauê Cardoso <br> Ramon Fraga Pereira <br> Maurício Cecilio Magnaguagno <br> Artur Freitas <br> Túlio Basegio <br> Alison Roberto Panisson <br> Guilherme Azevedo <br> Guilherme Krzisch <br> Tabajara Krausburg <br> Anibal Sólon Heinsfeld <br> Felipe Rech Meneguzzi | JaCaMo |
| Python-DTU | Technical<br> University<br> of Denmark | Jørgen Villadsen <br> Andreas Halkjær From <br> Salvador Jacobi <br> Nikolaj Nøkkentved Larsen | Python | [PDF](../registration/python-dtu.pdf) |

Important dates
---------------

{% include_relative _schedule.html %}

Downloads
---------

<div class="actions">
  <a href="/2016/massim-2016-1.3.2-bin.tar.gz" title="massim-2016-1.3.2-bin.tar.gz">
    <span class="title">Software package</span>
    <br>
    <span class="filename">massim-2016-1.3.2-bin.tar.gz</span>
    <br>
    <span class="filename">(requires Java 8 to run)</span>
  </a>
</div>

<div class="centered">
  <p><a href="/2016/registration.pdf">Registration PDF</a></p>
  <p><a href="/2016/registration.zip">Registration Template (short)</a></p>
  <p><a href="/2016/cfp.txt">Call for Participation</a></p>
  <p><a href="/2016/statistics-1.0.zip">Statistics tool</a></p>
</div>

The Scenario
------------

<iframe width="960" height="720" src="https://www.youtube.com/embed/ZZRl3GCZF8Y" frameborder="0" allowfullscreen></iframe>

Our scenario consists of two teams of agents moving through the
streets of a realistic city. The goal for each team is to earn as much
money as possible. [Read the full description](/2016/scenario/).

Starting the Software
---------------------

* **Unzip** the file.
* **documents/readmefirst.pdf** is a good starting point (optional).
* You're running on Windows? Just go to [http://www.mingw.org/wiki/msys/](http://www.mingw.org/wiki/msys/) and **install msys**. Note that you don't need mingw, just the msys part.
* Go to the massim/scripts directory: `cd massim/scripts`
* **Start the server**: `./startServer.sh`
* In another shell, **start the monitor**: `./startMapMonitor.sh`
* In yet another shell, go to the javaagents/scripts directory: `cd javaagents/scripts`
* **Start some agents:** `./startAgents.sh`
* Press *ENTER* on the server shell.

**Problems?** Just write to the mailing list. **No problems?** *Register yourself to the mailing list anyway and write us a short hello message.*

Mailing List for 2015/2016
--------------------------

Participants and all interested colleagues are invited to subscribe to the **agentcontest2015 [at] in.tu-clausthal.de** mailing list.

All the important details and announcements including scenario and communication protocol specifications as well as software release announcements and bug reports will be announced and discussed via this list.

To subscribe, send an **empty** e-mail to [agentcontest2015-subscribe@in.tu-clausthal.de](mailto:agentcontest2015-subscribe@in.tu-clausthal.de) with the subject **subscribe**.

The confirmation request and welcome message will be sent to you shortly afterwards. Please follow the instructions in the automatic mailing list replies and do not delete the confirmation mail, you most likely want to use the confirmation id later.

The **archive** is semi-public. That means, it is accessible to list subscribers. The link is as follows:
https://mail.in.tu-clausthal.de/Lists/agentcontest2015/List.html?Language=english

In order to login, you need to provide your e-mail address with which you are subscribed to the list and the confirmation ID. You get the confirmation ID in the confirmation e-mail right after you subscribed.
In the case you do not have that e-mail any more, simply send an arbitrary e-mail to
agentcontest2015-confirm@in.tu-clausthal.de

In return the system will send you your confirmation ID which you can use to login.

Participation Requirements
--------------------------

The participation in this contest consists of these parts:

1. Declaring the intent to participate by registering to the mailing list.
2. Submission of a short team description. Thus registering to the contest officially.
3. Participation in the contest tournament by taking part in the final online tournament.
4. Submitting the source-code of your application right after the tournament.
5. Submitting a short paper describing different aspects regarding your participation in the contest (content tentative).

Publications
------------

After the tournament we invite every participant to submit a paper
about their team. The papers of which the quality has been assured
will be regularly published. The publication outlet will be announced
as soon as possible.

Prize
-----

The winner of the contest will be awarded with a voucher for
500 EUR worth in books, thankfully provided by Springer Verlag.
Requirements are the submission of a paper and the source codes
of the agents.
