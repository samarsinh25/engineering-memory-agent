import openai 
import os
import json
import sys
from dotenv import load_dotenv

# Step 1: Load the API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Step 2: Get file path from CLI arg
if len(sys.argv) != 2:
    print("Usage: python generate_embeddings.py <path_to_json>")
    sys.exit(1)

input_path = sys.argv[1]

# Step 3: Read log messages from JSON
with open(input_path, "r") as f:
    texts = json.load(f)

# Step 4: Call OpenAI to embed all messages
try:
    response = openai.Embedding.create(
        input=texts,
        model="text-embedding-3-small"  # or "text-embedding-3-large"
    )
except Exception as e:
    print("❌ Error while fetching embeddings:", e)
    sys.exit(1)

# Step 5: Extract embeddings from response
embeddings = [item['embedding'] for item in response['data']]

# Step 6: Save to vectors.json
with open("vectors.json", "w") as f:
    json.dump(embeddings, f)

print(f"✅ Successfully embedded {len(embeddings)} logs → vectors.json")
