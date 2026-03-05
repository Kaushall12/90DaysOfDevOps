#### Git Reset vs Revert \& Branching Strategies



---



##### 1\. Git Reset



Difference between --soft, --mixed and --hard



git reset --soft HEAD~1  

Moves HEAD back one commit but keeps all changes staged.



git reset --mixed HEAD~1  

Moves HEAD back one commit and unstages the changes but keeps them in the working directory.



git reset --hard HEAD~1  

Moves HEAD back one commit and completely deletes the changes from working directory.



---



Which reset is destructive?



git reset --hard



Because it permanently deletes commits and working changes.



---



When to use each reset



--soft  

Used when you want to modify the last commit but keep changes staged.



--mixed  

Used when you want to redo the commit but review files again.



--hard  

Used when you want to completely discard changes.



---



Should you use reset on pushed commits?



No.



Reset rewrites history. If the commit is already pushed and others pulled it, resetting will break the shared history.



---



##### 2\. Git Revert



What happens when you revert commit Y?



Git creates a new commit that reverses the changes made in commit Y.



The original commit still remains in history.



Example:



A → B → C → D



After revert B:



A → B → C → D → E



E is the commit that undoes B.



---



How is revert different from reset?



Reset removes commits from history.



Revert creates a new commit that cancels the changes.



---



Why is revert safer?



Because it preserves commit history and does not rewrite it.



This makes it safe for shared repositories.



---



When to use revert vs reset



Use reset:



For local commits that have not been pushed.



Use revert:



For commits already pushed to shared repositories.



---



##### 3\. Reset vs Revert Summary



| Feature | git reset | git revert |

|-------|------|------|

| What it does | Moves branch pointer backward | Creates a commit that reverses changes |

| Removes commit from history | Yes | No |

| Safe for shared branches | No | Yes |

| Typical use | Local mistake fix | Undo pushed commits |



---



##### 4\. Branching Strategies



---



GitFlow



Structure:



main → production branch  

develop → integration branch  

feature → new features  

release → release preparation  

hotfix → urgent fixes



Flow:



main

&nbsp;│

develop

&nbsp;├─ feature/login

&nbsp;├─ feature/payment

&nbsp;└─ release



Pros



Good for structured releases

Clear separation of work



Cons



Complex

Too many branches for small teams



Used in:



Large enterprise teams



---



GitHub Flow



Structure:



main

&nbsp;└─ feature branches



Workflow:



1\. Create branch from main

2\. Make changes

3\. Open pull request

4\. Review

5\. Merge into main



Pros



Simple

Fast development



Cons



Less control for scheduled releases



Used in:



Most GitHub projects.



---



Trunk-Based Development



Structure:



main (trunk)



Developers commit directly or with very short-lived branches.



main

&nbsp;├─ small feature

&nbsp;├─ bug fix

&nbsp;└─ improvement



Pros



Very fast integration

Works well with CI/CD



Cons



Requires strong automated testing.



Used in:



Google

Facebook

Modern DevOps teams.



---



##### 5\. Strategy Comparison



Startup shipping fast



Trunk-Based Development or GitHub Flow.



Large team with scheduled releases



GitFlow.



Open source example



Kubernetes → GitHub Flow style with feature branches and pull requests.



---



Key Takeaways



\- reset rewrites history

\- revert safely undoes changes

\- never reset pushed commits

\- branching strategy depends on team size and release process

