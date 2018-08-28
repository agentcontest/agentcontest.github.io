---
layout: page
title: The 2018 Contest
permalink: /2018/
---

Important dates
---------------

{% include_relative _schedule.html %}

The Scenario: Agents in the City
--------------------------------

![Agents in the City](/2016/banner.jpg){:width="630" height="280"}

Our scenario consists of two teams of agents moving through the streets of a realistic city.
Agents can earn money by completing tasks and build wells to fight a water crisis.
[Full specification](https://github.com/agentcontest/massim/blob/master/docs/scenario.md).

This builds on the [previous edition](/2017/). You can [watch](https://multiagentcontest.org/2017/replays/?2017-09-21-18-07-25-2017-MAPC-Sim3) replays from last year [here](https://multiagentcontest.org/2017/#replays). ([CFP](/2018/CFP.txt))

Registration
------------

- Six teams have registered for MAPC 2018!
- [DONE] To register, download the registration [form](registration/registration.pdf) and/or [template](registration/registration.tex) and follow the instructions inside.

| Team | Affiliation | Members | Language/<br>Platform |
| -- |
| [Dumping to Gather](registration/dtg.pdf) | TU Berlin | Christopher-Eyk Hrabia, <br> Josephine Alice Krause, <br> Marc Schmidt, <br> Andrea Marie Weintraud | ROS Hybrid Behavior Planner |
| [Jason-DTU](registration/jason-dtu.pdf) | Technical University <br> of Denmark <br> (DTU) | Jørgen Villadsen, <br> Mads Okholm Bjørn, <br> Andreas Halkjær From, <br> Thomas Søren Henney, <br> John Bruntse Larsen | Jason + CArtAgO |
| [TUBDAI](registration/tubdai.pdf) | TU Berlin | Michael Franz Ettlinger, <br> Christopher-Eyk Hrabia | ROS Hybrid Behavior Planner |
| [Akuanduba-UDESC](registration/akuanduba.pdf) | Santa Catarina <br> State University <br> (UDESC) | Giovanni Jakubiak de Albuquerque, <br> Tiago Funk, <br> Vilson de Deus Corrêa Júnior, <br> Tiago Luiz Schmitz | |
| [SMART_JaCaMo](registration/smart-jacamo.pdf) | <sup>1</sup>Pontifícia<br> Universidade<br> Católica<br> do Rio Grande<br> do Sul (PUCRS), <sup>2</sup>University of <br> Liverpool, <br> <sup>3</sup>Universidade <br> Federal <br> de Santa <br> Catarina <br> (UFSC) | Tabajara Krausburg<sup>1</sup>, <br> Rafael C. Cardoso<sup>2</sup>, <br> Débora Engelmann<sup>1</sup>, <br> Vitor Peres<sup>1</sup>, <br> Vágner Gabriel<sup>1</sup>, <br> Juliana Damasio<sup>1</sup>, <br> Rafael H. Bordini<sup>1</sup>, <br> Jomi F. Hübner<sup>3</sup> | JaCaMo |
| [FIT BUT](registration/fitbut.pdf) | Brno University of Technology | Vaclav Uhlir, <br> Peter Hamran | Python |

Downloads
---------

<div class="actions">
  <a href="https://github.com/agentcontest/massim/releases" title="MASSim on GitHub">
    <span class="title">Software package</span>
    <br>
    <span class="filename">massim-2018-1.1-bin.tar.gz</span>
  </a>
</div>

### The server

Unpack the software package and start the contest server for development and testing. In a shell:

```bash
cd server
java -jar server-2018-1.1-jar-with-dependencies.jar \
  --monitor 8000  # with webmonitor on port 8000
```

[Detailed documentation](https://github.com/agentcontest/massim/blob/master/docs/server.md).

### Your client

The package contains some dummy agents. You can use these as a starting point:

* [Java](https://github.com/agentcontest/massim/blob/master/docs/javaagents.md)
* [Jason/Eismassim](https://github.com/agentcontest/massim/blob/master/docs/eismassim.md) (Java & AgentSpeak)

There have also always been teams that implemented the
[communication protocol](https://github.com/agentcontest/massim/blob/master/docs/protocol.md)
themselves.

Prize
-----

The winner of this year's contest will be awarded a voucher for 500 EUR worth in books,
thankfully provided by [Springer Verlag](https://www.springer.com). Requirements are the submission of
a team description paper and the source code of the agents.

Mailing List
------------

Participants and all intrested colleagues are invited to
[subscribe to our mailing list](https://groups.google.com/forum/#!forum/agentcontest):

`agentcontest@googlegroups.com`

All the important details and announcements including scenario and
communication protocol specifications as well as software release announcements
and bug reports will be shared on this list.

The [mailing list archive](https://groups.google.com/forum/#!forum/agentcontest)
is publically available.

Changelog
---------

There have been some [changes since the 2017 version](https://github.com/agentcontest/massim/blob/master/CHANGELOG.md).
Most notably money is no longer the primary goal. Instead you build wells to generate points.

Publications
------------

After the tournament we invite every participant to submit a paper about their
team. Once the quality of the papers has been assured they will be regularly
published. The publication outlet will be announced as soon as possible.
