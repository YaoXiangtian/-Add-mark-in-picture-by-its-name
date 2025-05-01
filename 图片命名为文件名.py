from PIL import Image, ImageDraw, ImageFont
import os

def auto_add_watermark():
    """
    自动处理程序所在文件夹的所有图片
    输出到当前目录下的watermarked文件夹
    """
    # 设置路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_dir, "watermarked")
    
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 字体配置（Windows/Mac自动适配）
    font_paths = [
        'C:/Windows/Fonts/simhei.ttf',  # Windows
        '/System/Library/Fonts/PingFang.ttc',  # macOS
        '/usr/share/fonts/wenquanyi/wqy-zenhei/wqy-zenhei.ttc'  # Linux
    ]
    
    # 自动检测可用字体
    font = None
    for path in font_paths:
        if os.path.exists(path):
            try:
                font = ImageFont.truetype(path, 24)
                break
            except:
                continue
    
    # 没有找到字体时使用默认字体
    if not font:
        font = ImageFont.load_default()
        print("注意: 未找到中文字体，中文显示可能异常")

    # 支持的文件格式
    valid_ext = ['.jpg', '.jpeg', '.png', '.webp', '.bmp']

    # 遍历当前目录
    for filename in os.listdir(current_dir):
        # 过滤非图片文件
        if os.path.splitext(filename)[1].lower() not in valid_ext:
            continue

        input_path = os.path.join(current_dir, filename)
        output_path = os.path.join(output_dir, f"WM_{filename}")

        try:
            with Image.open(input_path) as img:
                draw = ImageDraw.Draw(img)
                width, height = img.size

                # 计算文字位置 (n-50, 50)
                x = width - 50
                y = 50

                # 绘制带描边的文字
                draw.text(
                    (x, y),
                    filename,
                    font=font,
                    fill=(255, 255, 255),  # 白色文字
                    anchor="rd",          # 右下角对齐
                    stroke_width=2,       # 描边宽度
                    stroke_fill=(0, 0, 0) # 黑色描边
                )

                # 保存图片（保持原格式）
                img.save(output_path)
                print(f"成功处理: {filename}")

        except Exception as e:
            print(f"处理失败 [{filename}]: {str(e)}")

if __name__ == "__main__":
    auto_add_watermark()
    print("处理完成，请查看watermarked文件夹")
