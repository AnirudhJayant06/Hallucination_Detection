import os
import json
import pickle
from collections import defaultdict

# Define input/output folders
raw_folder = r"E:\Users\Anirudh\Study\MS\Implementation\Thesis\datasets\Wiki-Dump\raw"
pkl_folder = r"E:\Users\Anirudh\Study\MS\Implementation\Thesis\datasets\Wiki-Dump\pickle_file"

# # Create output folder if it doesn't exist
# os.makedirs(pkl_folder, exist_ok=True)

# Loop through all .jsonl files in raw folder
for filename in os.listdir(raw_folder):
    if filename.endswith(".jsonl"):
        file_path = os.path.join(raw_folder, filename)
        wiki_index = defaultdict(dict)

        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                entry = json.loads(line)

                # Skip placeholder entries like {"id": "", "text": "", "lines": ""}
                if not entry["id"] or not entry["lines"]:
                    continue

                page = entry["id"]

                # Split "lines" field into sentence entries
                for line in entry["lines"].strip().split("\n"):
                    if "\t" in line:
                        try:
                            sent_id_str, sent_text = line.split("\t", 1)
                            sent_id = int(sent_id_str)
                            wiki_index[page][sent_id] = sent_text
                        except ValueError:
                            continue  # Skip malformed entries

        # Output file path
        output_file = os.path.join(pkl_folder, filename.replace(".jsonl", ".pkl"))

        # Save as pickle
        with open(output_file, "wb") as out_f:
            pickle.dump(dict(wiki_index), out_f)

        print(f"Converted: {filename} → {os.path.basename(output_file)}")

print("All .jsonl files converted to .pkl successfully.")
