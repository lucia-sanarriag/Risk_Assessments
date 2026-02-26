# ☁️ Cloud Security Review  
### Fictional AWS Environment Assessment  
Author: Lucia Santillan Arriaga  
UTSA | Cybersecurity Student | AI Enthusiast  

---

## 🔍 Overview  
This Cloud Security Review evaluates a fictional AWS environment focusing on identity management, storage security, compute instances, network segmentation, encryption, and logging. The goal is to identify misconfigurations, assess risk, and provide actionable recommendations.

---

## 🔐 IAM (Identity & Access Management)

### Findings:
- Excessive permissions assigned to multiple IAM users  
- Lack of MFA enforcement  
- IAM roles not used consistently  
- Access keys older than 90 days  

### Recommendations:
- Enforce MFA for all users  
- Implement least‑privilege access  
- Replace long‑term access keys with IAM roles  
- Rotate keys every 90 days  

---

## 🗄️ S3 Storage Security

### Findings:
- One bucket publicly accessible  
- No bucket‑level encryption enabled  
- Logging not configured  

### Recommendations:
- Remove public access unless explicitly required  
- Enable SSE‑S3 or SSE‑KMS encryption  
- Turn on S3 access logging  

---

## 🖥️ EC2 Instances

### Findings:
- Security groups allow inbound SSH from 0.0.0.0/0  
- Unpatched AMIs  
- No IAM roles attached to instances  

### Recommendations:
- Restrict SSH to trusted IPs  
- Patch and update AMIs regularly  
- Attach IAM roles instead of embedding credentials  

---

## 🌐 VPC & Network Security

### Findings:
- Flat network architecture  
- No network ACLs configured  
- Missing flow logs  

### Recommendations:
- Segment workloads using subnets  
- Implement NACLs for traffic filtering  
- Enable VPC Flow Logs for monitoring  

---

## 🔒 Encryption

### Findings:
- EBS volumes not encrypted  
- RDS encryption disabled  
- No KMS key rotation  

### Recommendations:
- Enable EBS and RDS encryption  
- Use KMS CMKs for sensitive workloads  
- Rotate KMS keys annually  

---

## 📜 Logging & Monitoring

### Findings:
- CloudTrail disabled in some regions  
- No centralized log storage  
- No alerting configured  

### Recommendations:
- Enable CloudTrail in all regions  
- Centralize logs in a secure S3 bucket  
- Configure CloudWatch alarms for critical events  

---

## 🧠 Summary  
This fictional AWS environment contains several common misconfigurations that increase risk exposure. By implementing IAM hardening, enabling encryption, segmenting the network, and improving monitoring, the environment can reach a significantly stronger security posture.

---

## 🎯 Purpose  
This Cloud Security Review demonstrates my ability to:  
- Analyze cloud environments  
- Identify misconfigurations  
- Apply security best practices  
- Communicate findings clearly and professionally  

It is part of my growing cybersecurity portfolio.
