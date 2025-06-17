import re

text = "The quick brown fox jumps over the lazy dog."
pattern = r"\bfox\b"  # Matches the word "fox"

match = re.search(pattern, text)
if match:
    print(f"Match found: {match.group()}")

matches = re.findall(r"\b\w{4}\b", text) # Matches words with exactly 4 characters
print(f"Matches found: {matches}")

new_text = re.sub(r"dog", "cat", text) # Replace "dog" with "cat"
print(f"New text: {new_text}")

split_text = re.split(r"\s", text) # Split by white space
print(f"Split text: {split_text}")