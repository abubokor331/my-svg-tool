import streamlit as st
import svgwrite
import random
import math
import io
import json
from datetime import datetime

# Professional Color Palettes
PALETTES = {
    "Corporate": [
        ["#1E3A8A", "#3B82F6", "#60A5FA", "#93C5FD", "#DBEAFE"],
        ["#065F46", "#10B981", "#34D399", "#6EE7B7", "#D1FAE5"],
        ["#7C2D12", "#EA580C", "#FB923C", "#FDBA74", "#FED7AA"],
    ],
    "Retro": [
        ["#FFC300", "#FF5733", "#C70039", "#900C3F", "#581845"],
        ["#FF6B6B", "#4ECDC4", "#45B7D1", "#FFA07A", "#98D8C8"],
        ["#E63946", "#F1FAEE", "#A8DADC", "#457B9D", "#1D3557"],
    ],
    "Pastel": [
        ["#FFE5E5", "#FFF0F0", "#E5F3FF", "#FFF5E5", "#F0E5FF"],
        ["#FFB3BA", "#FFDFBA", "#FFFFBA", "#BAFFC9", "#BAE1FF"],
        ["#FADADD", "#E0BBE4", "#957DAD", "#D291BC", "#FEC8D8"],
    ],
    "Luxury": [
        ["#2C3E50", "#34495E", "#95A5A6", "#BDC3C7", "#ECF0F1"],
        ["#8E44AD", "#9B59B6", "#BB8FCE", "#D7BDE2", "#F4ECF7"],
        ["#C0392B", "#E74C3C", "#EC7063", "#F1948A", "#F5B7B1"],
    ],
    "Vibrant": [
        ["#FF6B9D", "#C44569", "#FFA502", "#F79F1F", "#EE5A6F"],
        ["#00D2FF", "#3498DB", "#9B59B6", "#E056FD", "#686DE0"],
        ["#20BF6B", "#26DE81", "#FED330", "#FACC15", "#F59E0B"],
    ],
}

PHI = (1 + math.sqrt(5)) / 2  # Golden Ratio

def generate_geometric_pattern(width=3000, height=2000, palette_name="Corporate"):
    """Generate professional geometric SVG pattern"""
    
    # Select random palette
    palette = random.choice(PALETTES[palette_name])
    bg_color = palette[0]
    colors = palette[1:]
    
    dwg = svgwrite.Drawing(size=(f"{width}px", f"{height}px"))
    dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill=bg_color))
    
    pattern_type = random.choice([
        "circles_grid",
        "triangles_mosaic",
        "hexagons",
        "waves",
        "golden_spiral",
        "concentric_circles",
        "geometric_flowers",
        "diamond_grid"
    ])
    
    if pattern_type == "circles_grid":
        draw_circles_grid(dwg, width, height, colors)
    elif pattern_type == "triangles_mosaic":
        draw_triangles_mosaic(dwg, width, height, colors)
    elif pattern_type == "hexagons":
        draw_hexagons(dwg, width, height, colors)
    elif pattern_type == "waves":
        draw_waves(dwg, width, height, colors)
    elif pattern_type == "golden_spiral":
        draw_golden_spiral(dwg, width, height, colors)
    elif pattern_type == "concentric_circles":
        draw_concentric_circles(dwg, width, height, colors)
    elif pattern_type == "geometric_flowers":
        draw_geometric_flowers(dwg, width, height, colors)
    elif pattern_type == "diamond_grid":
        draw_diamond_grid(dwg, width, height, colors)
    
    return dwg.tostring(), pattern_type, palette_name

def draw_circles_grid(dwg, width, height, colors):
    """Grid of overlapping circles with golden ratio spacing"""
    spacing = int(width / (PHI * 6))
    for x in range(0, width + spacing, spacing):
        for y in range(0, height + spacing, spacing):
            radius = random.randint(spacing // 3, spacing // 2)
            color = random.choice(colors)
            opacity = random.uniform(0.6, 0.9)
            dwg.add(dwg.circle(center=(x, y), r=radius, fill=color, opacity=opacity))

def draw_triangles_mosaic(dwg, width, height, colors):
    """Mosaic of geometric triangles"""
    triangle_size = int(width / 15)
    for x in range(0, width, triangle_size):
        for y in range(0, height, triangle_size):
            color = random.choice(colors)
            opacity = random.uniform(0.7, 0.95)
            
            if random.choice([True, False]):
                points = [(x, y), (x + triangle_size, y), (x + triangle_size // 2, y + triangle_size)]
            else:
                points = [(x, y), (x + triangle_size, y + triangle_size), (x, y + triangle_size)]
            
            dwg.add(dwg.polygon(points=points, fill=color, opacity=opacity))

def draw_hexagons(dwg, width, height, colors):
    """Hexagonal pattern with golden ratio"""
    hex_size = int(width / (PHI * 8))
    for row in range(-1, int(height / (hex_size * 1.5)) + 2):
        for col in range(-1, int(width / (hex_size * math.sqrt(3))) + 2):
            x = col * hex_size * math.sqrt(3)
            if row % 2 == 1:
                x += hex_size * math.sqrt(3) / 2
            y = row * hex_size * 1.5
            
            hexagon = []
            for i in range(6):
                angle = math.radians(60 * i)
                px = x + hex_size * math.cos(angle)
                py = y + hex_size * math.sin(angle)
                hexagon.append((px, py))
            
            color = random.choice(colors)
            opacity = random.uniform(0.65, 0.9)
            dwg.add(dwg.polygon(points=hexagon, fill=color, opacity=opacity, 
                               stroke="none"))

def draw_waves(dwg, width, height, colors):
    """Flowing wave patterns"""
    wave_height = height // 8
    num_waves = 6
    
    for i in range(num_waves):
        y_offset = (height / num_waves) * i
        amplitude = random.randint(wave_height // 2, wave_height)
        frequency = random.uniform(0.002, 0.005)
        
        path_data = f"M 0,{y_offset}"
        for x in range(0, width, 10):
            y = y_offset + amplitude * math.sin(frequency * x)
            path_data += f" L {x},{y}"
        path_data += f" L {width},{height} L 0,{height} Z"
        
        color = random.choice(colors)
        opacity = random.uniform(0.5, 0.8)
        dwg.add(dwg.path(d=path_data, fill=color, opacity=opacity))

def draw_golden_spiral(dwg, width, height, colors):
    """Golden ratio spiral with geometric elements"""
    center_x, center_y = width // 2, height // 2
    
    for i in range(12):
        angle = i * (360 / PHI)
        radius = (i + 1) * (min(width, height) / 30)
        
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        
        size = radius / PHI
        color = random.choice(colors)
        opacity = random.uniform(0.6, 0.85)
        
        if i % 2 == 0:
            dwg.add(dwg.circle(center=(x, y), r=size, fill=color, opacity=opacity))
        else:
            dwg.add(dwg.rect(insert=(x - size, y - size), size=(size * 2, size * 2), 
                           fill=color, opacity=opacity))

def draw_concentric_circles(dwg, width, height, colors):
    """Concentric circles with golden ratio sizing"""
    center_x, center_y = width // 2, height // 2
    max_radius = min(width, height) // 2
    
    num_circles = 15
    for i in range(num_circles):
        radius = max_radius * (1 - i / (num_circles * PHI))
        color = colors[i % len(colors)]
        opacity = random.uniform(0.5, 0.85)
        dwg.add(dwg.circle(center=(center_x, center_y), r=radius, 
                          fill="none", stroke=color, stroke_width=radius / 10, 
                          opacity=opacity))

def draw_geometric_flowers(dwg, width, height, colors):
    """Flower patterns using circles and symmetry"""
    num_flowers = 12
    for _ in range(num_flowers):
        cx = random.randint(0, width)
        cy = random.randint(0, height)
        petal_count = random.choice([5, 6, 8])
        petal_size = random.randint(80, 150)
        
        color = random.choice(colors)
        opacity = random.uniform(0.6, 0.85)
        
        for i in range(petal_count):
            angle = (360 / petal_count) * i
            x = cx + petal_size * math.cos(math.radians(angle))
            y = cy + petal_size * math.sin(math.radians(angle))
            dwg.add(dwg.circle(center=(x, y), r=petal_size // 2, 
                             fill=color, opacity=opacity))

def draw_diamond_grid(dwg, width, height, colors):
    """Diamond/rhombus grid pattern"""
    diamond_size = int(width / 12)
    for x in range(0, width, diamond_size):
        for y in range(0, height, diamond_size):
            color = random.choice(colors)
            opacity = random.uniform(0.65, 0.9)
            
            points = [
                (x + diamond_size // 2, y),
                (x + diamond_size, y + diamond_size // 2),
                (x + diamond_size // 2, y + diamond_size),
                (x, y + diamond_size // 2)
            ]
            dwg.add(dwg.polygon(points=points, fill=color, opacity=opacity))

def generate_seo_keywords(pattern_type, palette_name):
    """Generate 50 SEO-optimized keywords for microstock"""
    
    base_keywords = [
        "abstract geometric pattern", "vector background", "modern design", 
        "geometric shapes", "abstract art", "digital illustration",
        "minimalist pattern", "contemporary design", "vector graphic",
        "seamless pattern", "geometric background", "modern abstract"
    ]
    
    pattern_keywords = {
        "circles_grid": ["circle pattern", "dots background", "bubble design"],
        "triangles_mosaic": ["triangle pattern", "polygon design", "mosaic art"],
        "hexagons": ["hexagon pattern", "honeycomb design", "geometric tiles"],
        "waves": ["wave pattern", "flowing lines", "organic shapes"],
        "golden_spiral": ["spiral design", "golden ratio", "fibonacci pattern"],
        "concentric_circles": ["concentric design", "radial pattern", "circular"],
        "geometric_flowers": ["floral geometric", "symmetrical design", "mandala"],
        "diamond_grid": ["diamond pattern", "rhombus design", "grid background"]
    }
    
    palette_keywords = {
        "Corporate": ["business", "professional", "corporate", "blue", "formal"],
        "Retro": ["vintage", "retro", "70s style", "nostalgic", "classic"],
        "Pastel": ["soft colors", "gentle", "feminine", "light", "delicate"],
        "Luxury": ["elegant", "premium", "sophisticated", "classy", "refined"],
        "Vibrant": ["colorful", "bright", "energetic", "vivid", "dynamic"]
    }
    
    descriptive = [
        "high quality", "commercial use", "print ready", "scalable vector",
        "web design", "graphic design", "texture", "wallpaper", "backdrop",
        "creative", "artistic", "trendy", "stylish", "clean", "simple"
    ]
    
    keywords = base_keywords.copy()
    keywords.extend(pattern_keywords.get(pattern_type, []))
    keywords.extend(palette_keywords.get(palette_name, []))
    keywords.extend(descriptive)
    keywords.extend([
        "SVG", "EPS compatible", "Adobe Stock", "Shutterstock", 
        "illustration", "decoration", "layout", "composition",
        "symmetrical", "balanced", "harmonious", "aesthetic"
    ])
    
    # Ensure exactly 50 keywords
    while len(keywords) < 50:
        keywords.append(f"{random.choice(['abstract', 'geometric', 'modern', 'vector'])} design {len(keywords)}")
    
    return keywords[:50]

# Streamlit App
st.set_page_config(page_title="Professional SVG Generator", page_icon="🎨", layout="wide")

st.title("🎨 Professional Abstract & Geometric SVG Generator")
st.markdown("**Optimized for Microstock Platforms** | Shutterstock & Adobe Stock Ready")

# Sidebar Controls
st.sidebar.header("⚙️ Generation Settings")
resolution = st.sidebar.selectbox(
    "Resolution",
    ["3000x2000px (Landscape)", "2000x2000px (Square)"],
    index=0
)

palette_choice = st.sidebar.selectbox(
    "Color Palette",
    list(PALETTES.keys())
)

st.sidebar.markdown("---")
st.sidebar.info("""
**Features:**
- ✅ Vector-ready SVG format
- ✅ Golden Ratio proportions
- ✅ Professional color palettes
- ✅ 50 SEO keywords included
- ✅ Microstock optimized
""")

# Main Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🖼️ Live Preview")
    preview_container = st.empty()

with col2:
    st.subheader("📥 Download & Keywords")
    
    if st.button("🎲 Generate New Design", type="primary", use_container_width=True):
        with st.spinner("Generating professional SVG..."):
            # Parse resolution
            if "3000x2000" in resolution:
                w, h = 3000, 2000
            else:
                w, h = 2000, 2000
            
            # Generate SVG
            svg_content, pattern_type, palette_used = generate_geometric_pattern(w, h, palette_choice)
            
            # Store in session state
            st.session_state.svg = svg_content
            st.session_state.pattern = pattern_type
            st.session_state.palette = palette_used
            st.session_state.keywords = generate_seo_keywords(pattern_type, palette_used)
            st.session_state.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Display if generated
if 'svg' in st.session_state:
    with col1:
        preview_container.image(st.session_state.svg.encode(), use_container_width=True)
    
    with col2:
        # Download button
        st.download_button(
            label="⬇️ Download SVG",
            data=st.session_state.svg,
            file_name=f"abstract_geometric_{st.session_state.timestamp}.svg",
            mime="image/svg+xml",
            use_container_width=True
        )
        
        st.success(f"**Pattern:** {st.session_state.pattern.replace('_', ' ').title()}")
        st.info(f"**Palette:** {st.session_state.palette}")
        
        # Keywords section
        st.markdown("### 📋 SEO Keywords (50)")
        keywords_text = ", ".join(st.session_state.keywords)
        st.text_area("Copy these keywords:", keywords_text, height=200)
        
        # Download keywords as TXT
        st.download_button(
            label="📄 Download Keywords (TXT)",
            data=keywords_text,
            file_name=f"keywords_{st.session_state.timestamp}.txt",
            mime="text/plain",
            use_container_width=True
        )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p><strong>Professional SVG Generator v1.0</strong></p>
    <p>Designed for Microstock Success | Vector Perfect | SEO Optimized</p>
</div>
""", unsafe_allow_html=True)
