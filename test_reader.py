
from document_reader import extract_text

file_path = input("Enter your PDF file path: ")

text = extract_text(file_path)

print("\n--- Extracted PDF Text ---")
print(text)
