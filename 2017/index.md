---
layout: page
title: The Upcoming Contest 2017
permalink: /2017/
---

Registration
------------

To register for the contest, please fill out the [Registration Template](/2017/registration-template-2017.zip) and follow the instructions in the sample PDF.

Preliminary Schedule
--------------------

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
java -jar server-2017-0.3-jar-with-dependencies.jar \
  --monitor 8000  # with webmonitor on port 8000
```

[Detailed documentation](https://github.com/agentcontest/massim/blob/master/docs/server.md).

### Your client

The package contains dummy agents for several platforms. You can use these
as starting points:

* [Jason/Eismassim](https://github.com/agentcontest/massim/blob/master/docs/eismassim.md) (Java & AgentSpeak)
* [Java](https://github.com/agentcontest/massim/blob/master/docs/javaagents.md)
* <del>Pyson (Python & AgentSpeak)</del> *coming soon*

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
