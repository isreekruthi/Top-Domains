# Top Domains Analyzer

This Python script analyzes domain names from a list of URLs contained in a CSV file and identifies how frequently each domain appears. It uses **Pandas** for data processing and simple string manipulation to extract the base domain names.

---

## Features

- Loads a CSV file of ranked domains (`top-1m.csv`)
- Extracts base domain names (for example, `"google"` from `"www.google.com"`)
- Counts the frequency of each unique domain
- Reports how many domains appear fewer than 3.5 times

---

## How It Works

1. The script reads the file `top-1m.csv` into a Pandas DataFrame with no header.  
2. It extracts the second column (index `1`) as the list of URLs.  
3. For each URL:
   - Splits the domain string by `"."`
   - Takes the second-to-last element as the domain name (for example, `"amazon"` from `"www.amazon.co.uk"`)
4. It appends the resulting domain list as a new column named `'domain'`.
5. Uses `value_counts()` to calculate how often each domain occurs.
6. Counts and prints how many of those domains appear less than 3.5 times.

---
## Input File

The script expects a CSV file named `top-1m.csv` in the same directory. The file will not contain headers; the first domain is in the first row of the excel.

Example format:

| Rank | Domain          |
|------|----------------|
| 1    | google.com     |
| 2    | facebook.com   |
| 3    | youtube.com    |
| 4    | news.google.com|

---

## Example Output

There are 213128 domains with a frequency less than 3.5.

---

## Requirements

Make sure you have **Python 3.x** and **Pandas** installed.

Install Pandas with:

```bash
pip install pandas

