import os

def create_svg(filename, text, color):
    # color is a tuple (r, g, b)
    hex_color = '#{:02x}{:02x}{:02x}'.format(*color)
    svg_content = f'''<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="{hex_color}" />
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Arial" font-size="24" fill="white">{text}</text>
</svg>'''
    
    with open(filename, 'w') as f:
        f.write(svg_content)

os.makedirs('常見的風格/images', exist_ok=True)

styles = {
    'impressionism.svg': ('Impressionism', (100, 149, 237)),
    'surrealism.svg': ('Surrealism', (255, 105, 180)),
    'abstract.svg': ('Abstract', (255, 69, 0)),
    'ukiyo_e.svg': ('Ukiyo-e', (218, 165, 32)),
    'art_nouveau.svg': ('Art Nouveau', (46, 139, 87)),
    'pop_art.svg': ('Pop Art', (255, 215, 0)),
    'cyberpunk.svg': ('Cyberpunk', (0, 255, 255)),
    'steampunk.svg': ('Steampunk', (139, 69, 19)),
    'pixel_art.svg': ('Pixel Art', (50, 205, 50)),
    'low_poly.svg': ('Low Poly', (70, 130, 180)),
    'vector_art.svg': ('Vector Art', (255, 140, 0)),
    'anime_manga.svg': ('Anime/Manga', (255, 192, 203)),
    'synthwave.svg': ('Synthwave', (148, 0, 211)),
    'cinematic_lighting.svg': ('Cinematic', (0, 0, 0)),
    'macro_photography.svg': ('Macro', (34, 139, 34)),
    'long_exposure.svg': ('Long Exposure', (72, 61, 139)),
    'bokeh.svg': ('Bokeh', (255, 228, 225)),
    'polaroid.svg': ('Polaroid', (245, 245, 220)),
    'drone_view.svg': ('Drone View', (135, 206, 235)),
    'unreal_engine_5.svg': ('UE5', (65, 105, 225)),
    'octane_render.svg': ('Octane', (128, 128, 128)),
    'isometric.svg': ('Isometric', (210, 105, 30)),
    'claymation.svg': ('Claymation', (205, 92, 92)),
    'origami.svg': ('Origami', (255, 250, 205)),
    'stained_glass.svg': ('Stained Glass', (123, 104, 238)),
    'watercolor.svg': ('Watercolor', (176, 224, 230)),
    'oil_painting.svg': ('Oil Painting', (160, 82, 45)),
    'ink_wash.svg': ('Ink Wash', (0, 0, 0)),
    'line_art.svg': ('Line Art', (100, 100, 100)),
    'concept_art.svg': ('Concept Art', (112, 128, 144)),
    'childrens_book.svg': ('Children Book', (255, 182, 193)),
}

for filename, (text, color) in styles.items():
    create_svg(f'常見的風格/images/{filename}', text, color)
