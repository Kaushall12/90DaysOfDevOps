#### YAML Basics



YAML Files



\### person.yaml

```yaml

name: Kaushal Patel

role: DevOps Learner

experience\_years: 0

learning: true



tools:

&#x20; - Docker

&#x20; - Git

&#x20; - GitHub Actions

&#x20; - AWS

&#x20; - Nginx



hobbies: \[coding, learning, cricket]





\###server.yaml

```yaml



server:

&#x20; name: web-server-1

&#x20; ip: 192.168.1.10

&#x20; port: 8080



database:

&#x20; host: localhost

&#x20; name: app\_db

&#x20; credentials:

&#x20;   user: admin

&#x20;   password: secret123



startup\_script\_literal: |

&#x20; echo "Starting application..."

&#x20; sudo systemctl start nginx

&#x20; sudo systemctl start docker



startup\_script\_folded: >

&#x20; echo "Starting application..."

&#x20; sudo systemctl start nginx

&#x20; sudo systemctl start docker

What I Learned



YAML depends heavily on proper indentation and spaces must be used instead of tabs.



Lists in YAML can be written in block style using - or inline style using \[item1, item2].



The | block style preserves line breaks, while > folds multiple lines into a single line.



Notes

Two ways to write a list in YAML



Block style



Inline style



Difference between | and >



| preserves newlines exactly as written



> folds lines into a single paragraph



What is wrong with Block 2?



Broken block:



name: devops

tools:

\- docker

&#x20; - kubernetes



Problem:



Indentation is inconsistent



\- kubernetes is incorrectly indented under the first list item



Correct version:



name: devops

tools:

&#x20; - docker

&#x20; - kubernetes

