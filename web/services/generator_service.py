import os
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

from src.nlp.parser import parsing_output

MODEL_PATH = os.getenv("MODEL_PATH", "models/gpt2_finetuned")

_tokenizer = None
_model = None

def _load_model():
    global _tokenizer, _model
    if _tokenizer is None or _model is None:
        _tokenizer = GPT2Tokenizer.from_pretrained(MODEL_PATH)
        _model = GPT2LMHeadModel.from_pretrained(MODEL_PATH)
        _model.eval()
    return _tokenizer, _model

def generate_playlist_text(user_prompt: str) -> str:
    tokenizer, model = _load_model()

    prompt = f"<PROMPT>{user_prompt}<OUT>\n"
    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=120,
            temperature=0.8,
            top_p=0.9,
            do_sample=True,
            repetition_penalty=1.15
        )

    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text

def generate_structured(user_prompt: str) -> dict:
    raw = generate_playlist_text(user_prompt)

    # stop at first ###
    cleaned = raw.split("###")[0] + "###"

    parsed = parsing_output(cleaned)
    # minimal validation / fallback
    if not parsed.get("title"):
        parsed["title"] = "Mood Playlist"
    if not parsed.get("description"):
        parsed["description"] = "A playlist generated from your mood prompt."
    if not parsed.get("tags"):
        parsed["tags"] = ["mood"]

    parsed["raw_text"] = cleaned
    return parsed
