import re

style_block = "Chunky solid flat glyph style with crisp chamfered corners and clean geometric silhouettes, viewed from a direct flat 2D front perspective. Every element uses solid uniform fills separated by crisp negative space cutouts. The palette is strictly limited to two solid flat colors: deep film charcoal #1E293B for the primary body silhouette, and vivid cine amber #D97706 for all functional hardware accents and controls."

subjects = [
    "Director's slate clapperboard with a deep film charcoal #1E293B slate board, vivid cine amber #D97706 hinged top stick with chevron cutouts, and vivid cine amber #D97706 pivot screw accents",
    "Studio cinema camera with a deep film charcoal #1E293B camera body and matte box, and vivid cine amber #D97706 top handle, lens ring, and control dial accents",
    "Director's folding canvas chair with deep film charcoal #1E293B cross-strut legs and armrests, and vivid cine amber #D97706 canvas seat and backrest panels",
    "Studio fresnel spotlight with a deep film charcoal #1E293B lamp housing, and vivid cine amber #D97706 four-leaf barn door flaps, yoke bracket, and lens ring",
    "Telescopic camera crane jib arm with a deep film charcoal #1E293B main truss arm and fulcrum stand, and vivid cine amber #D97706 counterweight plates and pan-tilt head",
    "Steadicam camera stabilizing sled rig with a deep film charcoal #1E293B central post, and vivid cine amber #D97706 top mounting stage and bottom counterweight battery base",
    "Professional boom pole shotgun microphone with a deep film charcoal #1E293B slotted acoustic barrel and pole shaft, and vivid cine amber #D97706 suspension shock mount rings",
    "Celluloid 35mm motion picture film reel with deep film charcoal #1E293B three-spoke circular flanges, and vivid cine amber #D97706 central hub and curled film leader strip",
    "Round film reel canister tin with a deep film charcoal #1E293B base container, and vivid cine amber #D97706 lid cover plate and perimeter sealing clasp",
    "Vintage movie film projector with a deep film charcoal #1E293B cabinet body, and vivid cine amber #D97706 dual spoked film reels and front projection lens cone",
    "Director's pocket optical viewfinder monocular with a deep film charcoal #1E293B barrel casing, and vivid cine amber #D97706 knurled zoom collar and front lens ring",
    "Heavy-duty studio lighting C-stand with a deep film charcoal #1E293B three-leg turtle base and riser column, and vivid cine amber #D97706 extension gobo arm and grip knuckle heads",
    "Camera dolly track wheel carriage with a deep film charcoal #1E293B platform base, and vivid cine amber #D97706 skate wheels and dual parallel track rails",
    "Portable multi-track field audio sound recorder with a deep film charcoal #1E293B console chassis and side handles, and vivid cine amber #D97706 rotary gain knobs and meter dials",
    "Studio teleprompter hood unit with a deep film charcoal #1E293B camera shroud hood, and vivid cine amber #D97706 monitor tray frame and angled glass reflector outline",
    "Desktop celluloid film editing splicer with a deep film charcoal #1E293B base block, and vivid cine amber #D97706 hinged cutting lever and sprocket registration pins",
    "Wireless director's handheld video monitor cage with a deep film charcoal #1E293B monitor chassis, and vivid cine amber #D97706 dual handgrip frames and folding sun hood flaps",
    "Large studio softbox lighting diffuser with a deep film charcoal #1E293B rear reflector shell and mounting ring, and vivid cine amber #D97706 front diffusion baffle face",
    "Cinema follow focus controller unit with a deep film charcoal #1E293B rod clamp bridge and gear housing, and a vivid cine amber #D97706 manual focus handwheel",
    "Professional audio blimp zeppelin windscreen with a deep film charcoal #1E293B acoustic mesh capsule, and vivid cine amber #D97706 pistol grip handle and mount collar",
    "Wooden soundstage apple box block with a deep film charcoal #1E293B box body, and vivid cine amber #D97706 corner joinery seams and oval center carry handle cutout",
    "Studio sandbag saddle weight ballast with deep film charcoal #1E293B double saddle pouches, and vivid cine amber #D97706 reinforced perimeter trim and center carry handle",
    "Gaffer tape roll with a deep film charcoal #1E293B wound fabric tape body, and vivid cine amber #D97706 inner core ring and peeled tape leader tab",
    "Studio green screen background roll assembly with deep film charcoal #1E293B upright support stands, and vivid cine amber #D97706 crossbar roller and backdrop sheet corners",
    "Bound film screenplay script binder with deep film charcoal #1E293B cardstock script covers, and vivid cine amber #D97706 interior page block edge and screw post brads",
    "Soundstage industrial wind effect fan machine with a deep film charcoal #1E293B tubular tilting floor stand, and vivid cine amber #D97706 circular wire cage and fan propeller blades",
    "Professional cinema prime camera lens with a deep film charcoal #1E293B cylinder barrel, and vivid cine amber #D97706 knurled focus rings and front optical element ring",
    "Motion picture film negative strip segment with a deep film charcoal #1E293B film base ribbon, and vivid cine amber #D97706 rectangular frame dividers and edge sprocket holes",
    "Cinema camera V-mount brick battery pack with a deep film charcoal #1E293B battery housing block, and vivid cine amber #D97706 V-wedge lock mount and charge level indicator bars",
    "Studio production wireless walkie-talkie radio with a deep film charcoal #1E293B radio handset body, and vivid cine amber #D97706 top antenna, channel knob, and belt clip"
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
    
    # Check that only #1E293B and #D97706 appear as hex codes
    hexes = re.findall(r'#[0-9A-Fa-f]{6}', before_avoid)
    unique_hexes = set([h.upper() for h in hexes])
    if unique_hexes != {'#1E293B', '#D97706'}:
        print(f"ERROR: unexpected hex codes in prompt {i}: {unique_hexes}")
        
    prompts.append(p)

title = "Cinematography Equipment and Film Production Rig Icons"
print(f"Title: {title} ({len(title)} chars, max 70)")
assert len(title) <= 70

keywords = "film production, cinematography, camera rig, clapperboard, director chair, c-stand, boom microphone, film reel, follow focus, softbox, matte box, soundstage gear, teleprompter, movie equipment, prime lens, camera dolly, steadicam, apple box, flat vector icons, solid glyphs"
kw_list = [k.strip() for k in keywords.split(',')]
print(f"Keywords count: {len(kw_list)}")
assert len(kw_list) == 20

with open("/home/rifat/prompts/movies_prompts.txt", "w") as f:
    for p in prompts:
        f.write(p + "\n")

print("All validations passed with strictly 2 colors on white! movies_prompts.txt updated!")
