from datasets import load_dataset

ds = load_dataset("GBaker/MedQA-USMLE-4-options")
for split in ds:
    ds[split].to_json(f"data/raw/medqa_{split}.jsonl")

print(ds)            # shows the splits and how many questions each has
print(ds["test"][0]) # shows one full example