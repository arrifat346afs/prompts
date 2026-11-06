import re

style_block = "Chunky solid flat glyph style with refined rounded corners and elegant geometric contours, viewed from a direct flat 2D front perspective. Every shape features solid uniform fills separated by crisp negative space cutouts. The palette is strictly limited to two solid flat colors: deep Parisian navy #152238 for the primary structural silhouette, and warm champagne gold #C89D3C for fine dining accents, trims, and service details."

subjects = [
    "Leather-bound restaurant dining menu with a deep Parisian navy #152238 folder cover, and warm champagne gold #C89D3C corner protector brackets and ribbon bookmark",
    "Formal restaurant dining table with a deep Parisian navy #152238 pedestal base and flanking chairs, and a warm champagne gold #C89D3C draped floor-length tablecloth",
    "Waiter service cloche platter carried on a deep Parisian navy #152238 serving hand and arm, featuring a warm champagne gold #C89D3C domed platter lid and folded linen towel",
    "Restaurant bill presenter folder with a deep Parisian navy #152238 leather booklet cover, and warm champagne gold #C89D3C paper receipt tab and payment card corner",
    "Domed restaurant food cloche cover with a deep Parisian navy #152238 round serving platter plate, and a warm champagne gold #C89D3C domed bell lid and top lift knob",
    "Fine dining formal place setting with deep Parisian navy #152238 dinner fork, knife, and soup spoon, and a warm champagne gold #C89D3C circular rimmed dinner plate",
    "Tabletop reservation stand with a deep Parisian navy #152238 pedestal stem and weighted base, and a warm champagne gold #C89D3C reserved plaque card panel",
    "Pair of long-stemmed wine glasses with deep Parisian navy #152238 glass stems and bases, and warm champagne gold #C89D3C wine glass bowls clinking in a toast",
    "Tabletop champagne ice bucket with a deep Parisian navy #152238 bucket basin and ring handles, and a warm champagne gold #C89D3C chilled champagne bottle neck and ice cubes",
    "Folded formal table napkin with deep Parisian navy #152238 folded linen cloth pleats, and a warm champagne gold #C89D3C napkin ring band and standing crown fold",
    "Dining table candle holder with a deep Parisian navy #152238 candlestick holder base, and a warm champagne gold #C89D3C tall taper candle stick and teardrop flame",
    "Tiered dessert trolley stand with a deep Parisian navy #152238 structural upright frame and caster wheels, and warm champagne gold #C89D3C round tiered serving shelf plates",
    "Sommelier tastevin cup medallion with a deep Parisian navy #152238 link chain loop, and a warm champagne gold #C89D3C shallow fluted wine tasting dish",
    "Waiter's pocket corkscrew tool with a deep Parisian navy #152238 folding lever body, and warm champagne gold #C89D3C spiral worm screw and foil cutter blade",
    "Desktop service call bell with a deep Parisian navy #152238 circular stand base, and a warm champagne gold #C89D3C domed chime bell and top push button",
    "Woven table bread basket with a deep Parisian navy #152238 wicker basket basin, and warm champagne gold #C89D3C folded cloth napkin and crusty bread rolls",
    "Wide-base wine decanter with a deep Parisian navy #152238 aerating flask base, and a warm champagne gold #C89D3C slender pouring spout and wine liquid level",
    "Table condiments caddy rack with a deep Parisian navy #152238 wire carrier frame and handle, and warm champagne gold #C89D3C porcelain salt and pepper cruets",
    "Traditional ceramic gravy boat with a deep Parisian navy #152238 sauce boat saucer, and a warm champagne gold #C89D3C pouring boat body and curved loop handle",
    "Outdoor restaurant menu podium stand with a deep Parisian navy #152238 floor stanchion post, and a warm champagne gold #C89D3C illuminated menu display cabinet case",
    "Hanging wine glass stemware rack with a deep Parisian navy #152238 overhead ceiling track channel, and warm champagne gold #C89D3C hanging stemware glass bases",
    "Porcelain espresso cup and saucer with a deep Parisian navy #152238 saucer dish and cup handle, and a warm champagne gold #C89D3C coffee cup bowl and stirring spoon",
    "Table crumber sweeper blade with a deep Parisian navy #152238 pocket clip handle, and a warm champagne gold #C89D3C curved stainless table scraping blade",
    "Formal waiter tuxedo vest uniform with deep Parisian navy #152238 tailored vest panels, and a warm champagne gold #C89D3C bowtie, buttons, and pocket square handkerchief",
    "Coat check token hanger with a deep Parisian navy #152238 coat hanger silhouette, and a warm champagne gold #C89D3C circular claim check token ring",
    "Fine dining finger bowl with a deep Parisian navy #152238 underplate saucer, and a warm champagne gold #C89D3C rinse water bowl basin and floating lemon slice",
    "Lazy Susan tabletop turntable with a deep Parisian navy #152238 rotating turntable disc base, and warm champagne gold #C89D3C appetizer condiment ramekin bowls",
    "Dessert sorbet coupe glass with a deep Parisian navy #152238 pedestal stem and foot, and warm champagne gold #C89D3C wide coupe bowl and rounded sorbet scoop",
    "Restaurant dining booth with a deep Parisian navy #152238 high-back tufted bench seat, and a warm champagne gold #C89D3C dining tabletop and support pedestal",
    "Maitre d' host greeting podium with a deep Parisian navy #152238 floor lectern stand, and a warm champagne gold #C89D3C reservation ledger book and desk light hood"
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
    if unique_hexes != {'#152238', '#C89D3C'}:
        print(f"ERROR: unexpected hex codes in prompt {i}: {unique_hexes}")
        
    prompts.append(p)

title = "Fine Dining Hospitality Service and Table Setting Icons"
print(f"Title: {title} ({len(title)} chars, max 70)")
assert len(title) <= 70

keywords = "restaurant icons, dining menu, restaurant table, waiter service, bill presenter, food cloche, place setting, wine glasses, champagne bucket, folded napkin, corkscrew, wine decanter, service bell, bread basket, gravy boat, host podium, table booth, banquet service, flat vector icons, solid glyphs"
kw_list = [k.strip() for k in keywords.split(',')]
print(f"Keywords count: {len(kw_list)}")
assert len(kw_list) == 20

with open("/home/rifat/prompts/restaurant_prompts.txt", "w") as f:
    for p in prompts:
        f.write(p + "\n")

print("All validations passed! restaurant_prompts.txt written successfully!")
