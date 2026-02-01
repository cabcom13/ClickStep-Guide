# Quick fix script to add the missing signal connection
import sys

# Read the file
with open('g:/Neuer Ordner (3)/pro_recorder.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the line with "self.setup_ui()"
for i, line in enumerate(lines):
    if 'self.setup_ui()' in line and i > 1200 and i < 1300:
        # Insert the signal connection after setup_ui
        lines.insert(i + 1, '        \n')
        lines.insert(i + 2, '        # CRITICAL: Connect selection changes to properties panel updates\n')
        lines.insert(i + 3, '        self.scene.selectionChanged.connect(self.update_properties)\n')
        print(f"Added signal connection after line {i+1}")
        break

# Write back
with open('g:/Neuer Ordner (3)/pro_recorder.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("File updated successfully!")
