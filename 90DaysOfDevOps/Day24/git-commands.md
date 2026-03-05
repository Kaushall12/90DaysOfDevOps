#### Advanced Git



git merge <branch>

→ Merge branch into current branch



git rebase <branch>

→ Reapply commits on top of another branch



git merge --squash <branch>

→ Combine multiple commits into one during merge



git stash

→ Save uncommitted changes temporarily



git stash list

→ Show stashed changes



git stash pop

→ Apply and remove stash



git stash apply

→ Apply stash without removing it



git cherry-pick <commit>

→ Apply a specific commit from another branch



git log --oneline --graph --all

→ Visualize commit history



## Undoing Changes

git reset --soft HEAD~1
→ Undo last commit but keep changes staged

git reset --mixed HEAD~1
→ Undo last commit and unstage changes

git reset --hard HEAD~1
→ Undo last commit and delete changes

git revert <commit>
→ Create a commit that reverses changes

git reflog
→ Shows all recent HEAD movements (safety recovery tool)