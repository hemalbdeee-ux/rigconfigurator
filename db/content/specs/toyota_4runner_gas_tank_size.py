"""Spec page: Toyota 4Runner gas tank size. Figures copied from Toyota's 2024 4Runner brochure specification table."""
KEY = ('toyota', '4runner', 'gas-tank-size')
MAKE, MODEL, TOPIC_LABEL = 'Toyota', '4Runner', 'Gas tank size'
PUBLISH = True
PUBLISH_AT = '2026-11-24'

TITLE = 'Toyota 4Runner Gas Tank Size: 23 Gallons (2024)'
SEO_TITLE = 'Toyota 4Runner Gas Tank Size: 23 Gallons (2024)'
META = "Toyota 4Runner gas tank size from Toyota's 2024 spec table: 23 gallons on every grade, from SR5 to TRD Pro. How to estimate range from it."

FAQ = [('How many gallons does a 2024 Toyota 4Runner hold?', "23 gallons, by Toyota's 2024 specification table. The figure is the same in all seven grade columns."), ('Is the tank the same on the TRD Pro?', 'Yes. Toyota prints 23 gallons for the TRD Pro as for every other 2024 grade.'), ('How far will a tank take me?', 'Multiply the tank size by the EPA figure on your window sticker for an estimate; the usable range is lower because you refuel before empty.')]

PAGE = {'answer': "The 2024 Toyota 4Runner holds 23 gallons of fuel, according to Toyota's specification table. The figure is the same on every grade, from SR5 to TRD Pro.", 'covers': 'Model year 2024', 'not_covered': "2010 to 2023, and the redesigned 2025 and 2026 4Runner: Toyota's figures for these years are not on this page yet.", 'sections': [{'id': 'tank', 'h': 'Fuel tank capacity (2024)', 'table': {'head': ['Grades', 'Fuel tank'], 'rows': [['SR5, TRD Sport, SR5 Premium, TRD Off-Road, TRD Off-Road Premium, Limited and TRD Pro', '23 gal', 1]]}}], 'check': ["The pump may stop before or after the listed figure: the capacity is the tank's rated volume, not what fits after the low-fuel light.", 'For range, multiply the tank size by the fuel economy on your window sticker and allow a margin, since you refuel before empty.', 'The redesigned 2025 4Runner is a different vehicle: do not carry this figure forward to it.', "Your owner's manual and the labels on your own vehicle override this page."], 'related': ['roof-racks', 'cargo-boxes', 'hitches'], 'sources': [('Toyota, 2024 4Runner eBrochure, specifications and features tables', 'https://www.toyota.com/content/dam/toyota/brochures/pdf/2024/4runner_ebrochure.pdf')], 'reviewed': '2026-11-22'}
