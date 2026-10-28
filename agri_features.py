"""
AgriNet Smart Agricultural Tools & Assistant Engine
Provides calculations, database lookup, and conversational agronomy intelligence.
"""

import re

# 1. FERTILIZER & NPK RECOMMENDATION ENGINE
FERTILIZER_CROP_DB = {
    "wheat": {
        "name": "Wheat (Gehu)",
        "npk": (120, 60, 40), # kg N, P2O5, K2O per hectare
        "fym_ton": 5.0,
        "zinc_kg": 10.0,
        "stages": {
            "Basal / Sowing": "Apply 50% Nitrogen, 100% Phosphorus, and 100% Potash at sowing time.",
            "Crown Root Initiation (21 DAS)": "Top-dress 25% Nitrogen with first irrigation (Crown root stage).",
            "Tillering / Flowering (45 DAS)": "Top-dress remaining 25% Nitrogen before flowering."
        }
    },
    "rice": {
        "name": "Rice / Paddy (Dhan)",
        "npk": (100, 50, 50),
        "fym_ton": 6.0,
        "zinc_kg": 12.0,
        "stages": {
            "Basal / Transplanting": "Apply 50% Nitrogen + 100% DAP & MOP during final puddling.",
            "Active Tillering (25-30 DAT)": "Top-dress 25% Nitrogen with standing water.",
            "Panicle Initiation (50-55 DAT)": "Top-dress remaining 25% Nitrogen."
        }
    },
    "tomato": {
        "name": "Tomato (Tamatar)",
        "npk": (150, 100, 120),
        "fym_ton": 8.0,
        "zinc_kg": 8.0,
        "stages": {
            "Basal / Transplanting": "Apply 30% Nitrogen + 100% Phosphorus + 40% Potash as basal dose.",
            "Vegetative / First Flower": "Apply 35% Nitrogen + 30% Potash 3 weeks after transplanting.",
            "Fruit Setting & Bulking": "Apply remaining 35% Nitrogen + 30% Potash in 2-3 fertigation splits."
        }
    },
    "potato": {
        "name": "Potato (Aalu)",
        "npk": (180, 100, 150),
        "fym_ton": 10.0,
        "zinc_kg": 10.0,
        "stages": {
            "Basal at Planting": "Apply 50% Nitrogen + 100% Phosphorus + 100% Potash in furrows.",
            "Earthing-up (30-35 DAP)": "Top-dress remaining 50% Nitrogen prior to earthing up and tuber initiation."
        }
    },
    "corn": {
        "name": "Corn / Maize (Makka)",
        "npk": (120, 60, 40),
        "fym_ton": 6.0,
        "zinc_kg": 10.0,
        "stages": {
            "Basal": "Apply 33% Nitrogen + 100% Phosphorus + 100% Potash at sowing.",
            "Knee-High Stage (30 DAS)": "Top-dress 33% Nitrogen with hoeing.",
            "Tasseling Stage (50 DAS)": "Top-dress remaining 34% Nitrogen."
        }
    },
    "cotton": {
        "name": "Cotton (Kapas)",
        "npk": (150, 60, 60),
        "fym_ton": 6.0,
        "zinc_kg": 10.0,
        "stages": {
            "Basal at Sowing": "Apply 25% Nitrogen + 100% Phosphorus + 50% Potash.",
            "Square Formation (45 DAS)": "Apply 50% Nitrogen in band placement.",
            "Boll Development (75 DAS)": "Apply remaining 25% Nitrogen + 50% Potash."
        }
    },
    "sugarcane": {
        "name": "Sugarcane (Ganna)",
        "npk": (250, 115, 115),
        "fym_ton": 12.0,
        "zinc_kg": 15.0,
        "stages": {
            "Basal Planting": "Apply 25% Nitrogen + 100% Phosphorus + 50% Potash in furrows.",
            "Tillering (45-60 DAP)": "Apply 50% Nitrogen.",
            "Grand Growth (90-120 DAP)": "Apply remaining 25% Nitrogen + 50% Potash before earthing."
        }
    },
    "onion": {
        "name": "Onion (Pyaz)",
        "npk": (100, 50, 80),
        "fym_ton": 8.0,
        "zinc_kg": 6.0,
        "stages": {
            "Basal": "Apply 50% Nitrogen + 100% Phosphorus + 100% Potash.",
            "Bulb Development (30-45 DAT)": "Top-dress remaining 50% Nitrogen."
        }
    },
    "mustard": {
        "name": "Mustard (Sarson)",
        "npk": (80, 40, 40),
        "fym_ton": 4.0,
        "zinc_kg": 8.0,
        "stages": {
            "Basal": "Apply 50% Nitrogen + 100% Phosphorus + 100% Potash + 20 kg Sulfur per hectare.",
            "First Irrigation (30 DAS)": "Top-dress remaining 50% Nitrogen."
        }
    },
    "soybean": {
        "name": "Soybean",
        "npk": (30, 80, 40), # Legume: needs low N due to Rhizobium nodules
        "fym_ton": 4.0,
        "zinc_kg": 8.0,
        "stages": {
            "Basal": "Apply 100% N, P, and K at sowing along with Rhizobium seed treatment."
        }
    },
    "apple": {
        "name": "Apple Orchard (Seb)",
        "npk": (140, 70, 140),
        "fym_ton": 15.0,
        "zinc_kg": 5.0,
        "stages": {
            "Dormancy / Early Spring": "Apply 50% N + 100% P + 100% K in basin beneath drip line.",
            "Fruit Set (3 weeks post-bloom)": "Apply remaining 50% Nitrogen."
        }
    }
}

def calculate_fertilizer(crop_key, area, unit="Acre"):
    """
    Computes exact commercial fertilizer bags/kg (Urea, DAP, MOP)
    based on NPK recommendations and land area.
    """
    crop_key = crop_key.lower().strip()
    # Find matching crop
    match_crop = None
    for key, data in FERTILIZER_CROP_DB.items():
        if key in crop_key or crop_key in key:
            match_crop = data
            break
            
    if not match_crop:
        match_crop = FERTILIZER_CROP_DB["wheat"]
        
    # Convert unit to Hectares (standard base)
    unit_lower = unit.lower().strip()
    if "acre" in unit_lower:
        ha_area = area * 0.404686
    elif "bigha" in unit_lower:
        ha_area = area * 0.16187 # Standard ~2.5 Bigha per Acre
    else: # Hectare
        ha_area = area
        
    n_rec, p_rec, k_rec = match_crop["npk"]
    
    # Total nutrients needed for total area
    total_n = n_rec * ha_area
    total_p = p_rec * ha_area
    total_k = k_rec * ha_area
    
    # DAP contains 18% N and 46% P2O5
    # DAP kg = total_p / 0.46
    dap_kg = total_p / 0.46
    n_from_dap = dap_kg * 0.18
    
    # Remaining N to be supplied by Urea (46% N)
    remaining_n = max(0.0, total_n - n_from_dap)
    urea_kg = remaining_n / 0.46
    
    # MOP (Muriate of Potash) contains 60% K2O
    mop_kg = total_k / 0.60
    
    # FYM compost in Metric Tons
    fym_tons = match_crop["fym_ton"] * ha_area
    zinc_kg = match_crop["zinc_kg"] * ha_area
    
    # Bags (standard 45 kg bag for Urea, 50 kg for DAP & MOP in India)
    urea_bags = urea_kg / 45.0
    dap_bags = dap_kg / 50.0
    mop_bags = mop_kg / 50.0
    
    return {
        "crop_name": match_crop["name"],
        "area_requested": f"{area} {unit}",
        "hectare_equivalent": round(ha_area, 2),
        "urea": {
            "kg": round(urea_kg, 1),
            "bags_45kg": round(urea_bags, 1),
            "nutrient_supplied": f"{round(total_n, 1)} kg Total N"
        },
        "dap": {
            "kg": round(dap_kg, 1),
            "bags_50kg": round(dap_bags, 1),
            "nutrient_supplied": f"{round(total_p, 1)} kg P₂O₅"
        },
        "mop": {
            "kg": round(mop_kg, 1),
            "bags_50kg": round(mop_bags, 1),
            "nutrient_supplied": f"{round(total_k, 1)} kg K₂O"
        },
        "micronutrients": {
            "zinc_sulphate_kg": round(zinc_kg, 1),
            "organic_compost_tons": round(fym_tons, 1)
        },
        "application_stages": match_crop["stages"]
    }


# 2. MANDI COMMODITY MARKET RATES
MANDI_PRICES = [
    {
        "crop": "Wheat (Gehu)",
        "variety": "Sharbati / Lokwan",
        "market": "Azadpur Mandi, Delhi",
        "price_qtl": 2480,
        "min_price": 2350,
        "max_price": 2620,
        "change_24h": "+1.8%",
        "trend": "bullish",
        "advisory": "Firm demand from flour mills. Good time to release stored stock."
    },
    {
        "crop": "Paddy / Rice (Basmati)",
        "variety": "1121 Pusa Basmati",
        "market": "Karnal Mandi, Haryana",
        "price_qtl": 3890,
        "min_price": 3650,
        "max_price": 4150,
        "change_24h": "+2.4%",
        "trend": "bullish",
        "advisory": "Export shipments active. Prices favorable for selling."
    },
    {
        "crop": "Tomato (Tamatar)",
        "variety": "Hybrid Desi / Shivam",
        "market": "Kolar Mandi, Karnataka",
        "price_qtl": 1640,
        "min_price": 1400,
        "max_price": 1900,
        "change_24h": "-3.1%",
        "trend": "bearish",
        "advisory": "Fresh arrivals increasing. Sell mature harvest without delay."
    },
    {
        "crop": "Potato (Aalu)",
        "variety": "Kufri Jyoti / Pukhraj",
        "market": "Agra Mandi, Uttar Pradesh",
        "price_qtl": 1450,
        "min_price": 1320,
        "max_price": 1600,
        "change_24h": "+0.7%",
        "trend": "stable",
        "advisory": "Cold storage releases steady. Price expected to remain rangebound."
    },
    {
        "crop": "Onion (Pyaz)",
        "variety": "Nasik Red",
        "market": "Lasalgaon Mandi, Maharashtra",
        "price_qtl": 2350,
        "min_price": 2100,
        "max_price": 2680,
        "change_24h": "+3.2%",
        "trend": "bullish",
        "advisory": "Supply tightening in southern markets. Price trend positive."
    },
    {
        "crop": "Mustard (Sarson)",
        "variety": "Pusa Bold (Oil 42%)",
        "market": "Kota Mandi, Rajasthan",
        "price_qtl": 5720,
        "min_price": 5450,
        "max_price": 5950,
        "change_24h": "+1.1%",
        "trend": "bullish",
        "advisory": "Crushing demand strong above MSP. Stagger your sales."
    },
    {
        "crop": "Soybean",
        "variety": "JS 335 / Yellow",
        "market": "Indore Mandi, Madhya Pradesh",
        "price_qtl": 4860,
        "min_price": 4650,
        "max_price": 5100,
        "change_24h": "-0.4%",
        "trend": "stable",
        "advisory": "Steady trade. Hold if expecting festive international oil uptick."
    },
    {
        "crop": "Cotton (Kapas)",
        "variety": "Bt Long Staple (29mm)",
        "market": "Rajkot Mandi, Gujarat",
        "price_qtl": 7320,
        "min_price": 7000,
        "max_price": 7650,
        "change_24h": "+1.6%",
        "trend": "bullish",
        "advisory": "Textile mill inquiries buoyant. Higher grades commanding premium."
    },
    {
        "crop": "Maize (Makka)",
        "variety": "Feed Grade Yellow",
        "market": "Davanagere Mandi, Karnataka",
        "price_qtl": 2180,
        "min_price": 2050,
        "max_price": 2300,
        "change_24h": "+0.5%",
        "trend": "stable",
        "advisory": "Poultry and starch demand consistent. Stable trend."
    },
    {
        "crop": "Garlic (Lahsun)",
        "variety": "G-282 Ooty Bold",
        "market": "Neemuch Mandi, Madhya Pradesh",
        "price_qtl": 13400,
        "min_price": 11500,
        "max_price": 15800,
        "change_24h": "+4.5%",
        "trend": "bullish",
        "advisory": "High seasonal demand. Grade well before bringing to auction."
    },
    {
        "crop": "Chili (Lal Mirch)",
        "variety": "Teja / Guntur Sannam",
        "market": "Guntur Mandi, Andhra Pradesh",
        "price_qtl": 18500,
        "min_price": 16000,
        "max_price": 21000,
        "change_24h": "+1.2%",
        "trend": "bullish",
        "advisory": "Export trade to Southeast Asia active. Keep dry moisture <10%."
    },
    {
        "crop": "Gram / Chickpea (Chana)",
        "variety": "Desi Chana",
        "market": "Bikaner Mandi, Rajasthan",
        "price_qtl": 5980,
        "min_price": 5750,
        "max_price": 6200,
        "change_24h": "+0.9%",
        "trend": "stable",
        "advisory": "Traded above government MSP. Good return on pulses."
    }
]


# 3. PEST & WEED DIRECTORY
PEST_DIRECTORY = [
    {
        "id": "aphids",
        "name": "Aphids (Mahu / Chepa)",
        "scientific": "Aphis gossypii / Brevicoryne brassicae",
        "target_crops": "Mustard, Tomato, Cotton, Vegetables, Pulses",
        "damage": "Colonies cluster on tender shoots and leaf undersides, sucking sap. Excrete sticky honeydew attracting black sooty mold and curling leaves.",
        "chemical_medicine": "Imidacloprid 17.8% SL (Confidor) @ 0.5 ml/L or Thiamethoxam 25% WG @ 0.5 g/L",
        "organic_remedy": "Cold-pressed Neem Oil 10,000 PPM @ 5 ml/L + soap spray, or 10% Sour Buttermilk spray.",
        "threshold": "5-10 aphids per terminal shoot"
    },
    {
        "id": "whitefly",
        "name": "Whitefly (Safed Makhi)",
        "scientific": "Bemisia tabaci",
        "target_crops": "Tomato, Cotton, Chili, Soybean, Cucurbits",
        "damage": "Tiny moth-like white insects suck phloem sap and transmit devastating viral diseases including TYLCV and Cotton Leaf Curl Virus.",
        "chemical_medicine": "Diafenthiuron 50% WP (Pegasus) @ 1.2 g/L or Spiromesifen 22.9% SC @ 1.0 ml/L",
        "organic_remedy": "Yellow Sticky Traps (25 traps/acre) + Agniastra spray (30 ml/L)",
        "threshold": "4-6 adults per leaf"
    },
    {
        "id": "fall_armyworm",
        "name": "Fall Armyworm (FAW)",
        "scientific": "Spodoptera frugiperda",
        "target_crops": "Maize/Corn, Sorghum, Millets, Sugarcane",
        "damage": "Aggressive nocturnal caterpillars devour leaf whorls, creating windowpane feeding holes and sawdust-like frass inside the central leaf funnel.",
        "chemical_medicine": "Chlorantraniliprole 18.5% SC (Coragen) @ 0.4 ml/L or Emamectin Benzoate 5% SG (Proclaim) @ 0.5 g/L",
        "organic_remedy": "Bacillus thuringiensis (Bt kurstaki) @ 2 g/L or Neem cake extract placed in central whorl.",
        "threshold": "5% infested whorls at seedling stage"
    },
    {
        "id": "spider_mites",
        "name": "Two-Spotted Spider Mite",
        "scientific": "Tetranychus urticae",
        "target_crops": "Tomato, Chili, Eggplant, Apple, Polyhouse crops",
        "damage": "Pierces leaf cells under hot dry conditions (>32°C). Causes dusty bronze speckled stippling and dense webs across terminal crowns.",
        "chemical_medicine": "Spiromesifen 22.9% SC (Oberon) @ 1.0 ml/L or Fenazaquin 10% EC @ 1.5 ml/L",
        "organic_remedy": "Pressurized cold water spray on leaf undersides + Wettable Sulfur 80% @ 2.5 g/L",
        "threshold": "2-3 mites per leaf square inch"
    },
    {
        "id": "fruit_borer",
        "name": "Tomato Fruit Borer / Bollworm",
        "scientific": "Helicoverpa armigera",
        "target_crops": "Tomato, Gram/Chana, Cotton, Pigeonpea",
        "damage": "Caterpillars bore circular holes into developing tomato fruits and cotton bolls, feeding with their body half inside and rotting fruit.",
        "chemical_medicine": "Flubendiamide 39.35% SC (Fame) @ 0.3 ml/L or Spinosad 45% SC @ 0.3 ml/L",
        "organic_remedy": "Helicoverpa NPV (HaNPV) viral culture @ 1.5 ml/L + Pheromone traps (5/acre)",
        "threshold": "1 borer larva per plant or 1 damaged fruit per meter row"
    },
    {
        "id": "parthenium_weed",
        "name": "Parthenium / Carrot Grass (Gajar Ghas)",
        "scientific": "Parthenium hysterophorus (Noxious Weed)",
        "target_crops": "All Field Crops, Orchards, Non-cropped borders",
        "damage": "Aggressive allelopathic weed that suppresses crop germination, triggers human dermatitis and respiratory allergies, and harbors disease vectors.",
        "chemical_medicine": "Glyphosate 41% SL @ 10 ml/L (non-crop directed spray) or Metribuzin 70% WP @ 1.5 g/L",
        "organic_remedy": "Bio-agent Zygogramma bicolorata (Mexican beetle) release or spray of 20% Common Salt (NaCl) brine solution.",
        "threshold": "Zero tolerance; eradicate before flowering"
    },
    {
        "id": "cyperus_weed",
        "name": "Purple Nutsedge (Motha Ghas)",
        "scientific": "Cyperus rotundus (Perennial Sedge)",
        "target_crops": "Rice, Wheat, Sugarcane, Vegetables",
        "damage": "Extremely persistent weed with underground tubers/nuts that rob crops of up to 40% applied nitrogen and moisture.",
        "chemical_medicine": "Halosulfuron-methyl 75% WG (Sempra) @ 36 g/acre in 150L water",
        "organic_remedy": "Deep summer plowing (solarization) to desiccate underground tubers, followed by dense green-manuring cover crops.",
        "threshold": "Eradicate at 3-4 leaf stage before new tuber formation"
    }
]


# 4. ORGANIC BIO-LAB RECIPES (DESI KHETI)
ORGANIC_RECIPES = [
    {
        "title": "Jeevamrut (Microbial Soil Life Booster)",
        "category": "Soil Fertility & Immunity",
        "shelf_life": "7-10 Days",
        "application": "200 Liters per Acre via drip, flood irrigation, or 10% foliar spray.",
        "ingredients": [
            "Fresh Desi Cow Dung: 10 kg",
            "Desi Cow Urine (Gomutra): 5 to 10 Liters",
            "Organic Jaggery (Gur): 1 to 2 kg",
            "Pulse Flour (Besan): 1 to 2 kg",
            "Fertile Forest / Field Border Soil: 1 handful (100g)",
            "Clean Water: 200 Liters in a drum"
        ],
        "steps": [
            "Fill a 200L plastic drum with 190 Liters of water in a shaded place.",
            "Mix 10 kg cow dung and 10L cow urine in a bucket and pour into the drum.",
            "Dissolve 2 kg jaggery and 2 kg besan in water and stir thoroughly into the drum.",
            "Add a handful of virgin forest/fencerow soil (acts as microbial mother inoculum).",
            "Stir the mixture with a wooden stick clockwise for 5 minutes twice daily (morning & evening).",
            "Cover with a porous jute bag. Jeevamrut is ready in 48-72 hours when pleasant fermentation smell arises."
        ],
        "benefits": "One gram of Jeevamrut contains billions of beneficial bacteria (Azotobacter, Rhizobium, PSB, Actinomycetes) that mobilize locked-up soil phosphorus and micronutrients."
    },
    {
        "title": "Neemastra (Natural Sucking Pest Repellent)",
        "category": "Organic Insecticide",
        "shelf_life": "6 Months",
        "application": "Direct foliar spray without dilution on crops affected by aphids, whiteflies, or small caterpillars.",
        "ingredients": [
            "Fresh Neem Leaves (crushed): 5 kg",
            "Desi Cow Dung: 1 kg",
            "Desi Cow Urine: 5 Liters",
            "Clean Water: 100 Liters"
        ],
        "steps": [
            "Pound or crush 5 kg of fresh neem leaves into a coarse paste.",
            "In a 100L drum, mix water, cow dung, cow urine, and the crushed neem leaf pulp.",
            "Stir clockwise with a wooden stick for 5 minutes.",
            "Cover with a cloth and let it ferment in the shade for 48 hours, stirring twice daily.",
            "Filter the solution through a fine muslin cloth. Spray directly onto infested crops."
        ],
        "benefits": "Azadirachtin acts as an antifeedant, insect growth regulator (IGR), and reproductive deterrent without harming honeybees or earthworms."
    },
    {
        "title": "Agniastra (Potent Botanical Bio-Insecticide)",
        "category": "Broad-Spectrum Pest Control",
        "shelf_life": "3 Months",
        "application": "Dilute 2 to 3 Liters of Agniastra in 100 Liters of water for 1 Acre foliar spray.",
        "ingredients": [
            "Desi Cow Urine: 10 Liters",
            "Crushed Neem Leaves: 2 kg",
            "Hot Green Chili Paste: 500 grams",
            "Crushed Raw Garlic Paste: 250 grams",
            "Crushed Tobacco Leaves (optional): 250 grams"
        ],
        "steps": [
            "In an earthen or stainless steel pot, combine 10 Liters cow urine with neem, chili, garlic, and tobacco.",
            "Boil the mixture gently on a slow flame until it reduces by about 20% (approx. 20-25 minutes).",
            "Allow the decoction to cool in the shade for 48 hours, stirring once daily.",
            "Filter through a double-layered cloth and store in an airtight glass or plastic container."
        ],
        "benefits": "Combines capsaicin, allicin, and azadirachtin to penetrate the thick cuticles of stem borers, pod borers, armyworms, and leaf rollers."
    },
    {
        "title": "Fermented Sour Buttermilk (Khatti Chhachh)",
        "category": "Natural Bio-Fungicide",
        "shelf_life": "Use within 2-3 days of fermentation",
        "application": "Dilute 1 Liter sour buttermilk with 10 Liters water for foliar spray.",
        "ingredients": [
            "Fresh Sour Cow Buttermilk / Whey: 5 Liters",
            "Clean Copper Coin / Wire Piece: 1 clean piece (acts as copper ion catalyst)",
            "Clean Water: 50 Liters for final dilution"
        ],
        "steps": [
            "Take 5 Liters of fresh buttermilk in an earthen pitcher or plastic container.",
            "Drop a scrubbed, clean copper coin or copper wire coil into the buttermilk.",
            "Cover loosely and store in a dark, warm place for 6 to 8 days until a greenish-blue hue develops.",
            "Remove the copper piece and strain the buttermilk through a fine sieve.",
            "Dilute 1:10 with water and spray on crops during early morning."
        ],
        "benefits": "Natural lactic acid and ionized copper act as an organic shield against powdery mildew, early blight, rust, and damping-off."
    }
]


# 5. SOIL HEALTH ADVISOR ENGINE
def evaluate_soil_health(ph_val, texture="Loamy"):
    """
    Evaluates soil pH and texture to prescribe corrective agricultural amendments.
    """
    ph = float(ph_val)
    texture = texture.capitalize()
    
    if ph < 5.5:
        category = "Strongly Acidic"
        badge = "critical"
        diagnosis = "Excessive soil acidity locks up phosphorus, calcium, magnesium, and molybdenum while risking toxic aluminum/manganese uptake."
        amendment = "Agricultural Limestone (CaCO₃) @ 1.5 - 2.5 Tons per Acre or Dolomite Lime to supply magnesium. Apply 4 weeks prior to planting and incorporate into top 15 cm soil."
    elif ph < 6.5:
        category = "Moderately Acidic"
        badge = "moderate"
        diagnosis = "Slightly below optimum for most crops. Phosphorus availability may be sluggish in cool soils."
        amendment = "Apply Well-rotted Farmyard Manure (5 Tons/Acre) + 500 kg/Acre Agricultural Lime or Wood Ash (rich in potassium and calcium carbonate)."
    elif ph <= 7.5:
        category = "Optimal Neutral"
        badge = "safe"
        diagnosis = "Ideal root zone pH! Maximum availability of all primary (N, P, K), secondary (Ca, Mg, S), and micronutrients (Zn, Fe, Mn, B, Cu)."
        amendment = "No chemical amendments required! Maintain soil organic carbon by applying 2-3 tons of vermicompost and practice cover cropping."
    elif ph <= 8.5:
        category = "Moderately Alkaline / Calcareous"
        badge = "moderate"
        diagnosis = "Free calcium carbonate binds soluble phosphorus into insoluble tricalcium phosphate; iron and zinc chlorosis frequently occurs."
        amendment = "Apply Agricultural Gypsum (Calcium Sulfate) @ 1.0 - 1.5 Tons per Acre + Elemental Sulfur @ 100 kg/Acre. Use Ammonium Sulfate and SSP fertilizers which exert acidifying effects."
    else:
        category = "Strongly Alkaline / Sodic (Kallar)"
        badge = "critical"
        diagnosis = "High exchangeable sodium percentage (ESP > 15%). Poor soil aeration, water logging, sodium crusting, and severe micronutrient starvation."
        amendment = "Apply Phosphogypsum @ 2.5 - 4 Tons per Acre based on Gypsum Requirement test, followed by heavy fresh water leaching. Incorporate green manure (Dhaincha / Sesbania aculeata) at 45 days."

    # Texture guidance
    texture_notes = {
        "Sandy": "High drainage, low cation exchange capacity (CEC). Apply fertilizers in small frequent splits (fertigation) and incorporate biochar or compost to retain moisture.",
        "Loamy": "Perfect balance of sand, silt, and clay! High organic matter retention and excellent capillary moisture holding.",
        "Clayey": "High nutrient retention but prone to compaction and waterlogging. Avoid tilling when wet; incorporate coarse organic manure and gypsum to improve aggregate porosity."
    }.get(texture, "Balanced texture profile.")

    return {
        "ph": ph,
        "texture": texture,
        "category": category,
        "badge": badge,
        "diagnosis": diagnosis,
        "recommended_amendment": amendment,
        "texture_guidance": texture_notes
    }


# 6. BUILT-IN INTELLIGENT AGRONOMY ASSISTANT (CONVERSATIONAL BRAIN)
def smart_agri_assistant(query):
    """
    Intelligent agronomy chatbot engine that handles greetings, explains site features,
    answers crop/disease/medicine questions, and outputs UI action commands.
    Ensures AgriNet AI ALWAYS provides a warm, smart, and useful response
    without requiring external API availability.
    """
    q = query.strip().lower()
    
    # Check for direct UI Action Commands first
    if any(k in q for k in ["open camera", "turn on camera", "camera chalu", "camera on", "start camera", "video"]):
        return {
            "reply": "Opening your device camera now. Position the leaf inside the frame and click 'Capture'.",
            "action": "CAMERA"
        }
    if any(k in q for k in ["upload", "browse", "select image", "choose file", "photo upload", "file chuno"]):
        return {
            "reply": "Opening file browser. Choose a clear close-up image of the leaf specimen.",
            "action": "BROWSE"
        }
    if any(k in q for k in ["analyze", "detect", "check disease", "scan leaf", "jaanch", "shuru karo", "init inference"]):
        return {
            "reply": "Running AI inference on the leaf specimen with multimodal environmental context...",
            "action": "ANALYZE"
        }
    if any(k in q for k in ["reset", "clear", "hatao", "saaf", "fresh start"]):
        return {
            "reply": "Resetting the workspace for a new diagnostic specimen.",
            "action": "RESET"
        }
    if any(k in q for k in ["fertilizer calc", "open fertilizer", "khad calculator", "npk calc"]):
        return {
            "reply": "Opening the Smart Fertilizer & NPK Calculator for you.",
            "action": "TAB_FERTILIZER"
        }
    if any(k in q for k in ["open mandi", "mandi bhav", "mandi rate", "market price", "gehu ka bhav"]):
        return {
            "reply": "Opening Mandi Bhav & Market Price tracker for major agricultural commodities.",
            "action": "TAB_MANDI"
        }
    if any(k in q for k in ["open pests", "pest guide", "keede", "weeds", "weed guide", "kharpatwar"]):
        return {
            "reply": "Switching to Crop Pest & Weed Directory with approved insecticides and dosages.",
            "action": "TAB_PESTS"
        }
    if any(k in q for k in ["open organic", "organic lab", "jaivik kheti", "jeevamrut recipe", "neemastra"]):
        return {
            "reply": "Opening Organic Bio-Lab with step-by-step DIY formulations like Jeevamrut and Neemastra.",
            "action": "TAB_ORGANIC"
        }
    if any(k in q for k in ["crop calendar", "open calendar", "fasal calendar", "mausam"]):
        return {
            "reply": "Opening Seasonal Crop Calendar and sowing schedule.",
            "action": "TAB_CALENDAR"
        }
    if any(k in q for k in ["open soil", "soil health", "ph advisor", "mitti"]):
        return {
            "reply": "Opening Soil Health & pH Advisor tool.",
            "action": "TAB_SOIL"
        }
    if any(k in q for k in ["close", "exit", "band karo", "shut down", "bye", "alvida"]):
        return {
            "reply": "Goodbye! Closing AgriNet Assistant. Have a bountiful and healthy harvest!",
            "action": "CLOSE"
        }

    # Greetings in English & Hindi/Hinglish
    greetings = ["hi", "hii", "hiii", "hello", "hoi", "hey", "heya", "namaste", "namaskar", "pranam", "ram ram", "kya haal", "kaise ho", "how are you"]
    if any(re.search(rf"\b{re.escape(g)}\b", q) for g in greetings):
        return {
            "reply": "Hello! 🌾 I am AgriNet AI, your smart agricultural assistant. I'm here to help you diagnose plant diseases, calculate fertilizer requirements, check mandi market rates, identify crop pests, and guide you through organic remedies! How can I help your farm or garden today?",
            "action": None
        }

    # Questions asking about site features or what the agent can do
    feature_triggers = ["feature", "features", "kya kar sakte", "kya feature", "site me kya", "about site", "what can you do", "help", "guide", "how to use", "kaise use kare"]
    if any(k in q for k in feature_triggers):
        return {
            "reply": (
                "AgriNet brings together 8 powerful smart agriculture tools:\n"
                "🌿 1. AI Leaf Doctor: Instant scan of 38 plant diseases with exact chemical medicines, dosages, and organic remedies.\n"
                "🧪 2. Fertilizer & NPK Calculator: Calculates exact Urea, DAP, and MOP required for your crop and land acreage.\n"
                "🌾 3. Mandi Market Bhav: Live market price trends and selling advice across agricultural mandis.\n"
                "🐛 4. Pest & Weed Guide: Identification, damage marks, and approved treatments for common pests.\n"
                "🌱 5. Organic Bio-Lab: Step-by-step DIY recipes for Jeevamrut, Neemastra, and Agniastra.\n"
                "🌦️ 6. Crop Calendar: Seasonal sowing windows, water needs, and climate guidance.\n"
                "🩺 7. Soil Health & pH Advisor: Soil acidity/alkalinity assessment and corrective gypsum/lime recommendations.\n"
                "Click any feature tab at the top or say commands like 'open camera' or 'check fertilizer'!"
            ),
            "action": None
        }

    # Specific disease queries
    if "early blight" in q:
        return {
            "reply": "For Early Blight (Alternaria solani): Spray Mancozeb 75% WP (Dithane M-45) @ 2.5 g/L or systemic Difenoconazole 25% EC (Score) @ 1 ml/L. Organically, spray 10,000 PPM Neem Oil @ 5 ml/L or 10% sour buttermilk. Prune lower infected leaves and avoid overhead sprinkler watering.",
            "action": None
        }
    if "late blight" in q:
        return {
            "reply": "Late Blight (Phytophthora infestans) is an emergency! Spray Metalaxyl-M 4% + Mancozeb 64% WP (Ridomil Gold) @ 2.5 g/L or Dimethomorph 50% WP (Acrobat) @ 1 g/L immediately. For organic care, apply 1% Bordeaux Mixture and hill soil high around potato tubers.",
            "action": None
        }
    if "powdery mildew" in q or "mildew" in q:
        return {
            "reply": "For Powdery Mildew: Spray Propiconazole 25% EC (Tilt) @ 1 ml/L or Wettable Sulfur 80% WDG @ 2.5 g/L. Organically, spray 5 g Potassium Bicarbonate or 1:9 diluted cow milk in bright morning sunlight.",
            "action": None
        }
    if "whitefly" in q or "safed makhi" in q:
        return {
            "reply": "For Whiteflies: Spray Diafenthiuron 50% WP (Pegasus) @ 1.2 g/L or Imidacloprid 17.8% SL @ 0.5 ml/L. Install yellow sticky traps (25/acre) and spray Agniastra or Neem oil 10,000 PPM weekly.",
            "action": None
        }
    if "aphid" in q or "mahu" in q or "chepa" in q:
        return {
            "reply": "For Aphids (Mahu): Spray Thiamethoxam 25% WG (Actara) @ 0.5 g/L or Imidacloprid @ 0.5 ml/L. Organically, spray 5 ml/L Neem Oil with mild soap water or fermented sour buttermilk.",
            "action": None
        }
    if "jeevamrut" in q or "jivrit" in q:
        return {
            "reply": "Jeevamrut Recipe: Mix 10 kg cow dung + 10L cow urine + 2 kg jaggery + 2 kg gram flour (besan) + 1 handful fertile soil in 200L water. Stir clockwise for 5 mins twice daily. Ready in 48 hours! Apply 200 Liters per acre to replenish soil microflora.",
            "action": "TAB_ORGANIC"
        }
    if "fertilizer" in q or "khad" in q or "urea" in q or "dap" in q:
        return {
            "reply": "To calculate the exact fertilizer for your farm, open the Fertilizer Calculator tab. You can input your crop (Wheat, Rice, Tomato, Potato, etc.), land size in Acres, and get the exact Urea, DAP, and MOP bags needed!",
            "action": "TAB_FERTILIZER"
        }
    if "mandi" in q or "bhav" in q or "price" in q or "rate" in q:
        return {
            "reply": "Today's Mandi Trends: Wheat is trading strong around ₹2,480/Qtl, Basmati Paddy is around ₹3,890/Qtl, and Mustard is high at ₹5,720/Qtl. Click the 'Mandi Market Bhav' tab to check rates for 12+ crops across major markets!",
            "action": "TAB_MANDI"
        }
    if "soil" in q or "ph" in q or "mitti" in q:
        return {
            "reply": "Ideal soil pH for most vegetables and field crops is 6.5 to 7.5. For acidic soils (pH < 6.0), apply Agricultural Lime or Dolomite. For alkaline soils (pH > 8.0), apply Agricultural Gypsum and green manure. Check the 'Soil Health Advisor' tab to analyze your soil!",
            "action": "TAB_SOIL"
        }

    # Conversational fallback
    return {
        "reply": (
            f"I understand your query regarding '{query}'. AgriNet can help you diagnose leaf diseases, calculate NPK fertilizer doses, view mandi rates, and explore organic recipes. "
            "You can upload or photograph a leaf specimen, or select any feature tab from the top navigation bar!"
        ),
        "action": None
    }
