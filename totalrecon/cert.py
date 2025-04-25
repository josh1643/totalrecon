"""
Module to fetch subdomains from Certificate Transparency logs using crt.sh.
"""

import requests

def get_cert_domains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        domains = set()
        for entry in data:
            for name in entry.get("name_value", "").split("\n"):
                if domain in name:
                    domains.add(name.strip())

        return sorted(domains)
    except Exception as e:
        print(f"[ERROR] crt.sh request failed: {e}")
        return []
