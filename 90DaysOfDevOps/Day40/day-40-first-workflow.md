#### Your First GitHub Actions Workflow



##### Workflow YAML



```yaml

name: Hello Workflow



on:

&#x20; push:



jobs:

&#x20; greet:

&#x20;   runs-on: ubuntu-latest



&#x20;   steps:

&#x20;     - name: Checkout repository

&#x20;       uses: actions/checkout@v4



&#x20;     - name: Print hello message

&#x20;       run: echo "Hello from GitHub Actions!"



&#x20;     - name: Print current date and time

&#x20;       run: date



&#x20;     - name: Print branch name

&#x20;       run: echo "Branch name is ${{ github.ref\_name }}"



&#x20;     - name: List files in repository

&#x20;       run: ls -la



&#x20;     - name: Print runner operating system

&#x20;       run: echo "Runner OS is $RUNNER\_OS"

Workflow Anatomy

on:



Defines the event that triggers the workflow.

In this case, every push starts the pipeline.



jobs:



Contains the list of jobs that will run in the workflow.

A workflow can have one or more jobs.



runs-on:



Specifies the operating system or runner environment where the job will execute.



steps:



Defines the sequence of actions or commands inside a job.



uses:



Uses a prebuilt GitHub Action.

Here, actions/checkout@v4 checks out the repository code onto the runner.



run:



Executes a shell command directly on the runner.



name: (on a step)



Gives a readable label to a step so it is easy to understand in the Actions tab.



What I Observed



The workflow started automatically after pushing code.



GitHub Actions created a runner in the cloud and executed each step one by one.



A successful pipeline run shows a green checkmark.



When I added a failing step, the workflow stopped at that step and showed a red failed status.



What a Failed Pipeline Looks Like



A failed pipeline shows a red cross in the Actions tab.

Clicking the failed job shows which step failed and the exact error message in the logs.

This helps identify what went wrong and where it happened.



Screenshot



Add your screenshot of the first green pipeline run here.



What I Learned



GitHub Actions workflows are written in YAML and stored in .github/workflows/.



Every push can automatically trigger a pipeline in the cloud.



Pipeline logs make it easier to understand both successful and failed runs.

