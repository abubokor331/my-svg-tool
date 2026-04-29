# Professional SVG Generator for Microstock Platforms

A professional-grade web application that generates unique Abstract and Geometric SVG designs optimized for microstock platforms like Shutterstock and Adobe Stock.

## 🎯 Features

- **8 Geometric Pattern Types**: Circles grid, triangles mosaic, hexagons, waves, golden spiral, concentric circles, geometric flowers, diamond grid
- **5 Professional Palettes**: Corporate, Retro, Pastel, Luxury, Vibrant
- **Golden Ratio Integration**: Mathematical perfection in design proportions
- **Vector Perfect**: Clean SVG output with no messy paths
- **SEO Optimized**: Auto-generates 50 high-ranking keywords per design
- **Microstock Ready**: 3000x2000px and 2000x2000px resolutions
- **One-Click Generation**: Simple, intuitive interface

## 🚀 Quick Start

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`

## ☁️ FREE Deployment Options

### Option 1: Streamlit Cloud (RECOMMENDED - Easiest)

**Steps:**

1. **Create GitHub Repository**
   - Go to [github.com](https://github.com) and create a new repository
   - Upload these files: `app.py`, `requirements.txt`, `README.md`

2. **Deploy to Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository, branch (main), and main file (`app.py`)
   - Click "Deploy"

3. **Your Free URL**
   - You'll get a URL like: `https://yourname-svg-generator.streamlit.app`
   - 100% free, no credit card required
   - Auto-updates when you push to GitHub

**Custom Domain (Optional):**
- Streamlit Cloud provides free subdomains
- For custom domains, upgrade to Streamlit Cloud Teams ($20/month)

---

### Option 2: Vercel (Flask Alternative)

**Note:** Streamlit doesn't work on Vercel. For Vercel, you need a Flask version.

**Quick Flask Conversion:**

Create `flask_app.py`:

```python
from flask import Flask, render_template, request, send_file
import svgwrite
import random
import math
import io

app = Flask(__name__)

# Copy all generation functions from app.py here
# (draw_circles_grid, draw_triangles_mosaic, etc.)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    width = int(request.form.get('width', 3000))
    height = int(request.form.get('height', 2000))
    palette = request.form.get('palette', 'Corporate')
    
    svg_content, pattern_type, _ = generate_geometric_pattern(width, height, palette)
    
    return send_file(
        io.BytesIO(svg_content.encode()),
        mimetype='image/svg+xml',
        as_attachment=True,
        download_name=f'design_{pattern_type}.svg'
    )

if __name__ == '__main__':
    app.run(debug=True)
```

**Deploy to Vercel:**

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

**Vercel Configuration** (`vercel.json`):

```json
{
  "builds": [
    {
      "src": "flask_app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "flask_app.py"
    }
  ]
}
```

---

### Option 3: Render (Streamlit Compatible)

1. Create account at [render.com](https://render.com)
2. Click "New" → "Web Service"
3. Connect your GitHub repository
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
6. Free tier available

---

### Option 4: Hugging Face Spaces (AI Community)

1. Create account at [huggingface.co](https://huggingface.co)
2. Go to "Spaces" → "Create new Space"
3. Choose "Streamlit" as SDK
4. Upload your files
5. Free forever with GPU options available

---

## 📊 Resolution Options

- **3000x2000px**: Landscape format (standard for most microstock)
- **2000x2000px**: Square format (social media friendly)

Both formats are accepted by Shutterstock and Adobe Stock.

## 🎨 Color Palettes

1. **Corporate**: Professional blues, greens, oranges
2. **Retro**: Vintage warm tones
3. **Pastel**: Soft, gentle colors
4. **Luxury**: Elegant purples, reds, grays
5. **Vibrant**: Bright, energetic colors

## 📝 SEO Keywords

Each generated design comes with 50 optimized keywords including:
- Pattern-specific terms
- Color palette descriptors
- Microstock-friendly phrases
- Commercial use keywords

## 🎯 Microstock Upload Tips

1. **File Format**: SVG (vector) - perfect for scaling
2. **Resolution**: Use 3000x2000px for general use
3. **Keywords**: Use all 50 provided keywords
4. **Title**: "[Pattern Type] Abstract Geometric Design"
5. **Description**: "Professional vector design with golden ratio proportions"
6. **Categories**: Abstract, Backgrounds, Patterns

## 🛠️ Technical Stack

- **Python**: Core logic
- **Streamlit**: Web framework
- **svgwrite**: SVG generation
- **Mathematical Design**: Golden Ratio (Φ ≈ 1.618)

## 📦 File Structure

```
svg_generator/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🔧 Customization

### Add New Pattern Type

Edit `app.py` and add your function:

```python
def draw_custom_pattern(dwg, width, height, colors):
    # Your pattern logic here
    pass

# Add to pattern_type list in generate_geometric_pattern()
```

### Add New Color Palette

```python
PALETTES["YourPalette"] = [
    ["#COLOR1", "#COLOR2", "#COLOR3", "#COLOR4", "#COLOR5"],
]
```

## 💡 Usage Tips

1. **Generate Multiple**: Create 10-20 designs, pick the best
2. **Test Keywords**: Try variations of the auto-generated keywords
3. **Batch Upload**: Generate several designs before uploading
4. **Track Performance**: Monitor which patterns sell best

## 🚨 Important Notes

- **Commercial Use**: These designs are YOUR creation - you own the rights
- **Uniqueness**: Each generation is random - every design is unique
- **Quality**: Vector format ensures infinite scalability
- **No Gradients**: Clean paths only (microstock requirement)

## 📞 Support

For deployment issues:
- Streamlit Cloud: [docs.streamlit.io](https://docs.streamlit.io)
- Vercel: [vercel.com/docs](https://vercel.com/docs)
- Render: [render.com/docs](https://render.com/docs)

## 📈 Monetization Strategy

1. Generate 50-100 unique designs
2. Upload to multiple platforms:
   - Shutterstock
   - Adobe Stock
   - Freepik
   - Creative Market
3. Use consistent keywords
4. Track which styles perform best
5. Iterate based on sales data

## 🎓 Learning Resources

- **SVG Basics**: [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/SVG)
- **Golden Ratio in Design**: [Canva Design School](https://www.canva.com/learn/golden-ratio/)
- **Microstock Tips**: [Shutterstock Contributor Blog](https://www.shutterstock.com/blog)

---

**Ready to Generate Professional SVG Assets!** 🚀

Deploy to Streamlit Cloud for the easiest free hosting experience.
