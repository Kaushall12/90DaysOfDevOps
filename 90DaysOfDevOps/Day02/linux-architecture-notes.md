##### Linux Architecture, Processes, and systemd



###### &nbsp;1. Core Components of Linux



&nbsp;Kernel

\- The kernel is the \*\*core of Linux\*\*

\- It manages:

&nbsp; - CPU scheduling

&nbsp; - Memory management

&nbsp; - Device drivers

&nbsp; - Process control

\- Applications do not access hardware directly — they go through the kernel



&nbsp;User Space

\- Where "users and applications" run

\- Includes:

&nbsp; - Shell (bash)

&nbsp; - System utilities (ls, ps, top)

&nbsp; - Applications (nginx, docker, etc.)

\- User space communicates with the kernel using system calls



&nbsp;Init / systemd

\- The first process started by the kernel 

\- Responsible for:

&nbsp; - Starting services

&nbsp; - Managing system boot

&nbsp; - Handling service failures







###### &nbsp;2. Process Creation and Management



\- Every process has a \*\*PID (Process ID)\*\*

\- New processes are created using:

&nbsp; - `fork()` → creates a copy of a process

&nbsp; - `exec()` → replaces it with a new program

\- The kernel schedules processes using time-sharing



&nbsp;Process States

\- \*\*Running (R): Currently using CPU

\- \*\*Sleeping (S): Waiting for input or event

\- \*\*Uninterruptible Sleep (D): Waiting for I/O

\- \*\*Stopped (T): Paused manually or by signal

\- \*\*Zombie (Z): Finished execution but not cleaned up by parent







###### &nbsp;3. systemd and Why It Matters



\- systemd is the service manager for modern Linux systems

\- Uses units (service, socket, timer, target)

\- Key benefits:

&nbsp; - Parallel service startup (faster boot)

&nbsp; - Automatic service restart

&nbsp; - Centralized logging with 'journalctl'



Example:

\- If a web service crashes, systemd can restart it automatically







###### &nbsp;4. Daily Linux Commands (DevOps Use)



\- `ps aux` → View running processes

\- `top` / `htop` → Monitor CPU \& memory usage

\- `systemctl status service-name` → Check service health

\- `journalctl -u service-name` → View service logs

\- `kill -9 PID` → Stop a stuck process





###### &nbsp;5. Why This Matters for DevOps



\- Most production servers run on Linux

\- Understanding processes and systemd helps to:

&nbsp; - Debug crashed services

&nbsp; - Identify performance issues

&nbsp; - Handle incidents confidently



Strong Linux fundamentals = faster problem solving.



