# Game-Search-Adversarial-Search
Implemented a game tree algorithm for scheduling uber/lyft drivers to different areas of pickup so as to maximize their profit per day.
# Problem Description:
Uber and Lyft drivers must decide which regions of a city to drive around in each
day. Consider the following artificial scenarios involving how two ride-sharing
drivers (R1 and R2), who are roommates, decide which region of the city to drive
around in each day. Both of the roommates are interested in maximizing their
profit. For this scenario we assume that the roommates will make more money if
they choose not to pick up passengers in the same regions of the city.
Assume that each morning the two roommates take turns picking a region of the
map until the regions are split up between them. The roommates have a deal that
once a region of the map is picked; the person who picked it is the only one who has
the right to pick up new passengers in that region. For their first pick the
roommates can pick any region. After they choose a region any subsequent regions
they pick must be an adjacent regions (regions are adjacent if their borders touch)
to a region that they have already picked. If at some point a roommate can no
longer pick a region of the map that is adjacent to a region they already picked then
that player may not pick any other regions and the other roommate is free to pick
the rest of the regions that are adjacent to regions that the other roommate has
already picked. We signify the choice of the roommate who can no longer pick
regions with the symbol PASS. If neither roommate can make a choice the activity is
terminated with the rest of the regions left un-chosen.
We assume that each day at midnight profitability numbers are released by the ridesharing
companies and posted online in the Region Profitability List (RPL). This
list assigns numbers to each region that represents how profitable the region will be
for the day for drivers who have the rights to pick up passengers there. We assume
that all profitability factors are taken into account in these numbers and the number
is the best criterion to use for estimating how much money you will make if you
have rights to pick up passengers in that region. Therefore, each of the roommates
want to maximize the sum of the numbers corresponding to the regions they choose
in the picking activity, i.e.- their total score.
