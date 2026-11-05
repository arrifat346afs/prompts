import re

style_block = "Chunky solid geometric glyphs with smooth rounded corners, rendered in a direct flat 2D front view. Every shape uses a single flat fill with crisp negative space cutout lines separating overlapping parts. The palette is restricted to three solid flat colors: obsidian black #18181B for the primary body silhouette, crimson red #E11D48 for main action elements, and golden yellow #F59E0B strictly for small badge accents."

subjects = [
    "Handheld retail price label gun with an obsidian black #18181B body, crimson red #E11D48 trigger and label roll slot, and a golden yellow #F59E0B star emblem accent",
    "Square gift box with an obsidian black #18181B box base, crimson red #E11D48 crisscross wrapping ribbon, and a golden yellow #F59E0B top bow accent",
    "Countdown stopwatch with an obsidian black #18181B circular casing, crimson red #E11D48 top push button and pointer hand, and golden yellow #F59E0B dial tick accents",
    "Symmetrical sand hourglass with an obsidian black #18181B outer support frame, crimson red #E11D48 glass bulbs, and golden yellow #F59E0B sand reservoir accents",
    "Perforated discount coupon ticket with an obsidian black #18181B ticket stub body, crimson red #E11D48 edge notches, and a golden yellow #F59E0B central diamond emblem",
    "Sealed cardboard parcel box with an obsidian black #18181B box silhouette, crimson red #E11D48 center adhesive tape strip, and a golden yellow #F59E0B corner fragile sticker accent",
    "Counter service desk call bell with an obsidian black #18181B stand base, crimson red #E11D48 curved chime dome, and a golden yellow #F59E0B top plunger button",
    "Unlocked open security padlock with an obsidian black #18181B rectangular lock body, crimson red #E11D48 swung-open curved shackle, and a golden yellow #F59E0B round keyhole accent",
    "Retail shopping gift card with an obsidian black #18181B card plate, crimson red #E11D48 horizontal ribbon band, and a golden yellow #F59E0B square microchip accent",
    "Twelve-pointed starburst deal rosette with an obsidian black #18181B outer starburst rim, crimson red #E11D48 inner circular core, and a golden yellow #F59E0B central star cutout accent",
    "Bi-fold pocket wallet with an obsidian black #18181B leather wallet fold, crimson red #E11D48 interior divider lining, and golden yellow #F59E0B credit card edge accents",
    "Electronic cash register terminal with an obsidian black #18181B register console, crimson red #E11D48 keypad button panel, and a golden yellow #F59E0B paper receipt feed accent",
    "Tailor cutting scissors snipping a line with obsidian black #18181B scissor blades, crimson red #E11D48 finger loop handles, and golden yellow #F59E0B dashed cut mark accents",
    "Storefront awning canopy with alternating obsidian black #18181B and crimson red #E11D48 roof stripes, crimson red valance scallops, and golden yellow #F59E0B hanging banner accents",
    "Ceramic coin piggy bank with an obsidian black #18181B piggy body, crimson red #E11D48 ear and snout accents, and a golden yellow #F59E0B coin drop slot",
    "Wire shopping basket with an obsidian black #18181B basket rim, crimson red #E11D48 grid mesh sides, and golden yellow #F59E0B folding wire handle grips",
    "Wooden mystery deal crate with an obsidian black #18181B wood plank frame, crimson red #E11D48 diagonal cross braces, and golden yellow #F59E0B reinforced metal corner bracket accents",
    "Pistol-grip barcode scanner with an obsidian black #18181B scanner housing, crimson red #E11D48 handle trigger, and a golden yellow #F59E0B optical scan target beam line",
    "Warehouse hand truck dolly with an obsidian black #18181B frame and wheels, crimson red #E11D48 lower toe plate, and golden yellow #F59E0B stacked parcel box accents",
    "Express delivery moped scooter with an obsidian black #18181B scooter chassis and wheels, crimson red #E11D48 front fairing and handlebars, and a golden yellow #F59E0B rear cargo storage box",
    "Unrolling paper till receipt with an obsidian black #18181B paper roll core, crimson red #E11D48 ribbon paper path, and golden yellow #F59E0B serrated tear-edge accents",
    "Circular prize giveaway wheel with an obsidian black #18181B wheel rim and floor stand, alternating crimson red #E11D48 wedges, and golden yellow #F59E0B boundary peg accents",
    "Crowd-control stanchion barrier post with an obsidian black #18181B upright post and round base, crimson red #E11D48 draped velvet rope, and golden yellow #F59E0B post finial accents",
    "Payment credit card with an obsidian black #18181B card plate, crimson red #E11D48 diagonal accent band, and a golden yellow #F59E0B contact microchip accent",
    "Angular lightning bolt flash emblem with an obsidian black #18181B outer silhouette backing, crimson red #E11D48 lightning zigzag bolt, and a golden yellow #F59E0B core spark accent",
    "Open antique treasure chest with an obsidian black #18181B lower chest body, crimson red #E11D48 raised curved lid, and golden yellow #F59E0B front latch and hinge accents",
    "Squeeze-frame coin purse with an obsidian black #18181B fabric pouch body, crimson red #E11D48 rim collar, and golden yellow #F59E0B dual metal ball-clasp accents",
    "Retail clothing anti-theft security sensor tag with an obsidian black #18181B circular hub body, crimson red #E11D48 lock core ring, and a golden yellow #F59E0B central pin cap accent",
    "Hanging storefront door plaque sign with an obsidian black #18181B rectangular plaque, crimson red #E11D48 inner border frame, and golden yellow #F59E0B suspension chain link accents",
    "Digital electronic shelf label with an obsidian black #18181B mounting bracket, crimson red #E11D48 display bezel casing, and a golden yellow #F59E0B digital screen panel accent"
]

forbidden = ["gradient", "fade", "glow", "shine", "glossy", "3d", "shadow", "soft light", "ombre", "metallic"]

print(f"Total subjects: {len(subjects)}")
assert len(subjects) == 30, "Not 30 subjects!"
assert len(set(subjects)) == 30, "Duplicate subjects exist!"

tail = "centered with even padding, plain solid white background, flat vector illustration style, solid flat colors only, uniform fills. Avoid: gradients, shading, shadows, glow, highlights, textures, transparency, blur, text."

prompts = []
for i, subj in enumerate(subjects, 1):
    p = f"{subj}, single icon, {style_block}, {tail}"
    # check forbidden words before 'Avoid:'
    before_avoid = p.split("Avoid:")[0].lower()
    for f in forbidden:
        # Match whole words or substrings as appropriate
        if re.search(r'\b' + re.escape(f) + r'\b', before_avoid):
            print(f"ERROR: forbidden word '{f}' in prompt {i} before Avoid:")
    prompts.append(p)

title = "Black Friday Flash Sale and Discount Checkout Mechanics"
print(f"Title length: {len(title)} chars (max 70)")
assert len(title) <= 70

keywords = "black friday, flash sale, doorbuster, discount voucher, price label gun, countdown timer, retail promotion, cash register, barcode scanner, mystery box, shopping basket, gift card, prize wheel, midnight sale, store awning, delivery scooter, checkout counter, coupon ticket, flat vector icons, solid glyphs"
kw_list = [k.strip() for k in keywords.split(',')]
print(f"Keywords count: {len(kw_list)}")
assert len(kw_list) == 20

print("All validations passed!")
