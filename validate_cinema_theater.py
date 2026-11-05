import re

style_block = "Bold solid flat glyph style with smooth rounded corners and clean geometric silhouettes, viewed from a direct flat 2D front perspective. Every element uses solid uniform fills separated by crisp negative space cutouts. The palette is strictly limited to two solid flat colors: rich cinema burgundy #701A28 for the primary body silhouette, and warm maize gold #E5A93C for all decorative trims, concession accents, and functional details."

subjects = [
    "Striped popcorn tub with a rich cinema burgundy #701A28 striped container body, and warm maize gold #E5A93C puffy popped corn kernels overflowing the rim",
    "Fountain soda cup with a rich cinema burgundy #701A28 paper cup body, and a warm maize gold #E5A93C plastic fountain lid, straw, and condensation droplet accents",
    "Classic theater box office ticket booth with a rich cinema burgundy #701A28 kiosk pavilion body, and a warm maize gold #E5A93C service counter shelf and round speaker grill",
    "Cinema admission ticket stub with a rich cinema burgundy #701A28 admission card body, and warm maize gold #E5A93C notched tear line perforations and central star emblem",
    "Theater auditorium tip-up seat with a rich cinema burgundy #701A28 cushioned velvet seat pan and backrest, and warm maize gold #E5A93C structural armrests and beverage cup holder",
    "Cinema marquee canopy entrance signboard with a rich cinema burgundy #701A28 canopy roof, and warm maize gold #E5A93C perimeter fascia trim and circular illumination studs",
    "Proscenium stage opening framed by rich cinema burgundy #701A28 gathered pleated velvet theater curtains, and a warm maize gold #E5A93C scalloped overhead valance drapery",
    "Drive-in movie speaker box unit with a rich cinema burgundy #701A28 speaker housing, and a warm maize gold #E5A93C hanging hook bracket, coiled cord, and volume rotary knob",
    "Concession nacho tray with a rich cinema burgundy #701A28 partitioned snack tray, and warm maize gold #E5A93C triangular tortilla chips and circular cheese sauce bowl",
    "Cardboard cinema concession combo carrier tray with a rich cinema burgundy #701A28 molded pulp tray base, and warm maize gold #E5A93C dual beverage cups and center popcorn tub accents",
    "Movie theater candy concession box with a rich cinema burgundy #701A28 rectangular card package, and warm maize gold #E5A93C tuck-flap borders and decorative star emblem",
    "Concession hot dog in a rich cinema burgundy #701A28 fluted paper boat tray, featuring a warm maize gold #E5A93C bun and wavy mustard squiggle accent",
    "Twisted soft concession pretzel with a rich cinema burgundy #701A28 braided dough knot, and warm maize gold #E5A93C coarse pretzel salt grain flakes",
    "Frozen slushie beverage cup with a rich cinema burgundy #701A28 cup base, and a warm maize gold #E5A93C domed freeze lid and thick drinking straw",
    "Movie poster wall display case with a rich cinema burgundy #701A28 snap frame casing, and warm maize gold #E5A93C corner mounting rosettes and poster border outline",
    "Theater auditorium exit door with a rich cinema burgundy #701A28 rectangular door slab, and a warm maize gold #E5A93C horizontal emergency panic push bar and hinge plates",
    "Cinema lobby showtime board with a rich cinema burgundy #701A28 display plaque frame, and warm maize gold #E5A93C horizontal movie scheduling line slots and clock icon",
    "Classic cinema award statuette trophy featuring a rich cinema burgundy #701A28 tiered pedestal plinth, and a warm maize gold #E5A93C stylized geometric victory figure",
    "Walk of Fame sidewalk star plaque featuring a rich cinema burgundy #701A28 square terrazzo border, and a warm maize gold #E5A93C five-point star centerpiece",
    "Cinema velvet curtain tieback cord with a rich cinema burgundy #701A28 braided hanging rope, and a warm maize gold #E5A93C hanging decorative fringe tassel",
    "Wall-mounted theater auditorium surround sound speaker with a rich cinema burgundy #701A28 angled cabinet enclosure, and warm maize gold #E5A93C speaker driver cone rings",
    "Cinema ticket admission turnstile with a rich cinema burgundy #701A28 pedestal housing, and warm maize gold #E5A93C rotating barrier tripod arms and scanner slit",
    "Vintage commercial popcorn popping machine with a rich cinema burgundy #701A28 cabinet frame and wheels, and a warm maize gold #E5A93C internal popping kettle and handle",
    "Chocolate-dipped ice cream ice pop with a rich cinema burgundy #701A28 frozen chocolate coating, warm maize gold #E5A93C ice cream core bite cutout, and wooden stick base",
    "Concession bulk candy dispenser unit with a rich cinema burgundy #701A28 dispenser stand and chute, and a warm maize gold #E5A93C hopper globe and dispensing rotary handle",
    "Theater stage footlights trough strip with a rich cinema burgundy #701A28 floor fixture casing, and a row of warm maize gold #E5A93C upward-facing stage lamp reflectors",
    "Cinema VIP loyalty membership card featuring a rich cinema burgundy #701A28 card plate, and warm maize gold #E5A93C embossed star emblem crest and ribbon stripe",
    "Folding theater opera glasses binocular with rich cinema burgundy #701A28 dual optical barrels, and a warm maize gold #E5A93C center focus bridge wheel and extendable handgrip",
    "Cinema concession cotton candy paper cone with a warm maize gold #E5A93C rolled paper cone stem, and a rich cinema burgundy #701A28 puffy spun sugar cloud",
    "Movie theater popcorn ball treat with a rich cinema burgundy #701A28 ribbon bow knot, and a warm maize gold #E5A93C round glazed popcorn cluster ball"
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
    if unique_hexes != {'#701A28', '#E5A93C'}:
        print(f"ERROR: unexpected hex codes in prompt {i}: {unique_hexes}")
        
    prompts.append(p)

title = "Classic Cinema Experience and Theater Concession Icons"
print(f"Title: {title} ({len(title)} chars, max 70)")
assert len(title) <= 70

keywords = "cinema concession, movie theater, popcorn tub, fountain soda, ticket booth, admission stub, theater seat, stage curtains, drive-in speaker, nacho tray, candy box, concession hot dog, soft pretzel, slushie cup, poster frame, award statuette, walk of fame star, opera glasses, popcorn popper, flat vector icons"
kw_list = [k.strip() for k in keywords.split(',')]
print(f"Keywords count: {len(kw_list)}")
assert len(kw_list) == 20

with open("/home/rifat/prompts/cinema_theater_prompts.txt", "w") as f:
    for p in prompts:
        f.write(p + "\n")

print("All validations passed! cinema_theater_prompts.txt written successfully!")
