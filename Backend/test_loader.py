from app.ingestion.loader import load_document

file_path="data/sample.pdf"

documents=load_document(file_path)

print(f"Total extracted document {len(documents)}")

for index,doc in enumerate(documents):

  print(f"\n---Document {index+1}---")

  print("Metadata:",doc.metadata)

  print("Extracted Content:")
  print(doc.page_content[:500])
