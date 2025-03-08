#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Build script to create an executable using PyInstaller.
"""

import os
import subprocess
import sys
import shutil
import datetime

def build_executable():
    """Build the executable using PyInstaller."""
    print("Building Calculate Age executable...")
    
    # Get the root directory
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    # Set paths
    src_dir = os.path.join(root_dir, 'src')
    build_dir = os.path.join(root_dir, '.build')
    dist_dir = os.path.join(root_dir, 'dist')
    
    # Ensure we're using the correct python executable (virtual env if available)
    python_exe = sys.executable
    
    # Build command
    cmd = [
        python_exe, 
        '-m', 'PyInstaller',
        '--noconfirm',
        '--onefile',
        '--windowed',
        '--name', 'CalculateAge',
        os.path.join(src_dir, 'calculate_age.py')
    ]
    
    # Run the build
    subprocess.run(cmd, check=True)
    
    # Create version from date if no version specified
    version = f"v{datetime.datetime.now().strftime('%Y.%m.%d')}"
    
    # Create zip archive
    zip_name = f"Calculateage-{version}.zip"
    shutil.make_archive(
        os.path.join(root_dir, f"Calculateage-{version}"),
        'zip',
        dist_dir
    )
    
    print(f"Build completed: {zip_name}")
    
if __name__ == "__main__":
    build_executable() 