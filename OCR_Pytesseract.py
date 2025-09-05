import fitz  # PyMuPDF
import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pdf_path = r"D:\Project\Ngu_Van_12_Tap_1.pdf"
output_path = r"D:\Project\output.txt"

doc = fitz.open(pdf_path)

with open(output_path, "w", encoding="utf-8") as f:
    for i in range(len(doc)):
        page = doc[i]
        pix = page.get_pixmap(dpi=300)
        img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
        img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        if pix.n == 4:
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        text = pytesseract.image_to_string(img, lang='vie')

        f.write(f"=== Trang {i+1} ===\n")
        f.write(text + "\n\n")

print(f"OCR xong! Kết quả được lưu tại: {output_path}")
