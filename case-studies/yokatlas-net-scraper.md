English | [Türkçe](yokatlas-net-scraper.tr.md)

# YÖK Atlas Net Scraper

During university preference season I kept opening YÖK Atlas pages one by one to check the scores of the last student placed in each programme.

## What I built

A tool that pulls those numbers in bulk into Excel. It started as a command-line script, and I added a desktop interface so others could use it too.

## Key features

- Cut-off score, school grade points and TYT/AYT/YDT nets for bachelor's and associate programmes
- Filter by year, type and programme name, ignoring case and Turkish accents
- Export to Excel, CSV or JSON; stopping midway still saves what was fetched
- Switched to the site's JSON service after the 2026 redesign; offline unit tests; can be packaged as an .exe

## Stack

Python, Tkinter, PyInstaller

## My role

Personal tool, built and maintained by me.

## Outcome

A full year, about 21,000 rows, downloads in 20 to 40 seconds.

---

The source code is private. I'm happy to show a demo or walk through the code on request.

[← Back to profile](../README.md)
