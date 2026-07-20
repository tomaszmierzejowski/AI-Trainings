import os
import sys

# Allow running from any directory by adding carousels/ to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from brand import (
    PURPLE_DARK, ORANGE, WHITE, LIGHT_BG, DARK_BG,
    FONT_HEADLINE, FONT_SUBHEAD, FONT_BODY, FONT_SMALL,
    SLIDE_W, SLIDE_H, PADDING,
)
from PIL import Image, ImageDraw, ImageFont


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def load_font(size):
    candidates = [
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibri.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def draw_centered(draw, text, y, font, color, width=1080, padding=80):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    x = max(padding, (width - text_w) // 2)
    draw.text((x, y), text, font=font, fill=color)


def draw_wrapped(draw, text, x, y, max_width, font, color):
    words = text.split()
    line = ""
    line_height = font.size + 8
    for word in words:
        test = line + word + " "
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] > max_width and line:
            draw.text((x, y), line.rstrip(), font=font, fill=color)
            y += line_height
            line = word + " "
        else:
            line = test
    if line.strip():
        draw.text((x, y), line.rstrip(), font=font, fill=color)
    return y + line_height


def new_slide(bg_color):
    img = Image.new("RGB", (SLIDE_W, SLIDE_H), hex_rgb(bg_color))
    draw = ImageDraw.Draw(img)
    return img, draw


def save(img, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path)


# ---------------------------------------------------------------------------
# Resolve base output directory relative to this script
# ---------------------------------------------------------------------------

BASE = os.path.dirname(os.path.abspath(__file__))
# carousels/ lives inside LinkedIn_Campaign/carousels/
# output dirs are siblings of carousels/ under LinkedIn_Campaign/
CAMPAIGN = os.path.dirname(BASE)   # LinkedIn_Campaign/
POST1_DIR = os.path.join(CAMPAIGN, "carousels", "post1_alarm")
POST4_DIR = os.path.join(CAMPAIGN, "carousels", "post4_scale")
POST7_DIR = os.path.join(CAMPAIGN, "carousels", "post7_reckoning")
GRAPHICS_DIR = os.path.join(CAMPAIGN, "graphics")


# ===========================================================================
# POST 1 — THE ALARM (10 slides)
# ===========================================================================

def post1_slide01():
    img, draw = new_slide(DARK_BG)
    draw_centered(draw, "THE CODE NOBODY READ", 120, load_font(22), hex_rgb(ORANGE))
    draw_centered(draw, "Every assessment", 300, load_font(72), hex_rgb(WHITE))
    draw_centered(draw, "described a story", 400, load_font(72), hex_rgb(WHITE))
    draw_centered(draw, "about your code.", 500, load_font(72), hex_rgb(WHITE))
    draw_centered(draw, "Nobody actually read it.", 700, load_font(48), hex_rgb(ORANGE))
    draw_centered(draw, "Swipe to see what reading everything finds →", 880, load_font(22), hex_rgb(WHITE))
    return img


def post1_slide02():
    img, draw = new_slide(LIGHT_BG)
    draw_centered(draw, "THE PROBLEM", 120, load_font(22), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Enterprise discovery", 260, load_font(60), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "samples 10–15%", 340, load_font(60), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "of your codebase.", 420, load_font(60), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Interviews. Documentation.", 580, load_font(36), hex_rgb(ORANGE))
    draw_centered(draw, "Sampling. Eight weeks.", 640, load_font(36), hex_rgb(ORANGE))
    draw_centered(draw, "The findings are approximately true.", 750, load_font(28), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "“Approximately” is doing", 810, load_font(36), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "enormous work.", 860, load_font(36), hex_rgb(PURPLE_DARK))
    return img


def post1_slide03():
    img, draw = new_slide(DARK_BG)
    draw_centered(draw, "WHAT FULL ANALYSIS FOUND", 120, load_font(22), hex_rgb(ORANGE))
    draw_centered(draw, "529", 260, load_font(180), hex_rgb(ORANGE))
    draw_centered(draw, "API endpoints", 480, load_font(48), hex_rgb(WHITE))
    draw_centered(draw, "with no authentication.", 550, load_font(48), hex_rgb(WHITE))
    draw_centered(draw, "One enterprise platform.", 700, load_font(28), hex_rgb(WHITE))
    draw_centered(draw, "No production access.", 750, load_font(28), hex_rgb(WHITE))
    draw_centered(draw, "Just reading the code.", 800, load_font(28), hex_rgb(WHITE))
    draw_centered(draw, "Source: ComplianceIssuesSummary lines 29, 54, 336, 434", 900, load_font(22), hex_rgb(ORANGE))
    return img


def post1_slide04():
    img, draw = new_slide(LIGHT_BG)
    draw_centered(draw, "WHAT FULL ANALYSIS FOUND", 120, load_font(22), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "98", 260, load_font(180), hex_rgb(ORANGE))
    draw_centered(draw, "integration connections", 480, load_font(48), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "documented as 30.", 550, load_font(48), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Seven protocols.", 700, load_font(28), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "None of it in the diagrams.", 750, load_font(28), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Source: MASTER_CONSOLIDATED_REPORT line 478", 900, load_font(22), hex_rgb(PURPLE_DARK))
    return img


def post1_slide05():
    img, draw = new_slide(DARK_BG)
    draw_centered(draw, "WHAT FULL ANALYSIS FOUND", 120, load_font(22), hex_rgb(ORANGE))
    draw_centered(draw, "Business logic", 300, load_font(60), hex_rgb(WHITE))
    draw_centered(draw, "in 17 modules.", 380, load_font(60), hex_rgb(WHITE))
    draw_centered(draw, "No single person", 500, load_font(36), hex_rgb(ORANGE))
    draw_centered(draw, "could enumerate it.", 560, load_font(36), hex_rgb(ORANGE))
    draw_centered(draw, "100 business rules extracted.", 720, load_font(28), hex_rgb(WHITE))
    draw_centered(draw, "Verified. Deduplicated.", 780, load_font(28), hex_rgb(WHITE))
    return img


def post1_slide06():
    img, draw = new_slide(LIGHT_BG)
    draw_centered(draw, "THE METHOD", 120, load_font(22), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "AI reads everything.", 260, load_font(54), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Senior architect", 360, load_font(54), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "verifies everything.", 430, load_font(54), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Every finding cites", 560, load_font(32), hex_rgb(ORANGE))
    draw_centered(draw, "a source file and line.", 610, load_font(32), hex_rgb(ORANGE))
    draw_centered(draw, "Not a sample. Not documentation.", 760, load_font(28), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "The actual code.", 820, load_font(28), hex_rgb(PURPLE_DARK))
    return img


def post1_slide07():
    img, draw = new_slide(DARK_BG)
    draw_centered(draw, "TRADITIONAL VS FULL COVERAGE", 120, load_font(22), hex_rgb(ORANGE))
    # Column headers
    draw.text((80, 220), "Traditional", font=load_font(28), fill=hex_rgb(WHITE))
    draw.text((560, 220), "Full Coverage", font=load_font(28), fill=hex_rgb(ORANGE))
    # Rows
    rows = [
        (300, "10–15% of codebase", "100% of codebase"),
        (380, "8–14 weeks", "3 weeks"),
        (460, "2.3M NOK", "500K NOK"),
        (540, "Approximate findings", "Verified findings"),
    ]
    f_row = load_font(28)
    for y, left, right in rows:
        draw.text((80, y), left, font=f_row, fill=hex_rgb(WHITE))
        draw.text((560, y), right, font=f_row, fill=hex_rgb(ORANGE))
    # Vertical divider
    draw.line([(540, 260), (540, 600)], fill=hex_rgb(WHITE), width=1)
    # Bottom
    draw_centered(draw, "Same platform. Same scope.", 720, load_font(28), hex_rgb(WHITE))
    draw_centered(draw, "Different methodology.", 780, load_font(36), hex_rgb(ORANGE))
    return img


def post1_slide08():
    img, draw = new_slide(LIGHT_BG)
    draw_centered(draw, "REAL CLIENT. REAL PROJECT.", 120, load_font(22), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "20 interconnected", 260, load_font(48), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "applications.", 330, load_font(48), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Nobody knew how", 420, load_font(36), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "they all connected.", 475, load_font(36), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "3 weeks.", 580, load_font(54), hex_rgb(ORANGE))
    draw_centered(draw, "Full roadmap.", 660, load_font(54), hex_rgb(ORANGE))
    draw_centered(draw, "Every finding traced to source code.", 820, load_font(22), hex_rgb(PURPLE_DARK))
    return img


def post1_slide09():
    img, draw = new_slide(DARK_BG)
    draw_centered(draw, "THE QUESTION", 120, load_font(22), hex_rgb(ORANGE))
    draw_centered(draw, "Your platform", 280, load_font(54), hex_rgb(WHITE))
    draw_centered(draw, "almost certainly", 360, load_font(54), hex_rgb(WHITE))
    draw_centered(draw, "contains findings", 440, load_font(54), hex_rgb(WHITE))
    draw_centered(draw, "like this.", 520, load_font(54), hex_rgb(WHITE))
    draw_centered(draw, "The question is", 660, load_font(48), hex_rgb(ORANGE))
    draw_centered(draw, "who reads them first.", 730, load_font(48), hex_rgb(ORANGE))
    return img


def post1_slide10():
    img, draw = new_slide(LIGHT_BG)
    draw_centered(draw, "NEXT STEP", 120, load_font(22), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "DM Tomasz", 260, load_font(54), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Mierzejowski", 340, load_font(54), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "AI App Modernization Architect", 460, load_font(32), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Sopra Steria", 510, load_font(32), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "tomasz.mierzejowski", 640, load_font(32), hex_rgb(ORANGE))
    draw_centered(draw, "@soprasteria.com", 690, load_font(32), hex_rgb(ORANGE))
    draw_centered(draw, "Every number verified. Every finding traced to source code.", 820, load_font(22), hex_rgb(PURPLE_DARK))
    return img


def generate_post1():
    print("Generating Post 1 carousel...")
    slides = [
        post1_slide01, post1_slide02, post1_slide03, post1_slide04, post1_slide05,
        post1_slide06, post1_slide07, post1_slide08, post1_slide09, post1_slide10,
    ]
    for i, fn in enumerate(slides, 1):
        img = fn()
        path = os.path.join(POST1_DIR, f"slide_{i:02d}.png")
        save(img, path)
        print(f"  Saved {path}")


# ===========================================================================
# POST 4 — PROOF OF SCALE (10 slides)
# ===========================================================================

def post4_slide01():
    img, draw = new_slide(DARK_BG)
    draw_centered(draw, "PROOF OF SCALE", 120, load_font(22), hex_rgb(ORANGE))
    draw_centered(draw, "20 interconnected", 300, load_font(60), hex_rgb(WHITE))
    draw_centered(draw, "applications.", 380, load_font(60), hex_rgb(WHITE))
    draw_centered(draw, "Nobody knew how", 500, load_font(48), hex_rgb(ORANGE))
    draw_centered(draw, "they all connected.", 570, load_font(48), hex_rgb(ORANGE))
    draw_centered(draw, "Not the architects. Not the vendors. →", 820, load_font(22), hex_rgb(WHITE))
    return img


def post4_slide02():
    img, draw = new_slide(LIGHT_BG)
    draw_centered(draw, "THE PROBLEM", 120, load_font(22), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "The diagrams", 260, load_font(54), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "were wrong.", 340, load_font(54), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Not because of negligence.", 480, load_font(32), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Because diagrams describe", 535, load_font(32), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "what people remember.", 590, load_font(32), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Code shows what", 760, load_font(36), hex_rgb(ORANGE))
    draw_centered(draw, "actually runs.", 820, load_font(36), hex_rgb(ORANGE))
    return img


def post4_slide03():
    img, draw = new_slide(DARK_BG)
    draw_centered(draw, "WHAT WE FOUND", 120, load_font(22), hex_rgb(ORANGE))
    draw_centered(draw, "187", 260, load_font(180), hex_rgb(ORANGE))
    draw_centered(draw, "API endpoints", 480, load_font(48), hex_rgb(WHITE))
    draw_centered(draw, "discovered and classified.", 550, load_font(48), hex_rgb(WHITE))
    draw_centered(draw, "Source: MASTER_CONSOLIDATED_REPORT line 477", 900, load_font(22), hex_rgb(ORANGE))
    return img


def post4_slide04():
    img, draw = new_slide(LIGHT_BG)
    draw_centered(draw, "WHAT WE FOUND", 120, load_font(22), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "98", 260, load_font(180), hex_rgb(ORANGE))
    draw_centered(draw, "integration connections", 480, load_font(48), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "across 7+ protocols.", 550, load_font(48), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Source: MASTER_CONSOLIDATED_REPORT line 478", 900, load_font(22), hex_rgb(PURPLE_DARK))
    return img


def post4_slide05():
    img, draw = new_slide(DARK_BG)
    draw_centered(draw, "THE TIMELINE", 120, load_font(22), hex_rgb(ORANGE))
    draw_centered(draw, "3", 300, load_font(120), hex_rgb(WHITE))
    draw_centered(draw, "weeks", 460, load_font(60), hex_rgb(ORANGE))
    draw_centered(draw, "First code scan", 580, load_font(48), hex_rgb(WHITE))
    draw_centered(draw, "to complete roadmap.", 650, load_font(48), hex_rgb(WHITE))
    draw_centered(draw, "Traditional scope: 8–14 weeks.", 820, load_font(28), hex_rgb(WHITE))
    return img


def post4_slide06():
    img, draw = new_slide(LIGHT_BG)
    draw_centered(draw, "THE COST COMPARISON", 120, load_font(22), hex_rgb(PURPLE_DARK))
    # Left block
    draw.text((80, 250), "Traditional", font=load_font(22), fill=hex_rgb(PURPLE_DARK))
    draw.text((80, 310), "2.3M", font=load_font(80), fill=hex_rgb(PURPLE_DARK))
    draw.text((80, 420), "NOK", font=load_font(48), fill=hex_rgb(PURPLE_DARK))
    # Divider
    draw.line([(540, 220), (540, 700)], fill=hex_rgb(PURPLE_DARK), width=1)
    # Right block
    draw.text((580, 250), "Our engagement", font=load_font(22), fill=hex_rgb(ORANGE))
    draw.text((580, 310), "500K", font=load_font(80), fill=hex_rgb(ORANGE))
    draw.text((580, 420), "NOK", font=load_font(48), fill=hex_rgb(ORANGE))
    # Bottom
    draw_centered(draw, "Same platform. Same scope.", 760, load_font(28), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Full coverage, not partial.", 820, load_font(32), hex_rgb(ORANGE))
    return img


def post4_slide07():
    img, draw = new_slide(DARK_BG)
    draw_centered(draw, "THE DELIVERABLE", 120, load_font(22), hex_rgb(ORANGE))
    draw_centered(draw, "Not a slide deck.", 280, load_font(54), hex_rgb(WHITE))
    draw_centered(draw, "An interactive report.", 380, load_font(32), hex_rgb(WHITE))
    draw_centered(draw, "Every finding traces", 460, load_font(32), hex_rgb(WHITE))
    draw_centered(draw, "to a line in source code.", 515, load_font(32), hex_rgb(WHITE))
    draw_centered(draw, "The client can interrogate", 640, load_font(42), hex_rgb(ORANGE))
    draw_centered(draw, "any claim.", 700, load_font(42), hex_rgb(ORANGE))
    draw_centered(draw, "The evidence is there.", 870, load_font(22), hex_rgb(WHITE))
    return img


def post4_slide08():
    img, draw = new_slide(LIGHT_BG)
    draw_centered(draw, "WHY THIS MATTERS", 120, load_font(22), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Traditional discovery", 260, load_font(54), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "can’t cover everything.", 340, load_font(54), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Not because of effort.", 480, load_font(32), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Because full coverage", 535, load_font(32), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "in a traditional billing model", 590, load_font(32), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "is economically irrational.", 645, load_font(32), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "AI changed the economics.", 800, load_font(36), hex_rgb(ORANGE))
    draw_centered(draw, "Not the need.", 860, load_font(36), hex_rgb(ORANGE))
    return img


def post4_slide09():
    img, draw = new_slide(DARK_BG)
    draw_centered(draw, "THE QUESTION", 120, load_font(22), hex_rgb(ORANGE))
    draw_centered(draw, "What would your", 280, load_font(54), hex_rgb(WHITE))
    draw_centered(draw, "platform reveal", 360, load_font(54), hex_rgb(WHITE))
    draw_centered(draw, "if someone read", 440, load_font(54), hex_rgb(WHITE))
    draw_centered(draw, "all of it?", 520, load_font(54), hex_rgb(WHITE))
    draw_centered(draw, "The answer is in", 760, load_font(36), hex_rgb(ORANGE))
    draw_centered(draw, "your source code.", 820, load_font(36), hex_rgb(ORANGE))
    return img


def post4_slide10():
    img, draw = new_slide(LIGHT_BG)
    draw_centered(draw, "NEXT STEP", 120, load_font(22), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "DM Tomasz", 260, load_font(54), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Mierzejowski", 340, load_font(54), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "AI App Modernization Architect", 460, load_font(32), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Sopra Steria", 510, load_font(32), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "tomasz.mierzejowski", 640, load_font(32), hex_rgb(ORANGE))
    draw_centered(draw, "@soprasteria.com", 690, load_font(32), hex_rgb(ORANGE))
    draw_centered(draw, "Every number verified. Every finding traced to source code.", 820, load_font(22), hex_rgb(PURPLE_DARK))
    return img


def generate_post4():
    print("Generating Post 4 carousel...")
    slides = [
        post4_slide01, post4_slide02, post4_slide03, post4_slide04, post4_slide05,
        post4_slide06, post4_slide07, post4_slide08, post4_slide09, post4_slide10,
    ]
    for i, fn in enumerate(slides, 1):
        img = fn()
        path = os.path.join(POST4_DIR, f"slide_{i:02d}.png")
        save(img, path)
        print(f"  Saved {path}")


# ===========================================================================
# POST 7 — THE RECKONING (8 slides)
# ===========================================================================

def post7_slide01():
    img, draw = new_slide(DARK_BG)
    draw_centered(draw, "THE VERIFIED TRACK RECORD", 120, load_font(22), hex_rgb(ORANGE))
    draw_centered(draw, "Every number", 300, load_font(60), hex_rgb(WHITE))
    draw_centered(draw, "that follows comes", 380, load_font(60), hex_rgb(WHITE))
    draw_centered(draw, "from a real client.", 460, load_font(60), hex_rgb(WHITE))
    draw_centered(draw, "Not ‘up to.’", 700, load_font(36), hex_rgb(ORANGE))
    draw_centered(draw, "Not an industry benchmark.", 760, load_font(36), hex_rgb(ORANGE))
    draw_centered(draw, "The actual project.", 820, load_font(36), hex_rgb(ORANGE))
    return img


def post7_slide02():
    img, draw = new_slide(LIGHT_BG)
    draw_centered(draw, "6+ ENGAGEMENTS", 120, load_font(22), hex_rgb(PURPLE_DARK))
    # Rows: left ORANGE big, right PURPLE_DARK smaller
    rows = [
        (220, "4 days", 54, "emergency migration", 28),
        (330, "3 weeks", 54, "20-app platform discovery", 28),
        (440, "1 month", 54, "2-year deployment restored", 28),
        (550, "92%", 54, "code preserved in migration", 28),
        (660, "500K NOK", 42, "vs 2.3M traditional", 28),
    ]
    for y, left_text, left_size, right_text, right_size in rows:
        draw.text((80, y), left_text, font=load_font(left_size), fill=hex_rgb(ORANGE))
        # Right text: approximate x offset for alignment
        draw.text((420, y + (left_size - right_size) // 2), right_text, font=load_font(right_size), fill=hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Every number traced to source code.", 820, load_font(22), hex_rgb(PURPLE_DARK))
    return img


def post7_slide03():
    img, draw = new_slide(DARK_BG)
    draw_centered(draw, "ZERO REGRESSIONS", 120, load_font(22), hex_rgb(ORANGE))
    draw_centered(draw, "0", 260, load_font(120), hex_rgb(WHITE))
    draw_centered(draw, "regressions", 420, load_font(54), hex_rgb(ORANGE))
    draw_centered(draw, "across every transformation", 500, load_font(32), hex_rgb(WHITE))
    draw_centered(draw, "in the track record.", 560, load_font(32), hex_rgb(WHITE))
    draw_centered(draw, "100% on-time delivery.", 760, load_font(28), hex_rgb(WHITE))
    draw_centered(draw, "100% first-submission approval.", 820, load_font(28), hex_rgb(WHITE))
    return img


def post7_slide04():
    img, draw = new_slide(LIGHT_BG)
    draw_centered(draw, "THE METHODOLOGY", 120, load_font(22), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "AI accelerates coverage.", 260, load_font(54), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Senior architect", 360, load_font(54), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "verifies every finding.", 430, load_font(54), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Every claim cites", 570, load_font(36), hex_rgb(ORANGE))
    draw_centered(draw, "a source file and line.", 630, load_font(36), hex_rgb(ORANGE))
    draw_centered(draw, "When I say ‘estimated,’ I say so explicitly.", 820, load_font(22), hex_rgb(PURPLE_DARK))
    return img


def post7_slide05():
    img, draw = new_slide(DARK_BG)
    draw_centered(draw, "ESTIMATED vs VERIFIED", 120, load_font(22), hex_rgb(ORANGE))
    draw_centered(draw, "What is verified:", 260, load_font(48), hex_rgb(WHITE))
    verified_items = [
        "187 endpoints — MASTER_CONSOLIDATED_REPORT line 477",
        "529 endpoints — ComplianceIssuesSummary lines 29, 54",
        "4 days — Barnas Plattform engagement log",
        "92% code preserved — project measurement",
        "500K vs 2.3M NOK — engagement cost data",
    ]
    y = 360
    f = load_font(28)
    for item in verified_items:
        draw_centered(draw, item, y, f, hex_rgb(WHITE))
        y += 60
    draw_centered(draw, "What is estimated:", 720, load_font(48), hex_rgb(ORANGE))
    draw_centered(draw, "Cost avoidance (projected from traditional quotes)", 800, load_font(28), hex_rgb(WHITE))
    return img


def post7_slide06():
    img, draw = new_slide(LIGHT_BG)
    draw_centered(draw, "THE CONVERSATION I’M OFFERING", 120, load_font(22), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Not a pitch deck.", 260, load_font(54), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Not a roadmap.", 360, load_font(54), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "A conversation about", 490, load_font(32), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "what is actually in", 545, load_font(32), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "your code.", 600, load_font(32), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "I will tell you honestly", 780, load_font(36), hex_rgb(ORANGE))
    draw_centered(draw, "whether our approach fits.", 840, load_font(36), hex_rgb(ORANGE))
    return img


def post7_slide07():
    img, draw = new_slide(DARK_BG)
    draw_centered(draw, "WHO THIS IS FOR", 120, load_font(22), hex_rgb(ORANGE))
    draw_centered(draw, "VP Engineering.", 260, load_font(54), hex_rgb(WHITE))
    draw_centered(draw, "CTO. Enterprise Architect.", 340, load_font(54), hex_rgb(WHITE))
    draw_centered(draw, "Managing a legacy platform.", 440, load_font(32), hex_rgb(WHITE))
    draw_centered(draw, "About to commission", 500, load_font(32), hex_rgb(WHITE))
    draw_centered(draw, "a discovery or modernization.", 560, load_font(32), hex_rgb(WHITE))
    draw_centered(draw, "This post was", 680, load_font(48), hex_rgb(ORANGE))
    draw_centered(draw, "written for you.", 750, load_font(48), hex_rgb(ORANGE))
    return img


def post7_slide08():
    img, draw = new_slide(LIGHT_BG)
    draw_centered(draw, "NEXT STEP", 120, load_font(22), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "DM me.", 260, load_font(60), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "First conversation is free.", 380, load_font(32), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "No pitch deck.", 440, load_font(32), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "No proposal.", 510, load_font(32), hex_rgb(PURPLE_DARK))
    draw_centered(draw, "Tomasz Mierzejowski", 630, load_font(32), hex_rgb(ORANGE))
    draw_centered(draw, "tomasz.mierzejowski@soprasteria.com", 680, load_font(32), hex_rgb(ORANGE))
    draw_centered(draw, "AI App Modernization Architect | Sopra Steria", 740, load_font(28), hex_rgb(ORANGE))
    draw_centered(draw, "Every number verified. Every finding traced to source code.", 900, load_font(22), hex_rgb(PURPLE_DARK))
    return img


def generate_post7():
    print("Generating Post 7 carousel...")
    slides = [
        post7_slide01, post7_slide02, post7_slide03, post7_slide04,
        post7_slide05, post7_slide06, post7_slide07, post7_slide08,
    ]
    for i, fn in enumerate(slides, 1):
        img = fn()
        path = os.path.join(POST7_DIR, f"slide_{i:02d}.png")
        save(img, path)
        print(f"  Saved {path}")


# ===========================================================================
# POST 2 GRAPHIC: 529 unauthenticated endpoints
# ===========================================================================

def generate_post2_graphic():
    print("Generating Post 2 graphic...")
    img, draw = new_slide(DARK_BG)
    # Large "529" centered
    f_big = load_font(200)
    bbox = draw.textbbox((0, 0), "529", font=f_big)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (SLIDE_W - tw) // 2
    # Vertical center of top ~650px zone
    y = (650 - th) // 2
    draw.text((x, y), "529", font=f_big, fill=hex_rgb(ORANGE))
    draw_centered(draw, "unauthenticated endpoints", 700, load_font(48), hex_rgb(WHITE))
    draw_centered(draw, "in one enterprise platform.", 775, load_font(36), hex_rgb(WHITE))
    draw_centered(draw, "Source: ComplianceIssuesSummary", 920, load_font(22), hex_rgb(WHITE))
    path = os.path.join(GRAPHICS_DIR, "post2_529_graphic.png")
    save(img, path)
    print(f"  Saved {path}")


# ===========================================================================
# POST 3 GRAPHIC: 4 days / 92%
# ===========================================================================

def generate_post3_graphic():
    print("Generating Post 3 graphic...")
    img = Image.new("RGB", (SLIDE_W, SLIDE_H), hex_rgb(LIGHT_BG))
    draw = ImageDraw.Draw(img)

    # Left half: PURPLE_DARK background (0 to 540)
    draw.rectangle([(0, 0), (540, SLIDE_H)], fill=hex_rgb(PURPLE_DARK))

    # Right half: LIGHT_BG background (540 to 1080) — already the base

    # Bottom strip (900 to 1080): DARK_BG
    draw.rectangle([(0, 900), (SLIDE_W, SLIDE_H)], fill=hex_rgb(DARK_BG))

    # Left half content: "4" centered in left panel (above strip)
    panel_h = 900
    f_4 = load_font(120)
    bbox_4 = draw.textbbox((0, 0), "4", font=f_4)
    tw_4 = bbox_4[2] - bbox_4[0]
    th_4 = bbox_4[3] - bbox_4[1]
    x_4 = (540 - tw_4) // 2
    y_4 = (panel_h - th_4) // 2 - 60
    draw.text((x_4, y_4), "4", font=f_4, fill=hex_rgb(WHITE))
    # "DAYS" below
    f_days = load_font(48)
    bbox_days = draw.textbbox((0, 0), "DAYS", font=f_days)
    tw_days = bbox_days[2] - bbox_days[0]
    x_days = (540 - tw_days) // 2
    draw.text((x_days, 660), "DAYS", font=f_days, fill=hex_rgb(WHITE))

    # Right half content: "92%" centered in right panel
    f_92 = load_font(120)
    bbox_92 = draw.textbbox((0, 0), "92%", font=f_92)
    tw_92 = bbox_92[2] - bbox_92[0]
    th_92 = bbox_92[3] - bbox_92[1]
    x_92 = 540 + (540 - tw_92) // 2
    y_92 = (panel_h - th_92) // 2 - 60
    draw.text((x_92, y_92), "92%", font=f_92, fill=hex_rgb(PURPLE_DARK))
    # "code preserved" below
    f_cp = load_font(36)
    bbox_cp = draw.textbbox((0, 0), "code preserved", font=f_cp)
    tw_cp = bbox_cp[2] - bbox_cp[0]
    x_cp = 540 + (540 - tw_cp) // 2
    draw.text((x_cp, 660), "code preserved", font=f_cp, fill=hex_rgb(PURPLE_DARK))

    # Bottom strip text centered
    strip_label = "Barnas Plattform · Xamarin → .NET 8 MAUI"
    f_strip = load_font(28)
    bbox_s = draw.textbbox((0, 0), strip_label, font=f_strip)
    tw_s = bbox_s[2] - bbox_s[0]
    x_s = (SLIDE_W - tw_s) // 2
    strip_text_y = 900 + (180 - (bbox_s[3] - bbox_s[1])) // 2
    draw.text((x_s, strip_text_y), strip_label, font=f_strip, fill=hex_rgb(ORANGE))

    path = os.path.join(GRAPHICS_DIR, "post3_4days_graphic.png")
    save(img, path)
    print(f"  Saved {path}")


# ===========================================================================
# Main
# ===========================================================================

def main():
    generate_post1()
    generate_post4()
    generate_post7()
    generate_post2_graphic()
    generate_post3_graphic()
    print("Done. All slides generated.")


if __name__ == "__main__":
    main()
