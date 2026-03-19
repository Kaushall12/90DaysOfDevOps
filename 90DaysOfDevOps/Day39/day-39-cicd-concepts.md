#### What is CI/CD?



##### 1\. The Problem



Imagine a team of 5 developers pushing code to the same repository and deploying manually to production.



What can go wrong?

\- Code conflicts between developers

\- One developer may overwrite another's changes

\- Bugs may reach production because testing is skipped

\- Manual deployment steps may be missed

\- Different environments can cause unexpected issues

\- Rollbacks become difficult and stressful



What does "it works on my machine" mean?

This means the code works correctly on the developer’s local system but fails on another machine or server because the environments are different.  

It is a real problem because production systems need consistency, not personal machine-specific setups.



How many times a day can a team safely deploy manually?

Usually only a few times, because manual deployments take time, require coordination, and increase the risk of mistakes.



\---



##### 2\. CI vs CD



Continuous Integration (CI)

Continuous Integration is the practice of frequently merging code changes into a shared repository.  

Each push or pull request triggers automated checks such as build, linting, and tests to catch issues early.



Example: 

A developer pushes code to GitHub, and GitHub Actions automatically runs tests.



Continuous Delivery

Continuous Delivery means code is automatically built, tested, and prepared for release, but the final deployment to production usually needs manual approval.



Example:  

A team’s pipeline builds the app, runs tests, and creates a deployable package for staging or production approval.



Continuous Deployment

Continuous Deployment goes one step further than Continuous Delivery.  

If all tests pass, code is automatically deployed to production without manual approval.



Example:  

A SaaS product automatically deploys every successful merge to the main branch directly to production.



\---



##### 3\. Pipeline Anatomy



Trigger

An event that starts the pipeline, such as a push, pull request, or manual run.



Stage

A logical phase in the pipeline, such as build, test, or deploy.



Job

A unit of work inside a stage. A pipeline may have one or more jobs.



Step

A single command or action inside a job.



Runner

The machine or environment that executes pipeline jobs.



Artifact

A file or output produced by a job, such as a build package, report, or Docker image.



\---



##### 4\. Pipeline Diagram



Text-based Pipeline Diagram



```text

Developer Pushes Code to GitHub

&#x20;             │

&#x20;             ▼

&#x20;       Trigger Pipeline

&#x20;             │

&#x20;             ▼

&#x20;       Stage 1: Build

&#x20;     - Install dependencies

&#x20;     - Build application

&#x20;             │

&#x20;             ▼

&#x20;       Stage 2: Test

&#x20;     - Run unit tests

&#x20;     - Run lint checks

&#x20;             │

&#x20;             ▼

&#x20;    Stage 3: Package

&#x20;     - Build Docker image

&#x20;     - Store artifact

&#x20;             │

&#x20;             ▼

&#x20;     Stage 4: Deploy

&#x20;     - Deploy to staging server

&#x20;             │

&#x20;             ▼

&#x20;        Verify Deployment





##### 

##### 5\. Explore in the Wild



I explored the FastAPI GitHub repository and checked one workflow file in .github/workflows. The repository has GitHub Actions workflows for automated checks and testing. GitHub Actions itself is a CI/CD platform that can automate build, test, and deployment pipelines.



What triggers it?



The workflow is triggered when relevant source files or workflow files change, based on path filters in the workflow. The visible workflow file includes a changes job that uses dorny/paths-filter to decide whether source-related paths were modified.



How many jobs does it have?



From the visible portion of the FastAPI workflow file, it clearly has at least one job named changes. There may be more jobs below in the same file, but the snippet confirms at least that one job.



What does it do? (best guess)



It checks whether relevant files changed and then likely uses that information to decide whether later testing-related jobs should run. That helps avoid unnecessary work in CI.





##### 6\. What I Learned



CI/CD is a practice that automates software build, test, and deployment workflows.



CI helps catch issues early, while Delivery and Deployment focus on releasing code safely.



Pipelines reduce manual errors and make software releases faster and more reliable.

