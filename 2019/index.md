---
layout: page
title: The 2019 Contest
permalink: /2019/
---

The Scenario: Agents Assemble(*)
--------------------------------

In the new scenario, agents have to put blocks together to assemble more complex structures and deliver them in a grid world. For more information, see the [Scenario documentation](https://github.com/agentcontest/massim_2019/blob/master/docs/scenario.md).

![Agents Assemble](/2019/banner.png){:width="630" height="314"}

Contest
-------

[Organisation & Guidelines](downloads/organisation.txt)

### Schedule



Time | ac1 | ac2
--- | --- | ---
tba. | A vs. B | C vs. D
tba. | A vs. D | C vs. B
tba. | A vs. C | B vs. D

### Registrations

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
Contest | 16th October 2019

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
thankfully provided by [Springer Verlag](https://www.springer.com). Requirements are the submission of
a team description paper and the source code of the agents.

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
