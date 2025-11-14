#!/bin/bash

# CPU Scheduling UI Script with smart input order

if ! command -v dialog &> /dev/null; then
    echo "dialog not found. Install it using: sudo apt install dialog"
    exit 1
fi

# Step 1: Choose Scheduling Algorithm
choice=$(dialog --menu "Select Scheduling Algorithm" 18 50 7 \
1 "FCFS" \
2 "SJF" \
3 "Priority" \
4 "Round Robin" \
5 "SRTF" \
6 "All Algorithms" \
--stdout)

# Step 2: Ask number of processes
num=$(dialog --inputbox "Enter number of processes:" 8 40 3 --stdout)
tmpfile=$(mktemp)

# Step 3: Collect process data
for ((i=1; i<=num; i++))
do
    pid="P$i"
    at=$(dialog --inputbox "Enter Arrival Time for $pid:" 8 40 0 --stdout)
    bt=$(dialog --inputbox "Enter Burst Time for $pid:" 8 40 5 --stdout)
    
    # Ask priority only if required
    if [ "$choice" -eq 3 ] || [ "$choice" -eq 6 ]; then
        pr=$(dialog --inputbox "Enter Priority for $pid:" 8 40 1 --stdout)
    else
        pr=0
    fi
    echo "$pid $at $bt $pr" >> "$tmpfile"
done

# Step 4: Ask quantum only if needed
if [ "$choice" -eq 4 ] || [ "$choice" -eq 6 ]; then
    quantum=$(dialog --inputbox "Enter Quantum Time (for Round Robin):" 8 40 2 --stdout)
else
    quantum=2
fi

# Step 5: Run Python code with inputs
python3 cpu_scheduler_gantt.py < <(
    echo "$num"
    while read pid at bt pr; do
        echo "$at"
        echo "$bt"
        echo "$pr"
    done < "$tmpfile"
    echo "$quantum"
) > result.txt

# Step 6: Show specific output
case "$choice" in
    1)
        awk '/=== FCFS Scheduling ===/{flag=1} /=== SJF Scheduling ===/{flag=0} flag' result.txt > output.txt
        ;;
    2)
        awk '/=== SJF Scheduling ===/{flag=1} /=== Priority Scheduling ===/{flag=0} flag' result.txt > output.txt
        ;;
    3)
        awk '/=== Priority Scheduling ===/{flag=1} /=== Round Robin Scheduling ===/{flag=0} flag' result.txt > output.txt
        ;;
    4)
        awk '/=== Round Robin Scheduling ===/{flag=1} /=== SRTF Scheduling ===/{flag=0} flag' result.txt > output.txt
        ;;
    5)
        awk '/=== SRTF Scheduling ===/{flag=1} END{if(flag)print ""} flag' result.txt > output.txt
        ;;
    6)
        cp result.txt output.txt
        ;;
esac

dialog --textbox output.txt 30 80
rm "$tmpfile"
