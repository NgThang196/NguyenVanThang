import re

def load_text(input_path: str) -> str:
    """Đọc text từ file OCR"""
    with open(input_path, "r", encoding="utf-8") as f:
        return f.read()

def clean_text(text: str) -> str:
    """Làm sạch text cơ bản từ OCR và loại bỏ header trang"""
    # Xóa các dòng kiểu '=== Trang 1 ==='
    text = re.sub(r"===\s*Trang\s*\d+\s*===", " ", text)
    # Xóa ký tự rác (chỉ giữ chữ, số, dấu câu cơ bản)
    text = re.sub(r"[^0-9A-Za-zÀ-ỹ\s.,;:!?()\"'\-]", " ", text)
    # Gộp nhiều khoảng trắng thành 1
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def chunk_text(text: str, chunk_size=1000, overlap=100):
    """Chia nhỏ văn bản thành các chunks"""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk.strip())
        start += chunk_size - overlap
    return chunks

if __name__ == "__main__":
    input_path = r"D:\Project\output.txt"      # file OCR gốc
    output_path = r"D:\Project\chunks.txt"     # file sau khi chunk

    # 1. Load & clean text
    text = load_text(input_path)
    text = clean_text(text)

    # 2. Chunk text
    chunks = chunk_text(text, chunk_size=1000, overlap=100)

    # 3. Lưu vào file
    with open(output_path, "w", encoding="utf-8") as f:
        for i, chunk in enumerate(chunks, 1):
            f.write(f"=== Chunk {i} ===\n{chunk}\n\n")

    print(f"✅ Đã chia thành {len(chunks)} chunks, lưu tại: {output_path}")
