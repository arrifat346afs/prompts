import re

style_block = "Chunky solid flat glyph style with crisp chamfered corners and clean geometric silhouettes, viewed from a direct flat 2D front perspective. Each element uses solid uniform fills separated by fine white negative space cutout slits to define overlapping components. The palette consists of three solid flat colors: deep film charcoal #1E293B for the primary body silhouette, deep marine teal #0F766E for secondary hardware brackets and mount frames, and vivid cine amber #D97706 strictly for adjustment knobs, lens rings, and operational focal points."

subjects = [
    "Director's slate clapperboard with a deep film charcoal #1E293B slate board, deep marine teal #0F766E hinged top stick with zebra chevron cutouts, and vivid cine amber #D97706 pivot screw bolt accents",
    "Studio cinema camera with a deep film charcoal #1E293B camera body, deep marine teal #0F766E rectangular matte box lens hood and top handle, and vivid cine amber #D97706 control dial buttons",
    "Director's folding wooden canvas chair with deep film charcoal #1E293B cross-strut legs, deep marine teal #0F766E armrests and footrest, and vivid cine amber #D97706 taut canvas seat and backrest panels",
    "Studio fresnel spotlight with a deep film charcoal #1E293B cylindrical lamp housing, deep marine teal #0F766E four-leaf barn door flaps and yoke bracket, and vivid cine amber #D97706 lens ring and tilt lock knob",
    "Telescopic camera crane jib arm with a deep film charcoal #1E293B main truss arm, deep marine teal #0F766E fulcrum stand and pan-tilt head, and vivid cine amber #D97706 counterweight disc plates",
    "Steadicam camera stabilizing sled rig with a deep film charcoal #1E293B central carbon post, deep marine teal #0F766E bottom counterweight battery stage, and vivid cine amber #D97706 top camera mounting stage plate",
    "Professional boom pole shotgun microphone with a deep film charcoal #1E293B slotted acoustic barrel, deep marine teal #0F766E telescopic pole shaft, and vivid cine amber #D97706 elastic suspension shock mount bands",
    "Celluloid 35mm motion picture film reel with a deep film charcoal #1E293B reel hub, deep marine teal #0F766E three-spoke circular flanges, and vivid cine amber #D97706 curled film strip leader tape",
    "Round film reel canister tin with a deep film charcoal #1E293B base container, deep marine teal #0F766E lid cover plate, and vivid cine amber #D97706 perimeter sealing band clasp",
    "Vintage movie film projector with a deep film charcoal #1E293B projector body cabinet, deep marine teal #0F766E upper and lower dual spoked film reels, and vivid cine amber #D97706 front projection barrel cone",
    "Director's pocket optical viewfinder monocular with a deep film charcoal #1E293B barrel casing, deep marine teal #0F766E front objective ring, and vivid cine amber #D97706 knurled aspect ratio zoom collar",
    "Heavy-duty studio lighting C-stand with a deep film charcoal #1E293B three-leg turtle base, deep marine teal #0F766E vertical riser column and gobo extension arm, and vivid cine amber #D97706 circular grip knuckle heads",
    "Camera dolly track wheel carriage with a deep film charcoal #1E293B floor platform base, deep marine teal #0F766E skate wheel assemblies, and vivid cine amber #D97706 dual parallel track rails",
    "Portable multi-track field audio sound recorder with a deep film charcoal #1E293B console chassis, deep marine teal #0F766E side bumper handles, and vivid cine amber #D97706 rotary gain knobs and meter needles",
    "Studio teleprompter hood unit with a deep film charcoal #1E293B rear camera shroud hood, deep marine teal #0F766E monitor tray frame, and vivid cine amber #D97706 angled beam-splitter glass pane outline",
    "Desktop celluloid film editing splicer with a deep film charcoal #1E293B cast base block, deep marine teal #0F766E hinged cutting guillotine lever, and vivid cine amber #D97706 sprocket registration pins",
    "Wireless director's handheld video monitor cage with a deep film charcoal #1E293B monitor chassis, deep marine teal #0F766E dual ergonomic handgrip frames, and vivid cine amber #D97706 folding sun hood flaps",
    "Large studio softbox lighting diffuser with a deep film charcoal #1E293B rear reflector shell, deep marine teal #0F766E mounting speed ring, and vivid cine amber #D97706 rectangular front diffusion panel face",
    "Cinema follow focus controller unit with a deep film charcoal #1E293B rod clamp bridge, deep marine teal #0F766E drive gear housing, and vivid cine amber #D97706 large white-ring focus handwheel",
    "Professional audio blimp zeppelin windscreen with a deep film charcoal #1E293B pistol grip handle, deep marine teal #0F766E rounded acoustic mesh capsule, and vivid cine amber #D97706 internal suspension rings",
    "Wooden soundstage apple box block with a deep film charcoal #1E293B box body, deep marine teal #0F766E corner joinery seams, and vivid cine amber #D97706 oval center carry handle cutout",
    "Studio sandbag saddle weight ballast with deep film charcoal #1E293B double saddle pouches, deep marine teal #0F766E reinforced perimeter stitching, and a vivid cine amber #D97706 center webbing carry handle",
    "Gaffer tape roll with a deep film charcoal #1E293B inner cardboard tube core, deep marine teal #0F766E wound fabric tape body, and vivid cine amber #D97706 peeled tape leader tab",
    "Studio green screen background roll assembly with deep film charcoal #1E293B upright support stands, deep marine teal #0F766E crossbar roller, and vivid cine amber #D97706 backdrop sheet corners",
    "Bound film screenplay script binder with deep film charcoal #1E293B cardstock script covers, deep marine teal #0F766E stacked interior paper page block, and vivid cine amber #D97706 round brass screw post brads",
    "Soundstage industrial wind effect fan machine with a deep film charcoal #1E293B tubular tilting floor stand, deep marine teal #0F766E circular blade wire shroud, and vivid cine amber #D97706 three-blade fan prop",
    "Professional cinema prime camera lens with a deep film charcoal #1E293B lens cylinder barrel, deep marine teal #0F766E lens mount bayonet, and vivid cine amber #D97706 knurled aperture and focus scale rings",
    "Motion picture film negative strip segment with a deep film charcoal #1E293B film base ribbon, deep marine teal #0F766E rectangular frame dividers, and vivid cine amber #D97706 bilateral edge sprocket holes",
    "Cinema camera V-mount brick battery pack with a deep film charcoal #1E293B battery housing block, deep marine teal #0F766E V-wedge lock mount, and vivid cine amber #D97706 LED charge level indicator bars",
    "Studio production wireless walkie-talkie radio with a deep film charcoal #1E293B radio handset body, deep marine teal #0F766E top antenna and belt clip, and vivid cine amber #D97706 channel knob and push-to-talk button"
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

print("All validations passed and movies_prompts.txt written successfully!")
