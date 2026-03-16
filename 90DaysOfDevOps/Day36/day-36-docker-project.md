#### Docker Project



\## Project

Dockerized Flask Application with PostgreSQL.



\## Why this app

Flask apps are common in backend development and easy to containerize for learning Docker workflows.



\## Dockerfile Explanation



FROM python:3.11-slim AS builder  

Used as builder stage to install dependencies.



FROM python:3.11-alpine  

Minimal runtime image to keep container small.



USER appuser  

Runs container as non-root user for security.



\## Challenges



Database readiness – solved using healthchecks and depends\_on.



Environment configuration – solved using .env file.



\## Final Image Size



\~120MB



\## Docker Hub



https://hub.docker.com/r/kaushalpatel1284/flask-docker-project

