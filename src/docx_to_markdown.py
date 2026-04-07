#!/usr/bin/env python3
"""Convert Word documents (.docx) to Markdown using pandoc.

Usage:
    python src/docx_to_markdown.py <input.docx> [-o output-dir]

Examples:
    python src/docx_to_markdown.py ~/Downloads/document.docx
    python src/docx_to_markdown.py ~/Downloads/document.docx -o ./custom-dir
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename by removing/replacing whitespaces and special characters.
    
    Args:
        filename: Original filename (without extension)
    
    Returns:
        Sanitized filename safe for filesystems and URLs
    """
    # Replace whitespace with hyphens
    sanitized = re.sub(r'\s+', '-', filename)
    # Remove special characters except hyphens, underscores, and alphanumeric
    sanitized = re.sub(r'[^a-zA-Z0-9\-_]', '', sanitized)
    # Remove multiple consecutive hyphens
    sanitized = re.sub(r'-+', '-', sanitized)
    # Remove leading/trailing hyphens
    sanitized = sanitized.strip('-')
    return sanitized


def import_docx(input_file: Path, output_dir: Path = Path("import")) -> tuple[bool, str]:
    """
    Import a Word document to Markdown using pandoc.
    
    Args:
        input_file: Path to the input .docx file
        output_dir: Directory where output files will be created (default: import/)
    
    Returns:
        Tuple of (success: bool, message: str)
    """
    # Validate input file
    if not input_file.exists():
        return False, f"Error: Input file not found: {input_file}"
    
    if input_file.suffix.lower() != ".docx":
        return False, f"Error: Input file must be a .docx file, got: {input_file.suffix}"
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Extract base filename (without extension) and sanitize
    original_name = input_file.stem
    base_name = sanitize_filename(original_name)
    
    # Define output paths
    output_md = output_dir / f"{base_name}.md"
    media_dir = output_dir / base_name
    
    # Show sanitization if name changed
    if base_name != original_name:
        print(f"Sanitized filename: '{original_name}' -> '{base_name}'")
    
    # Build pandoc command
    # Use relative path for media extraction so links work correctly
    # When running from output_dir, use just the filename for output
    cmd = [
        "pandoc",
        "-o", f"{base_name}.md",
        "--extract-media", f"./{base_name}",
        str(input_file.expanduser())
    ]
    
    print(f"Converting: {input_file.name}")
    print(f"Output MD:  {output_md}")
    print(f"Media dir:  {media_dir}")
    print(f"\nRunning: {' '.join(cmd)}")
    print(f"Working directory: {output_dir.absolute()}\n")
    
    try:
        # Run pandoc from the output directory for correct relative paths
        result = subprocess.run(
            cmd,
            cwd=output_dir,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Check if output file was created
        if output_md.exists():
            file_size = output_md.stat().st_size
            success_msg = f"✅ Success! Created {output_md} ({file_size:,} bytes)"
            
            # Check if media was extracted
            if media_dir.exists():
                media_files = list(media_dir.rglob("*"))
                media_count = len([f for f in media_files if f.is_file()])
                success_msg += f"\n   Extracted {media_count} media file(s) to {media_dir}/"
            
            return True, success_msg
        else:
            return False, "Error: Output file was not created"
            
    except subprocess.CalledProcessError as e:
        error_msg = f"❌ Pandoc failed with exit code {e.returncode}"
        if e.stderr:
            error_msg += f"\n\nError output:\n{e.stderr}"
        return False, error_msg
    
    except FileNotFoundError:
        return False, "❌ Error: pandoc command not found. Install with: brew install pandoc"


def main():
    parser = argparse.ArgumentParser(
        description="Convert Word documents to Markdown using pandoc",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python src/docx_to_markdown.py ~/Downloads/document.docx
  python src/docx_to_markdown.py document.docx -o ./custom
        """
    )
    
    parser.add_argument(
        "input_file",
        type=Path,
        help="Path to input .docx file (e.g., ~/Downloads/document.docx)"
    )
    
    parser.add_argument(
        "-o", "--output-dir",
        type=Path,
        default=Path("import"),
        help="Output directory for markdown and media files (default: import/)"
    )
    
    args = parser.parse_args()
    
    # Expand ~ in input file path
    input_file = args.input_file.expanduser()
    
    # Run conversion
    success, message = import_docx(input_file, args.output_dir)
    
    print(f"\n{message}")
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
