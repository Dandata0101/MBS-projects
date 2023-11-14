# Instructions for our Python and Data Management Projects

## FIFA Data
Q1. Work on the FIFA dataset: FIFA.db (9 pts)
The FIFA dataset contains seven tables: Attacking, Club, Defending, Goalkeeping, Movement,
Player and Skill.

The relationship between these seven tables is summarised below:
* pid in Player is also the foreign key to Attacking, Defending, Movement, Goalkeeping, and Skill.
* club_team_id in Player is the foreign key to Club

