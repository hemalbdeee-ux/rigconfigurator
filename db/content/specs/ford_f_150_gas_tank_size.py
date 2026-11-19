"""Spec page: Ford F-150 gas tank size. Figures copied from Ford's 2026 technical specification sheet."""
KEY = ('ford', 'f-150', 'gas-tank-size')
MAKE, MODEL, TOPIC_LABEL = "Ford", 'F-150', 'Gas tank size'
PUBLISH = True
PUBLISH_AT = '2026-11-19'

TITLE = 'Ford F-150 Gas Tank Size by Engine (2026)'
SEO_TITLE = 'Ford F-150 Gas Tank Size by Engine (2026)'
META = "Ford F-150 gas tank size from Ford's 2026 spec sheet: 23, 30.6 or 36 gallons, depending on the engine, cab and box."

FAQ = [('How many gallons does an F-150 hold?', '23, 30.6 or 36 gallons for 2026. Most trucks have the 36 gallon tank, the PowerBoost hybrid has 30.6 gallons, and the shortest-wheelbase 2.7L and 5.0L trucks have 23 gallons.'), ('Which F-150 has the 36 gallon tank?', "By Ford's 2026 sheet: the 3.5L EcoBoost, the 3.5L High Output and the 5.2L V8 in every configuration, and the 2.7L and 5.0L except on the shortest wheelbase."), ("How big is the hybrid's tank?", '30.6 gallons for the 3.5L PowerBoost.')]

PAGE = {'answer': 'The 2026 Ford F-150 has a 23, 30.6 or 36 gallon fuel tank. The 3.5L PowerBoost hybrid holds 30.6 gallons. The other engines hold 36 gallons, except the 2.7L EcoBoost and 5.0L V8 on the shortest wheelbase, which hold 23 gallons.', 'reviewed': '2026-11-19', 'covers': 'Model year 2026', 'not_covered': 'Earlier model years are not on this page yet.', 'sections': [{'id': 'tank', 'h': 'Fuel tank capacity by engine (2026)', 'intro': 'Ford states that capacity depends on the cab and box configuration.', 'table': {'head': ['Engine', 'Fuel tank capacity'], 'rows': [['2.7L EcoBoost V6', '23.0 gal (122.5 in wheelbase); 36 gal (all others)', 1], ['5.0L V8', '23.0 gal (122.5 in wheelbase); 36 gal (all others)', 1], ['3.5L EcoBoost V6', '36.0 gal', 1], ['3.5L PowerBoost Full Hybrid V6', '30.6 gal', 1], ['3.5L EcoBoost V6 High Output', '36.0 gal', 1], ['5.2L supercharged V8', '36.0 gal', 1]]}, 'notes': ["Ford's fuel table prints the short wheelbase as 122.5 in. Elsewhere the same sheet lists the Regular Cab with the 6.5 ft box, the shortest F-150, at 122.8 in."]}], 'check': ["The fuel tank capacity for your truck is in the capacities table of its owner's manual.", 'A Regular Cab with the 6.5 ft box and the 2.7L or 5.0L engine is the truck to check for the 23 gallon tank.', "Your owner's manual and the labels on your own vehicle override this page."], 'related': ['hitches', 'tonneau-covers'], 'sources': [('Ford, 2026 F-150 Technical Specifications (v1.1, 31 Mar 2026)', 'https://www.fromtheroad.ford.com/content/dam/fordmediasite/us/en/library/2026/specs/2026_Ford_F150_Specs.pdf')]}
