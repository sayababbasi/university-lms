# University LMS & ERP Monorepo

A monorepo containing a Django REST backend (LMS + ERP) and a Next.js frontend.

## Overview

- `backend/` — Django project and apps (lms_crm)
- `frontend/` — Next.js + TypeScript dashboard and UI
- `docs/` — API docs, ERD, architecture
- `docker-compose.yml` — local development stack (Postgres, Redis, MinIO, Celery, Next.js, Nginx)

## Quickstart (development)

1. Copy environment example files (update secrets):
   ```bash
   cp backend/.env.example backend/.env
   cp frontend/.env.local.example frontend/.env.local
