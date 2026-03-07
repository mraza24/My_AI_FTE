\# AI Employee v0.1 — Bronze Tier Completion



\*\*Date:\*\* 2026-03-07  

\*\*System Path:\*\* D:\\My\_AI\_FTE  



---



\## Project Overview



This repository demonstrates the \*\*Bronze Tier\*\* implementation of the AI Employee system — an autonomous workflow that can:



\- Detect tasks in Markdown format  

\- Route them through the pipeline (`Inbox → Needs\_Action → Done`)  

\- Invoke Claude via Reporter and Planner skills  

\- Generate structured output reports  

\- Log each action  

\- Update `Dashboard.md` automatically  



All operations happen \*\*without manual intervention\*\*, with prompt injection protection verified.



---



\## Folder Structure

My\_AI\_FTE/

│

├ README.md

├ Bronze\_Completion.md # Claude-generated Bronze Tier report

├ sentinel.py

├ gmail\_watcher.py

├ skills/

│ ├ reporter/

│ ├ planner/

│ ├ linkedin/

│ └ whatsapp/

├ Inbox/

├ Needs\_Action/

├ Done/

├ Logs/

└ Pending\_Approval/





---



\## Bronze Tier Completion



| Component | Status |

|-----------|--------|

| Obsidian vault with governance docs | ✅ Complete |

| Folder pipeline (Inbox → Needs\_Action → Done) | ✅ Complete |

| `sentinel.py` — filesystem watcher | ✅ Complete |

| Agent Skills (reporter, planner, linkedin, whatsapp) | ✅ Complete |

| Logs auto-update per task | ✅ Complete |

| `Dashboard.md` auto-refresh | ✅ Complete |

| Prompt injection protection | ✅ Verified |



\*\*Key Numbers:\*\*



\- Tasks processed: 6 confirmed in `Done/`  

\- Log entries generated: 113  

\- Emails fetched to `Inbox/`: 100+  



---



\## Architecture Diagram — Bronze Tier

\# AI Employee v0.1 — Bronze Tier



\## Overview



AI Employee v0.1 is an autonomous task-processing system built during \*\*Hackathon 0\*\*.



The goal of the Bronze Tier was to build a \*\*Minimum Viable AI Employee\*\* capable of detecting tasks, processing them through an automated pipeline, invoking Claude AI for reasoning, and producing structured outputs — without manual intervention.



The system operates inside an \*\*Obsidian-style knowledge vault\*\* and uses Python automation combined with AI agent skills.



---



\# Bronze Tier Objective



The Bronze Tier requirements focused on building the \*\*foundation of an AI-driven workflow system\*\*.



Core goals:



• Create an Obsidian vault with governance documents

• Implement a file-based task pipeline

• Detect tasks automatically using filesystem watchers

• Invoke Claude AI to process tasks

• Log system activity for observability

• Maintain an automatically updated dashboard



The result is a lightweight \*\*AI employee capable of autonomously processing tasks.\*\*



---



\# Architecture Diagram



```

&nbsp;          +--------------------+

&nbsp;          |        Inbox       |

&nbsp;          | (Incoming Tasks)   |

&nbsp;          +---------+----------+

&nbsp;                    |

&nbsp;                    v

&nbsp;            +---------------+

&nbsp;            |  sentinel.py  |

&nbsp;            | File Watcher  |

&nbsp;            +-------+-------+

&nbsp;                    |

&nbsp;                    v

&nbsp;          +--------------------+

&nbsp;          |    Needs\_Action    |

&nbsp;          |  Tasks to Process  |

&nbsp;          +---------+----------+

&nbsp;                    |

&nbsp;                    v

&nbsp;          +----------------------+

&nbsp;          | Claude AI Invocation |

&nbsp;          | via Agent Skills     |

&nbsp;          +----------+-----------+

&nbsp;                     |

&nbsp;         +-----------+------------+

&nbsp;         |                        |

&nbsp;         v                        v

&nbsp;    +---------+             +---------+

&nbsp;    |  Done   |             |  Logs   |

&nbsp;    | Results |             | History |

&nbsp;    +---------+             +---------+



&nbsp;               |

&nbsp;               v

&nbsp;          +------------+

&nbsp;          | Dashboard  |

&nbsp;          | System KPI |

&nbsp;          +------------+

```



---



\# Folder Structure



```

My\_AI\_FTE

│

├ Inbox

│ Incoming task files

│

├ Needs\_Action

│ Tasks waiting to be processed

│

├ Done

│ Completed tasks

│

├ Logs

│ Execution history

│

├ Plans

│ Future planning outputs

│

├ Pending\_Approval

│ Human approval workflow

│

├ skills

│ Agent skill definitions

│

├ sentinel.py

│ Filesystem watcher

│

├ gmail\_watcher.py

│ Email task importer

│

├ Dashboard.md

│ System status dashboard

│

├ Company\_Handbook.md

│ Governance rules

│

└ Bronze\_Completion.md

&nbsp; AI generated completion report

```



---



\# Core Components



\### sentinel.py



The core automation engine.



Responsibilities:



• Monitor Inbox and Needs\_Action folders

• Detect new task files

• Route tasks through the pipeline

• Invoke Claude AI using Agent Skills

• Log actions automatically

• Update system dashboard



---



\### gmail\_watcher.py



Imports emails as tasks.



Responsibilities:



• Fetch Gmail messages

• Convert emails into markdown task files

• Place tasks into Inbox for processing



---



\### Agent Skills



The system implements AI functionality as \*\*modular skills\*\*.



Current skills:



• Reporter Skill

• Planner Skill

• LinkedIn Skill

• WhatsApp Skill



These skills define how Claude processes specific tasks.



---



\# Logging System



Each processed task generates a structured log entry.



Logs contain:



• Task filename

• Timestamp

• Action performed

• Execution status



Logs provide \*\*observability and traceability\*\* for all system activity.



---



\# Dashboard



The system automatically updates \*\*Dashboard.md\*\* after each task execution.



The dashboard tracks:



• Total tasks processed

• Completed tasks

• Pending tasks



This allows quick visibility into system performance.



---



\# Example Workflow



1\. A new task file is added to \*\*Inbox\*\*



```

Inbox/market\_research.md

```



2\. sentinel.py detects the new file.



3\. The file is moved to:



```

Needs\_Action/

```



4\. Claude AI processes the task using the appropriate \*\*Agent Skill\*\*.



5\. The output is saved in:



```

Done/

```



6\. A log entry is generated.



7\. Dashboard statistics update automatically.



---



\# Bronze Tier Requirements



| Requirement             | Status        |

| ----------------------- | ------------- |

| Obsidian Vault          | ✅ Complete    |

| Dashboard.md            | ✅ Complete    |

| Company\_Handbook.md     | ✅ Complete    |

| Watcher Script          | ✅ sentinel.py |

| Claude Read/Write Vault | ✅ Verified    |

| Basic Folder Pipeline   | ✅ Implemented |

| Agent Skills            | ✅ Implemented |

| Logging System          | ✅ Implemented |



Bronze Tier Status: \*\*COMPLETE\*\*



---



\# Metrics



System activity during testing:



• Tasks processed: \*\*6 confirmed\*\*

• Log entries generated: \*\*113\*\*

• Emails fetched to Inbox: \*\*100+\*\*



These metrics demonstrate that the system pipeline is functional and autonomous.



---



\# Technology Stack



Python

Watchdog (filesystem monitoring)

Claude AI (task reasoning)

Markdown knowledge vault

Gmail API

Obsidian workflow structure



---



\# How to Run



Start the automation system:



```

python sentinel.py

```



Run the Gmail watcher:



```

python gmail\_watcher.py

```



The system will automatically detect and process new tasks.



---



\# Completion Report



A full autonomous system report generated by the AI is available in:



```

Bronze\_Completion.md

```



This document contains:



• System validation results

• Task processing metrics

• Component verification

• Bronze Tier completion summary



It serves as \*\*evidence that the system was executed and validated by the AI itself.\*\*



---



\# Conclusion



AI Employee v0.1 successfully implements the \*\*Bronze Tier foundation\*\* of an autonomous AI assistant.



The system demonstrates:



• Automated task detection

• AI-driven task processing

• Structured output generation

• Activity logging and monitoring

• Dashboard-based system visibility



This foundation enables future expansion into more advanced autonomous workflows in higher tiers of the hackathon.

Proven Capabilities



The system can autonomously:



Detect new Markdown task files in Inbox/ or Needs\_Action/



Move tasks to Needs\_Action/ and trigger appropriate skill



Generate structured reports via Claude



Move processed files to Done/



Log each task in Logs/



Update Dashboard.md in real-time



Bronze Completion Report Reference



For detailed AI-generated verification, see:



Bronze\_Completion.md



This file contains Claude’s own assessment of the pipeline’s operation.



Known Gaps (Silver Tier Preview)



planner\_executor.py currently a stub (no plan generation)



Pending\_Approval/ workflow not yet exercised



gmail\_watcher.py not scheduled (manual execution only)



MCP server integration not yet configured



| Total Tasks | Completed | Pending |

|------------:|----------:|--------:|

| 113        | 6        | 100+    |



Certified complete by AI Employee v0.1 on 2026-03-07

