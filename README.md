# AWS Flask Visitor Counter

A full-stack cloud application that records visitor IPs and displays a live counter.

## Live Demo
**http://16.171.11.203:8080** 

## Architecture
- **Compute**: AWS EC2 (t2.micro, Amazon Linux 2023)
- **Database**: AWS RDS PostgreSQL
- **Backend**: Python Flask
- **Process Manager**: systemd (to auto start on boot)

## Features
- Records every visitor's IP address
- Persistent counter using RDS
- Auto-restarts on crash
- Professional frontend with gradient design

## Author
Prashant - Aspiring Cloud Engineer
