import re

style_block = "Chunky solid flat glyph style with crisp rounded silhouettes and modern geometric contours, viewed from a direct flat 2D front perspective. Every shape features solid uniform fills separated by crisp negative space cutouts. The palette is strictly limited to two solid flat colors: deep blackberry #231A33 for the primary container silhouette, and tropical guava #E04F6E for straws, fruit garnishes, and beverage fill accents."

subjects = [
    "Mason jar fresh pressed juice with a deep blackberry #231A33 jar contour and threaded rim, and tropical guava #E04F6E striped straw and floating citrus wheel accents",
    "Thick blended smoothie in a deep blackberry #231A33 hurricane glass, and tropical guava #E04F6E wide straw and layered fruit puree wave accents",
    "Boba milk bubble tea cup with a deep blackberry #231A33 cup body and sealed film lid, and tropical guava #E04F6E diagonal fat straw and tapioca pearl spheres",
    "Vintage glass soda bottle with a deep blackberry #231A33 contoured fluted bottle body, and a tropical guava #E04F6E crimped crown bottle cap and carbonation bubbles",
    "Frozen slushie beverage cup with a deep blackberry #231A33 tapered cup base, and a tropical guava #E04F6E rounded dome lid and spoon-straw handle",
    "Takeaway fountain soda cup with a deep blackberry #231A33 paper cup silhouette, and tropical guava #E04F6E snap-on plastic lid and bent drinking straw",
    "Cold brew iced coffee glass bottle with a deep blackberry #231A33 bottle silhouette, and tropical guava #E04F6E label band, floating ice cubes, and straw",
    "Young coconut fresh water drink with a deep blackberry #231A33 round carved coconut shell, and tropical guava #E04F6E drinking straw and hibiscus blossom garnish",
    "Aluminum beverage soda can with a deep blackberry #231A33 cylinder can body, and tropical guava #E04F6E top rim, pull-tab ring, and condensation droplets",
    "Iced matcha latte tumbler with a deep blackberry #231A33 tumbler glass, and tropical guava #E04F6E floating ice cubes and straight reusable drinking straw",
    "Countertop masticating juicer machine with a deep blackberry #231A33 motor housing base, and a tropical guava #E04F6E feed chute, auger drum, and juice pitcher",
    "High-speed smoothie blender jar with a deep blackberry #231A33 pitcher body and handle, and tropical guava #E04F6E measuring tick marks and blender blade assembly",
    "Tabletop manual citrus juicer press with a deep blackberry #231A33 press frame and base, and a tropical guava #E04F6E reamer cone and halved citrus fruit",
    "Detox fruit-infused water jar with a deep blackberry #231A33 glass canister body, and tropical guava #E04F6E floating cucumber round slices and mint leaf sprigs",
    "Cocktail mocktail shaker tin with a deep blackberry #231A33 stainless shaker cup, and tropical guava #E04F6E built-in strainer cap and jigger cup top",
    "Chilled beverage ice bucket with a deep blackberry #231A33 bucket basin and bail handle, and tropical guava #E04F6E square ice cubes and metal scoop handle",
    "Tall fluted milkshake fountain glass with a deep blackberry #231A33 ribbed pedestal glass, and tropical guava #E04F6E swirl topping dollop and long dessert spoon",
    "Iced lemonade glass pitcher with a deep blackberry #231A33 pitcher body, pour spout, and handle, and tropical guava #E04F6E floating lemon wheels and ice cubes",
    "Vintage soda fountain draft tap with a deep blackberry #231A33 chrome dispensing tower, and a tropical guava #E04F6E pull tap handle and dispense nozzle",
    "Folded gable milk box pitcher with a deep blackberry #231A33 box silhouette, and tropical guava #E04F6E folded spout lip and beverage wave graphic",
    "Sparkling kombucha swing-top bottle with a deep blackberry #231A33 glass bottle body, and tropical guava #E04F6E wire bail clamp clasp and carbonation bubble dots",
    "Perforated boba tapioca scoop with a deep blackberry #231A33 long wire handle, and a tropical guava #E04F6E perforated ladle bowl holding tapioca pearls",
    "Insulated stainless steel travel tumbler with a deep blackberry #231A33 tumbler flask body, and tropical guava #E04F6E flip-top sip lid and silicone grip band",
    "Iced berry fruit tea glass mug with a deep blackberry #231A33 glass mug handle and body, and tropical guava #E04F6E strawberry garnish wedge and straw",
    "Handheld electric milk frother with a deep blackberry #231A33 battery motor handle, and a tropical guava #E04F6E stainless frothing coil whisk ring",
    "Frozen ice pop popsicle mold with a deep blackberry #231A33 multi-cavity mold base, and tropical guava #E04F6E reusable popsicle stick handles with drip guards",
    "Glass seltzer siphon bottle with a deep blackberry #231A33 mesh flask body, and a tropical guava #E04F6E siphon trigger lever and gas cylinder capsule casing",
    "Crushed ice cocktail tumbler with a deep blackberry #231A33 lowball glass rim, and tropical guava #E04F6E mounded crushed ice pellets and aromatic herb garnish",
    "Double-wall insulated drink cup with a deep blackberry #231A33 outer cup silhouette, and tropical guava #E04F6E floating coconut jelly cubes and angled straw",
    "Four-cup takeaway beverage carrier with a deep blackberry #231A33 molded drink tray, and tropical guava #E04F6E four nested beverage cup lids and straws"
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
    if unique_hexes != {'#231A33', '#E04F6E'}:
        print(f"ERROR: unexpected hex codes in prompt {i}: {unique_hexes}")
        
    prompts.append(p)

title = "Artisanal Chilled Juices Smoothies and Bubble Tea Icons"
print(f"Title: {title} ({len(title)} chars, max 70)")
assert len(title) <= 70

keywords = "beverage icons, bubble tea, smoothie glass, pressed juice, soda bottle, boba cup, iced coffee, blender jar, soda can, iced matcha, citrus juicer, milkshake glass, lemonade pitcher, kombucha bottle, seltzer siphon, tapioca pearls, detox water, travel tumbler, flat vector icons, solid glyphs"
kw_list = [k.strip() for k in keywords.split(',')]
print(f"Keywords count: {len(kw_list)}")
assert len(kw_list) == 20

with open("/home/rifat/prompts/beverages_prompts.txt", "w") as f:
    for p in prompts:
        f.write(p + "\n")

print("All validations passed! beverages_prompts.txt written successfully!")
