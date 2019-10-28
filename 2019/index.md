---
layout: page
title: The 2019 Contest
permalink: /2019/
---

The Scenario: Agents Assemble
-----------------------------

In the new scenario, agents have to put blocks together to assemble more complex structures and deliver them in a grid world. For more information, see the [Scenario documentation](https://github.com/agentcontest/massim_2019/blob/master/docs/scenario.md).

![Agents Assemble](/2019/contest_banner_small.png)

Contest
-------

### Results

Placement | Team | Total score | Sources
--- | --- | --- | ---
1 | LFC | 22 | [Git](https://github.com/autonomy-and-verification-uol/mapc2019-liv) [Zip](/2019/sources/mapc2019-lfc.zip)
2 | FIT BUT | 15 | [Zip](/2019/sources/FitBut.zip)
3 | GOAL-DTU | 10 | [Zip](/2019/sources/MAPC2019-GOAL-DTU.zip)
4 | TRG | 5 | [Git](https://github.com/MikeVezina/massim2019) [Zip](/2019/sources/mapc2019-trg.zip)

### Replays

Match | Sim 1 | Sim 2 | Sim 3 | Score
--- | --- | --- | --- | ---
LFC vs. FIT BUT | [**210**&nbsp;:&nbsp;0](/2019/replays/?2019-10-16-14-16-27-1571228187194_LFC_FIT-BUT) | [**170**&nbsp;:&nbsp;0](/2019/replays/?2019-10-16-14-16-27-1571228815095_LFC_FIT-BUT) | [**220**&nbsp;:&nbsp;40](/2019/replays/?2019-10-16-14-16-27-1571229197887_LFC_FIT-BUT) | 9:0
GOAL-DTU vs. TRG | [40&nbsp;:&nbsp;40](/2019/replays/?2019-10-16-14-07-44-1571227664602_GOAL-DTU_TRG) | [**40**&nbsp;:&nbsp;0](/2019/replays/?2019-10-16-14-37-04-1571229424884_GOAL-DTU_TRG) | [**40**&nbsp;:&nbsp;0](/2019/replays/?2019-10-16-15-02-26-1571230946067_GOAL-DTU_TRG) | 7:1
LFC vs. TRG | [**180**&nbsp;:&nbsp;120](/2019/replays/?2019-10-16-15-32-19-1571232739091_LFC_TRG) | [0&nbsp;:&nbsp;0](/2019/replays/?2019-10-16-15-39-17-1571233157086_LFC_TRG) | [**210**&nbsp;:&nbsp;40](/2019/replays/?2019-10-16-15-50-00-1571233800721_LFC_TRG) | 7:1
GOAL-DTU vs. FIT BUT | [0&nbsp;:&nbsp;**340**](/2019/replays/?2019-10-16-15-21-50-1571232110105_GOAL-DTU_FIT-BUT) | [0&nbsp;:&nbsp;**40**](/2019/replays/?2019-10-16-15-47-46-1571233666717_GOAL-DTU_FIT-BUT) | [0&nbsp;:&nbsp;**680**](/2019/replays/?2019-10-16-16-22-05-1571235725395_GOAL-DTU_FIT-BUT) | 0:9
FIT BUT vs. TRG | [**80**&nbsp;:&nbsp;0](/2019/replays/?2019-10-16-16-46-42-1571237202721_TRG_FIT-BUT) | [80&nbsp;:&nbsp;**210**](/2019/replays/?2019-10-16-16-53-51-1571237631601_TRG_FIT-BUT) | [**500**&nbsp;:&nbsp;180](/2019/replays/?2019-10-16-17-00-42-1571238042365_TRG_FIT-BUT) | 6:3
LFC vs. GOAL-DTU | [**380**&nbsp;:&nbsp;40](/2019/replays/?2019-10-16-16-52-05-1571237525849_GOAL-DTU_LFC) | [40&nbsp;:&nbsp;**130**](/2019/replays/?2019-10-16-17-22-57-1571239377138_GOAL-DTU_LFC) | [**380**&nbsp;:&nbsp;40](/2019/replays/?2019-10-16-17-43-04-1571240584642_GOAL-DTU_LFC) | 6:3


### Schedule

All times are CEST.

Time | ac1 | ac2
--- | --- | ---
14:00 | LFC vs. FIT BUT | GOAL-DTU vs. TRG
~15:30 | LFC vs. TRG | GOAL-DTU vs. FIT BUT
~17:00 | LFC vs. GOAL-DTU | FIT BUT vs. TRG
~18:30 | Live-Replays | |

### Registrations

[Organisation & Guidelines](downloads/organisation.txt)

Team | Affiliation | Members | Using
--- | --- | ---
[FIT BUT](registrations/FIT_BUT_public.pdf) | Brno University of Technology | Uhlir Vaclav <br> Zboril Frantisek <br> Vidensky Frantisek | Java
[GOAL-DTU](registrations/DTU_public.pdf) | Technical University of Denmark | Jørgen Villadsen <br> Alexander Birch Jensen <br> Andreas Halkjær From | [GOAL](https://goalapl.atlassian.net/wiki/)
[LFC](registrations/LFC_public.pdf) | University of Liverpool | Rafael C. Cardoso <br> Angelo Ferrando <br> Fabio Papacchini | [JaCaMo](http://jacamo.sourceforge.net/)
[TRG](registrations/TRG_public.pdf) | Carleton University | Michael Vezina | [Jason](http://jason.sourceforge.net/wp/)

Registration
------------

Please fill out the [registration form](downloads/registration.tex) and
follow the instructions within.

Important dates
---------------

What | When
--- | ---
(done) First software package available | now!
(done) Scenario is feature complete | July 2019
(done) Registration Deadline | 1st September 2019
(done) Qualification | 9th September 2019
(done) Contest | 16th October 2019

The platform
------------

The MASSim server is available on [GitHub](https://github.com/agentcontest/massim_2019).

<!--div class="actions">
  <a href="https://github.com/agentcontest/massim_2019/releases" title="MASSim on GitHub">
    <span class="title">Software package</span>
    <br>
    <span class="filename">massim-2018-1.1-bin.tar.gz</span>
  </a>
</div-->

### The server

Unpack the software package and start the contest server for development and testing. In a shell:

```bash
cd server
java -jar server-*-jar-with-dependencies.jar \
  --monitor 8000  # with webmonitor on port 8000
```

[Detailed documentation](https://github.com/agentcontest/massim_2019/blob/master/docs/server.md).

### Your client

The package contains some dummy agents. You can use these as a starting point:

* [Java](https://github.com/agentcontest/massim_2019/blob/master/docs/javaagents.md)
* [Jason/Eismassim](https://github.com/agentcontest/massim_2019/blob/master/docs/eismassim.md) (Java & AgentSpeak)

There have also always been teams that implemented the
[communication protocol](https://github.com/agentcontest/massim_2019/blob/master/docs/protocol.md)
themselves.

Prize
-----

The winner of this year's contest will be awarded a voucher for 500 EUR worth in books,
thankfully provided by [Springer Verlag](https://www.springer.com). Requirements are the submission of a team description paper and the source code of the agents.

Mailing List
------------

Participants and all interested colleagues are invited to
[subscribe to our mailing list](https://groups.google.com/forum/#!forum/agentcontest):

`agentcontest@googlegroups.com`

All the important details and announcements including scenario and
communication protocol specifications as well as software release announcements
and bug reports will be shared on this list.

The [mailing list archive](https://groups.google.com/forum/#!forum/agentcontest)
is publically available.

Publications
------------

After the tournament we invite every participant to submit a paper about their
team. Once the quality of the papers has been assured they will be regularly
published. The publication outlet will be announced as soon as possible.
