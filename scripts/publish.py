#!/usr/bin/env python
"""Script to automate PyPI publishing process."""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, check=True):
    """Run a shell command and return the result."""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if check and result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(1)
    
    print(result.stdout)
    return result

def main():
    """Main publishing workflow."""
    print("🚀 Starting PyPI Publishing Process...\n")
    
    # Check if we're in the right directory
    if not Path("pyproject.toml").exists():
        print("Error: pyproject.toml not found. Are you in the project root?")
        sys.exit(1)
    
    # Step 1: Clean previous builds
    print("📧 Step 1: Cleaning previous builds...")
    for dir in ["dist", "build"]:
        if Path(dir).exists():
            run_command(f"rmdir /s /q {dir}" if os.name == 'nt' else f"rm -rf {dir}")
    
    # Clean egg-info directories
    for egg_info in Path(".").glob("*.egg-info"):
        run_command(f"rmdir /s /q {egg_info}" if os.name == 'nt' else f"rm -rf {egg_info}")
    
    # Step 2: Run tests
    print("\n🧪 Step 2: Running tests...")
    result = run_command("pytest tests/ -v", check=False)
    if result.returncode != 0:
        response = input("Tests failed. Continue anyway? (y/n): ")
        if response.lower() != 'y':
            sys.exit(1)
    
    # Step 3: Build the package
    print("\n📦 Step 3: Building the package...")
    run_command("python -m build")
    
    # Step 4: Check the distribution
    print("\n✅ Step 4: Checking distribution...")
    run_command("twine check dist/*")
    
    # Step 5: Ask for publishing target
    print("\n🎯 Step 5: Choose publishing target:")
    print("1. TestPyPI (recommended for first time)")
    print("2. PyPI (production)")
    choice = input("Enter choice (1 or 2): ")
    
    if choice == "1":
        print("\n📤 Publishing to TestPyPI...")
        run_command("twine upload --repository testpypi dist/*")
        print("\n✅ Published to TestPyPI!")
        print("Test installation with:")
        print("pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ langgraph-crosschain")
    elif choice == "2":
        confirm = input("\n⚠️  Are you sure you want to publish to production PyPI? (yes/no): ")
        if confirm.lower() == "yes":
            print("\n📤 Publishing to PyPI...")
            run_command("twine upload dist/*")
            print("\n✅ Published to PyPI!")
            print("Install with: pip install langgraph-crosschain")
        else:
            print("Publishing cancelled.")
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)
    
    print("\n🎉 Publishing process complete!")

if __name__ == "__main__":
    main()
