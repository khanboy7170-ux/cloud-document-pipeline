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
- ⚡ **In-Memory Stream Processing:** Reads and parses documents directly in
