#### Advanced Git Notes



---



##### 1\. Git Merge



What is a fast-forward merge?



A fast-forward merge happens when the target branch has no new commits since the branch was created.  

Git simply moves the branch pointer forward instead of creating a new merge commit.



Example:



main → A  

feature → A → B → C  



After merge:



main → A → B → C



No extra commit is created.





---



When does Git create a merge commit?



Git creates a merge commit when both branches have diverged (both have new commits).



Example:



main → A → D  

feature → A → B → C  



After merge:



main → A → D → M  

&nbsp;             ↘ B → C



Git creates a merge commit \*\*M\*\* to combine both histories.





---



What is a merge conflict?



A merge conflict happens when the same line of a file is modified in two branches.



Example conflict marker:



<<<<<<< HEAD

main branch code

=======

feature branch code

>>>>>>> feature



You must manually resolve the conflict and commit the fix.



---



##### 2\. Git Rebase



What does rebase do?



Rebase moves your branch commits onto another base commit.



Instead of merging histories, Git \*\*replays your commits on top of the latest branch\*\*.



Example:



Before rebase:



main → A → D  

feature → A → B → C  



After rebase:



main → A → D  

feature → A → D → B → C



---



How is history different from merge?



Merge keeps branch history intact with a merge commit.



Rebase creates a \*\*clean linear history\*\* without merge commits.



---



Why should you not rebase shared commits?



Rebasing rewrites commit history.  

If others already pulled those commits, rebasing will cause conflicts and confusion.



Rule:



Never rebase commits that are already pushed to shared repositories.



---



When to use merge vs rebase?



Use merge:



\- When working on shared branches

\- When you want to preserve history



Use rebase:



\- To clean up local commit history

\- Before merging feature branches



---



##### 3\. Squash Merge



What does squash merge do?



Squash merge combines multiple commits into \*\*one single commit\*\* before merging.



Example:



feature branch commits:



A → B → C → D



After squash merge:



main → A → E



All changes are merged but only one commit is created.



---



When to use squash merge?



\- Small feature branches

\- Fixing many small commits

\- Keeping main history clean



---



Trade-off of squash merging



Pros:



Clean commit history.



Cons:



Loses detailed commit history of the feature branch.



---





##### 4\. Git Stash



What does git stash do?



git stash temporarily saves uncommitted changes so you can switch branches safely.



---



Difference between stash pop and stash apply



git stash apply



Applies stash but keeps it in stash list.



git stash pop



Applies stash and removes it from stash list.



---



Real-world use of stash



Example scenario:



You are working on a feature but need to urgently fix a bug in another branch.



You stash your changes:



git stash



Switch branch:



git switch main



After finishing:



git switch feature

git stash pop



---



##### 5\. Git Cherry Pick



What does cherry-pick do?



Cherry-pick applies a specific commit from another branch onto your current branch.



Example:



git cherry-pick <commit\_hash>



---



When to use cherry-pick?



\- Apply a hotfix to multiple branches

\- Copy a specific commit without merging the entire branch



---



Risks of cherry-picking



\- Duplicate commits

\- Confusing history

\- Possible conflicts



Cherry-pick should be used carefully.

