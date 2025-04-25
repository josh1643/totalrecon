"""
Extraction module for parsing recon data from text, PDFs, and TXT files.
"""

import re
from totalrecon.ai import summarize_recon

def extract_from_text(text):
    domains = re.findall(r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b", text)
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    s3_buckets = re.findall(r"s3://[^\s]+", text)

    recon_summaries = []
    keywords = [
        "subdomain", "email", "bucket", "domain", "traffic", "exposed",
        "internal", "admin", "credential", "login", "leak", "host",
        "dev", "prod", "api"
    ]

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        summary = summarize_recon(line)
        if summary and any(word in summary.lower() for word in keywords):
            recon_summaries.append(summary.strip())

    return {
        "domains": sorted(set(domains)),
        "emails": sorted(set(emails)),
        "s3_buckets": sorted(set(s3_buckets)),
        "recon_summaries": recon_summaries
    }

def extract_from_pdf(path):
    try:
        import fitz 
        with fitz.open(path) as doc:
            full_text = "".join(page.get_text() for page in doc)
        return extract_from_text(full_text)
    except Exception as e:
        return {"error": f"PDF extraction failed: {e}"}

def extract_from_txt(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            full_text = f.read()
        return extract_from_text(full_text)
    except Exception as e:
        return {"error": f"Text file extraction failed: {e}"}