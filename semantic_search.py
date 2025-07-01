import pinecone
import os

pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment="us-west1-gcp")

index_name = "smart-city-index"

if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=1536)

index = pinecone.Index(index_name)
index.upsert([("doc1", [0.1]*1536)])
res = index.query(vector=[0.1]*1536, top_k=1, include_metadata=True)
print(res)