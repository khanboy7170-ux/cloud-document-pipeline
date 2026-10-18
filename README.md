# 🚀 Automated Cloud Document Processing Pipeline

An automated, cloud-native document ingestion and text analytics pipeline built with **Supabase (Storage & PostgreSQL)** and **Python**.

---

## 📌 Architecture & Overview
Manual document processing and file auditing can create operational bottlenecks. This project automates document ingestion by:
- **Ingestion Bucket (`khan.boy`):** Secure object storage layer for incoming raw `.txt` files.
- **Analysis Engine (Python):** Streams file contents in-memory to extract line, word, and character metrics.
- **Storage Layer (`processed-results`):** Stores structured analytics reports as isolated JSON files.
- **Relational Logging (`document_logs`):** Logs processing status and metadata into a PostgreSQL table using `upsert` queries to prevent primary key collision errors.

