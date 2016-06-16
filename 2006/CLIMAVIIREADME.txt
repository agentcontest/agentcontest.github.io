-----------------------------------------------------------------------
MASSim Package - CLIMA Contest infrastructure 
Copyright (C) 2005,2006 Computational Intelligence Group, Department of
Computer Science, Clausthal University of Technology, Germany

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
-----------------------------------------------------------------------

		       *** CLIMA VII Contest ***
	   (brief manual for package installation and usage)
		    (relevant version v0.1 Beta)

		Mehdi Dastani, Juergen Dix, Peter Novak
	      http://cig.in.tu-clausthal.de/CLIMAContest/


*** General
This README file contains the instructions to run and use the Beta
release development packages of CLIMA Contest server.

MASSim is a bundle of software packages for facilitating the CLIMA
Contests serie written in Java. Authors provide this package in order to
allow CLIMA Contest participants to build and test their software agents
for CLIMA Contest.

Current bundle of software packages (as of February 5th 2006) is fully
compliant with the CLIMA VII Contest scenario and is specifically built
for 2006 contest edition (Future University Hakodat, Hokkaido, Japan).

*** Copying (GNU/GPL License)
See the GNU/GPL License, or the reminder at the beginning of this file.


*** Packages

massim-server-<version>.tar.gz - contains the binaries of the
	CLIMA Contest server together with the default configuration.

massim-demoAgent-<version>.tar.gz - contains the binaries of sample agents
	which are able to connect to the contest server and fully comply
	with the CLIMA VII Contest protocol.

massim-serverMonitor-<version>.tar.gz - contains the server monitoring
	console application which can display the details of current
	server status on the console.

*** Usage
** Prerequisities
- We developed and tested our software packages on Linux operating
  system (Debian based distributions). These instructions refer to usage on Linux
  OS. In the near future we will release also packages compatible with
  other operating systems (MS Windows based OS).
- Java Runtime Environment 1.5 (Sun). Download and install according to
  instructions at http://java.sun.com/ (for GNU/Debian you can check
  e.g. http://www.debian-administration.org/articles/142 on how to
  properly install JRE 1.5)
- For watching the visual output of simulations (SVG images), install
  the Adobe SVG Viewer plug-in for Internet Explorer. Download and
  install according to instructions at
  http://www.adobe.com/svg/viewer/install/main.html.


** Installation
- download and unpack the three packages into a directory of your choice.
- configure the server - in order to correctly run the simulation server,
  you have to slightly modify the configuration of it:
  - open the file ./massim-server-<version>/startServer and on the
    marked place enter the correct ID (or IP) of the host where the
    server is going to run. Read the corresponding README file
    carefully.
- configure the server monitor - modify the file
  ./massim-serverMonitor-<version>/startServerMonitor according to
  instructions in the corresponding README file.


** Usage
- First start the server by launching the script ./startServer in
  massim-server-<version> directory. It will start the server, launch
  the RMI Registry service and wait for agents to connect. By default
  the server waits for a RETURN key to launch the tournament
  automatically.  In the case you need to change some parameters of the
  server, edit the file serverconfig.xml.
- Then start the server monitor by launching the script ./startMonitor
  in the massim-serverMonitor-<version> directory. The server monitor
  has to be properly configured in order to connect to correct
  simulation server. It displays the status of the server with refresh
  of one second. During the agents development, this tool may become
  very usefull, therefore storing and analyzing the output can be of
  good use to participants.
- Start the agents which connect to the server and participate
  in the tournament by running the script ./startAgents in
  massim-demoAgent-<version> directory.
- Start the tournament by pressing a RETURN key in the console of the
  simulation server.


** Visualization
After the tournament is over, in the directory
./massim-server-<version>/output you can find visualisation records of
all the simulations. The directory contains subfolders in the format
<TournamentName>_<Team1ID><Team2ID>_<SimulationName>. Each such
subdirectory contains a number of SVG images, each containing the status
of the simulation environment in one simulation step. To see the
animation of the simulation record open the file SimulationPreview.svg
in Internet Explorer. To view the simulation you have to have Adobe SVG
Viewer plug-in installed. Unfortunately nowadays, there's no better SVG
viewer, however we are still working on improvements of the simulation
record output in order to allow also other browsers to correctly display
simulation records.

In the browser window you can see the grid together with a snapshot of
fraction of the simulation statistics and controls. You can control the
simulation animation as a video animation by these controls.

Note, that the content of the directory output is always rewritten. If
you want to change the output directory change the corresponding
configuration file (see README file of the massim-server-<version>
package).

*** Agents development
The released simulation server should serve to participants by
development of their agents for CLIMA VII Contest. In order to test your
own agents you need to change the server configuration. Currently it
runs two teams of identical agents (see the startAgents script in the
package massim-demoAgents-<version>). The file serverconfig.xml
(package massim-server-<version>), section <accounts> contains
credentials of all the agents participating in the tournament. Let's say
you are going to run your agents as team "china". You will have 4 agents
with usernames "china1", "china2", "china3" and "china4". Their
corresponding passwords are "1", "2", "3" and "4". Configure your own
agents to connect with these credentials to the server and do replace
lines in the script startAgents starting agents of team "china" by your
own agents. That means comment the lines
java -jar demoAgent.jar china1 1 &
java -jar demoAgent.jar china2 2 &
java -jar demoAgent.jar china3 3 &
java -jar demoAgent.jar china4 4 &

and put there starting commands for your own agents with credentials
according to the serverconfig.xml file.

Currently the server runs 3 simulations with two agent teams "china" and
"portuguese". 


*** Sample Installation Session
In this section we describe step-by-step tutorial on how to run and use
the server, server monitor and agents on the localhost. Please follow it
carefully in order to test your server and agents deployment. Please
read the instructions in particular directories in order to run your
setup from different network hosts.


cig:~/download/agents# ls
massim-demoAgent-v0_1_beta_1.tar.gz
massim-server-v0_1_beta_1.tar.gz
massim-serverMonitor-v0_1_beta_1.tar.gz

cig:~/download/agents# tar -xzf massim-demoAgent-v0_1_beta_1.tar.gz 
cig:~/download/agents# tar -xzf massim-serverMonitor-v0_1_beta_1.tar.gz 
cig:~/download/agents# tar -xzf massim-server-v0_1_beta_1.tar.gz 

cig:~/download/agents# ls
massim-demoAgent-v0_1_beta_1
massim-serverMonitor-v0_1_beta_1.tar.gz
massim-demoAgent-v0_1_beta_1.tar.gz  massim-server-v0_1_beta_1
massim-serverMonitor-v0_1_beta_1     massim-server-v0_1_beta_1.tar.gz

cig:~/download/agents# vim massim-server-v0_1_beta_1/startServer

edit the line
name=192.168.123.100

with the real server name (or IP) where the simulation server will run.

cig:~/download/agents# vim ./massim-serverMonitor-v0_1_beta_1/startServerMonitor 

again edit the line with the variable "name" to the server name (or IP)
to the server where the server runs (you can run server monitor from a
different computer than the one where the simulation server).

now open two additional terminal windows

WINDOW 1:
cig:~/download/agents# cd massim-serverMonitor-v0_1_beta_1
cig:~/download/agents/massim-serverMonitor-v0_1_beta_1# ./startServerMonitor 
Lauching ServerMonitor
#################################################################
# Starting Massim-ServerMonitor                                 #
#                                                               #
# host = <YOUR HOST>, port = 1099, service = simulation
# #
# sleeptime = 1000                                              #
# To leave this programm enter "quit" and press the enter-key   #
#################################################################

Currently no simulation running on cig.in.tu-clausthal.de 1099...

########################################

Sleeping 10 seconds...

########################################

...
Now server monitor will refresh every 10 seconds with the updated
simulation server status. You can change the refresh rate in the
startServerMonitor script according to the corresponding README file.

WINDOW 2:
cig:~/download/agents# cd massim-server-v0_1_beta_1/
cig:~/download/agents/massim-server-v0_1_beta_1# ./startServer 
./massim/simulation/competition2006/bin:massim/framework/bin:massim/agent/bin:massim/visualization/davidmainzer/bin:massim/visualization/davidmainzer/batik/lib/batik-svg-dom.jar:massim/visualization/davidmainzer/batik/lib/batik-xml.jar:massim/visualization/davidmainzer/batik/lib/batik-css.jar:massim/visualization/davidmainzer/batik/lib/batik-dom.jar:massim/visualization/davidmainzer/batik/lib/batik-ext.jar:massim/visualization/davidmainzer/batik/lib/batik-util.jar:
Launching RMI Registry
Please run the agents
Launching Server
20060104 21:35:07.401 1 massim.server.Server.<init>:117  Server launched
20060104 21:35:07.481 1 massim.connection.InetSocketListener.<init>:11
InetSocketListener created. Set to port 12300 with backlog 10 node:[match: null]
20060104 21:35:07.670 7
massim.connection.InetSocketListener.waitForIncomingSocket:23
20060104 21:35:07.765 7
massim.connection.InetSocketListener.waitForIncomingSocket:26  waitingt
for connection...

...
Server now waits for agents to connect. Simulation won't start until
either the tournament initial phase is over, or you press a key in the
console of simulation server.

Let's start agents.

WINDOW 3:
cig:~/download/agents# cd massim-demoAgent-v0_1_beta_1/
cig:~/download/agents/massim-demoAgent-v0_1_beta_1# ./startAgents 

Lauching agents
cig:~/download/agents/massim-demoAgent-v0_1_beta_1# Server -> Agent:
<?xml version="1.0" encoding="UTF-8"?><message
type="auth-response"><authentication result="ok"/></message>
Server -> Agent:
<?xml version="1.0" encoding="UTF-8"?><message
type="auth-response"><authentication result="ok"/></message>
Server -> Agent:
<?xml version="1.0" encoding="UTF-8"?><message
type="auth-response"><authentication result="ok"/></message>
---#-#-#-#-#-#-- login --#-#-#-#-#-#---
Server -> Agent:
<?xml version="1.0" encoding="UTF-8"?><message
type="auth-response"><authentication result="ok"/></message>
---#-#-#-#-#-#-- login --#-#-#-#-#-#---
...

Now you can see all 8 agents of 2 teams to connect and login to the
server. In WINDOW 2 you can see their authentication requests and in the
WINDOW 3 you see responses they got from the server.

Now we can start the tournament. Press RETURN in the WINDOW 2.

The first simulation of the tournament started. In WINDOW 1 (server
monitor) you can see current status of the simulation. If you want to
change the refresh rate of server monitor, edit the monitor starting
script (according to its README file).

In the WINDOW 2, the server is logging steps of simulation. This output
is not really usefull for you.

The WINDOW 3 (agents) show you all messages agents send to server and
its responses. Taking a close look into these messages can help you to
build and debug your agents.




Good luck with agents development!!!
