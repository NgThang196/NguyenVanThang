from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain_community.embeddings import HuggingFaceEmbeddings

# 1️⃣ Load embeddings local (offline, nhẹ, chạy CPU)
embeddings_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 2️⃣ Đọc chunk từ file
with open(r"D:\Project\chunks.txt", "r", encoding="utf-8") as f:
    chunks = f.read().split("\n\n")  # mỗi chunk cách nhau 1 dòng trống

# 3️⃣ Chuyển chunk thành Document
documents = [Document(page_content=chunk) for chunk in chunks]

# 4️⃣ Tạo FAISS vectorstore offline
vectorstore = FAISS.from_documents(documents, embeddings_model)

# 5️⃣ Lưu vectorstore
vectorstore.save_local("vectorstore_local")
print("✅ Vectorstore local đã tạo và lưu")

# 6️⃣ Test query offline
vectorstore = FAISS.load_local(
    "vectorstore_local",
    embeddings_model,
    allow_dangerous_deserialization=True
)

query = "Khái quát văn học Việt Nam từ cách mạng tháng Tám năm 1945 đến năm 1975?"
docs = vectorstore.similarity_search(query, k=5)

response_text = "\n\n".join([doc.page_content for doc in docs])

# In ra console
print("\n--- Response ---\n")
print(response_text)

# Lưu vào file response.txt
with open(r"D:\Project\response.txt", "w", encoding="utf-8") as f:
    f.write(response_text)

print("\n✅ Response đã được lưu vào response.txt")