import re

style_block = "Chunky solid flat glyph style with bold rounded silhouettes and expressive geometric contours, rendered in a direct flat 2D front view. Every shape features solid uniform fills separated by crisp negative space cutouts. The palette is strictly limited to two solid flat colors: deep cast iron #252528 for the primary structural silhouette, and vibrant chili orange #E15A1D for all food textures, fiery spices, and stall fittings."

subjects = [
    "Skewered shish kebab with deep cast iron #252528 charred meat chunks and skewer rod, and vibrant chili orange #E15A1D sliced bell pepper squares and onion wedge accents",
    "Crispy pastry samosa with a deep cast iron #252528 triangular pastry base and crimped perimeter seam, and vibrant chili orange #E15A1D blistered crust texture and filling peak accents",
    "Takeaway street food noodle box with a deep cast iron #252528 folded cardboard carton and chopsticks, and vibrant chili orange #E15A1D curly wok noodles and chili slice accents",
    "Roadside tea stall station with a deep cast iron #252528 chai brewing kettle pot, and a vibrant chili orange #E15A1D wire caddy holding cutting chai glasses",
    "Vertical shawarma doner spit with a deep cast iron #252528 roasting skewer pole and carving knife, and a vibrant chili orange #E15A1D stacked marinated meat cone cylinder",
    "Round cast-iron cooking wok with a deep cast iron #252528 wok bowl and dual loop handles, and vibrant chili orange #E15A1D stir-fry spatula and rising steam vapor plumes",
    "Steamed bao bun in a bamboo steamer with a deep cast iron #252528 round woven steamer basket, and vibrant chili orange #E15A1D pleated dough bun top and slatted lid handle",
    "Japanese takoyaki octopus balls in a deep cast iron #252528 boat-shaped serving tray, featuring vibrant chili orange #E15A1D round batter balls with zigzag sauce drizzle and flakes",
    "Steamed momo dumplings with deep cast iron #252528 circular bamboo tray rims, and vibrant chili orange #E15A1D pleated dumpling pouches surrounding a central dipping sauce cup",
    "Mexican street corn elote with a deep cast iron #252528 wooden skewer stick, and a vibrant chili orange #E15A1D grilled corn cob coated in cheese crumb flecks and chili seasoning",
    "Crispy pani puri hollow sphere with a deep cast iron #252528 cracked puri shell rim, and vibrant chili orange #E15A1D spiced filling core and herb mint garnish leaf",
    "Grilled satay skewers with deep cast iron #252528 bamboo sticks and grill marks, and vibrant chili orange #E15A1D marinated meat cubes and a bowl of thick peanut sauce",
    "Vietnamese banh mi sandwich with a deep cast iron #252528 crusty split baguette roll, and vibrant chili orange #E15A1D meat slices, pickled carrot strips, and cilantro leaves",
    "Crispy falafel pita pocket with a deep cast iron #252528 round pita bread envelope, and vibrant chili orange #E15A1D herb falafel balls, tahini drizzle, and vegetable slices",
    "Battered street food corn dog with a deep cast iron #252528 wooden stick handle, and a vibrant chili orange #E15A1D golden fried cornmeal batter shell with a wavy mustard squiggle",
    "Grilled street sausage on a skewer with a deep cast iron #252528 skewer rod and grill char lines, and a vibrant chili orange #E15A1D plump sausage link with diagonal cut scores",
    "Japanese yakitori skewer with deep cast iron #252528 charred chicken pieces and skewer tip, and vibrant chili orange #E15A1D tare sauce glaze drops and scallion rounds",
    "Indian pav bhaji platter with deep cast iron #252528 round serving plate and toasted buns, and vibrant chili orange #E15A1D spiced vegetable bhaji curry bowl and lemon wedge",
    "Crispy fried spring rolls lumpia with deep cast iron #252528 rolled pastry wrappers and basket rim, and a vibrant chili orange #E15A1D dipping sauce bowl and chili seed flecks",
    "Roadside street food vendor kiosk stall with a deep cast iron #252528 booth framework and prep counter, and a vibrant chili orange #E15A1D striped canopy awning and hanging menu sign",
    "Flat-top griddle plancha with a deep cast iron #252528 cooking surface plate, and a vibrant chili orange #E15A1D rectangular burger smash spatula and sizzle splatter droplets",
    "Wire deep-fryer spider skimmer with a deep cast iron #252528 long wire handle, and a vibrant chili orange #E15A1D woven wire mesh basket lifting golden fried snack bites",
    "Handheld culinary blowtorch with a deep cast iron #252528 fuel canister body and trigger grip, and a vibrant chili orange #E15A1D burner nozzle and sear flame cone",
    "Paper cone of churros with a deep cast iron #252528 fluted paper sleeve cone, and vibrant chili orange #E15A1D ridged fried churro sticks and a warm dipping sauce cup",
    "Fresh street food coconut drink with a deep cast iron #252528 carved coconut husk shell, and vibrant chili orange #E15A1D drinking straw and festive cocktail umbrella",
    "Pair of street food squeeze sauce bottles with deep cast iron #252528 bottle bodies, and vibrant chili orange #E15A1D pointed nozzle dispensing caps and sauce stream droplet",
    "Stackable metal tiffin lunch box with a deep cast iron #252528 tiered round container tower, and vibrant chili orange #E15A1D locking latch clamps and top carry handle",
    "Sizzling cast-iron skillet platter with a deep cast iron #252528 heavy fajita pan and handle, and vibrant chili orange #E15A1D wooden underliner base and sizzling meat strips",
    "Mango sticky rice dessert with a deep cast iron #252528 folded banana leaf boat tray, and vibrant chili orange #E15A1D sliced ripe mango fillets and sesame seed toppings",
    "Roadside beverage dispenser jar with a deep cast iron #252528 glass beverage barrel and spigot tap, and vibrant chili orange #E15A1D metal lid and floating citrus fruit slices"
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
    if unique_hexes != {'#252528', '#E15A1D'}:
        print(f"ERROR: unexpected hex codes in prompt {i}: {unique_hexes}")
        
    prompts.append(p)

title = "Roadside Street Food Snacks and Vendor Stall Icons"
print(f"Title: {title} ({len(title)} chars, max 70)")
assert len(title) <= 70

keywords = "street food, shish kebab, samosa, noodle box, tea stall, chai kettle, shawarma spit, bao bun, takoyaki, momo dumplings, elote corn, banh mi, falafel pita, bamboo steamer, satay skewers, pani puri, food stall, churros cone, flat vector icons, solid glyphs"
kw_list = [k.strip() for k in keywords.split(',')]
print(f"Keywords count: {len(kw_list)}")
assert len(kw_list) == 20

with open("/home/rifat/prompts/street_food_prompts.txt", "w") as f:
    for p in prompts:
        f.write(p + "\n")

print("All validations passed! street_food_prompts.txt written successfully!")
