# Self-Healing Infrastructure with Prometheus, Alertmanager & Ansible

## Project Overview

This project demonstrates a self-healing infrastructure workflow that monitors an NGINX application, detects service failures, generates alerts, and automatically recovers the application using Ansible.

The project is implemented in a local Ubuntu environment using Docker containers.

## Objective

To reduce manual intervention during application failures by combining monitoring, alerting, and automated recovery.

## Technologies Used

- Ubuntu on WSL
- Docker
- NGINX
- Prometheus
- Blackbox Exporter
- Alertmanager
- Python Flask
- Ansible
- Shell scripting

## Architecture

```text
                 NGINX Application
                        |
                        v
                Blackbox Exporter
                        |
                        v
                   Prometheus
                        |
                 ApplicationDown
                        |
                        v
                  Alertmanager
                        |
                        v
                 Recovery Webhook
                  (Flask/Python)
                        |
                        v
                  Ansible Playbook
                        |
                        v
                Restart NGINX Container
                        |
                        v
                 Service Recovered
```

## Project Workflow

1. NGINX runs inside a Docker container.
2. Blackbox Exporter checks the application's HTTP availability.
3. Prometheus collects probe metrics and evaluates alert rules.
4. When the application becomes unavailable, Prometheus triggers the `ApplicationDown` alert.
5. Alertmanager sends the alert to the Flask recovery webhook.
6. The webhook executes the Ansible recovery playbook.
7. Ansible restarts the NGINX container and verifies that it is running.

## Key Features

- HTTP availability monitoring
- Application failure detection
- Prometheus alert rule
- Alertmanager webhook integration
- Automated NGINX container restart
- Ansible-based recovery
- Recovery verification
- Failure simulation and recovery testing

## Project Structure

```text
self-healing-infrastructure/
├── app/
├── ansible/
│   └── recovery.yml
├── alertmanager/
│   └── alertmanager.yml
├── blackbox/
├── prometheus/
│   ├── prometheus.yml
│   └── alerts.yml
├── recovery/
│   └── webhook.py
├── screenshots/
├── docs/
├── README.md
└── .gitignore
```

## Failure Detection and Recovery Test

The recovery workflow was tested by stopping the NGINX container.

Expected behavior:

- Prometheus detects the failed HTTP probe.
- The `ApplicationDown` alert is generated.
- Alertmanager sends the alert to the recovery webhook.
- The webhook executes the Ansible playbook.
- Ansible restarts the NGINX container.
- The playbook verifies that the container is running.

## Test Result

The automatic recovery test completed successfully.

Ansible play recap:

```text
ok=2
changed=1
unreachable=0
failed=0
```

The webhook received the `ApplicationDown` alert, executed the recovery playbook, and returned HTTP 200 for the alert request.

## Screenshots and Evidence

The `screenshots/` directory contains evidence of:

- NGINX application running
- Prometheus target status
- Failure detection
- Prometheus alert rule
- Automatic recovery execution

## Learning Outcomes

- Understanding monitoring and alerting workflows
- Configuring Prometheus scrape targets and alert rules
- Integrating Alertmanager with a webhook
- Automating recovery using Ansible
- Testing service failure and recovery
- Working with Docker containers and networking

## Limitations

This is a local learning and demonstration project. The Flask webhook uses a development server and is not intended for production deployment.

The recovery webhook has access to the Docker socket, which provides powerful control over the Docker host. It must remain restricted to a trusted local environment and should not be exposed publicly.

## Conclusion

This project demonstrates how monitoring, alerting, and configuration automation can work together to detect application failures and recover a service automatically.

It provides practical experience with Prometheus, Alertmanager, Docker, Flask, and Ansible in a self-healing infrastructure workflow.
