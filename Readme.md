# Instructions for our Python and Data Management Projects

## FIFA Data
Q1. Work on the FIFA dataset: FIFA.db (9 pts)
The FIFA dataset contains seven tables: Attacking, Club, Defending, Goalkeeping, Movement,
Player and Skill.

The relationship between these seven tables is summarised below:
• pid in Player is also the foreign key to Attacking, Defending, Movement, Goalkeeping, and Skill.
• club_team_id in Player is the foreign key to Club

 (3 pts) A. Find the average defending rating of players in each club and display the result based
on the average defending rating, ranked from highest to lowest.

(3 pts) B. Find the names of players, their clubs, and their attacking ratings for players who
have an attacking rating greater than 80. Note: attacking rating = (crossing + finishing +
heading_accuracy + short_passing + volleys)/5

(3 pts) C. Find clubs (i.e., the id and the name of the club) where the average shooting rating is
higher than or equal to the average shooting rating of 'AC Milan’.