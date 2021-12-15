---
layout: page
title: The 16th edition of the Multi-Agent Programming Contest
permalink: /2022/
---

The Scenario: Agents Assemble III
---------------------------------

Agents with limited local vision have to organize to assemble and deliver
complex structures made of blocks, in a grid world.

The scenario is a revision of the previous editions, [2019](/2019/) and [2020/21](/2020/) .

![Agents Assemble](/2019/banner.png){:width="630" height="342"}

Also see the official [Call for Participation](cfp.txt).


Timeline
--------

What | When
--- | ---
First software package and specifications available | December 2021
End of [Registration](#registration) and [Qualification](#qualification) | June 2022
Contest | July 2022


### Registration

To register, submit the registration form (tbd).


### Qualification

In order to participate in the contest, your agents have to demonstrate a stable connection and some basic scenario-related skills. Details will be made available closer to the contest.


### Connection Tests

After the registration deadline, you can contact us to schedule a connection test, where you can try out your connection to our severs (and possibly identify some issues before the qualification).


### Anonymous Test Matches

You can tell us if you'd like to play test matches against other teams (before the contest!). If we find a match, both teams' identities will be kept secret from each other. The full monitor will of course also be disabled.


The platform
------------

The MASSim server is [available on GitHub](https://github.com/agentcontest/massim_2022).

The package contains some dummy agents for different platforms. You can use them as a starting
point or implement the communication protocol yourself.


Prize
-----

The winner of the contest will be awarded a voucher for 500 EUR worth in books,
thankfully provided by [Springer Verlag](https://www.springer.com).
Requirements are the submission of a team description paper and the source code
of the agents.


Communication
-------------

### Mailing List

Participants and all interested colleagues are invited to
[subscribe to our mailing list](https://groups.google.com/forum/#!forum/agentcontest):

```
agentcontest@googlegroups.com
```

All the important details and announcements will be shared on this list.

The [mailing list archive](https://groups.google.com/forum/#!forum/agentcontest)
is publically available.

### Slack

You can also join our [Slack community](https://join.slack.com/t/agentcontest/shared_invite/zt-nkgzsczn-lErnivwTByekwyqaQ7ftGA) for discussions, questions, bug reports, etc.


Publications
------------

After the tournament we invite every participant to submit a paper about their
team. Once the quality of the papers has been assured, they will be regularly
published (as the [previous editions](https://link.springer.com/conference/mapc)) in Springer's [LNCS Challenges](https://www.springer.com/series/16528) subline.

Authors should consult Springer’s [authors’ guidelines](ftp://ftp.springernature.com/cs-proceeding/svproc/guidelines/Springer_Guidelines_for_Authors_of_Proceedings.pdf) and use their proceedings templates, either for [LaTeX](ftp://ftp.springernature.com/cs-proceeding/llncs/llncs2e.zip) or for [Word](ftp://ftp.springernature.com/cs-proceeding/llncs/word/splnproc1703.zip), for the preparation of their papers. Springer encourages authors to include their [ORCIDs](https://www.springer.com/gp/authors-editors/orcid?wt_mc=Other.Other.1.AUT642.ORCID+proceedings+pilot+2017&utm_medium=other&utm_source=other&utm_content=8232017&utm_campaign=1_barz01_orcid+proceedings+pilot+2017) in their papers. In addition, the corresponding author of each paper, acting on behalf of all of the authors of that paper, must complete and sign a Consent-to-Publish form. The corresponding author signing the copyright form should match the corresponding author marked on the paper. Once the files have been sent to Springer, changes relating to the authorship of the papers cannot be made.

- Tentative submission deadline: 1 October 2022
- Submission system: Springer OCS

Please answer and append the questionnaire (tbd.) to your team description paper. Also, please send us a draft version until 15 September.


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

- If an agent is somehow attached to another, it moves together with the other agent. These agents can coordinate their movements to move faster! (One move-action per agent and step.)
- Your agents can start or end up surrounded by obstacles. Make sure they know how to get out of such situations.