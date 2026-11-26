# Self-Healing Infrastructure
## Project-Based DevOps Interview Questions & Answers

These questions are selected from the DevOps interview-question set provided with the internship project. Answers are tailored to this project's actual implementation.

---

## 1. What is a self-healing infrastructure, and how can you implement it?

A self-healing infrastructure detects failures and automatically performs recovery actions with minimal manual intervention.

In my project, Prometheus detects the NGINX application failure through an HTTP probe. Alertmanager forwards the `ApplicationDown` alert to a Flask webhook, which executes an Ansible playbook to restart the NGINX container and verify that it is running.

## 2. How would you handle system failures and downtime in a DevOps environment?

I would monitor application health, configure meaningful alert rules, notify the responsible system, and automate safe recovery actions where possible.

In this project, I simulated an NGINX failure by stopping its Docker container. Prometheus detected the failed probe, and the alert triggered the automated recovery workflow.

## 3. How do you handle logging and monitoring in a DevOps environment?

Monitoring helps track service health and performance metrics. Logs help understand events, errors, and recovery actions.

In my project, Prometheus collects application availability metrics through Blackbox Exporter. The recovery webhook logs received alerts and Ansible execution output, which helps verify the recovery process.

## 4. What is the purpose of Prometheus and Grafana in DevOps?

Prometheus collects and stores time-series metrics and evaluates alerting rules. Grafana is commonly used to visualize metrics through dashboards.

I used Prometheus for metric collection and alert evaluation. Grafana was not part of my implementation.

## 5. How would you monitor the performance of a distributed application?

I would monitor service availability, response time, resource utilization, and application-specific metrics. I would also use logs and traces when diagnosing complex distributed systems.

In this project, I implemented HTTP availability monitoring using Blackbox Exporter and Prometheus. This project focuses on availability rather than full distributed tracing or detailed performance analysis.

## 6. What is Docker, and how does it work?

Docker is a containerization platform used to package and run applications in isolated containers.

In my project, Docker runs NGINX, Prometheus, Alertmanager, Blackbox Exporter, and the recovery webhook. Containers communicate through a Docker network.

## 7. What are some configuration management tools, and what are their advantages?

Common configuration management and automation tools include Ansible, Chef, and Puppet.

They help automate repeatable operational tasks, reduce manual errors, and maintain consistent configurations.

I used Ansible to automate the NGINX container restart and verify its running state.

## 8. What are the advantages of using Ansible over tools like Chef or Puppet?

Ansible uses a simple YAML-based playbook format and commonly connects through SSH for remote Linux automation. It can also run locally.

In my project, I used Ansible with a local connection to execute Docker commands and verify recovery. I chose it because the recovery workflow was small and straightforward to automate.

## 9. What is Git, and why is it commonly used in DevOps environments?

Git is a distributed version control system that tracks changes in source code and configuration files.

I used Git to track my project files, maintain commits, and push the project to GitHub. This makes the configuration and recovery workflow easier to review and share.

## 10. What is the role of a DevOps engineer in managing cloud infrastructure?

A DevOps engineer helps automate infrastructure and application delivery, monitor systems, improve reliability, manage configuration, and support secure operations.

This project gave me practical experience with monitoring, alerting, container management, and automated recovery in a local Linux environment.

## 11. How do you ensure the security and compliance of applications in a DevOps environment?

I would follow least privilege, protect credentials, restrict network access, use trusted images, review configuration, and maintain audit logs.

In this project, the recovery webhook has access to the Docker socket. This is powerful access, so the webhook must remain in a trusted local environment and must not be exposed publicly. The project is a learning demonstration, not a production-secured deployment.

## 12. How do you manage secrets such as API keys and passwords in a DevOps environment?

Secrets should not be hardcoded into source code or committed to Git. They should be stored using secure secret-management mechanisms or protected environment variables.

This project does not require cloud API keys. I added `.gitignore` rules to exclude environment files and other sensitive local files from Git.

## 13. How do you ensure high availability and scalability in a cloud environment?

High availability can involve multiple application instances, health checks, load balancing, redundancy, and recovery strategies. Scalability involves increasing or decreasing capacity based on demand.

My project demonstrates automated recovery of a single local NGINX container. It does not implement multi-node high availability or cloud-based scaling.

## 14. What is the difference between continuous integration and continuous delivery?

Continuous Integration (CI) frequently integrates code changes and runs automated checks.

Continuous Delivery (CD) keeps changes in a deployable state and supports controlled release to an environment.

This project focuses on monitoring and recovery automation; it does not implement a complete CI/CD pipeline.

## 15. How does your project detect an application failure?

Blackbox Exporter probes the NGINX HTTP endpoint. Prometheus collects the `probe_success` metric.

When the probe fails, `probe_success` becomes `0`. The `ApplicationDown` rule checks this condition and uses a 15-second pending period before firing.

## 16. What is the role of Alertmanager in your project?

Alertmanager receives alerts from Prometheus and routes them to the configured receiver.

In my project, it sends the `ApplicationDown` alert to the Flask recovery webhook using an HTTP request.

## 17. Why did you use a Flask webhook?

The webhook acts as the bridge between Alertmanager and the Ansible recovery process.

It receives the alert payload and invokes the recovery playbook. This connects monitoring and alerting with an automated operational action.

## 18. What does your Ansible recovery playbook do?

The playbook performs two main tasks:

1. Restarts the `self-healing-nginx` Docker container.
2. Checks whether the container is running.

The verification task fails if the container is not running, allowing the recovery result to be checked.

## 19. How did you test the self-healing workflow?

I stopped the NGINX container to simulate an application failure.

The alert was received by the webhook, Ansible restarted the container, and the verification task passed.

The recorded play recap showed:

```text
ok=2
changed=1
unreachable=0
failed=0
```

This confirms that the recovery playbook completed successfully during the test.

## 20. What are the limitations of your project?

The project is a local demonstration using Docker in Ubuntu on WSL. It recovers a single NGINX container.

It does not include production-grade high availability, multi-node failover, cloud deployment, Grafana dashboards, or a production web server for the webhook.

These are possible future improvements.

---

## Interview Tip

Explain the workflow in this order:

**NGINX → Blackbox Exporter → Prometheus → Alertmanager → Flask Webhook → Ansible → NGINX Restart → Verification**

Be clear about what you implemented and what you have only studied. The successful recovery test is the strongest practical evidence of this project.
