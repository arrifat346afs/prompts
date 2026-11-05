import re

style_block = "Chunky solid flat glyph style with refined tapered corners and clean geometric contours, viewed from a direct flat 2D front perspective. Every shape features solid uniform fills separated by crisp negative space cutouts. The palette is strictly limited to two solid flat colors: deep forest thyme #1C382B for the primary cookware silhouette, and warm culinary copper #C56B34 for handles, seasoning accents, and culinary tools."

subjects = [
    "Heavy frying pan skillet with a deep forest thyme #1C382B round skillet basin, and a warm culinary copper #C56B34 ergonomic long handle and helper loop grip",
    "Japanese santoku chef knife with a deep forest thyme #1C382B wide chopper blade, and a warm culinary copper #C56B34 riveted handle scale and bolster collar",
    "Glass seasoning spice jar with a deep forest thyme #1C382B jar contour and spice leaf emblem, and a warm culinary copper #C56B34 perforated sprinkler shaker lid",
    "Open culinary recipe book with deep forest thyme #1C382B hardcover binding and page spreads, and warm culinary copper #C56B34 text divider rules and hanging ribbon bookmark",
    "Heavy Dutch oven casserole pot with a deep forest thyme #1C382B round pot body and domed lid, and warm culinary copper #C56B34 dual loop side handles and top lid knob",
    "End-grain cutting chopping board with a deep forest thyme #1C382B rectangular wooden block body, and warm culinary copper #C56B34 routed perimeter juice groove and corner grip cutouts",
    "Stone mortar and pestle with a deep forest thyme #1C382B heavy grinding bowl, and a warm culinary copper #C56B34 pestle club and crushed herb leaf flecks",
    "Four-sided box grater with a deep forest thyme #1C382B pyramid grating tower and base rim, and a warm culinary copper #C56B34 top grip handle and perforated shredding teeth",
    "Tall wooden pepper mill grinder with a deep forest thyme #1C382B turned wooden body, and a warm culinary copper #C56B34 adjustment screw knob and ground pepper flakes",
    "Straight-sided sauté pan with a deep forest thyme #1C382B flat cooking basin, and warm culinary copper #C56B34 long pan handle and domed lid handle",
    "Curved mezzaluna mincing knife with a deep forest thyme #1C382B crescent rocking blade, and warm culinary copper #C56B34 twin vertical knob handles and herb sprigs",
    "Ceramic ramekin prep dish with a deep forest thyme #1C382B fluted bowl wall, and warm culinary copper #C56B34 minced herb garnish and rim edge",
    "Handheld lemon citrus squeezer with deep forest thyme #1C382B press lever handles, and a warm culinary copper #C56B34 hinged juicing cup with juice droplets",
    "Heavy-duty kitchen poultry shears with deep forest thyme #1C382B notched scissor blades, and warm culinary copper #C56B34 textured loop handles and hinge rivet",
    "Scalloped cooking tongs with deep forest thyme #1C382B spring arm bands, and warm culinary copper #C56B34 scalloped claw tips and pull-lock tab ring",
    "Footed mesh colander strainer with a deep forest thyme #1C382B perforated bowl and pedestal base, and warm culinary copper #C56B34 dual side loop carry handles",
    "Deep soup ladle with a deep forest thyme #1C382B cupped ladle bowl, and a warm culinary copper #C56B34 curved stem handle and hanging hook tip",
    "Glass olive oil cruet dispenser with a deep forest thyme #1C382B teardrop flask body, and a warm culinary copper #C56B34 tapered metal pouring spout and falling oil droplet",
    "Deep culinary stockpot cauldron with a deep forest thyme #1C382B cylindrical pot body, and warm culinary copper #C56B34 dual riveted ear handles and lid handle",
    "Oval ceramic gratin baking dish with a deep forest thyme #1C382B shallow baking basin, and warm culinary copper #C56B34 tab end handles and baked crumb crust accents",
    "Handheld mandoline vegetable slicer with a deep forest thyme #1C382B flat runway ramp frame, and a warm culinary copper #C56B34 angled cutting blade and food safety guard",
    "Wall-mounted magnetic knife bar strip with a deep forest thyme #1C382B mounting rail bar, and warm culinary copper #C56B34 culinary knife silhouettes clinging to the magnet",
    "Digital instant-read meat thermometer with a deep forest thyme #1C382B handheld display unit, and a warm culinary copper #C56B34 pivot needle probe and temperature display cutout",
    "Aromatic bouquet garni herb bundle with deep forest thyme #1C382B bundled rosemary and thyme sprigs, and a warm culinary copper #C56B34 knotted twine tie string and bay leaf",
    "Flat-edged wooden cooking stir spoon with a deep forest thyme #1C382B oval bowl and center hole cutout, and a warm culinary copper #C56B34 long straight handle",
    "Crank-handle food mill sieve with a deep forest thyme #1C382B straining bowl basin, and a warm culinary copper #C56B34 rotary crank lever and wooden knob handle",
    "Kitchen spoon rest tray with a deep forest thyme #1C382B contoured resting cradle, and a warm culinary copper #C56B34 sauce droplet pool and rim line",
    "Lever-action garlic press crusher with a deep forest thyme #1C382B perforated grid basket, and warm culinary copper #C56B34 ergonomic lever handles and plunger plate",
    "Pair of glass salt and pepper shakers with deep forest thyme #1C382B faceted shaker bodies, and warm culinary copper #C56B34 perforated screw caps and seasoning dots",
    "Set of culinary measuring cups nested together with deep forest thyme #1C382B graduated cup bowls, and warm culinary copper #C56B34 stacked handle tabs and connecting ring loop"
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
    if unique_hexes != {'#1C382B', '#C56B34'}:
        print(f"ERROR: unexpected hex codes in prompt {i}: {unique_hexes}")
        
    prompts.append(p)

title = "Culinary Kitchen Cookware and Seasoning Prep Icons"
print(f"Title: {title} ({len(title)} chars, max 70)")
assert len(title) <= 70

keywords = "cooking icons, frying pan, chef knife, spice jar, recipe book, dutch oven, cutting board, mortar pestle, pepper mill, box grater, mezzaluna, lemon squeezer, cooking tongs, stockpot, oil cruet, colander, garlic press, kitchen tools, flat vector icons, solid glyphs"
kw_list = [k.strip() for k in keywords.split(',')]
print(f"Keywords count: {len(kw_list)}")
assert len(kw_list) == 20

with open("/home/rifat/prompts/cooking_prompts.txt", "w") as f:
    for p in prompts:
        f.write(p + "\n")

print("All validations passed! cooking_prompts.txt written successfully!")
