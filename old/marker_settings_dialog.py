# Marker Settings Dialog
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QPushButton, 
                             QLabel, QSlider, QCheckBox, QColorDialog)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
import sys
import os

from clickstep.config.settings import ClickMarkerSettings

class ClickMarkerSettingsDialog(QDialog):
    """Dialog to configure global click marker settings"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.settings = ClickMarkerSettings()
        self.setWindowTitle("Klickmarker-Einstellungen")
        self.setModal(True)
        self.resize(400, 350)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        
        # Color
        layout.addWidget(QLabel("<b>Farbe:</b>"))
        color_layout = QHBoxLayout()
        self.color_preview = QPushButton()
        self.color_preview.setFixedSize(100, 40)
        self.update_color_preview()
        self.color_preview.clicked.connect(self.choose_color)
        color_layout.addWidget(self.color_preview)
        color_layout.addWidget(QLabel("Klicken zum Ändern"))
        color_layout.addStretch()
        layout.addLayout(color_layout)
        
        # Size
        layout.addWidget(QLabel(f"<b>Größe:</b> {self.settings.size}px"))
        self.size_slider = QSlider(Qt.Orientation.Horizontal)
        self.size_slider.setRange(20, 80)
        self.size_slider.setValue(self.settings.size)
        self.size_slider.valueChanged.connect(self.update_size_label)
        layout.addWidget(self.size_slider)
        self.size_label = QLabel(f"Radius: {self.settings.size}px")
        layout.addWidget(self.size_label)
        
        # Border Width
        layout.addWidget(QLabel(f"<b>Randstärke:</b>"))
        self.border_slider = QSlider(Qt.Orientation.Horizontal)
        self.border_slider.setRange(1, 10)
        self.border_slider.setValue(self.settings.border_width)
        self.border_slider.valueChanged.connect(self.update_border_label)
        layout.addWidget(self.border_slider)
        self.border_label = QLabel(f"{self.settings.border_width}px")
        layout.addWidget(self.border_label)
        
        # Number Size
        layout.addWidget(QLabel(f"<b>Nummern-Schriftgröße:</b>"))
        self.number_slider = QSlider(Qt.Orientation.Horizontal)
        self.number_slider.setRange(8, 32)
        self.number_slider.setValue(self.settings.number_size)
        self.number_slider.valueChanged.connect(self.update_number_label)
        layout.addWidget(self.number_slider)
        self.number_label = QLabel(f"{self.settings.number_size}pt")
        layout.addWidget(self.number_label)
        
        # Glow Effect
        self.glow_checkbox = QCheckBox("Leuchteffekt anzeigen")
        self.glow_checkbox.setChecked(self.settings.show_glow)
        layout.addWidget(self.glow_checkbox)
        
        layout.addStretch()
        
        # Buttons
        button_layout = QHBoxLayout()
        btn_reset = QPushButton("Zurücksetzen")
        btn_reset.clicked.connect(self.reset_defaults)
        btn_save = QPushButton("Speichern")
        btn_save.clicked.connect(self.save_settings)
        btn_cancel = QPushButton("Abbrechen")
        btn_cancel.clicked.connect(self.reject)
        
        button_layout.addWidget(btn_reset)
        button_layout.addStretch()
        button_layout.addWidget(btn_cancel)
        button_layout.addWidget(btn_save)
        layout.addLayout(button_layout)
    
    def update_color_preview(self):
        self.color_preview.setStyleSheet(f"background-color: {self.settings.color.name()}; border: 2px solid #666;")
    
    def choose_color(self):
        color = QColorDialog.getColor(self.settings.color, self)
        if color.isValid():
            self.settings.color = color
            self.update_color_preview()
    
    def update_size_label(self, value):
        self.size_label.setText(f"Radius: {value}px")
    
    def update_border_label(self, value):
        self.border_label.setText(f"{value}px")
    
    def update_number_label(self, value):
        self.number_label.setText(f"{value}pt")
    
    def reset_defaults(self):
        self.settings.color = QColor(0, 168, 255)
        self.settings.size = 40
        self.settings.border_width = 3
        self.settings.show_glow = True
        self.settings.number_size = 16
        
        self.size_slider.setValue(40)
        self.border_slider.setValue(3)
        self.number_slider.setValue(16)
        self.glow_checkbox.setChecked(True)
        self.update_color_preview()
    
    def save_settings(self):
        self.settings.size = self.size_slider.value()
        self.settings.border_width = self.border_slider.value()
        self.settings.show_glow = self.glow_checkbox.isChecked()
        self.settings.number_size = self.number_slider.value()
        self.settings.save()
        
        # Update all existing markers in scene
        if self.parent() and hasattr(self.parent(), 'scene'):
            for item in self.parent().scene.items():
                if hasattr(item, 'item_type') and item.item_type == 'click':
                    item.prepareGeometryChange()
                    item.update()
        
        self.accept()
