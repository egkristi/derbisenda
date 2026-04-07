#!/usr/bin/env python3
"""Convert PDF files to Markdown with embedded images.

Usage:
    python src/pdf_to_markdown.py <input.pdf> [-o output.md] [--images-dir DIR]

Examples:
    python src/pdf_to_markdown.py document.pdf
    python src/pdf_to_markdown.py document.pdf -o tmp/converted/document.md
    python src/pdf_to_markdown.py document.pdf -o tmp/converted/doc.md --images-dir tmp/converted/images/doc

Requires: pip install pymupdf
"""

import argparse
import os
import re
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Error: PyMuPDF not available. Install with: pip install pymupdf", file=sys.stderr)
    sys.exit(1)


def sanitize_filename(name):
    """Make a safe filename from arbitrary text."""
    return re.sub(r'[^\w\-.]', '_', name)


def convert_pdf(pdf_path, images_dir=None, img_rel_path=None, min_img_size=50):
    """Convert a PDF to markdown, optionally extracting images.

    Args:
        pdf_path: Path to the PDF file.
        images_dir: Directory to save extracted images. None = skip images.
        img_rel_path: Relative path from the .md file to images_dir.
        min_img_size: Minimum pixel dimension to keep an image (skip icons).

    Returns:
        Tuple of (markdown_string, image_count).
    """
    doc = fitz.open(str(pdf_path))
    base_safe = sanitize_filename(Path(pdf_path).stem)

    lines = []
    img_count = 0

    for page_num in range(len(doc)):
        page = doc[page_num]

        lines.append(f"\n---\n\n## Side {page_num + 1}\n")

        # Extract images if an output dir is provided
        page_has_images = False
        if images_dir:
            images = page.get_images(full=True)

            if images:
                # Render full page as image
                img_count += 1
                page_img_name = f"{base_safe}_p{page_num+1:02d}_full.png"
                page_img_path = os.path.join(images_dir, page_img_name)
                mat = fitz.Matrix(150 / 72, 150 / 72)  # 150 DPI
                pix = page.get_pixmap(matrix=mat)
                pix.save(page_img_path)
                ref = f"{img_rel_path}/{page_img_name}" if img_rel_path else page_img_name
                lines.append(f"\n![Side {page_num+1}]({ref})\n")
                page_has_images = True
                pix = None

            # Extract individual images
            for img_info in images:
                xref = img_info[0]
                try:
                    pix = fitz.Pixmap(doc, xref)
                    if pix.width < min_img_size or pix.height < min_img_size:
                        pix = None
                        continue
                    if pix.n - pix.alpha > 3:  # CMYK -> RGB
                        pix = fitz.Pixmap(fitz.csRGB, pix)
                    img_count += 1
                    img_name = f"{base_safe}_p{page_num+1:02d}_img{img_count:03d}.png"
                    img_path = os.path.join(images_dir, img_name)
                    pix.save(img_path)
                    if pix.width > 200 and pix.height > 200:
                        ref = f"{img_rel_path}/{img_name}" if img_rel_path else img_name
                        lines.append(f"\n![Illustrasjon]({ref})\n")
                    pix = None
                except Exception:
                    pass

        # Extract text
        text = page.get_text("text").strip()
        if text:
            text = re.sub(r'\n{3,}', '\n\n', text)
            lines.append(f"\n{text}\n")

    doc.close()
    return "\n".join(lines).strip() + "\n", img_count


def main():
    parser = argparse.ArgumentParser(description="Convert PDF to Markdown with images")
    parser.add_argument("input", type=Path, help="Input PDF file")
    parser.add_argument("-o", "--output", type=Path, help="Output .md file (default: stdout)")
    parser.add_argument("--title", help="Top-level heading (default: filename stem)")
    parser.add_argument("--images-dir", type=Path, help="Directory for extracted images")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Error: {args.input} not found", file=sys.stderr)
        sys.exit(1)

    title = args.title if args.title is not None else args.input.stem

    # Determine image output directory
    images_dir = None
    img_rel_path = None
    if args.images_dir:
        images_dir = str(args.images_dir)
        os.makedirs(images_dir, exist_ok=True)
        if args.output:
            img_rel_path = os.path.relpath(images_dir, args.output.parent)

    md_body, img_count = convert_pdf(
        args.input, images_dir=images_dir, img_rel_path=img_rel_path
    )

    # Prepend title and source info
    header = f"# {title}\n\n*Kilde: {args.input.name} ({fitz.open(str(args.input)).page_count} sider)*\n"
    md = header + md_body

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(md, encoding="utf-8")
        print(f"Wrote {args.output} ({img_count} images)")
    else:
        print(md)


if __name__ == "__main__":
    main()
