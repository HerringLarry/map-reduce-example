#Introduction
For my research I needed to learn about the MapReduce framework and how to implement it as well as the basics about Apache's Hadoop. This MapReduce implementation takes as input NYC taxicab data that has been preprocessed to include the zone in which the pickup occurred at the end of each row and assigns the zone and the date as the key and 1 as the value (not included in printed statement but implied and treated as such in reducer). The reducer than aggregates each identical zone and date value and totals the amount of pickups before returning the day in which the most pickups occurred for each separate zone. Scripts for preprocessing are included in repo. 

#How-To-Use
Although it can be run with Hadoop, configuring Hadoop can be a pain. Instead you can sign up for AWS (be careful to terminate your cluster when not in use) or just use the unix sort command. I use the bash code below:

                python ./mapper.py <  input.csv | sort | python ./reducer.py > output.csv

#Sample Output
            107, 2015-12-1, 6
            108, 2015-12-9, 15
            109, 2015-12-5, 3
            110, 2015-12-2, 2
            111, 2015-12-2, 2
            112, 2015-12-6, 1
            114, 2015-12-9, 1
            132, 2015-12-8, 23

#Dependencies
- csv 
- sys 
- string