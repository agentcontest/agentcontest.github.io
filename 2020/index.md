---
layout: page
title: The 15th edition of the Multi-Agent Programming Contest
permalink: /2020/
---

The Scenario: Agents Assemble II
--------------------------------

Agents with limited local vision have to organize to assemble and deliver
complex structures made of blocks, in a grid world.

The scenario is a revision of the [previous edition](/2019/).
[Replays](/2019/#replays) are available.

![Agents Assemble](/2019/banner.png){:width="630" height="342"}

Also see the official [Call for Participation](cfp.txt).

Participants
------------

In order of registration:

Team | Platform | Status
--- | ---
[JaCaMo Builders](registrations/JaCaMo_Builders.pdf) | [JaCaMo](http://jacamo.sourceforge.net/) |
[MLFC](registrations/MLFC.pdf) | [JaCaMo](http://jacamo.sourceforge.net/) | Q. Passed 08/31
[FIT BUT](registrations/FIT_BUT.pdf) | [Java](https://www.java.com/) |
[GOAL-DTU](registrations/GOAL-DTU.pdf) | [GOAL](https://goalapl.atlassian.net/wiki/) | Q. Passed 09/21
[UCD Builders](registrations/UCD_Builders.pdf) | [ASTRA](http://astralanguage.com/) |
[TRG](registrations/TRG.pdf) | [Jason](http://jason.sourceforge.net/wp/) | Reg. retracted
[LTI-USP](registrations/LTI-USP.pdf) | [Jason](http://jason.sourceforge.net/wp/) | Q. Passed 01/22

Provisional timeline
--------------------

What | When
--- | ---
First software package and specifications available | Complete
End of [Registration](#registration) and [Qualification](#qualification) | <del>22 October</del> 12 February 2021
Contest | <del>9 - 13 November</del> 15-19 March 2021

(Update 27th October: The contest has been postponed to spring 2021.)

### Registration

To register, please download the [registration form](registration.tex) and follow the instructions inside.

### Qualification

You can schedule qualification matches where your agent team plays alone in a setting similar to the [SampleQualification](https://github.com/agentcontest/massim_2020/commit/16ef714f408e16984fd0b07a182434dbbe9739e1) config.
**To qualify**, your agents have to
- complete one task in each of the two rounds and
- submit most actions in time (i.e. less than 30% "noAction").

If you do not succeed for some reason, you can attempt again at a later time (provided there is still time).

### Connection Tests

After the registration deadline, you can contact us to schedule a connection test, where you can try out your connection to our severs (and possibly identify some issues before the qualification).

### Anonymous Test Matches

You can tell us if you'd like to play test matches against other teams (before the contest!). If we find a match, both teams' identities will be kept secret from each other. The full monitor will of course also be disabled.

The platform
------------

The MASSim server is [available on GitHub](https://github.com/agentcontest/massim_2020).

The package contains some dummy agents. You can use them as a starting
point or implement the communication protocol yourself.

Prize
-----

The winner of the contest will be awarded a voucher for 500 EUR worth in books,
thankfully provided by [Springer Verlag](https://www.springer.com).
Requirements are the submission of a team description paper and the source code
of the agents.

Mailing List
------------

Participants and all interested colleagues are invited to
[subscribe to our mailing list](https://groups.google.com/forum/#!forum/agentcontest):

```
agentcontest@googlegroups.com
```

All the important details and announcements including scenario and
communication protocol specifications as well as software release announcements
and bug reports will be shared on this list.

The [mailing list archive](https://groups.google.com/forum/#!forum/agentcontest)
is publically available.

Publications
------------

After the tournament we invite every participant to submit a paper about their
team. Once the quality of the papers has been assured they will be regularly
published (as the [previous editions](https://link.springer.com/conference/mapc)) in Springer's [LNCS Challenges](https://www.springer.com/series/16528) subline.

Authors should consult Springer’s [authors’ guidelines](ftp://ftp.springernature.com/cs-proceeding/svproc/guidelines/Springer_Guidelines_for_Authors_of_Proceedings.pdf) and use their proceedings templates, either for [LaTeX](ftp://ftp.springernature.com/cs-proceeding/llncs/llncs2e.zip) or for [Word](ftp://ftp.springernature.com/cs-proceeding/llncs/word/splnproc1703.zip), for the preparation of their papers. Springer encourages authors to include their [ORCIDs](https://www.springer.com/gp/authors-editors/orcid?wt_mc=Other.Other.1.AUT642.ORCID+proceedings+pilot+2017&utm_medium=other&utm_source=other&utm_content=8232017&utm_campaign=1_barz01_orcid+proceedings+pilot+2017) in their papers. In addition, the corresponding author of each paper, acting on behalf of all of the authors of that paper, must complete and sign a Consent-to-Publish form. The corresponding author signing the copyright form should match the corresponding author marked on the paper. Once the files have been sent to Springer, changes relating to the authorship of the papers cannot be made.

- Tentative submission deadline: 1 June 2021
- Submission system: [Springer OCS](https://ocs.springer.com/ocs/en/home/MAPC2020)

General Advice
--------------

We have collected some tips and tricks for participating in the contest. If you have participated before, please send us your additions.

- Make sure your agents can handle transitions between simulations.
- During the contest, only the status monitor will be active. Maybe enable your agents to tell you what's going on.
- Often, we see agents reconnecting to the server during a simulation. Maybe try to ensure that:
    - your agents do not lose valuable information if they need to be restarted; and
    - they can handle different initial states (e.g., agent is carrying a block).
- Test your agents against other agents (e.g. a second instance of your team).
- Test your agents with different scenario parameters.
- Use the `skip()` action for each agent who needs to wait a step in order to speed up the simulation.

For the current scenario:

- If an agent is somehow attached to another, it moves together with the other agent. These agents can coordinate their movements to move twice as fast! (One move-action per agent and step.)
- Your agents can start or end up surrounded by obstacles. Make sure they know how to "dig" themselves out.
- Clear actions could also be used to scare away opponent agents.
