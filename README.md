Trivial statistical utils callable from bash
============================================

Examples:
---------


echo "1 2 3 4 5 3 2 1 2 1 2 3 4 5"| basestats.py

$ echo "1 2 3 4 5 3 2 1 2 1 2 3 4 5"| basestats.py

Card  :  14
Min   :  1
Median:  2.5
Mean  :  2.71428571429
Max   :  5
Std   :  1.33248272187
Var   :  1.77551020408


$ echo "1 2 3 4 5 3 2 1 2 1 2 3 4 5"| hist.py --nbins 50 --titlex "Time to generate key [s]" --xlabel "Time [s]" --ylabel "Rate [observations]" --saveas "time-to-generate-key" &

# Output: Graph (requires X-Server connection)

# or more realistic: 
# cat $data | grep Deltas | awk '{print $4}' | hist.py --nbins 50 --titlex "Time to generate key [s]" --xlabel "Time [s]" --ylabel "Rate [observations]" --saveas "time-to-generate-key" &