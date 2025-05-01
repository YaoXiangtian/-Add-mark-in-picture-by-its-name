from PIL import Image, ImageDraw, ImageFont
import os
import glob

def batch_add_filename(input_dir, font_path='arial.ttf', font_size=30):
    # 创建输出目录
    output_dir = os.path.join(input_dir, 'processed_images')
    os.makedirs(output_dir, exist_ok=True)

    # 支持的图片格式
    extensions = ['*.jpg', '*.jpeg', '*.png', '*.webp', '*.bmp']
    
    # 获取所有图片文件
    image_files = []
    for ext in extensions:
        image_files.extend(glob.glob(os.path.join(input_dir, ext)))

    # 设置字体
    try:
        font = ImageFont.truetype(font_path, font_size)
    except:
        font = ImageFont.load_default()
        print("警告：使用默认字体，建议提供字体文件以获得更好效果")

    for img_path in image_files:
        try:
            # 处理文件名
            filename = os.path.splitext(os.path.basename(img_path))[0]
            output_path = os.path.join(output_dir, os.path.basename(img_path))

            # 打开图片
            with Image.open(img_path) as img:
                draw = ImageDraw.Draw(img)
                
                # 动态调整坐标到图片右侧
                img_width, _ = img.size
                x = min(1400, img_width - 10)  # 确保不超过图片右边界
                position = (x, 100)
                
                # 添加文字（白色文字黑色描边）
                draw.text(position, filename, font=font, fill=(100, 100, 255))
                
                # 保存图片（保持原格式）
                img.save(output_path)
            print(f"已处理：{os.path.basename(img_path)}")
        except Exception as e:
            print(f"处理失败：{os.path.basename(img_path)} - {str(e)}")

if __name__ == "__main__":
    # 使用示例 - 处理当前目录图片
    batch_add_filename(
        input_dir=os.getcwd(),  # 当前目录
        font_path='arial.ttf',   # 字体文件路径
        font_size=100            # 字体大小
    )
