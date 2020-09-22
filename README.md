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
  - [ ] Root out players who aren't RBs

## Analytics ##

### How has NFL QB fantasy value changed over time? ###

The standard fantasy scoring system for QBs are as follows:

#### QB Fantasy Scoring System ####
1pt for every 25 passing yards
4pts for every passing TD
-2pts for every INT thrown
6pts for every running TD
1pt for every 10 rushing yards

Using the scoring rubric above 
![QB](https://github.com/nasriv/NFLFantasyAnalysis/blob/master/images/QBpoints.jpg "QB Fantasy Points")
