---
layout: page
title: The 2017 Contest
permalink: /2017/
---

Tournament
----------

The tournament will take place September 18th to 21st. All times are CEST.

| Time | Monday |  | Tuesday |  | Wednesday |  | Thursday |  |
| -- |
|  | ac1 |ac2 | ac1 | ac2 | ac1 | ac2 | ac1 | ac2 |
| 14:00 - 16:00 | SMART-JaCaMo | Chameleon | SMART-JaCaMo | BusyBeaver | Jason-DTU | lampe | Chameleon | SMART-JaCaMo |
|  | TUBDAI | lampe | Chameleon | Jason-DTU | Chameleon | TUBDAI | BusyBeaver | Jason-DTU |
| 16:00 - 18:00 | Flisvos | BusyBeaver | Flisvos | Jason-DTU | Flisvos | TUBDAI | Chameleon | Jason-DTU |
|  | TUBDAI | lampe | Chameleon | TUBDAI | Jason-DTU | BusyBeaver | TUBDAI | lampe |
| 18:00 - 20:00 | Flisvos || Flisvos | SMART-JaCaMo ||| BusyBeaver | SMART-JaCaMo |
| | SMART-JaCaMo || lampe | BusyBeaver ||| Flisvos | lampe |

- ac1: agentcontest1.in.tu-clausthal.de
- ac2: agentcontest2.in.tu-clausthal.de
- Matches may start early if both teams and server available
- Matches may start late, if preceding match is taking longer (unlikely)

Registration
------------

The registration phase has been completed! The following teams have registered:

| Team | Affiliation | Members | Language/<br>Platform | Details |
| -- |
| Busy Beaver | Technische<br> Universität<br> Clausthal<br> (Germany) | Jonathan Pieper | Pyson | [PDF](registration/Busy-Beaver.pdf) |
| Chameleon | Shahid Beheshti University (Iran) | Monire Abdoos, <br> Milad Momeni, <br> Sara Marahemi, <br> Mojtaba Nouroozi, <br> Ehsan Emami, <br> Peyman Hassan Abadi | Java | [PDF](registration/Chameleon.pdf) |
| Flisvos 2017 <br> ("Hot Stuff" edition) |  | Evangelos I. Sarmas | Python | [PDF](registration/Flisvos-2017.pdf) |
| Jason-DTU | Technical<br> University<br> of Denmark | Jørgen Villadsen, <br> Oliver Fleckenstein, <br> Helge Hatteland, <br> John Bruntse Larsen, <br> Eirik Oterholm Nielsen, <br> Martin Nielsen | Jason + CArtAgO | [PDF](registration/Jason-DTU.pdf) |
| lampe | Technische<br> Universität<br> Clausthal<br> (Germany) | Philipp Czerner, <br> Jonathan Pieper | C++ | [PDF](registration/lampe.pdf) |
| SMART-JaCaMo | Pontifícia<br> Universidade<br> Católica<br> do Rio Grande<br> do Sul & Universidade <br> Federal <br> de Santa <br> Catarina <br> (Brazil) | Rafael C. Cardoso, <br> Tabajara Krausburg, <br> Túlio Baségio, <br> Débora Engelmann, <br> Rafael H. Bordini, <br> Jomi F. Hübner | JaCaMo | [PDF](registration/SMART-JaCaMo.pdf) |
| TUBDAI | Technische<br> Universität<br> Berlin<br> (Germany) | Christopher-Eyk Hrabia, <br> Patrick Marvin Lehmann, <br> Yousuf Shaladi, <br> Nabil Battjbuer, <br> Axel Heßler | Python | [PDF](registration/TUBDAI.pdf) |

<del>To register for the contest, please fill out the [Registration Template](/2017/registration-template-2017.zip) and follow the instructions in the sample PDF.</del>

Important dates
---------------

{% include_relative _schedule.html %}

The Scenario: Agents in the City
--------------------------------

![Agents in the City](/2016/banner.jpg){:width="630" height="280"}

Our scenario consists of two teams of agents moving through the streets of a realistic city.
Agents can earn money by completing tasks. [Full specification](https://github.com/agentcontest/massim/blob/master/docs/scenario.md).


Downloads
---------

<div class="actions">
  <a href="https://github.com/agentcontest/massim/releases" title="MASSim on GitHub">
    <span class="title">Preview package</span>
    <br>
    <span class="filename">MASSim Releases on GitHub</span>
  </a>
</div>

**Problems with the software?** Just write to the mailing list. **No problems?** *Register yourself to the mailing list anyway and write us a short hello message.*

### The server

Unpack the software package and start the contest server for development and testing. In a shell:

```bash
cd server
java -jar server-2017-0.6-jar-with-dependencies.jar \
  --monitor 8000  # with webmonitor on port 8000
```

[Detailed documentation](https://github.com/agentcontest/massim/blob/master/docs/server.md).

### Your client

The package contains dummy agents for several platforms. You can use these
as starting points:

* [Jason/Eismassim](https://github.com/agentcontest/massim/blob/master/docs/eismassim.md) (Java & AgentSpeak)
* [Java](https://github.com/agentcontest/massim/blob/master/docs/javaagents.md)
* [Pyson](https://github.com/niklasf/pyson) (Python & AgentSpeak)

There have also always been teams that implemented the
[communication protocol](https://github.com/agentcontest/massim/blob/master/docs/protocol.md)
themselves.

Mailing List
------------

Participants and all interested colleagues are invited to [subscribe to our
mailing list](https://groups.google.com/forum/#!forum/agentcontest):

`agentcontest@googlegroups.com`

All the important details and announcements including scenario and communication protocol specifications as well as software release announcements and bug reports will be announced and discussed via this list.

The [mailing list archive](https://groups.google.com/forum/#!forum/agentcontest) is publically available.

Changelog
---------

We have listed some [major changes](changelog) in case you are coming from the 2016 version.

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
