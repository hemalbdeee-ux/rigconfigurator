"""Spec page: Ford Bronco gas tank size. Figures copied from Ford's 2026 technical specification sheet."""
KEY = ('ford', 'bronco', 'gas-tank-size')
MAKE, MODEL, TOPIC_LABEL = "Ford", 'Bronco', 'Gas tank size'
PUBLISH = True
PUBLISH_AT = '2026-11-21'

TITLE = 'Ford Bronco Gas Tank Size: 2-Door and 4-Door (2026)'
SEO_TITLE = 'Ford Bronco Gas Tank Size: 2-Door vs 4-Door (2026)'
META = "Ford Bronco gas tank size from Ford's 2026 spec sheet: 16.9 gallons on the 2-door and 20.8 gallons on the 4-door."

FAQ = [('How many gallons does a Ford Bronco hold?', "16.9 gallons on the 2-door and 20.8 gallons on the 4-door, by Ford's 2026 specification sheet."), ('Does the engine change the tank size?', "Ford's sheet lists the tank by body style only, 2-door or 4-door. It gives no separate figure by engine or trim."), ('How far will a tank take me?', 'Multiply the tank size by the EPA figure on your window sticker for an estimate; the usable range is lower because you refuel before empty.')]

PAGE = {'answer': "The 2026 Ford Bronco holds 16.9 gallons of fuel as a 2-door and 20.8 gallons as a 4-door, according to Ford's specification sheet.", 'reviewed': '2026-11-20', 'covers': 'Model year 2026', 'not_covered': "2021 to 2025: Ford's sheets for these years are not on this page yet. This page is about the Bronco, not the Bronco Sport.", 'sections': [{'id': 'tank', 'h': 'Fuel tank capacity by body style (2026)', 'table': {'head': ['Body style', 'Fuel tank capacity'], 'rows': [['2-Door', '16.9 gal', 1], ['4-Door', '20.8 gal', 1]]}, 'notes': ["Ford's table has no footnote and no breakdown by engine or trim."]}], 'check': ["Count the doors: Ford's figure depends only on the body style.", "The pump may stop before or after the listed figure: the capacity is the tank's rated volume, not what fits after the low-fuel light.", 'For range, multiply the tank size by the fuel economy on your window sticker and allow a margin, since you refuel before empty.', "Your owner's manual and the labels on your own vehicle override this page."], 'related': ['roof-racks', 'cargo-boxes', 'hitches'], 'sources': [('Ford, 2026 Bronco Technical Specifications (v1.0, 18 Feb 2026)', 'https://www.fromtheroad.ford.com/content/dam/fordmediasite/us/en/library/2026/specs/2026_Ford_Bronco_Technical_Specifications.pdf')]}
