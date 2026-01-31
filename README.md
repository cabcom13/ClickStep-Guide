# AutoGuide Pro

**AutoGuide Pro** is a high-performance, professional documentation and screen recording system designed for creating high-quality, step-by-step instructions and guides. With a Photoshop-style non-destructive editor, it allows for seamless annotation, blurring, and magnification of screen captures.

## 🚀 Key Features

- **Professional Recording**: Capture screen actions with intelligent step detection.
- **Photoshop-Style Editor**: Advanced graphics scene with layers and non-destructive editing.
- **Advanced Annotations**:
  - **Blur/Censure**: Protect sensitive data with adjustable Gaussian blur areas.
  - **Zoom/Magnify**: Highlight specific details with interactive zoom boxes and target markers.
  - **Editable Text**: Add professional typography with customizable fonts and colors.
  - **Click Markers**: Automatically numbered markers for precise step indication.
- **Global Editing**: Apply crops or blur layers globally across all steps in a project.
- **Modern UI**: Dark mode, glassmorphism-inspired elements, and a smooth, responsive experience.
- **Export Options**: Export your guides to professional Word documents (integration with `python-docx`).

## 🛠 Technology Stack

- **Core**: Python 3.x
- **UI Framework**: PyQt6
- **Computer Vision**: OpenCV, NumPy
- **Image Processing**: Pillow (PIL)
- **Input Handling**: pynput
- **Document Export**: python-docx

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd autoguide-pro
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🖥 Usage

Run the application:
```bash
python pro_recorder.py
```

## 🎨 Design Philosophy

AutoGuide Pro aims for a **premium aesthetic** and **intuitive UX**. The editor provides a powerful workspace reminiscent of professional design software while remaining specialized for documentation tasks.

---

*Part of the Advanced Agentic Coding Project.*
