English | [Türkçe](envanter-takip-sistemi.tr.md)

# Inventory Tracking System

Lab equipment was tracked in scattered spreadsheets. Nobody could say at a glance which devices were broken, waiting for parts or due for calibration, and the same item sometimes got bought twice.

## What I built

A web app where each lab's devices, maintenance and calibration dates, faults and missing parts live in one place, with a purchase request flow on top.

![Dashboard](images/envanter-takip-sistemi-1.png)

![Device inventory](images/envanter-takip-sistemi-2.png)

_Screenshots use made-up demo data._

## Key features

- Purchase requests: the lab manager opens one, purchasing checks stock and flags similar devices already in inventory, then the principal approves or rejects with a reason
- Approved and received items go straight into inventory
- Assign devices to people and take them back; fault and maintenance records; a timeline on each device page
- Dashboard warnings for upcoming maintenance or calibration and open faults, plus status and per-lab charts
- QR labels: scan with a phone camera to open the device page
- Role checks on the server: lab managers only see their own labs; full history log; CSV export and CSV import with preview

## Stack

PHP 8 (JSON API), MySQL/MariaDB, plain HTML and JavaScript, bundled QR libraries (no CDN)

## My role

I designed and built the whole thing: database, API, interface and install script.

## Outcome

Built for real lab use; the demo install ships with made-up sample data only.

---

The source code is private. I'm happy to show a demo or walk through the code on request.

[← Back to profile](../README.md)
