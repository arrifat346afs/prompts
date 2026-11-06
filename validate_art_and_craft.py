import re

style_block = "Chunky solid flat glyph style with fluid sculpted corners and balanced geometric contours, viewed from a direct flat 2D front perspective. Every shape features solid uniform fills separated by crisp negative space cutouts. The palette is strictly limited to two solid flat colors: deep Prussian indigo #172535 for the primary tool and canvas silhouette, and golden ochre #C88A2C for paint dollops, bristle ferrules, and craft accents."

subjects = [
    "Artist paintbrush with a deep Prussian indigo #172535 wooden tapered handle, and golden ochre #C88A2C ferrule band and fine pointed bristle tip",
    "Painter's kidney palette with a deep Prussian indigo #172535 wooden board and thumb hole cutout, and golden ochre #C88A2C mixed paint dollop blobs",
    "Craft scissors with deep Prussian indigo #172535 sharp tapered cutting blades, and golden ochre #C88A2C ergonomic finger loop handles and pivot screw",
    "Wooden studio A-frame easel with deep Prussian indigo #172535 tripod support mast legs, and a golden ochre #C88A2C stretched canvas board and crank shelf",
    "Crimped artist oil paint tube with a deep Prussian indigo #172535 flexible tube body and screw cap, and a golden ochre #C88A2C squeezed paint swirl dollop",
    "Articulated wooden drawing mannequin with a deep Prussian indigo #172535 stand post and circular base, and golden ochre #C88A2C jointed wooden figure segments",
    "Retractable precision hobby knife with a deep Prussian indigo #172535 ridged handle casing, and a golden ochre #C88A2C angled craft scalpel blade and slide lock",
    "Self-healing craft cutting mat with a deep Prussian indigo #172535 rectangular mat board, and golden ochre #C88A2C metric measurement grid rules and angle lines",
    "Pottery clay wire cutter with deep Prussian indigo #172535 twin turned toggle handles, and a golden ochre #C88A2C tensioned wire slicing through a clay block",
    "Tabletop pottery banding wheel with a deep Prussian indigo #172535 heavy pedestal base, and a golden ochre #C88A2C rotating turntable disc with concentric guide rings",
    "Ceramic brush rinse jar with a deep Prussian indigo #172535 water crock basin, and golden ochre #C88A2C resting paintbrush handles and water swirl ripple",
    "Offset painting palette knife with a deep Prussian indigo #172535 wooden handgrip handle, and a golden ochre #C88A2C cranked metal neck and flexible diamond blade",
    "Spiral-bound artist sketchbook with a deep Prussian indigo #172535 double-loop wire binding, and golden ochre #C88A2C open drawing paper sheets and page corner",
    "Printmaking brayer roller with a deep Prussian indigo #172535 heavy wire frame and handle, and a golden ochre #C88A2C cylindrical rubber roller coated in ink",
    "Linocut carving gouge tool with a deep Prussian indigo #172535 rounded wooden palm handle, and a golden ochre #C88A2C steel V-gouge cutting blade",
    "Ceramic clay ribbon tool with a deep Prussian indigo #172535 central wooden grip barrel, and golden ochre #C88A2C dual wire loop sculpting ends",
    "Hot melt craft glue gun with a deep Prussian indigo #172535 gun body casing and feed chamber, and a golden ochre #C88A2C trigger, wire kickstand, and nozzle drop",
    "Craft liquid glue bottle with a deep Prussian indigo #172535 squeeze bottle body, and a golden ochre #C88A2C twist-open applicator cone cap and glue droplet",
    "Set of artist sketching pencils with deep Prussian indigo #172535 hexagonal pencil bodies, and golden ochre #C88A2C sharpened cedar collars and ferrule bands",
    "Round wooden embroidery hoop with a deep Prussian indigo #172535 inner and outer ring hoop, and a golden ochre #C88A2C top brass tightening tension screw",
    "Stack of decorative washi tape with deep Prussian indigo #172535 patterned tape rolls, and golden ochre #C88A2C peeled tape strip ends and inner cardboard cores",
    "Handheld single-hole paper punch with a deep Prussian indigo #172535 metal lever handle, and a golden ochre #C88A2C hinge rivet, punch jaw, and confetti circle dots",
    "Tabletop printing etching press with deep Prussian indigo #172535 side upright support frames, and golden ochre #C88A2C heavy steel pressure rollers and star wheel crank",
    "Drafting triangle ruler with a deep Prussian indigo #172535 clear triangular edge frame, and golden ochre #C88A2C beveled center cutout and measurement tick increments",
    "Calligraphy dip pen with a deep Prussian indigo #172535 contoured wooden pen staff, and a golden ochre #C88A2C pointed flexible writing nib with ink breather hole",
    "Glass calligraphy ink bottle with a deep Prussian indigo #172535 faceted inkwell body, and a golden ochre #C88A2C threaded cap and dipping neck opening",
    "Artist portfolio case folder with a deep Prussian indigo #172535 zippered document case body, and golden ochre #C88A2C reinforced corner guards and top carry handle",
    "Kneaded artist eraser with a deep Prussian indigo #172535 rectangular block base, and a golden ochre #C88A2C hand-sculpted teardrop working tip",
    "Dual-tip artist marker pen with a deep Prussian indigo #172535 ergonomic barrel body, and golden ochre #C88A2C color indicator caps and chisel marker nib",
    "Porcelain watercolor daisy palette with a deep Prussian indigo #172535 circular tray rim, and golden ochre #C88A2C petal paint wells and central mixing pool"
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
    if unique_hexes != {'#172535', '#C88A2C'}:
        print(f"ERROR: unexpected hex codes in prompt {i}: {unique_hexes}")
        
    prompts.append(p)

title = "Traditional Artist Studio Painting and Craft Tools"
print(f"Title: {title} ({len(title)} chars, max 70)")
assert len(title) <= 70

keywords = "art icons, paintbrush, paint palette, craft scissors, studio easel, paint tube, drawing mannequin, hobby knife, cutting mat, clay wire cutter, palette knife, sketchbook, brayer roller, glue gun, embroidery hoop, dip pen, inkwell, washi tape, linocut gouge, flat vector icons"
kw_list = [k.strip() for k in keywords.split(',')]
print(f"Keywords count: {len(kw_list)}")
assert len(kw_list) == 20

with open("/home/rifat/prompts/art_and_craft_prompts.txt", "w") as f:
    for p in prompts:
        f.write(p + "\n")

print("All validations passed! art_and_craft_prompts.txt written successfully!")
