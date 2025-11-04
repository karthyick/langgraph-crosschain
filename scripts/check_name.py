#!/usr/bin/env python
"""Check if package name is available on PyPI."""

import requests
import sys

def check_pypi_name(package_name):
    """Check if a package name is available on PyPI."""
    
    # Check on PyPI
    pypi_url = f"https://pypi.org/project/{package_name}/"
    response = requests.get(pypi_url)
    
    if response.status_code == 404:
        print(f"✅ '{package_name}' is available on PyPI!")
        pypi_available = True
    else:
        print(f"❌ '{package_name}' is already taken on PyPI.")
        pypi_available = False
    
    # Check on TestPyPI
    test_pypi_url = f"https://test.pypi.org/project/{package_name}/"
    response = requests.get(test_pypi_url)
    
    if response.status_code == 404:
        print(f"✅ '{package_name}' is available on TestPyPI!")
        test_available = True
    else:
        print(f"⚠️ '{package_name}' is already taken on TestPyPI.")
        test_available = False
    
    return pypi_available, test_available

def suggest_alternatives(base_name):
    """Suggest alternative names if the base name is taken."""
    alternatives = [
        f"{base_name}-framework",
        f"{base_name}-lib",
        f"py{base_name}",
        f"{base_name}-extended",
        f"{base_name}-plus",
        base_name.replace("-", "_"),
        base_name.replace("langgraph-", "lg-"),
    ]
    
    print("\n🔍 Checking alternative names...")
    available = []
    
    for alt in alternatives:
        pypi_url = f"https://pypi.org/project/{alt}/"
        response = requests.get(pypi_url)
        if response.status_code == 404:
            available.append(alt)
            print(f"  ✅ {alt} - Available")
        else:
            print(f"  ❌ {alt} - Taken")
    
    return available

if __name__ == "__main__":
    package_name = "langgraph-crosschain"
    
    if len(sys.argv) > 1:
        package_name = sys.argv[1]
    
    print(f"\n🔍 Checking availability of '{package_name}'...\n")
    
    pypi_ok, test_ok = check_pypi_name(package_name)
    
    if not pypi_ok:
        print("\n💡 Suggestions:")
        available = suggest_alternatives(package_name)
        if available:
            print(f"\n✨ Available alternatives: {', '.join(available)}")
        else:
            print("\n💭 Consider a more unique name.")
    else:
        print(f"\n🎉 Great! '{package_name}' is available. You can proceed with publishing!")
