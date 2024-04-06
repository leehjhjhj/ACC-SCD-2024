from PIL import Image

def process_logo(file_path, original_format):
    if original_format == 'PNG':
        img = Image.open(file_path).convert("RGBA")
    else:
        img = Image.open(file_path)
    width, height = img.size
    max_dim = 400

    # 흰색 배경의 새 정사각형 이미지
    if original_format == 'PNG':
        new_img = Image.new('RGBA', (max_dim, max_dim), (0, 0, 0, 0))
    else:
        new_img = Image.new('RGB', (max_dim, max_dim), (255, 255, 255))

    # 가로가 길 경우
    if width > height:
        ratio = max_dim / width
        new_height = int(height * ratio)
        img = img.resize((max_dim, new_height), Image.Resampling.LANCZOS)
        new_img.paste(img, (0, (max_dim - new_height) // 2))

    # 세로가 길 경우
    elif height > width:
        ratio = max_dim / height
        new_width = int(width * ratio)
        img = img.resize((new_width, max_dim), Image.Resampling.LANCZOS)
        new_img.paste(img, ((max_dim - new_width) // 2, 0))

    # 이미 정사각형인 경우
    else:
        img = img.resize((max_dim, max_dim), Image.Resampling.LANCZOS)
        new_img.paste(img, (0, 0))

    return new_img

img_path = ''
original_logo = Image.open(img_path)
original_format = original_logo.format

new_logo = process_logo(original_logo, original_format)
new_logo.save(f'new_logo.{original_format.lower()}', original_format, quality=70)
