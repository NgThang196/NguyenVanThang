import ollama
import re

# Hàm chia text thành chunk nhỏ
def chunk_text(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap  # overlap để không mất mạch
    return chunks

# Đọc file
context = open(r"D:\Project\response.txt", "r", encoding="utf-8").read()
query = "Khái quát văn học Việt Nam từ cách mạng tháng Tám năm 1945 đến năm 1975?"

# Chia text thành chunk nhỏ
chunks = chunk_text(context)

full_response = []

for i, chunk in enumerate(chunks):
    prompt = f"""
    Dựa vào nội dung sau, trả lời câu hỏi bằng **tiếng Việt**, chi tiết và mạch lạc:
    {chunk}

    Câu hỏi: {query}
    """

    resp = ollama.chat(
        model="phi:2.7b",  # nhẹ, tối ưu CPU
        messages=[{"role": "user", "content": prompt}],
    )

    answer = resp["message"]["content"]
    full_response.append(answer)

# Gom tất cả kết quả lại
final_answer = "\n".join(full_response)
print(final_answer)

