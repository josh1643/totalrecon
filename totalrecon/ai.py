"""
AI summarization for recon data using a fine-tuned flan-t5-small model.
"""
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

HF_MODEL = "wassermanrjoshua/totalrecon-flan-t5"

tokenizer = AutoTokenizer.from_pretrained(HF_MODEL)
model = AutoModelForSeq2SeqLM.from_pretrained(HF_MODEL)

def summarize_recon(text: str) -> str:
    if not isinstance(text, str) or not text.strip():
        return ""
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=60)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
