#!/usr/bin/env python3
"""
ClickStep Guide - Professional Screenshot Documentation Tool
Main entry point for the application

This file serves as the primary entry point and will gradually import
from the modular structure as we refactor the codebase.
"""
import sys
import os

# Add the parent directory to the path to allow imports from clickstep package
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# For now, import from the existing pro_recorder.py
# As we refactor, we'll gradually replace these imports
from pro_recorder import ProRecorder, QApplication, QIcon, resource_path


def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(resource_path("icon.ico")))
    
    window = ProRecorder()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
