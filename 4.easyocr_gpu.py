import easyocr

# Tạo đối tượng Reader với tùy chọn sử dụng GPU
reader = easyocr.Reader(['en'], gpu=True)

# Đọc văn bản từ hình ảnh
result = reader.readtext('xemay.jpg')

# In kết quả
for (bbox, text, prob) in result:
    print(f'Detected text: {text} (Confidence: {prob:.2f})')
