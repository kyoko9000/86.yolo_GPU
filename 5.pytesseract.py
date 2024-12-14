import pytesseract
from PIL import Image

# Đường dẫn đến tesseract.exe trên Windows
pytesseract.pytesseract.tesseract_cmd = 'tesseract_exe/tesseract.exe'

# Đọc văn bản từ ảnh CCCD
image_path = 'dulieu.jpg'
img = Image.open(image_path)
text = pytesseract.image_to_string(img, lang='vie')

print(text)

