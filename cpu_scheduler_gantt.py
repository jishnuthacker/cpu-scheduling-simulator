# cpu_scheduler_gantt.py

def print_table(title, processes, headers):
    print(f"\n=== {title} ===")
    print(" ".join(h.ljust(6) for h in headers))
    for p in processes:
        print(" ".join(str(p[h]).ljust(6) for h in headers))
    avg_wt = sum(p['WT'] for p in processes) / len(processes)
    avg_tat = sum(p['TAT'] for p in processes) / len(processes)
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")


def fcfs(processes):
    time = 0
    gantt = []
    for p in sorted(processes, key=lambda x: x['AT']):
        if time < p['AT']:
            time = p['AT']
        p['CT'] = time + p['BT']
        p['TAT'] = p['CT'] - p['AT']
        p['WT'] = p['TAT'] - p['BT']
        gantt.append((p['PID'], time, p['CT']))
        time = p['CT']
    print_table("FCFS Scheduling", processes, ['PID', 'AT', 'BT', 'CT', 'TAT', 'WT'])
    print_gantt(gantt)


def sjf(processes):
    n = len(processes)
    time = 0
    gantt = []
    completed = 0
    ready = []
    proc = processes.copy()
    while completed < n:
        ready = [p for p in proc if p['AT'] <= time and 'done' not in p]
        if not ready:
            time += 1
            continue
        p = min(ready, key=lambda x: x['BT'])
        start = time
        time += p['BT']
        p['CT'] = time
        p['TAT'] = p['CT'] - p['AT']
        p['WT'] = p['TAT'] - p['BT']
        p['done'] = True
        gantt.append((p['PID'], start, time))
        completed += 1
    print_table("SJF Scheduling", processes, ['PID', 'AT', 'BT', 'CT', 'TAT', 'WT'])
    print_gantt(gantt)


def priority_scheduling(processes):
    n = len(processes)
    time = 0
    completed = 0
    gantt = []
    while completed < n:
        ready = [p for p in processes if p['AT'] <= time and 'done' not in p]
        if not ready:
            time += 1
            continue
        p = min(ready, key=lambda x: x['PR'])
        start = time
        time += p['BT']
        p['CT'] = time
        p['TAT'] = p['CT'] - p['AT']
        p['WT'] = p['TAT'] - p['BT']
        p['done'] = True
        gantt.append((p['PID'], start, time))
        completed += 1
    print_table("Priority Scheduling", processes, ['PID', 'AT', 'BT', 'PR', 'CT', 'TAT', 'WT'])
    print_gantt(gantt)


def round_robin(processes, quantum):
    from collections import deque
    queue = deque()
    gantt = []
    time = 0
    proc = [p.copy() for p in processes]
    for p in proc:
        p['RT'] = p['BT']

    visited = set()
    while True:
        available = [p for p in proc if p['AT'] <= time and p['PID'] not in visited]
        for p in available:
            queue.append(p)
            visited.add(p['PID'])
        if not queue:
            if all(p['RT'] == 0 for p in proc):
                break
            time += 1
            continue
        p = queue.popleft()
        start = time
        if p['RT'] <= quantum:
            time += p['RT']
            p['RT'] = 0
            p['CT'] = time
        else:
            time += quantum
            p['RT'] -= quantum
        gantt.append((p['PID'], start, time))
        available = [x for x in proc if x['AT'] <= time and x['PID'] not in visited]
        for x in available:
            queue.append(x)
            visited.add(x['PID'])
        if p['RT'] > 0:
            queue.append(p)

    for p in proc:
        p['TAT'] = p['CT'] - p['AT']
        p['WT'] = p['TAT'] - p['BT']

    print_table("Round Robin Scheduling", proc, ['PID', 'AT', 'BT', 'CT', 'TAT', 'WT'])
    print_gantt(gantt)


def srtf(processes):
    n = len(processes)
    time = 0
    gantt = []
    proc = [p.copy() for p in processes]
    for p in proc:
        p['RT'] = p['BT']
    completed = 0
    last_pid = None
    start_time = time

    while completed < n:
        ready = [p for p in proc if p['AT'] <= time and p['RT'] > 0]
        if not ready:
            time += 1
            continue
        p = min(ready, key=lambda x: x['RT'])
        if last_pid != p['PID']:
            if last_pid is not None:
                gantt.append((last_pid, start_time, time))
            start_time = time
            last_pid = p['PID']
        p['RT'] -= 1
        time += 1
        if p['RT'] == 0:
            p['CT'] = time
            completed += 1
    gantt.append((last_pid, start_time, time))

    for p in proc:
        p['TAT'] = p['CT'] - p['AT']
        p['WT'] = p['TAT'] - p['BT']

    print_table("SRTF Scheduling", proc, ['PID', 'AT', 'BT', 'CT', 'TAT', 'WT'])
    print_gantt(gantt)


def print_gantt(gantt):
    print("\nGantt Chart:")
    chart = ""
    for (pid, start, end) in gantt:
        chart += f"| {pid} ({start}-{end}) "
    print(chart + "|")


def main():
    n = int(input())
    processes = []
    for i in range(1, n + 1):
        pid = f"P{i}"
        at = int(input())
        bt = int(input())
        pr = int(input())
        processes.append({'PID': pid, 'AT': at, 'BT': bt, 'PR': pr})
    quantum = int(input())

    fcfs([p.copy() for p in processes])
    sjf([p.copy() for p in processes])
    priority_scheduling([p.copy() for p in processes])
    round_robin([p.copy() for p in processes], quantum)
    srtf([p.copy() for p in processes])


if __name__ == "__main__":
    main()
