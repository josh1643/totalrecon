"""
Command-line interface for TotalRecon - Passive Recon + AI Summarization
"""

import argparse
import json
from totalrecon.cert import get_cert_domains
from totalrecon.extract import extract_from_pdf, extract_from_txt

def print_recon_results(data):
    print("\n[+] Domains:")
    for d in data.get("domains", []):
        print("  -", d)

    print("\n[+] Emails:")
    for e in data.get("emails", []):
        print("  -", e)

    print("\n[+] S3 Buckets:")
    for b in data.get("s3_buckets", []):
        print("  -", b)

    print("\n[+] Recon AI Summaries:")
    for summary in data.get("recon_summaries", []):
        print("  -", summary)

def main():
    parser = argparse.ArgumentParser(description="TotalRecon CLI Tool")
    parser.add_argument("--domain", help="Target domain for cert.sh subdomain enumeration")
    parser.add_argument("--pdf", help="Path to PDF file for recon extraction")
    parser.add_argument("--txt", help="Path to TXT file for recon extraction")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    parser.add_argument("--version", action="version", version="totalrecon 0.1.0")

    args = parser.parse_args()

    if not args.domain and not args.pdf and not args.txt:
        parser.print_help()
        return

    results = {}

    if args.domain:
        subdomains = get_cert_domains(args.domain)
        results["subdomains"] = subdomains
        print(f"[+] Subdomains for {args.domain}:")
        for sub in subdomains:
            print("  -", sub)

    if args.pdf:
        print(f"\n[+] Scanning PDF: {args.pdf}")
        pdf_recon = extract_from_pdf(args.pdf)
        results["pdf_recon"] = pdf_recon
        print_recon_results(pdf_recon)

    if args.txt:
        print(f"\n[+] Scanning TXT: {args.txt}")
        txt_recon = extract_from_txt(args.txt)
        results["txt_recon"] = txt_recon
        print_recon_results(txt_recon)

    if args.json:
        print("\n[+] Full JSON Output:")
        print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()