import re

style_block = "Chunky solid flat glyph style with smooth rounded corners and clean geometric contours, viewed from a direct flat 2D front perspective. Every shape uses solid uniform fills separated by crisp negative space cutouts. The palette is strictly limited to two solid flat colors: deep roast cocoa #3B2317 for the primary structural silhouette, and warm baked cinnamon #C86446 for all crust accents, tools, and decorative toppings."

subjects = [
    "Crusty sourdough bread boule loaf with a deep roast cocoa #3B2317 rounded crust body, and warm baked cinnamon #C86446 curved expansion slashes and flour scoring accents",
    "Frosted dessert cupcake with a deep roast cocoa #3B2317 pleated paper baking liner, and a warm baked cinnamon #C86446 swirled frosting dome and cherry topper",
    "Classic baking rolling pin with a deep roast cocoa #3B2317 smooth cylindrical barrel, and warm baked cinnamon #C86446 ergonomic side handle grips",
    "Balloon wire baking whisk with deep roast cocoa #3B2317 curved teardrop wire loops, and a warm baked cinnamon #C86446 cylindrical handle and hanging ring",
    "French baguette bread loaf with a deep roast cocoa #3B2317 elongated loaf body, and warm baked cinnamon #C86446 diagonal crust vent incisions",
    "Flaky crescent croissant pastry with deep roast cocoa #3B2317 curved crescent horns, and warm baked cinnamon #C86446 layered laminated dough fold segments",
    "Round banneton dough proofing basket with a deep roast cocoa #3B2317 woven basket basin, and warm baked cinnamon #C86446 spiral dough flour imprint rings",
    "Baker's lame dough scoring tool with a deep roast cocoa #3B2317 curved wooden handle, and a warm baked cinnamon #C86446 arched razor blade and fastening screw",
    "Pastry icing piping bag with a deep roast cocoa #3B2317 conical cloth bag body, and a warm baked cinnamon #C86446 fluted star nozzle and piped frosting rosette swirl",
    "Handheld metal dough bench scraper with a deep roast cocoa #3B2317 broad rectangular blade, and a warm baked cinnamon #C86446 rolled tubular top handle grip",
    "Kitchen stand mixer appliance with a deep roast cocoa #3B2317 tilting motor housing and base pedestal, and a warm baked cinnamon #C86446 mixing bowl and beater wire hook",
    "Traditional brick bread baking oven with a deep roast cocoa #3B2317 arched oven wall facade, and warm baked cinnamon #C86446 stone hearth opening and interior chamber",
    "Baker's wooden bread peel shovel paddle with a deep roast cocoa #3B2317 long pole handle, and a warm baked cinnamon #C86446 wide flat shovel blade carrying a bread loaf",
    "Round ceramic pie baking dish with a deep roast cocoa #3B2317 fluted pie pan plate, and a warm baked cinnamon #C86446 woven lattice crust top and crimped rim",
    "Braided challah bread loaf with a deep roast cocoa #3B2317 braided plait body, and warm baked cinnamon #C86446 intertwined dough strands and poppy seed dot accents",
    "Sliced sandwich toast bread loaf with a deep roast cocoa #3B2317 rectangular loaf silhouette, and a warm baked cinnamon #C86446 sliced bread slice standing alongside",
    "Handheld flour sifter dredge with a deep roast cocoa #3B2317 cylindrical sifter cup and handle, and warm baked cinnamon #C86446 squeeze trigger and bottom mesh screen",
    "Glass baking measuring jug cup with a deep roast cocoa #3B2317 jug body and pour spout, and warm baked cinnamon #C86446 fill level graduation tick markings and side handle",
    "Rectangular bread loaf baking tin pan with a deep roast cocoa #3B2317 folded metal pan body, and a warm baked cinnamon #C86446 rolled perimeter rim and bottom corrugations",
    "Round tiered sponge cake with a deep roast cocoa #3B2317 layered cake base, and warm baked cinnamon #C86446 frosting spread layers and piped top cream dollops",
    "Twisted chocolate cinnamon babka loaf with a deep roast cocoa #3B2317 loaf contour, and warm baked cinnamon #C86446 twisted swirl ribbons and streusel crumb toppings",
    "Silicone pastry basting brush with a deep roast cocoa #3B2317 brush handle and hanging loop, and warm baked cinnamon #C86446 flexible flat bristle fringe",
    "Stack of round biscuit cookie cutters with deep roast cocoa #3B2317 nested circular cutting bands, and warm baked cinnamon #C86446 rolled top rim grips",
    "Set of baking measuring spoons with deep roast cocoa #3B2317 spoon bowls, and warm baked cinnamon #C86446 connected ring hoop and stamped handle measurements",
    "Wicker bread display basket with a deep roast cocoa #3B2317 woven basket frame, and a warm baked cinnamon #C86446 folded fabric baker's cloth liner napkin",
    "Heart-shaped breakfast waffle with a deep roast cocoa #3B2317 scalloped waffle edge, and warm baked cinnamon #C86446 deep square grid indentations",
    "Glass sourdough starter jar with a deep roast cocoa #3B2317 jar contour and wire clamp lid, and warm baked cinnamon #C86446 bubbly fermented starter culture fill",
    "Fabric oven mitt baking glove with a deep roast cocoa #3B2317 mitt hand silhouette, and warm baked cinnamon #C86446 quilted diamond pattern seams and wrist hanging loop",
    "Pleated baker's toque chef hat with a deep roast cocoa #3B2317 gathering lower headband band, and a warm baked cinnamon #C86446 vertical pleated crown pouch",
    "Wooden dough kneading pastry board with a deep roast cocoa #3B2317 rectangular board surface, and warm baked cinnamon #C86446 front counter lip and concentric crust guide rings"
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
    if unique_hexes != {'#3B2317', '#C86446'}:
        print(f"ERROR: unexpected hex codes in prompt {i}: {unique_hexes}")
        
    prompts.append(p)

title = "Artisanal Bakery Bread and Pastry Baking Tools"
print(f"Title: {title} ({len(title)} chars, max 70)")
assert len(title) <= 70

keywords = "bakery icons, sourdough bread, cupcake, rolling pin, wire whisk, pastry tools, french baguette, croissant, dough scraper, piping bag, bread peel, stand mixer, banneton basket, baking pan, pie crust, challah bread, flour sifter, oven mitt, bakers hat, flat vector icons"
kw_list = [k.strip() for k in keywords.split(',')]
print(f"Keywords count: {len(kw_list)}")
assert len(kw_list) == 20

with open("/home/rifat/prompts/bakery_prompts.txt", "w") as f:
    for p in prompts:
        f.write(p + "\n")

print("All validations passed! bakery_prompts.txt written successfully!")
