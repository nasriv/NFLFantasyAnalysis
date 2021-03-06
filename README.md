# NFLFantasyAnalysis

My passion for sports and data analytics led me to start developing a local historic sports database in order to identify trends and burning questions that keep me up at night. After watching a Monday Night Football game, the following question popped into my head..."NFL fantasy players typically draft QBs much later on in the draft than other positions (WR, RB, etc..)...why is that?"

This idea got me excited to develop a personal database of NFL statistics in order to answer some of these questions. Using Python I built a simple HTML parser which copied NFL QB statistics from https://www.pro-football-reference.com/. This data was extracted, tranformed and cleaned, by year and saved into various Excel CSV files for future use and in case the website eventually went down. 

### Data Pipeline ###
The formal steps I took to building this data pipeline is listed below:
1. Define html websites which have structured/semi-structured data
2. Build Python functions to loop through html websites based on a user defined range of playing years/seasons as well as clean and transform data as needed
3. Develop a "storage" function to lay the groundwork on how to compile the information in a csv format which is easy enough to later on build into a master database (SQL, etc).
4. Run data analytic studies to answer all my burning questions

![data pipeline image](https://github.com/nasriv/NFLFantasyAnalysis/blob/master/images/Database_flow.png "Data Pipeline")

#### ToDo List ####
- [x] Compile QB passing database
- [ ] Compile RB Rushing Database
  - [ ] Sort by player and fill in position where missing information exists
  - [ ] Filter out players who aren't RBs.
- [ ] Compile WR Database
- [ ] Establish SQL data schema to load master CSV files into for future querying and data storage methods

## Analytics ##

### How has NFL QB fantasy value changed over time? ###
Several QB's have entered and left the league without throwing a single pass, or only playing a select few number of games. This study will attempt to focus on NFL starting QBs who are defined as the first team player on the depth chart and plays more than any other QB on the teams roster. The NFL league has slowly shifted towards passing more and running less. This is evident when plotting the average number of pass attempts per game by a QB over the past 20 years (shown below).

<img src="https://github.com/nasriv/NFLFantasyAnalysis/blob/master/images/PassAttempt.jpg">

The more pass attempts there are, the more yards there should be, so again as expected there will be a high correlation between passing yards and attempts, again shown below.

<img src="https://github.com/nasriv/NFLFantasyAnalysis/blob/master/images/AttvYds.jpg">

Now taking our dataset and applying the traditional fantasy scoring system for QBs, we can generate a plot which will define the general QB fantasy point per game trend over the past 20 years and also give a hopeful fantasy player an average point baseline for what a QB will be expected to score per game. This is an important metric as it can help guide the player's drafting strategy and how to decide how much a QB is actually worth on their team. 

The standard fantasy scoring system for QBs is as follows:
* 1pt for every 25 passing yards
* 4pts for every passing TD
* -2pts for every INT thrown
* 6pts for every running TD
* 1pt for every 10 rushing yards

<img src="https://github.com/nasriv/NFLFantasyAnalysis/blob/master/images/QBpoints.jpg">

The chart shows the average points a QB scores per game has steadily increased over the years. This is again a reflection of the NFL's transition from a run heavy into a pass heavy league. More QBs are attempting more throws per game which has equated to a higher correlation of touchdowns scored and overall pass yards. Therefore, if you plan on drafting a QB in this year's league, you can hopefully expect them to score about 15 pts/game (which has been the rough average over the past 5 years).


