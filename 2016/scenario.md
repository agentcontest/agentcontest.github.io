---
title: "Scenario 2016: Agents in the City"
layout: page
permalink: /2016/scenario/
---

<iframe width="960" height="720" src="https://www.youtube.com/embed/ZZRl3GCZF8Y" frameborder="0" allowfullscreen></iframe>


Our scenario consists of two teams of agents moving through the
streets of a realistic city. The goal for each team is to earn as much
money as possible. Money is rewarded for completing certain jobs. Jobs
comprise the acquisition, assembling, and transportation of goods.
These jobs can be created by either the system (environment) or one of
the agent teams.There are two kind of jobs: priced and auctioned. A
team can accept an auctioned job by bidding on it. The bid amount of
money is the reward. If both teams bid, naturally the lowest bid wins.
If a job is not completed in time, the corresponding team is fined.
Priced job have a reward defined upfront, that is given to the first
team to complete that job. The teams have to decide which jobs to
complete and how to do that, i.e. where to get the resources and how
to navigate the map considering targets like shops, warehouses,
charging stations, storage facilities.

A team consists of different types of agents. The agents differ in
their speed, how they move around the city, battery charge, the volume
of goods they can carry, and which tools they can employ to craft
other goods. Currently we have 4 types: cars, trucks, motorcycles, and
drones.

Goods can be bought, crafted, given to a teammate, stored, delivered
as part of a job completion, recovered from a storage facility, and
dumped. These action may happen at their respective specific
locations/facilities. The crafting of an item requires the use of
other goods, some which serve as prime matter and some which serve as
tools. Since each kind of agent can only handle a subset of the tools,
the crafting of some goods require the explicit collaboration of 2 or
more agents.

Agents posses a battery charge that gets decreased as they move around
from one place to another. They need to make sure they never run out
of charge, and therefore should plan their visits to the charging
stations accordingly. Moving from one place to another, as well as
recharging the battery at a charging station, are actions that are
carried on only partially on each step, an may require several steps
for completion.

Tournament points are distributed according to the amount of money a
team owns at the end of the simulation. To get the most points, a team
has to beat the other, as well as surpass a certain threshold. If a
team has a large debt, points are deducted.

An overview of the scenario’s monitor during a sample simulation, in
which only one team is active, can be seen at the top of this entry.
