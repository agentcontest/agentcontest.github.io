---
title: "MASSim 2017: Major changes"
layout: page
permalink: /2017/changelog/
---

Here, we summarize some major changes compared to the 2016 edition.

## massim server

* it's almost a complete rewrite
    * (please accept and report any new bugs)
* new/adapted message formats
    * especially _action_
        * parameters are now given in a list
* added command line
    * e.g. you can _pause_ server execution between steps

## protocol

* message formats have been extracted to protocol module
* this might be useful for other Java systems

## scenario

* matches with more than 2 teams simultaneously are now possible
* no cost any more for: charging, dumps, storage
* added new job type: _missions_
* added new facility: _resource node_
    * added _gather_ action
* added limit for simultaneously active jobs posted by the same team
* adapted proximity and cellsize
    * locations are now trimmed to a number of decimals according to the proximity
    * cellSize now gives a "real" distance in meters
* at most 1 tool of each type now required for assembly
* generated jobs now always require assembled items
* assembled items can no longer be bought in shops
* removed the possibility to post auction jobs
* changed a few minor things here and there (please consult the documentation)
* finally wrote a background story

## monitor

* new webmonitor replaces legacy Java RMI monitor

## eismassim

* upgraded dependency to EIS 0.5.0
* percepts might have new names/parameters
* percepts have been adapted to the new circumstances

## misc.

* dropped support for older scenarios (use legacy packages instead)
* JSON config for massim, eismassim, javaagents
* removed shell scripts - everything can now be run directly through the jar files (configuration selection has been moved to the Java code)
