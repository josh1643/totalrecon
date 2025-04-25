# totalrecon

**totalrecon** is a lightweight Python library for passive reconnaissance. It extracts subdomains, emails, and S3 buckets from text and PDF files, and uses a fine-tuned AI model to summarize sensitive infrastructure mentions.

>  Built for red teamers, bug bounty hunters, CTF players, and cyber analysts.

---

## Features

- Extract intelligence from plaintext and PDF files  
- Detect subdomains, emails, and AWS S3 buckets  
- Summarize recon info with a fine-tuned `flan-t5-small` model  
- Offline and lightweight — no OpenAI key required  
- Trained on synthetic recon examples tailored for real-world use  

---

## Installation

```bash
pip install totalrecon
```

Or from source:

```bash
git clone https://github.com/josh1643/totalrecon.git
cd totalrecon
pip install .
```

---

## Quick Start

### Python Example

```python
from totalrecon.extract import extract_from_text

text = '''
Found subdomain: api.dev.example.com
Email: admin@example.com
S3 bucket: s3://backup-prod-private
'''

results = extract_from_text(text)

print(results["domains"])          # ['api.dev.example.com']
print(results["emails"])           # ['admin@example.com']
print(results["s3_buckets"])       # ['s3://backup-prod-private']
print(results["recon_summaries"])  # ['Possible backup S3 bucket exposed via dev subdomain.']
```

---

## About the Model

This project uses a fine-tuned `flan-t5-small` model hosted on the Hugging Face Hub:

🔗 https://huggingface.co/wassermanrjoshua/totalrecon-flan-t5

- Summarizes cyber recon and passive intel  
- Runs **entirely offline** after first load  
- No setup required — model is automatically downloaded on first use

This means:
- You don’t need to clone or manually download any model files
- Just `pip install totalrecon` and run it — the model loads when needed


---

## Contributing

Contributions welcome!  
1. Fork the repo  
2. Create a feature branch  
3. Open a pull request  

---

## License

MIT License — see [`LICENSE`](LICENSE) for full terms.

---

## Author

Created by Joshua Wasserman for real-world recon workflows and open-source tooling.
