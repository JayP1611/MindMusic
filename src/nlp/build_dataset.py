import json

path = "../../data/training/train.jsonl"

texts = []

with open(path, 'r', encoding = "utf-8") as f:
    for i, line in enumerate(f):
        obj = json.loads(line)
        assert "text" in obj
        print(f"Sample {i} OK")
        texts.append(obj['text'])

for i in range(len(texts)):
    print(f"{texts[i]}\n")