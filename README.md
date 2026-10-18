<div align="center">

# ⚡ CloudDoc-Pipeline
### Automated Cloud Document Processing & Relational Observability Pipeline

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Supabase](https://img.shields.io/badge/Supabase-Database%20%26%20Storage-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Relational%20DB-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)](#)

<p align="center">
  <b>A lightweight, event-driven cloud pipeline designed to automate document ingestion, extract in-memory text metrics, generate structured JSON reports, and synchronize real-time state with PostgreSQL.</b>
</p>

[Key Features](#-key-features) • [Architecture](#-architecture) • [Database Schema](#-database-schema) • [Quick Start](#-quick-start) • [Author](#-author)

---

</div>

## 📌 Executive Summary

Manual file auditing and text metric calculations create bottlenecks in modern data workflows. This project delivers an end-to-end cloud pipeline that eliminates manual intervention by isolating raw ingestion and processed outputs into distinct cloud storage layers, running automated in-memory analytics, and maintaining fault-tolerant database logs.

---

## ✨ Key Features

- 🗄️ **Dual-Bucket Object Isolation:** Dedicated ingestion bucket (`khan.boy`) and analytics bucket (`processed-results`) preventing data overwrite.
- ⚡ **In-Memory Stream Processing:** Reads and parses documents directly in memory without cluttering local disk storage.
- 📊 **Instant Text Analytics:** Automatically extracts quantitative metrics (line count, word count, character count).
- 🛡️ **Conflict-Free State Sync:** Employs smart `upsert` queries to ensure zero duplicate primary key collisions during repeated file processing.
- 🔒 **Enterprise-Grade Auth:** Connects via Supabase Service Role Secret Key for secure background execution.

---

## 🏗️ System Architecture & Live Data Flow

<div align="center">

```mermaid
flowchart TD
    subgraph Ingestion ["☁️ Step 1: Ingestion Layer"]
        A["📄 Raw File (demo.txt)"] -->|"Upload Event"| B[("🪣 Input Bucket: 'khan.boy'")]
    end

    subgraph Processing ["⚡ Step 2: In-Memory Processing Engine"]
        B -->|"Stream Download"| C{"⚙️ Python Worker (pipeline.py)"}
        C -->|"Calculate Metrics"| D["📊 Lines: 1 | Words: 4 | Characters: 27"]
    end

    subgraph DualOutput ["🚀 Step 3: Real-Time Dual Sync"]
        D -->|"Generate JSON"| E[("🪣 Output Bucket: 'processed-results'")]
        D -->|"Upsert Query"| F[("🗄️ PostgreSQL: 'document_logs'")]
    end

    style B fill:#3ECF8E,stroke:#111,stroke-width:2px,color:#fff
    style E fill:#3ECF8E,stroke:#111,stroke-width:2px,color:#fff
    style C fill:#3776AB,stroke:#111,stroke-width:2px,color:#fff
    style F fill:#4169E1,stroke:#111,stroke-width:2px,color:#fff
    style D fill:#2b3137,stroke:#fff,stroke-width:1px,color:#fff
```

</div>

### 🔄 End-to-End Execution Trace

```mermaid
sequenceDiagram
    autonumber
    actor User as 👤 Client / User
    participant IB as 🪣 Ingestion ('khan.boy')
    participant PY as ⚙️ Python Core Engine
    participant OB as 🪣 Output ('processed-results')
    participant DB as 🗄️ PostgreSQL ('document_logs')

    User->>IB: 1. Drop & upload 'demo.txt'
    activate IB
    Note over IB,PY: Continuous stream listening
    PY->>IB: 2. Pull file stream into memory
    deactivate IB
    activate PY
    Note over PY: Extract: Lines, Words & Characters
    PY->>OB: 3. Save structured 'result_demo.txt.json'
    activate OB
    OB-->>PY: 200 OK (Report Saved)
    deactivate OB
    PY->>DB: 4. Execute UPSERT statement
    activate DB
    DB-->>PY: State Synced: [PROCESSED]
    deactivate DB
    deactivate PY
```

---

## 📂 Cloud Storage Topology

| Bucket Name | Access Level | Purpose | File Formats |
| :--- | :--- | :--- | :--- |
| `khan.boy` | Private / Authenticated | Raw incoming file ingestion | `.txt`, `.csv` |
| `processed-results` | Private / Authenticated | Generated analytics reports | `.json` |

---

## 🗄️ Database Schema (`document_logs`)

```sql
CREATE TABLE document_logs (
    id BIGSERIAL PRIMARY KEY,
    file_name TEXT UNIQUE NOT NULL,
    status TEXT NOT NULL,
    word_count INT8 NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
