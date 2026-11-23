"""Spec page: Ford Ranger gas tank size. Figures copied from Ford's 2026 technical specification sheet."""
KEY = ('ford', 'ranger', 'gas-tank-size')
MAKE, MODEL, TOPIC_LABEL = 'Ford', 'Ranger', 'Gas tank size'
PUBLISH = True
PUBLISH_AT = '2026-11-22'

TITLE = 'Ford Ranger Gas Tank Size: 18.7 Gallons, 20.3 on the Raptor (2026)'
SEO_TITLE = 'Ford Ranger Gas Tank Size by Engine (2026)'
META = "Ford Ranger gas tank size from Ford's 2026 spec sheet: 18.7 gallons with the 2.3L or 2.7L EcoBoost and 20.3 gallons on the Raptor."

FAQ = [('How many gallons does a Ford Ranger hold?', "18.7 gallons with the 2.3L EcoBoost or the 2.7L EcoBoost V6, by Ford's 2026 specification sheet."), ('How big is the Ranger Raptor fuel tank?', '20.3 gallons. Ford lists that figure for the 3.0L V6, which it marks as Raptor only.'), ('How far will a tank take me?', 'Multiply the tank size by the EPA figure on your window sticker for an estimate; the usable range is lower because you refuel before empty.')]

PAGE = {'answer': "The 2026 Ford Ranger holds 18.7 gallons of fuel with the 2.3L EcoBoost or the 2.7L EcoBoost V6, according to Ford's specification sheet. The Ranger Raptor, with the 3.0L V6, holds 20.3 gallons.", 'covers': 'Model year 2026', 'not_covered': "2019 to 2025: Ford's sheets for these years are not on this page yet.", 'sections': [{'id': 'tank', 'h': 'Fuel tank capacity by engine (2026)', 'table': {'head': ['Engine', 'Fuel tank capacity'], 'rows': [['2.3L EcoBoost I-4 and 2.7L EcoBoost V6', '18.7 gal', 1], ['3.0L V6 (Raptor only)', '20.3 gal', 1]]}, 'notes': ["Ford's table lists the tank by engine only and has no footnote."]}], 'check': ['Confirm the engine on your window sticker: the Raptor is the only version with the larger tank.', "The pump may stop before or after the listed figure: the capacity is the tank's rated volume, not what fits after the low-fuel light.", 'For range, multiply the tank size by the fuel economy on your window sticker and allow a margin, since you refuel before empty.', "Your owner's manual and the labels on your own vehicle override this page."], 'related': ['tonneau-covers', 'bed-racks', 'hitches'], 'sources': [('Ford, 2026 Ranger Technical Specifications (v1.0, 13 Jan 2026)', 'https://www.fromtheroad.ford.com/content/dam/fordmediasite/us/en/library/2026/specs/2026_Ford_Ranger%20Technical_Specs.pdf')], 'reviewed': '2026-11-21'}
