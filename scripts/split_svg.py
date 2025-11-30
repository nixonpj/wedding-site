#!/usr/bin/env python3
"""
Split SVG file into individual elements by ID
Usage: python3 split_svg.py input.svg
"""

import sys
import re
from xml.etree import ElementTree as ET

def extract_element_by_id(svg_file, element_id, output_file):
    """Extract a specific element by ID and save as new SVG"""
    tree = ET.parse(svg_file)
    root = tree.getroot()
    
    # Find the element with the given ID
    namespace = {'svg': 'http://www.w3.org/2000/svg'}
    element = root.find(f".//*[@id='{element_id}']", namespace)
    
    if element is None:
        # Try without namespace
        for elem in root.iter():
            if elem.get('id') == element_id:
                element = elem
                break
    
    if element is None:
        print(f"Element with id '{element_id}' not found")
        return False
    
    # Create new SVG with the extracted element
    new_root = ET.Element('svg')
    new_root.set('xmlns', 'http://www.w3.org/2000/svg')
    new_root.set('xmlns:xlink', 'http://www.w3.org/1999/xlink')
    new_root.set('viewBox', root.get('viewBox', '0 0 800 600'))
    
    # Copy the element
    new_root.append(element)
    
    # Write to file
    tree = ET.ElementTree(new_root)
    ET.indent(tree, space="  ")
    tree.write(output_file, encoding='utf-8', xml_declaration=True)
    print(f"Extracted '{element_id}' to {output_file}")
    return True

def list_all_ids(svg_file):
    """List all element IDs in the SVG"""
    tree = ET.parse(svg_file)
    root = tree.getroot()
    
    ids = []
    for elem in root.iter():
        elem_id = elem.get('id')
        if elem_id:
            ids.append(elem_id)
    
    return ids

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 split_svg.py <svg_file> [element_id]")
        print("\nTo list all IDs:")
        print("  python3 split_svg.py <svg_file>")
        sys.exit(1)
    
    svg_file = sys.argv[1]
    
    if len(sys.argv) == 2:
        # List all IDs
        print("Elements with IDs in the SVG:")
        ids = list_all_ids(svg_file)
        for elem_id in ids:
            print(f"  - {elem_id}")
    else:
        # Extract specific element
        element_id = sys.argv[2]
        output_file = f"{element_id}.svg"
        extract_element_by_id(svg_file, element_id, output_file)

