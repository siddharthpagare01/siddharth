ACTS, PUNE
PG-DITISS 1
Suggested Teaching Guideline for
Network Defense & Countermeasures PG-DITISS August 2024
Duration: 30 class room hrs + 40 lab hrs (Total: 70 Hrs)
Objective: To introduce the students to Network Defense and Countermeasures. 
This includes the following:
• Network Security Concepts,
• Firewalls,
• IDS & IPS, and
• VPN
Prerequisites: OS and Network Concepts
Evaluation method:
Theory Exam: 40% weightage.
Lab Exam: 40%weightage.
Internal Assessment: 20%weightage.
List of books / Other training Material:
Courseware: Cryptography & Network Security: Principles and Practices by William 
Stalings.
Reference:
• Fundamentals of network and Security: Eric Maiwald/TMH
Note: each session and Lab consists of 2 Hours of duration 
Session 1:
 Introduction to Information Security
 Why Information Security?
 Security: The money factor involved
 Internet Statistics - Study from a security perspective
 Vulnerability, Threat and Risk
 Qos
Lab 1:
 Install and configure an antivirus software to scan your system.
 Analyze and summarize internet security statistics from OWASP or other 
reliable sources.
 Conduct a vulnerability scan on your local network using OpenVAS.
 Simulate network traffic and measure QoS parameters using Wireshark.
ACTS, PUNE
PG-DITISS 2
Suggested Teaching Guideline for
Network Defense & Countermeasures PG-DITISS August 2024
Session 2:
 Risk Management, Exposure and Countermeasure
 Firewall
 De-militarized Zone
 Two methods of implementing firewall
Lab 2:
 Identify and categorize risks in your network using the NIST Cybersecurity 
Framework.
 Install and configure pfSense as a firewall on your network.
 Set up a DMZ using a virtual environment to host a web server with pfSense.
 Configure and compare packet-filtering and proxy firewalls using iptables and 
Squid.
Session 3:
 Packet Filtering
 Screened Host Firewall
 Stateful Inspection Firewall
 NextGen Firewall app controls
 iptables - Linux Firewall
Lab 3:
 iptables - Rule Processing
 Default Policy
 iptables - Predefined tables
 INPUT
 OUTPUT
 FORWARD
Lab 4:
 Iptables / netfilter/ Xtables-Addons
 verifying iptables / netfilter
 internal working
 iptables / netfilter - concept of targets
 DROP
 ACCEPT
 iptables - SPI Firewall
 Setting up a SPI Firewall - Standard installation
 Iptables IPv6 Rule Management
ACTS, PUNE
PG-DITISS 3
Suggested Teaching Guideline for
Network Defense & Countermeasures PG-DITISS August 2024
Lab 5:
 Automating iptables and scripting
 Bash Scripting to automate iptables
 Advanced iptables
 Loading of modules
 Geo IP Blocking using Xtables-Addons
Lab 6:
 Access control using iptables
 Internet sharing Using Iptables
Session 4:
 Wireshark
 Create a filters for data collection and display
 Examine real-world packet captures
Lab 7:
 Wireshark
 Examine real-world packet captures
 Iptables Port Forwarding
 Iptables use case: Fail2ban
Session 5:
 Linux Software Firewall(ClearOS Pfsense)
 Nginx & Squid Reverse Proxy
 UTM
 Server Load Balancing
Lab 8:
 Nginx & Squid Reverse Proxy
 Configure reverse proxy URL using regex
 Server Farming
ACTS, PUNE
PG-DITISS 4
Suggested Teaching Guideline for
Network Defense & Countermeasures PG-DITISS August 2024
Session 6 & 7:
 VPN – Introduction
 VPN protocols/characteristics
 VPN Functions
 Types of VPN
 SecureVPN
 Trusted VPN
Lab 9:
 OpenVPN configuration in both Linux & Windows
 Site to Site Connectivity
 Certificate & Password dependent authentication
 VPN configuration for Mobile Device
Lab 10:
 Pfsense OS - Installation and Configuration
 Installation of Pfsense OS and Basic
 Configuration
Lab 11:
 UTM Configuration
 Basic Setup of UTM
Lab 12:
 Configuration for access control and Firewall features (UTM)
 UTM VPN Configuration
Session 8:
 Hybrid VPN
 IPsec
 Tunnel mode/transport mode
 Ipv6 VPN
 Split Tunnel full tunnel VPN
Lab 13:
 VPN Configuration under Windows 2016 using RRAS
 L2TP/PPTP VPN Setup
ACTS, PUNE
PG-DITISS 5
Suggested Teaching Guideline for
Network Defense & Countermeasures PG-DITISS August 2024
Session 9:
 Introduction to IDS and IPS
 IDS / IPS
 Types of Attacks
 IDS
 Security Events
 Vulnerability/design/implementation
Lab 14:
 Distributed Honeynet System (Developed by C-DAC)
 Dynamically configure Honeypot
 UAC (URL Analyzer and Classifier)
 Tcpdump installation, verification and basic usage of tcpdump
Session 10 & 11:
 Attacks-traditional/distributed
 Intruder types
 Types of IDS
 IPS categories
 Defence in depth
 IDS and IPS analysis scheme
 Detection methodologies
 Principles of IDS
 Threat Hunting model 
Lab 15:
 Install and compare Snort (NIDS) and OSSEC (HIDS) on your network.
 Set up Suricata as an IPS and configure rules for network intrusion 
prevention.
Lab 16:
 Analyze network traffic logs from Snort and Suricata to identify and respond to 
threats.
 Perform threat hunting using the ELK stack (Elasticsearch, Logstash, Kibana) 
to detect anomalies.
ACTS, PUNE
PG-DITISS 6
Suggested Teaching Guideline for
Network Defense & Countermeasures PG-DITISS August 2024
Session 12 & 13:
 Symptoms of attacks
 Tired architecture
 Sensors-network/host based
 Denial of services
 Dos & DDos Mitigation
 Sensor Deployment
 Agents
 Functions of IDS agents
 IDS Manager
Lab 17:
 Identify and document symptoms of various attacks using Wireshark.
 Design and implement a three-tier architecture in a virtual environment.
 Set up and configure network-based sensors with Snort and host-based 
sensors with OSSEC.
Lab 18:
 Simulate a DoS attack using LOIC and analyze its impact on a target system.
 Implement rate limiting and IP blacklisting using iptables to mitigate 
DoS/DDoS attacks.
Session 14:
 Introduction of Log Analyser
 Log
 SIEM Log Correlation and event triggering
 Introduction of SIEM
 SIEM Log Forwarding Configuration
 SIEM Log Correlation and event triggering
Lab 19:
 Snort
 Writing Basic Snort Rules
 Syslog Server
 BASE
 Configuration and deployment of SIEM
ACTS, PUNE
PG-DITISS 7
Suggested Teaching Guideline for
Network Defense & Countermeasures PG-DITISS August 2024
Session 15:
 Testing Snort in both Windows & Linux
 IDS architecture
 Bypassing an IDS
Lab 20:
 Testing of Snort using a simulated attack
 Nagios
 Nagios Sensor Configuration (Windows & Linux)
 Nagios with Email services
 Nagios with up/Down of Ram/Hard Disk
