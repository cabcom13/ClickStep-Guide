# Add spacer at end of update_properties
with open('g:/Neuer Ordner (3)/pro_recorder.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the line with status label in update_properties
for i, line in enumerate(lines):
    if 'self.props_layout.addWidget(QLabel(f"Status: {status}"))' in line:
        # Add spacer after status
        lines.insert(i + 1, '            \n')
        lines.insert(i + 2, '            # Add spacer to push content to top\n')
        lines.insert(i + 3, '            self.props_layout.addStretch()\n')
        print(f"Added spacer after line {i+1}")
        break

# Write back
with open('g:/Neuer Ordner (3)/pro_recorder.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Spacer added!")
