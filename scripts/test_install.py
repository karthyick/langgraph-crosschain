#!/usr/bin/env python
"""Test the package installation from TestPyPI or PyPI."""

import subprocess
import sys
import tempfile
import os
from pathlib import Path

def test_installation(source="testpypi"):
    """Test package installation in a clean virtual environment."""
    
    with tempfile.TemporaryDirectory() as tmpdir:
        venv_path = Path(tmpdir) / "test_venv"
        
        print(f"📦 Creating virtual environment at {venv_path}...")
        subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True)
        
        # Determine the pip path based on OS
        if os.name == 'nt':
            pip_path = venv_path / "Scripts" / "pip.exe"
            python_path = venv_path / "Scripts" / "python.exe"
        else:
            pip_path = venv_path / "bin" / "pip"
            python_path = venv_path / "bin" / "python"
        
        # Install the package
        print(f"\n📥 Installing langgraph-crosschain from {source}...")
        
        if source == "testpypi":
            cmd = [
                str(pip_path), "install",
                "--index-url", "https://test.pypi.org/simple/",
                "--extra-index-url", "https://pypi.org/simple/",
                "langgraph-crosschain"
            ]
        else:
            cmd = [str(pip_path), "install", "langgraph-crosschain"]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"❌ Installation failed:\n{result.stderr}")
            return False
        
        print("✅ Installation successful!")
        
        # Test imports
        print("\n🧪 Testing imports...")
        test_code = '''
import sys
try:
    from langgraph_crosschain import ChainRegistry, CrossChainNode, MessageRouter, SharedStateManager
    print("✅ All imports successful!")
    
    # Test basic functionality
    registry = ChainRegistry()
    print("✅ ChainRegistry instantiated")
    
    manager = SharedStateManager()
    print("✅ SharedStateManager instantiated")
    
    router = MessageRouter()
    print("✅ MessageRouter instantiated")
    
    print("\n✨ Package is working correctly!")
    sys.exit(0)
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
'''
        
        result = subprocess.run(
            [str(python_path), "-c", test_code],
            capture_output=True,
            text=True
        )
        
        print(result.stdout)
        if result.stderr:
            print(f"Errors:\n{result.stderr}")
        
        return result.returncode == 0

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Test package installation")
    parser.add_argument(
        "--source",
        choices=["testpypi", "pypi"],
        default="testpypi",
        help="Source to install from"
    )
    
    args = parser.parse_args()
    
    print(f"\n🚀 Testing installation from {args.source.upper()}\n")
    print("=" * 50)
    
    if test_installation(args.source):
        print("\n🎉 All tests passed! Package is ready for use.")
        sys.exit(0)
    else:
        print("\n❌ Tests failed. Please check the package.")
        sys.exit(1)
