"""Renders a plain Gmail-message-view screenshot (PNG) from arbitrary email content,
so an OCR/vision step downstream has something realistic to read. Content is supplied
entirely by the caller - this script has no data of its own, dummy or otherwise.

Usage: python3 generate_email_screenshot.py <input_data.json> <output.png>

Input JSON shape: {"subject": str, "sender_name": str|null, "sender_email": str,
"body": str (newlines as real \n or literal "\n")}
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 760, 420
BG = (255, 255, 255)
HEADER_BG = (245, 245, 245)
TEXT = (32, 33, 36)
SUBTLE = (95, 99, 104)


def pick_font(size):
    candidates = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "C:\\Windows\\Fonts\\arial.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return ImageFont.load_default()


def render(data, out_path):
    subject = data.get("subject") or ""
    sender_name = data.get("sender_name") or "Unknown sender"
    sender_email = data.get("sender_email") or ""
    body = data.get("body") or ""
    body_lines = body.split("\n")

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 56], fill=HEADER_BG)
    d.text((20, 18), subject, font=pick_font(20), fill=TEXT)
    d.line([0, 56, W, 56], fill=(220, 220, 220), width=1)
    d.text((20, 72), f"{sender_name}  <{sender_email}>", font=pick_font(14), fill=SUBTLE)
    d.line([0, 100, W, 100], fill=(230, 230, 230), width=1)
    y = 130
    body_font = pick_font(15)
    for line in body_lines:
        d.text((24, y), line, font=body_font, fill=TEXT)
        y += 30
        if y > H - 20:
            break
    img.save(out_path)


def main():
    if len(sys.argv) != 3:
        print("usage: generate_email_screenshot.py <input_data.json> <output.png>", file=sys.stderr)
        sys.exit(2)
    with open(sys.argv[1], "r") as f:
        data = json.load(f)
    render(data, sys.argv[2])


if __name__ == "__main__":
    main()
