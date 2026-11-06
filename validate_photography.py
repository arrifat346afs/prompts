import re

style_block = "Chunky solid flat glyph style with precise beveled corners and clean optical silhouettes, viewed from a direct flat 2D front perspective. Every shape features solid uniform fills separated by crisp negative space cutouts. The palette is strictly limited to two solid flat colors: deep carbon black #1E2022 for the primary camera hardware silhouette, and vivid lens red #CE2A37 for optical lens rings, shutter buttons, and operational accents."

subjects = [
    "Digital mirrorless camera body with a deep carbon black #1E2022 camera chassis and handgrip, and vivid lens red #CE2A37 shutter button and recording indicator dot accents",
    "Telephoto zoom camera lens with a deep carbon black #1E2022 cylindrical lens barrel, and vivid lens red #CE2A37 optical barrel ring and distance scale index line",
    "Studio camera tripod with deep carbon black #1E2022 telescoping tubular legs and pan-tilt head, and vivid lens red #CE2A37 leg clamp collars and pan lock knobs",
    "Camera speedlight flash unit with a deep carbon black #1E2022 flash body and hot shoe foot, and vivid lens red #CE2A37 optical sensor window and bounce head pivot ring",
    "Wide-angle prime lens with a deep carbon black #1E2022 barrel body and tulip hood, and vivid lens red #CE2A37 front lens element ring and focal index tick",
    "Studio strobe monolight flash with a deep carbon black #1E2022 cylindrical housing and stand mount, and vivid lens red #CE2A37 rear control dials and modeling lamp collar",
    "Octagonal photography softbox with a deep carbon black #1E2022 outer reflector shell and speed ring, and a vivid lens red #CE2A37 perimeter baffle trim border",
    "Studio photography umbrella with a deep carbon black #1E2022 center shaft rod and ribs, and vivid lens red #CE2A37 canopy tip caps and shaft handle ferrule",
    "Circular photography reflector disc with a deep carbon black #1E2022 collapsible disc rim, and vivid lens red #CE2A37 side fabric grip handles and border seam",
    "Digital incident light meter with a deep carbon black #1E2022 handheld meter body, and vivid lens red #CE2A37 spherical lumisphere dome collar and measure button",
    "Camera vertical battery grip with a deep carbon black #1E2022 contoured grip body and tray, and vivid lens red #CE2A37 vertical shutter button and dial wheel",
    "Camera memory card with a deep carbon black #1E2022 rectangular card plate and beveled notch, and a vivid lens red #CE2A37 lock switch slider and contact pin strip",
    "Multi-slot memory card reader with a deep carbon black #1E2022 hub casing and USB cable, and vivid lens red #CE2A37 media slot bezels and status LED dot",
    "Modular photography backpack with a deep carbon black #1E2022 backpack shell and shoulder straps, and vivid lens red #CE2A37 zipper pull loops and tripod strap buckles",
    "Rubber lens blower air duster with a deep carbon black #1E2022 squeeze bulb body and base stand, and a vivid lens red #CE2A37 precision air jet nozzle tip",
    "Double-ended lens cleaning pen with a deep carbon black #1E2022 pen barrel and pocket clip, and vivid lens red #CE2A37 brush slider switch and felt cap ring",
    "Three-axis motorized camera gimbal with deep carbon black #1E2022 stabilizer handle and base, and vivid lens red #CE2A37 motor joint rings and camera plate lock lever",
    "Woven camera neck strap with deep carbon black #1E2022 fabric webbing sling straps, and vivid lens red #CE2A37 quick-release anchor link connectors",
    "Circular camera lens filter with a deep carbon black #1E2022 knurled metal filter ring, and vivid lens red #CE2A37 optical glass tint circle and thread border",
    "Studio light stand with deep carbon black #1E2022 tripod base legs and riser columns, and vivid lens red #CE2A37 tension tightening knob screws and spigot tip",
    "Studio backdrop stand system with deep carbon black #1E2022 twin upright support poles, and a vivid lens red #CE2A37 horizontal crossbar and backdrop paper roll",
    "Wireless camera remote trigger with a deep carbon black #1E2022 compact remote transmitter body, and vivid lens red #CE2A37 two-stage shutter release button",
    "Lens calibration target card with a deep carbon black #1E2022 alignment target plate, and vivid lens red #CE2A37 concentric focus calibration circles and crosshairs",
    "Vintage twin-lens reflex camera with a deep carbon black #1E2022 boxy TLR camera body, and vivid lens red #CE2A37 viewing and taking lens surround rings",
    "Instant print camera with a deep carbon black #1E2022 rounded camera body and viewfinder, and vivid lens red #CE2A37 shutter button and ejected print photo frame",
    "Darkroom photographic enlarger with a deep carbon black #1E2022 vertical column and baseboard, and vivid lens red #CE2A37 accordion bellows and height lock crank knob",
    "Darkroom print developing tray with a deep carbon black #1E2022 molded tray basin and corner pour lip, and vivid lens red #CE2A37 print tongs tweezers",
    "Hard-shell protective equipment flight case with a deep carbon black #1E2022 ribbed case body, and vivid lens red #CE2A37 heavy-duty latch clamps and handle grip",
    "Tripod quick-release plate with a deep carbon black #1E2022 beveled dovetail mounting plate, and a vivid lens red #CE2A37 center camera locking thumbscrew",
    "Radio flash transceiver trigger with a deep carbon black #1E2022 hot shoe mount module, and vivid lens red #CE2A37 test button and channel selector switch"
]

forbidden = ["gradient", "fade", "glow", "shine", "glossy", "3d", "shadow", "soft light", "ombre", "metallic"]
generic = ["home", "user", "gear", "lightbulb", "magnifier", "cart", "chart"]

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
    for g in generic:
        if re.search(r'\b' + re.escape(g) + r'\b', before_avoid):
            print(f"ERROR: generic word '{g}' in prompt {i} before Avoid:")
    
    hexes = re.findall(r'#[0-9A-Fa-f]{6}', before_avoid)
    unique_hexes = set([h.upper() for h in hexes])
    if unique_hexes != {'#1E2022', '#CE2A37'}:
        print(f"ERROR: unexpected hex codes in prompt {i}: {unique_hexes}")
        
    prompts.append(p)

title = "Professional Camera Optics and Studio Photography Icons"
print(f"Title: {title} ({len(title)} chars, max 70)")
assert len(title) <= 70

keywords = "photography icons, camera body, telephoto lens, camera tripod, speedlight flash, studio strobe, octagonal softbox, photography umbrella, light reflector, light meter, battery grip, memory card, gimbal stabilizer, lens filter, camera strap, instant camera, tlr camera, lens blower, light stand, flat vector icons"
kw_list = [k.strip() for k in keywords.split(',')]
print(f"Keywords count: {len(kw_list)}")
assert len(kw_list) == 20

with open("/home/rifat/prompts/photography_prompts.txt", "w") as f:
    for p in prompts:
        f.write(p + "\n")

print("All validations passed! photography_prompts.txt written successfully!")
