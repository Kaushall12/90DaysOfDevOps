#### Git Branching Notes



##### What is a branch in Git?

A branch is a movable pointer to a commit. It allows parallel development without affecting the main codebase.



##### Why use branches instead of committing everything to main?

Branches isolate features, fixes, and experiments so the main branch stays stable.



##### What is HEAD?

HEAD is a pointer to the current branch and commit you are working on.



##### What happens when switching branches?

Git updates your working directory to match the selected branch’s latest commit.

Uncommitted changes may block switching if they conflict.





##### Branching



git branch

→ List branches



git branch <name>

→ Create branch



git switch <name>

→ Switch branch



git switch -c <name>

→ Create and switch



git branch -d <name>

→ Delete branch









##### Clone vs Fork



Clone → Copies a repository to your local machine.



Fork → Creates your own copy of someone else's repository on GitHub.



##### When to clone?

When you just want to use or explore a repo.



##### When to fork?

When you want to contribute to someone else's project.



##### How to keep fork updated?



git remote add upstream <original\_repo\_url>

git fetch upstream

git merge upstream/main

