#### GitHub CLI (gh)



---



##### 1\. Installing and Authenticating



Install GitHub CLI



Ubuntu / WSL example:



sudo apt install gh



Verify installation:



gh --version



---



Authenticate with GitHub



gh auth login



Steps usually include:



1\. Choose GitHub.com

2\. Choose HTTPS

3\. Authenticate via browser or token



Verify login:



gh auth status



---



Authentication Methods Supported



\- Browser-based OAuth login

\- Personal Access Token (PAT)

\- SSH authentication



---



##### 2\. Working with Repositories



Create a repository from terminal



gh repo create test-gh-cli --public --source=. --remote=origin



---



Clone repository



gh repo clone owner/repo



Example:



gh repo clone octocat/Hello-World



---



View repository details



gh repo view



---



List your repositories



gh repo list



---



Open repository in browser



gh repo view --web



---



Delete repository



gh repo delete owner/repo



Example:



gh repo delete kaushal/test-gh-cli

