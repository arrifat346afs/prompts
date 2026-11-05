import re

style_block = "Chunky solid technical glyphs with sharp angular chamfers and clean edges, rendered in a direct flat 2D front view. Each element is built from bold geometric silhouettes with crisp white negative space lines separating adjoining parts. The palette features three solid flat colors: midnight violet #1D1630 for the primary equipment chassis, electric violet #7C3AED for secondary frames and structural accents, and cyber mint green #00E599 strictly for buttons, ports, and interactive control points. Every shape is filled with a single solid flat color with uniform coverage."

subjects = [
    "Mechanical gaming keyboard with a midnight violet #1D1630 base casing, electric violet #7C3AED keycap rows, and cyber mint green #00E599 grouped directional arrow keycaps",
    "Ergonomic gaming mouse with a midnight violet #1D1630 palm shell, electric violet #7C3AED scroll wheel guard, and cyber mint green #00E599 tactile thumb side buttons",
    "Over-ear esports gaming headset with midnight violet #1D1630 earcups, electric violet #7C3AED headband frame, and a cyber mint green #00E599 flexible boom microphone tip",
    "Broadcast studio condenser microphone with a midnight violet #1D1630 capsule body, electric violet #7C3AED suspension shock mount, and cyber mint green #00E599 control gain dials",
    "Ultrawide curved gaming desktop monitor with a midnight violet #1D1630 screen display, electric violet #7C3AED angular tripod stand, and a cyber mint green #00E599 power indicator accent",
    "Portable handheld gaming console with a midnight violet #1D1630 main chassis, electric violet #7C3AED center wide screen, and cyber mint green #00E599 dual thumbsticks and directional pad",
    "Flight simulation joystick with a midnight violet #1D1630 desktop base, electric violet #7C3AED articulated flight stick shaft, and cyber mint green #00E599 top thumb hat switch and trigger",
    "Racing simulation steering wheel with a midnight violet #1D1630 grip rim, electric violet #7C3AED central steering hub, and cyber mint green #00E599 rear gear paddle shifters",
    "Arcade fight stick controller with a midnight violet #1D1630 console deck, electric violet #7C3AED joystick shaft with ball top, and cyber mint green #00E599 circular action attack buttons",
    "Stream broadcast macro keypad deck with a midnight violet #1D1630 angled desktop console, electric violet #7C3AED chassis bezel, and a grid of cyber mint green #00E599 square trigger key buttons",
    "External graphics card GPU enclosure dock with a midnight violet #1D1630 casing shell, electric violet #7C3AED ventilation slot louvers, and cyber mint green #00E599 connection port jacks",
    "High-airflow computer case chassis with a midnight violet #1D1630 tower body, electric violet #7C3AED geometric front intake grille, and cyber mint green #00E599 top power button and ports",
    "Modular gamepad game controller with a midnight violet #1D1630 winged handgrip shell, electric violet #7C3AED central faceplate, and cyber mint green #00E599 thumbsticks and shoulder bumper triggers",
    "Virtual reality VR headset visor with a midnight violet #1D1630 front face unit, electric violet #7C3AED adjustable head straps, and cyber mint green #00E599 optical sensor camera dots",
    "Pair of motion-tracking VR hand controllers with midnight violet #1D1630 ergonomic handle grips, electric violet #7C3AED circular tracking sensor rings, and cyber mint green #00E599 thumb triggers",
    "Smartphone mobile gaming gamepad cradle with midnight violet #1D1630 dual grip handles, electric violet #7C3AED center spring phone bracket, and cyber mint green #00E599 mini thumbsticks",
    "Desk-mounted mouse bungee cable holder with a midnight violet #1D1630 weighted triangular base, electric violet #7C3AED flexible spring arm, and a cyber mint green #00E599 rubberized cable clip",
    "Contoured ergonomic gaming wrist rest keyboard cushion with a midnight violet #1D1630 supportive base tray, electric violet #7C3AED padded wrist pad, and cyber mint green #00E599 geometric corner grips",
    "High-performance axial cooling fan with a midnight violet #1D1630 square mounting frame, electric violet #7C3AED curved fan blades, and a cyber mint green #00E599 center motor hub cap",
    "External video capture card box with a midnight violet #1D1630 compact aluminum casing, electric violet #7C3AED side bumper edges, and cyber mint green #00E599 video signal HDMI port slots",
    "Desktop headset stand cradle with a midnight violet #1D1630 circular weighted base, electric violet #7C3AED vertical riser pillar, and a cyber mint green #00E599 curved top resting perch",
    "Racing simulation floor pedal assembly with a midnight violet #1D1630 heel rest baseplate, electric violet #7C3AED pedal swing arms, and cyber mint green #00E599 textured foot pedal face plates",
    "Desktop gaming soundbar speaker with a midnight violet #1D1630 horizontal housing, electric violet #7C3AED speaker driver cones, and cyber mint green #00E599 center volume control rotary knob",
    "Hard-shell console travel carrying case with a midnight violet #1D1630 protective molded body, electric violet #7C3AED reinforced perimeter seam, and cyber mint green #00E599 double zipper pull tabs",
    "Streaming webcam with a midnight violet #1D1630 camera body, electric violet #7C3AED folding monitor clamp mount, and a cyber mint green #00E599 optical lens ring and privacy slide shutter",
    "Multi-port LAN network switch hub with a midnight violet #1D1630 desktop rack box, electric violet #7C3AED front faceplate, and a row of cyber mint green #00E599 Ethernet connector port jacks",
    "Angular esports tournament championship trophy cup with a midnight violet #1D1630 geometric base pedestal, electric violet #7C3AED polygonal cup body, and cyber mint green #00E599 sharp handle accents",
    "Dual-monitor heavy-duty desk mount bracket with a midnight violet #1D1630 desk clamp base, electric violet #7C3AED articulated gas-spring counter-balance arms, and cyber mint green #00E599 VESA mount plates",
    "Tournament winner's medal pendant with a midnight violet #1D1630 wide lanyard ribbon strap, electric violet #7C3AED outer medal border ring, and a cyber mint green #00E599 star emblem centerpiece",
    "Desktop gaming audio amplifier DAC hub with a midnight violet #1D1630 desktop unit chassis, electric violet #7C3AED audio jack input panel, and a cyber mint green #00E599 large stepped volume rotary dial"
]

forbidden = ["gradient", "fade", "glow", "shine", "glossy", "3d", "shadow", "soft light", "ombre", "metallic"]

print(f"Total subjects: {len(subjects)}")
assert len(subjects) == 30, "Not 30 subjects!"
assert len(set(subjects)) == 30, "Duplicate subjects exist!"

tail = "centered with even padding, plain solid white background, flat vector illustration style, solid flat colors only, uniform fills. Avoid: gradients, shading, shadows, glow, highlights, textures, transparency, blur, text."

prompts = []
for i, subj in enumerate(subjects, 1):
    p = f"{subj}, single icon, {style_block}, {tail}"
    before_avoid = p.split("Avoid:")[0].lower()
    for f in forbidden:
        if re.search(r'\b' + re.escape(f) + r'\b', before_avoid):
            print(f"ERROR: forbidden word '{f}' in prompt {i} before Avoid:")
    prompts.append(p)

title = "Competitive Esports Hardware and Gaming Peripherals"
print(f"Title length: {len(title)} chars (max 70)")
assert len(title) <= 70

keywords = "esports gear, gaming peripherals, mechanical keyboard, gaming mouse, gaming headset, game controller, flight stick, arcade fight stick, vr headset, streaming microphone, capture card, stream deck, racing wheel, gaming monitor, soundbar, lan switch, trophy cup, pc gaming, flat vector icons, solid glyphs"
kw_list = [k.strip() for k in keywords.split(',')]
print(f"Keywords count: {len(kw_list)}")
assert len(kw_list) == 20

with open("/home/rifat/prompts/gaming_prompts.txt", "w") as f:
    for p in prompts:
        f.write(p + "\n")

print("All validations passed and file written successfully!")
