# CPU Scheduling Simulator (TUI)

This project is a command-line utility for simulating five common CPU scheduling algorithms. It is designed as an interactive tool for learning and comparing scheduling concepts in an Operating Systems course.

The tool features an interactive **Text User Interface (TUI)** built with Bash and the `dialog` utility, with the core scheduling logic implemented in Python 3.

## Demo

Watch the interactive TUI in action and see the final output results.

<p align="center">
  <img src="https://github.com/jishnuthacker/cpu-scheduling-simulator/raw/main/Video%20Project.gif" alt="Simulator Demo GIF" width="800"/>
</p>

-----

## Features

### 1\. Interactive TUI (`os_project1.sh`)

The user interface uses the Linux `dialog` command to offer a polished, step-by-step experience directly in the terminal.

* **Algorithm Selection:** Choose from 5 individual algorithms (FCFS, SJF, Priority, Round Robin, SRTF) or select **"Compare All 5 Algorithms"** for a full batch comparison.
* **Streamlined Input:** Collects all process data (PID, Arrival Time, Burst Time, Priority) from a single, clean input box.
* **Custom Quantum:** Automatically prompts for the Time Quantum when Round Robin (RR) or the "All Algorithms" mode is selected.

### 2\. Core Scheduling Engine (`cpu_scheduler_gantt.py`)

The Python script contains robust, time-step-based logic for both non-preemptive and preemptive algorithms.

* **Five Algorithms Simulated:**
    * **F**irst **C**ome, **F**irst **S**erved (FCFS)
    * **S**hortest **J**ob **F**irst (SJF - Non-preemptive)
    * **P**riority (Non-preemptive, lower number = higher priority)
    * **R**ound **R**obin (RR - Preemptive)
    * **S**hortest **R**emaining **T**ime **F**irst (SRTF - Preemptive SJF)
* **Performance Metrics:** Calculates and displays **Completion Time (CT)**, **Turnaround Time (TAT)**, **Waiting Time (WT)**, and **Average TAT/WT**.
* **Gantt Chart:** Generates a text-based Gantt chart to visualize the execution timeline of the processes for each run.
* **Data Class Usage:** Uses Python's `dataclass` for clean and effective process state management.

-----

## Getting Started

<!-- THIS IS THE SECTION YOU ASKED FOR -->
### Prerequisites

This project requires a Unix-like environment (Linux, macOS, WSL) with the following tools installed:

1.  **Bash:** Standard shell.
2.  **Python 3:** Required to execute the scheduling logic in `cpu_scheduler_gantt.py`.
3.  **`dialog` utility:** Used by the `os_project1.sh` shell script for the interactive TUI.
    * *Installation (Debian/Ubuntu/Kali):* `sudo apt install dialog`
<!-- END OF PREREQUISITES SECTION -->

### Execution

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/jishnuthacker/cpu-scheduling-simulator](https://github.com/jishnuthacker/cpu-scheduling-simulator)
    cd Os_project
    ```
2.  **Make the script executable:**
    ```bash
    chmod +x os_project1.sh
    ```
3.  **Run the script:**
    ```bash
    ./os_project1.sh
    ```
4.  **Follow the Prompts:** The TUI will first ask for the process data, then guide you through selecting an algorithm and entering the necessary parameters (like Quantum).

### Input Format

When prompted for process data, use the following semicolon-separated format:
`PID-AT,BT,PR;PID-AT,BT,PR;...`

**Example Input:** `P1-0,5,0;P2-2,3,0;P3-4,2,0`
| Field | Description |
| :--- | :--- |
| **PID** | Process ID (e.g., P1) |
| **AT** | Arrival Time (Integer) |
| **BT** | Burst Time (Integer) |
| **PR** | Priority (Integer, lower number = higher priority) |

-----

## Project Structure

| File Name | Description |
| :--- | :--- |
| **`os_project1.sh`** | **The TUI Interface.** Manages user input via `dialog`, handles menus, collects quantum values, and runs the Python simulation script. |
| **`cpu_scheduler_gantt.py`** | **The Core Engine.** Contains the Python implementation of all five scheduling algorithms, calculation logic, and output formatting. |
| **`result.txt`** | *Temporary file* (now auto-managed) used to capture the output of the Python script before it is filtered and displayed by the TUI. |

-----

## ⚙️ Example Run (FCFS)

### Inputs

Using the example input: `P1-0,5,0;P2-2,3,0;P3-4,2,0`

| Process ID | Arrival Time (AT) | Burst Time (BT) | Priority (PR) |
| :---: | :---: | :---: | :---: |
| P1 | 0 | 5 | 0 |
| P2 | 2 | 3 | 0 |
| P3 | 4 | 2 | 0 |

### Calculated Results (FCFS)

| PID | AT | BT | CT | TAT | WT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| P1 | 0 | 5 | 5 | 5 | 0 |
| P2 | 2 | 3 | 8 | 6 | 3 |
| P3 | 4 | 2 | 10 | 6 | 4 |

| Average Metric | Value |
| :--- | :--- |
| **Average Waiting Time** | 2.33 |
| **Average Turnaround Time** | 5.67 |

### Gantt Chart (FCFS)

`| P1 (0-5) | P2 (5-8) | P3 (8-10) |`

-----

## Contribution

Feel free to fork the repository, open issues, or submit pull requests to improve the project! Any suggestions for optimizing the algorithms or enhancing the TUI are welcome.

### Contact

Created by **Jishnu Thacker**

* **GitHub:** [https://github.com/jishnuthacker](https://github.com/jishnuthacker)
* **Email:** jishnuthacker@gmail.com
