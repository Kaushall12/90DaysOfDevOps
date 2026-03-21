#### Triggers \& Matrix Builds



PR Trigger



Workflow runs when a pull request is opened or updated against main branch.



Scheduled Trigger



Runs every day at midnight using cron:

0 0 \* \* \*



Cron for every Monday at 9 AM:

0 9 \* \* 1



Manual Trigger



Allows running workflow manually with user input.



Matrix Build



Runs jobs across multiple environments.



Total combinations:

2 OS × 3 Python versions = 6  

Excluded 1 → Final = 5 jobs



Fail Fast



fail-fast: true → stops all jobs on first failure  

fail-fast: false → continues all jobs even if one fails  



What I Learned



1\. Workflows can be triggered automatically, manually, or on schedule.

2\. Matrix builds allow parallel execution across multiple environments.

3\. Fail-fast controls how pipeline behaves on failure.

