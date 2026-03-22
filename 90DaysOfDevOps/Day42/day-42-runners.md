#### Runners: GitHub-Hosted \& Self-Hosted



##### GitHub Hosted Runners



These are machines provided and managed by GitHub.

They automatically spin up when a workflow runs and are destroyed after execution.



##### Self Hosted Runner



I set up my own runner on my machine.

It stays online and executes jobs assigned by GitHub.



##### Pre-installed Tools



GitHub runners already include:

\- Docker

\- Python

\- Node.js

\- Git



This saves setup time and speeds up pipelines.



##### GitHub vs Self-Hosted



| Feature | GitHub-Hosted | Self-Hosted |

|--------|--------------|------------|

| Managed by | GitHub | User |

| Cost | Free (limited) | Depends on your infra |

| Tools | Pre-installed | You install |

| Use case | Quick CI/CD | Custom environments |

| Security | Safer | You manage risks |



##### What I Learned



1\. Runners are machines that execute CI/CD jobs.

2\. GitHub-hosted runners are temporary and managed by GitHub.

3\. Self-hosted runners allow full control over environment and hardware.

