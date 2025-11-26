from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder(filename, style_name, prompt_text, color):
    width, height = 400, 300
    img = Image.new('RGB', (width, height), color=color)
    d = ImageDraw.Draw(img)
    
    try:
        # Title font
        title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 24)
        # Body font
        body_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 14)
    except IOError:
        title_font = ImageFont.load_default()
        body_font = ImageFont.load_default()

    # Draw Style Name (Centered, Top)
    bbox = d.textbbox((0, 0), style_name, font=title_font)
    text_width = bbox[2] - bbox[0]
    d.text(((width - text_width) / 2, 30), style_name, fill=(255, 255, 255), font=title_font)

    # Draw Prompt Text (Wrapped, Center-ish)
    margin = 20
    current_h = 80
    
    # Simple word wrap for prompt
    words = prompt_text.split()
    lines = []
    current_line = []
    
    for word in words:
        current_line.append(word)
        # Check width
        line_str = ' '.join(current_line)
        bbox = d.textbbox((0, 0), line_str, font=body_font)
        if bbox[2] - bbox[0] > (width - 2 * margin):
            current_line.pop()
            lines.append(' '.join(current_line))
            current_line = [word]
    lines.append(' '.join(current_line))

    for line in lines:
        bbox = d.textbbox((0, 0), line, font=body_font)
        text_width = bbox[2] - bbox[0]
        d.text(((width - text_width) / 2, current_h), line, fill=(255, 255, 255), font=body_font)
        current_h += 20

    # Draw "Image Placeholder" note at bottom
    note = "(AI Image Quota Limit Reached)"
    bbox = d.textbbox((0, 0), note, font=body_font)
    text_width = bbox[2] - bbox[0]
    d.text(((width - text_width) / 2, height - 30), note, fill=(200, 200, 200), font=body_font)

    img.save(filename)

os.makedirs('商業應用場景/images', exist_ok=True)

# Style Name, Prompt Summary, Color
scenarios = {
    'bg_removal.png': ('Background Removal', 'Subject: Product, Action: Remove BG', (100, 149, 237)),
    'bg_removal_source.png': ('Source: Product', 'Subject: Product with BG', (150, 150, 150)),
    
    'image_merging.png': ('Image Merging', 'Subject: City & Forest, Action: Double Exposure', (255, 105, 180)),
    'image_merging_source.png': ('Source: City/Forest', 'Subject: City and Forest Photos', (150, 150, 150)),

    'image_conversion.png': ('Image Conversion', 'Subject: Photo, Action: To Anime', (255, 69, 0)),
    'image_conversion_source.png': ('Source: Real Photo', 'Subject: Real Person Photo', (150, 150, 150)),

    'style_transfer.png': ('Style Transfer', 'Subject: Landscape, Action: Van Gogh Style', (218, 165, 32)),
    'style_transfer_source.png': ('Source: Landscape', 'Subject: Landscape Photo', (150, 150, 150)),

    'image_enhancement.png': ('Image Enhancement', 'Subject: Old Photo, Action: Upscale', (46, 139, 87)),
    'image_enhancement_source.png': ('Source: Old Photo', 'Subject: Low Res/Old Photo', (150, 150, 150)),

    'image_inpainting.png': ('Image Inpainting', 'Subject: Damaged Photo, Action: Restore', (255, 215, 0)),
    'image_inpainting_source.png': ('Source: Damaged', 'Subject: Damaged Photo', (150, 150, 150)),
}

for filename, (style_name, prompt, color) in scenarios.items():
    create_placeholder(f'商業應用場景/images/{filename}', style_name, prompt, color)
