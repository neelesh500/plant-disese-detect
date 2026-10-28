"""
AgriNet Agronomy & Plant Disease Knowledge Engine
Contains comprehensive pathology, symptom profiles, commercial chemical medicines (brand + dosage),
organic bio-solutions, and cultural prevention protocols for all 38 PlantVillage classes.
"""

DISEASE_DATABASE = {
    # 1. Apple - Apple Scab
    "Apple - Apple Scab": {
        "crop": "Apple (Malus domestica)",
        "pathogen": "Venturia inaequalis (Ascomycete Fungus)",
        "risk_level": "High",
        "recovery_time": "10 - 15 Days",
        "brief": "Apple scab is one of the most serious fungal diseases of apples worldwide. It attacks leaves, blossoms, and fruits, creating velvety olive-green to black scabby lesions. Prolonged leaf wetness (over 6 hours) at 15-24°C heavily accelerates spore discharge and infection cycles, drastically degrading fruit market value.",
        "symptoms": [
            "Olive-green to dull dark brown velvety spots on upper leaf surfaces.",
            "Distorted, curled, and puckered leaves that turn yellow and drop prematurely.",
            "Dark, corky, cracked scabs on fruit skin leading to stunted and deformed fruit development.",
            "Premature defoliation weakening the tree's winter hardiness."
        ],
        "medicines": [
            {
                "brand": "Antracol / Score 250 EC",
                "active": "Propineb 70% WP or Difenoconazole 25% EC",
                "dosage": "2.5 g / Liter (Propineb) or 0.5 ml / Liter (Difenoconazole)",
                "timing": "Apply at green tip and pink bud stage before rain events.",
                "type": "Systemic & Protective Fungicide"
            },
            {
                "brand": "Dithane M-45",
                "active": "Mancozeb 75% WP",
                "dosage": "2.5 g per Liter water",
                "timing": "Protective cover spray during petal fall and fruit development.",
                "type": "Contact Fungicide"
            },
            {
                "brand": "Kocide 3000 / Blue Copper",
                "active": "Copper Hydroxide 53.8% DF",
                "dosage": "2.0 g per Liter water",
                "timing": "Dormant / early spring spray to reduce overwintering inocula.",
                "type": "Copper Fungicide"
            }
        ],
        "organic": [
            {
                "remedy": "Wettable Sulfur Spray",
                "ingredient": "Sulfur 80% WDG",
                "dosage": "3 g per Liter water",
                "instructions": "Apply in cool morning hours; avoid spraying when ambient temperature exceeds 28°C."
            },
            {
                "remedy": "Bio-fungicide Drench",
                "ingredient": "Bacillus subtilis (Serenade) or Trichoderma viride",
                "dosage": "5 ml/g per Liter water",
                "instructions": "Colonizes leaf surfaces and blocks Venturia spore germination organically."
            },
            {
                "remedy": "Potassium Bicarbonate Folio Spray",
                "ingredient": "Food-grade Potassium Bicarbonate + 0.5% Horticultural Oil",
                "dosage": "4 g per Liter water",
                "instructions": "Disrupts fungal cell wall pH and halts mycelial expansion."
            }
        ],
        "prevention": [
            "Shred or remove fallen apple leaves in autumn to eliminate overwintering fungal pseudothecia.",
            "Prune tree canopy annually during dormancy to enhance airflow and speed up leaf drying.",
            "Choose resistant cultivars such as Liberty, Enterprise, Freedom, or Prima where feasible.",
            "Avoid overhead irrigation; use drip lines at the root zone."
        ]
    },

    # 2. Apple - Black Rot
    "Apple - Black Rot": {
        "crop": "Apple (Malus domestica)",
        "pathogen": "Botryosphaeria obtusa (Physalospora obtusa)",
        "risk_level": "High",
        "recovery_time": "14 - 20 Days",
        "brief": "Black rot (also known as frogeye leaf spot) attacks apple leaves, limbs, and fruit. Fruit infections start as a brown rot that turns jet black and mummifies on the branch. Cankers on dead wood serve as the primary source of recurring orchard infections.",
        "symptoms": [
            "Frogeye leaf spots: small purple specks expanding into circular lesions with tan centers and purple margins.",
            "Sepal infection leading to blossom end rot on developing fruit.",
            "Fruit rot forming alternating dark and light concentric bands, eventually shriveling into hard black mummies.",
            "Sunken, reddish-brown bark cankers on branches and scaffold limbs."
        ],
        "medicines": [
            {
                "brand": "Captan 50% WP / Merpan",
                "active": "Captan 50% WP",
                "dosage": "2.5 g per Liter water",
                "timing": "Spray from silver tip through summer cover sprays.",
                "type": "Broad-Spectrum Protectant"
            },
            {
                "brand": "Topsin-M / Thiophanate-Methyl",
                "active": "Thiophanate-Methyl 70% WP",
                "dosage": "1.0 g per Liter water",
                "timing": "Apply at petal fall and post-bloom.",
                "type": "Systemic Fungicide"
            }
        ],
        "organic": [
            {
                "remedy": "Liquid Copper Fungicide",
                "ingredient": "Copper Octanoate (Copper soap)",
                "dosage": "3 ml per Liter water",
                "instructions": "Spray before rain during bud break and bloom."
            },
            {
                "remedy": "Neem Oil 10,000 PPM",
                "ingredient": "Cold-pressed Azadirachtin Neem Oil",
                "dosage": "5 ml per Liter water + mild liquid soap",
                "instructions": "Protective coating on foliage against spore attachment."
            }
        ],
        "prevention": [
            "Prune out all dead wood, fire-blight strikes, and cankered branches 15 cm below visible lesions.",
            "Collect and burn all mummified fruit hanging on trees or lying on orchard soil.",
            "Paint tree trunks with white latex paint to avoid winter sunscald wounds that invite cankers."
        ]
    },

    # 3. Apple - Cedar Apple Rust
    "Apple - Cedar Apple Rust": {
        "crop": "Apple (Malus domestica)",
        "pathogen": "Gymnosporangium juniperi-virginianae (Heteroecious Rust Fungus)",
        "risk_level": "Moderate",
        "recovery_time": "12 - 18 Days",
        "brief": "Cedar apple rust is a two-host fungal disease requiring both Eastern red cedar/juniper and apple trees to complete its life cycle. It creates brilliant yellow-orange spots on apple leaves and can defoliate susceptible apple varieties in damp spring conditions.",
        "symptoms": [
            "Bright yellow-orange or reddish circular spots on upper leaf surfaces.",
            "Small black fruiting bodies (pycnia) appearing in the center of the orange spots.",
            "Raised tube-like fungal projections (aecia) on the underside of leaves and fruit.",
            "Premature yellowing and dropping of infected leaves."
        ],
        "medicines": [
            {
                "brand": "Rally 40WSP / Systhane",
                "active": "Myclobutanil 40% WP or 10% WP",
                "dosage": "0.5 g per Liter water",
                "timing": "Apply from tight cluster through bloom and early cover.",
                "type": "Systemic Sterol Inhibitor"
            },
            {
                "brand": "Indofil M-45",
                "active": "Mancozeb 75% WP",
                "dosage": "2.5 g per Liter water",
                "timing": "Protective spray when orange gelatinous galls appear on nearby cedars.",
                "type": "Contact Protectant"
            }
        ],
        "organic": [
            {
                "remedy": "Wettable Micronized Sulfur",
                "ingredient": "Sulfur 80% WDG",
                "dosage": "3 g per Liter water",
                "instructions": "Apply at 7-day intervals during wet spring periods."
            },
            {
                "remedy": "Bio-inoculant Bacillus amyloliquefaciens",
                "ingredient": "Beneficial microbial antagonist",
                "dosage": "4 ml per Liter water",
                "instructions": "Spray on foliage to competitively inhibit rust spore germination."
            }
        ],
        "prevention": [
            "Remove all Eastern red cedar (Juniperus virginiana) trees within a 1-2 km radius if feasible.",
            "Cut off gelatinous brown galls from nearby juniper bushes before spring rains.",
            "Plant rust-immune varieties like Freedom, Liberty, Redfree, or William's Pride."
        ]
    },

    # 4. Apple - Healthy
    "Apple - Healthy": {
        "crop": "Apple (Malus domestica)",
        "pathogen": "None (Plant is Healthy)",
        "risk_level": "Safe",
        "recovery_time": "Optimal Growth",
        "brief": "The apple foliage displays excellent photosynthetic vitality, crisp cellular integrity, and no signs of foliar pathogens or nutrient deficiencies. Maintain routine orchard hygiene and balanced fertilization.",
        "symptoms": [
            "Uniform emerald green coloration across leaf lamina.",
            "Smooth leaf margins with no chlorosis, necrotic spotting, or curling.",
            "Robust shoot growth and healthy cuticle wax layer."
        ],
        "medicines": [
            {
                "brand": "No Chemical Intervention Required",
                "active": "None",
                "dosage": "0 g / L (Save chemical input cost)",
                "timing": "N/A",
                "type": "Preventive Maintenance"
            }
        ],
        "organic": [
            {
                "remedy": "Liquid Seaweed Extract Foliar Spray",
                "ingredient": "Ascophyllum nodosum Seaweed Concentrate",
                "dosage": "2 ml per Liter water",
                "instructions": "Spray every 20-30 days to enhance chlorophyll synthesis and stress tolerance."
            },
            {
                "remedy": "Jeevamrut / Cow Dung Microbial Elixir",
                "ingredient": "Fermented organic microbial culture",
                "dosage": "200 Liters per Acre via drip or soil drench",
                "instructions": "Boosts soil rhizosphere microflora and nutrient absorption."
            }
        ],
        "prevention": [
            "Continue regular monitoring for codling moth, aphids, and early fungal signs.",
            "Ensure balanced N-P-K fertilization according to tree age and soil test reports."
        ]
    },

    # 5. Blueberry - Healthy
    "Blueberry - Healthy": {
        "crop": "Blueberry (Vaccinium corymbosum)",
        "pathogen": "None (Plant is Healthy)",
        "risk_level": "Safe",
        "recovery_time": "Optimal Growth",
        "brief": "Blueberry leaves show optimal vigor, healthy acidic soil response, and absence of Mummy Berry, Anthracnose, or Phomopsis canker.",
        "symptoms": ["Lush, firm, glossy green foliage without reddish blotches or leaf spots."],
        "medicines": [{"brand": "None needed", "active": "None", "dosage": "None", "timing": "N/A", "type": "Maintenance"}],
        "organic": [{"remedy": "Pine Needle / Pine Bark Acid Mulching", "ingredient": "Organic acidic mulch", "dosage": "3-4 inch layer", "instructions": "Maintains acidic soil pH (4.5 - 5.2) and retains root moisture."}],
        "prevention": ["Maintain drip irrigation with rainwater or acidified water to preserve low soil pH."]
    },

    # 6. Cherry - Powdery Mildew
    "Cherry - Powdery Mildew": {
        "crop": "Cherry (Prunus avium)",
        "pathogen": "Podosphaera clandestina (Fungal Pathogen)",
        "risk_level": "Moderate to High",
        "recovery_time": "8 - 14 Days",
        "brief": "Cherry powdery mildew creates white, talcum-like powdery patches on leaves and developing fruit. It causes leaf puckering, upward curling, and unsightly webbing on cherry skin, making fruit unmarketable.",
        "symptoms": [
            "White powdery fungal patches on undersides of young leaves.",
            "Upward curling, twisting, and blistering of expanding leaves.",
            "White fungal web and russeting on green cherry fruits.",
            "Stunted terminal twig growth."
        ],
        "medicines": [
            {
                "brand": "Tilt 250 EC / Bayleton",
                "active": "Propiconazole 25% EC or Triadimefon",
                "dosage": "1.0 ml per Liter water",
                "timing": "Apply at shuck fall and repeat 14 days later.",
                "type": "Systemic Triazole"
            },
            {
                "brand": "Flint 50 WG / Quadris",
                "active": "Trifloxystrobin 50% WG",
                "dosage": "0.5 g per Liter water",
                "timing": "Spray alternately to prevent chemical resistance.",
                "type": "Strobilurin Fungicide"
            }
        ],
        "organic": [
            {
                "remedy": "Potassium Bicarbonate / Baking Soda Solution",
                "ingredient": "Potassium Bicarbonate 5g + 2ml Horticultural Oil",
                "dosage": "5 g per Liter water",
                "instructions": "Spray on both leaf sides; eradicates mycelium by altering surface pH."
            },
            {
                "remedy": "Diluted Sour Milk / Buttermilk Spray",
                "ingredient": "Fresh sour whey / buttermilk diluted 1:9 in water",
                "dosage": "Foliar spray under bright sunlight",
                "instructions": "Produces free radicals under UV light that destroy fungal hyphae naturally."
            }
        ],
        "prevention": [
            "Prune inner canopy to maximize sunlight penetration and airflow.",
            "Avoid excessive nitrogen fertilizer which causes succulent, highly susceptible shoots."
        ]
    },

    # 7. Cherry - Healthy
    "Cherry - Healthy": {
        "crop": "Cherry (Prunus avium)",
        "pathogen": "None (Healthy)",
        "risk_level": "Safe",
        "recovery_time": "Optimal Growth",
        "brief": "Cherry foliage is vigorous, shiny, and fully functional with no fungal lesions or shot-hole disease.",
        "symptoms": ["Smooth dark green leaves with uniform venation and healthy buds."],
        "medicines": [{"brand": "None needed", "active": "None", "dosage": "None", "timing": "N/A", "type": "Maintenance"}],
        "organic": [{"remedy": "Vermicompost Soil Top-Dress", "ingredient": "Earthworm castings", "dosage": "2 kg per tree", "instructions": "Provides slow-release micronutrients."}],
        "prevention": ["Prune annually during dry weather to prevent silver leaf disease."]
    },

    # 8. Corn - Gray Leaf Spot
    "Corn - Gray leaf spot": {
        "crop": "Corn / Maize (Zea mays)",
        "pathogen": "Cercospora zeae-maydis (Fungus)",
        "risk_level": "High",
        "recovery_time": "10 - 15 Days",
        "brief": "Gray leaf spot is one of the most yield-limiting diseases of maize in humid regions. It produces rectangular necrotic lesions restricted by leaf veins. Under warm (25-30°C) and cloudy, damp conditions, it can destroy the entire upper canopy during grain fill.",
        "symptoms": [
            "Distinct rectangular, tan-to-gray lesions running parallel between leaf veins.",
            "Lesions expand to 2-7 cm long, merging to cause extensive blighting.",
            "Premature death of ear leaves leading to poor ear fill and stalk lodging."
        ],
        "medicines": [
            {
                "brand": "Headline AMP / Priaxor",
                "active": "Pyraclostrobin + Fluxapyroxad",
                "dosage": "1.2 ml per Liter water",
                "timing": "Apply at tassel emergence (VT to R1 stage) when disease reaches ear leaf.",
                "type": "Systemic Dual-Action"
            },
            {
                "brand": "Nativo 75 WG",
                "active": "Tebuconazole 50% + Trifloxystrobin 25% WG",
                "dosage": "0.8 g per Liter water",
                "timing": "Spray upon early onset of rectangular lesions on lower canopy.",
                "type": "Systemic Curative & Protective"
            }
        ],
        "organic": [
            {
                "remedy": "Trichoderma harzianum Foliar Treatment",
                "ingredient": "Bio-fungicide spore suspension",
                "dosage": "5 g per Liter water",
                "instructions": "Apply in early morning; outcompetes Cercospora spores on leaf sheath."
            },
            {
                "remedy": "Neem Seed Kernel Extract (NSKE 5%)",
                "ingredient": "Fresh aqueous neem seed extract",
                "dosage": "50 ml per Liter water",
                "instructions": "Natural plant-based fungistatic spray."
            }
        ],
        "prevention": [
            "Plant maize hybrids with high genetic tolerance to Cercospora.",
            "Rotate corn with non-grass crops like soybean, pulses, or mustard.",
            "Till or manage corn crop residue to reduce fungal overwintering survival."
        ]
    },

    # 9. Corn - Common Rust
    "Corn - Common rust": {
        "crop": "Corn / Maize (Zea mays)",
        "pathogen": "Puccinia sorghi (Basidiomycete Fungus)",
        "risk_level": "Moderate",
        "recovery_time": "7 - 12 Days",
        "brief": "Common rust appears as cinnamon-brown, powdery pustules scattered across both leaf surfaces. It flourishes in moderate temperatures (16-24°C) with high relative humidity and dew. Severe infections during early whorl stages cause chlorosis and grain weight reduction.",
        "symptoms": [
            "Oval to elongated golden-brown to cinnamon-colored pustules (uredinia) on upper and lower leaf surfaces.",
            "Powdery rust spores rub off easily onto fingers when touched.",
            "Pustules turn dark brownish-black late in the season as overwintering teliospores develop.",
            "Chlorotic banding and leaf death under heavy infestation."
        ],
        "medicines": [
            {
                "brand": "Tilt 250 EC / Bumper",
                "active": "Propiconazole 25% EC",
                "dosage": "1.0 ml per Liter water",
                "timing": "Spray immediately when pustules appear before blister stage.",
                "type": "Systemic Fungicide"
            },
            {
                "brand": "Amistar Top",
                "active": "Azoxystrobin 18.2% + Difenoconazole 11.4% SC",
                "dosage": "1.0 ml per Liter water",
                "timing": "High-efficiency systemic protection for upper ear leaves.",
                "type": "Broad-Spectrum Systemic"
            }
        ],
        "organic": [
            {
                "remedy": "Micronized Wettable Sulfur 80%",
                "ingredient": "Elemental sulfur",
                "dosage": "3 g per Liter water",
                "instructions": "Inhibits rust spore respiration; spray below 30°C."
            },
            {
                "remedy": "Sour Buttermilk + Asafoetida (Hing) Spray",
                "ingredient": "5-day sour buttermilk (1L) + 2g Hing in 10L water",
                "dosage": "Foliar misting",
                "instructions": "Traditional Indian natural bio-shield against rusts."
            }
        ],
        "prevention": [
            "Select rust-resistant hybrids possessing the Rp1-D gene or general adult plant resistance.",
            "Plant early in the season to complete flowering before airborne spores arrive."
        ]
    },

    # 10. Corn - Northern Leaf Blight
    "Corn - Northern Leaf Blight": {
        "crop": "Corn / Maize (Zea mays)",
        "pathogen": "Exserohilum turcicum (Setosphaeria turcica)",
        "risk_level": "High",
        "recovery_time": "12 - 16 Days",
        "brief": "Northern corn leaf blight produces huge cigar-shaped grayish-green lesions that scorch corn foliage. Under wet, cool weather (18-27°C), it spreads rapidly from bottom leaves upward, causing entire fields to look burned or frozen prematurely.",
        "symptoms": [
            "Large, elongated, elliptical or cigar-shaped grayish-green to tan lesions (2 to 15 cm long).",
            "Dark olive-black fungal sporulation inside the center of older lesions during damp mornings.",
            "Leaves turn dry, brittle, and appear scorched, crippling grain fill."
        ],
        "medicines": [
            {
                "brand": "Opera / Priaxor",
                "active": "Pyraclostrobin + Epoxiconazole or Fluxapyroxad",
                "dosage": "1.0 ml per Liter water",
                "timing": "Spray at first sign on lower leaves before tasseling.",
                "type": "Systemic Protectant"
            },
            {
                "brand": "Dithane M-45 / Saaf",
                "active": "Mancozeb 63% + Carbendazim 12% WP",
                "dosage": "2.0 g per Liter water",
                "timing": "Apply thoroughly covering both sides of maize leaves.",
                "type": "Contact + Systemic Combination"
            }
        ],
        "organic": [
            {
                "remedy": "Trichoderma viride Bio-Shield",
                "ingredient": "Trichoderma formulation",
                "dosage": "5 g per Liter water with 1% jaggery",
                "instructions": "Spray during cloudy conditions to colonize leaf lesions."
            },
            {
                "remedy": "Neemastra Bio-Spray",
                "ingredient": "Fermented neem leaves + cow urine preparation",
                "dosage": "50 ml per Liter water",
                "instructions": "Provides natural botanical protection against fungal mycelia."
            }
        ],
        "prevention": [
            "Plant certified Ht-gene resistant hybrid seeds.",
            "Rotate with legumes or non-host crops for at least 1-2 seasons.",
            "Deep plow infected maize stubble after harvest to bury fungal conidia."
        ]
    },

    # 11. Corn - Healthy
    "Corn - Healthy": {
        "crop": "Corn / Maize (Zea mays)",
        "pathogen": "None (Healthy)",
        "risk_level": "Safe",
        "recovery_time": "Optimal Growth",
        "brief": "Corn plants exhibit vigorous erect green foliage, thick sturdy stalks, and complete absence of foliar blights or leaf spots.",
        "symptoms": ["Broad, deep green leaves with strong central midrib and no discoloration."],
        "medicines": [{"brand": "None needed", "active": "None", "dosage": "None", "timing": "N/A", "type": "Maintenance"}],
        "organic": [{"remedy": "Azotobacter & PSB Soil Treatment", "ingredient": "Bio-fertilizer culture", "dosage": "2 kg per Acre in compost", "instructions": "Fixes atmospheric nitrogen and mobilizes soil phosphorus."}],
        "prevention": ["Maintain weed-free perimeter and monitor for fall armyworm."]
    },

    # 12. Grape - Black Rot
    "Grape - Black Rot": {
        "crop": "Grape (Vitis vinifera)",
        "pathogen": "Guignardia bidwellii (Fungus)",
        "risk_level": "Critical",
        "recovery_time": "12 - 18 Days",
        "brief": "Grape black rot attacks all green parts of the vine, but fruit loss can approach 100% if unmanaged. Infected berries rapidly soften, turn brown, shrink, shrivel, and transform into hard, wrinkly black mummies that remain attached to the cluster.",
        "symptoms": [
            "Small circular reddish-brown leaf spots with black border and pinpoint black pycnidia dots inside.",
            "Elongated, sunken black cankers on young canes, tendrils, and petioles.",
            "Berries turn light brown, rot completely within 48 hours, and dry into hard black mummies."
        ],
        "medicines": [
            {
                "brand": "Abound / Quadris",
                "active": "Azoxystrobin 23% SC",
                "dosage": "1.0 ml per Liter water",
                "timing": "Apply from pre-bloom through 4-weeks post-bloom.",
                "type": "Systemic Strobilurin"
            },
            {
                "brand": "Dithane M-45 / Indofil M-45",
                "active": "Mancozeb 75% WP",
                "dosage": "2.5 g per Liter water",
                "timing": "Crucial protective spray at 1-3 inch shoot growth.",
                "type": "Protective Contact Fungicide"
            },
            {
                "brand": "Rally 40 WSP / Elite",
                "active": "Myclobutanil 40% WP",
                "dosage": "0.5 g per Liter water",
                "timing": "Curative spray within 72 hours of an infection rain event.",
                "type": "Systemic Sterol Inhibitor"
            }
        ],
        "organic": [
            {
                "remedy": "Bordeaux Mixture 1% (Copper + Lime)",
                "ingredient": "Copper Sulfate (100g) + Slaked Lime (100g) in 10L water",
                "dosage": "Freshly prepared 1% solution spray",
                "instructions": "Standard organic vineyard protectant against black rot and downy mildew."
            },
            {
                "remedy": "Pure Cold-Pressed Neem Oil",
                "ingredient": "Azadirachtin 10,000 PPM",
                "dosage": "5 ml per Liter water + organic soap",
                "instructions": "Spray on clusters during fruit set."
            }
        ],
        "prevention": [
            "Prune out and destroy all mummified grape clusters and infected canes during winter.",
            "Canopy management: Shoot positioning and leaf pulling around fruit clusters to speed up drying."
        ]
    },

    # 13. Grape - Esca (Black Measles)
    "Grape - Esca": {
        "crop": "Grape (Vitis vinifera)",
        "pathogen": "Complex of Phaeomoniella chlamydospora & Fomitiporia mediterranea",
        "risk_level": "High",
        "recovery_time": "Chronic / Management Required",
        "brief": "Esca (black measles) is a devastating grapevine trunk disease complex. Fungi penetrate through pruning wounds, decaying the inner heartwood and releasing toxins that cause 'tiger-stripe' leaf chlorosis and dark speckled measles on berries.",
        "symptoms": [
            "'Tiger-stripe' leaf pattern: Interveinal chlorosis and necrosis leaving a vivid yellow and reddish-brown striped appearance.",
            "Dark purple or black spotting ('measles') on berry skins.",
            "Sudden vine collapse (apoplexy) during hot summer spells.",
            "Spongy white rot visible in trunk cross-sections."
        ],
        "medicines": [
            {
                "brand": "Topsin-M / Pruning Sealant",
                "active": "Thiophanate-Methyl + Wound Protectant Paste",
                "dosage": "Brush directly onto large pruning cuts within 24 hours of cutting",
                "timing": "Immediately post-winter pruning.",
                "type": "Pruning Wound Protectant"
            },
            {
                "brand": "Cabrio Top / Nativo",
                "active": "Pyraclostrobin + Metiram",
                "dosage": "2.0 g per Liter water",
                "timing": "Foliar suppression spray during shoot emergence.",
                "type": "Systemic Broad-Spectrum"
            }
        ],
        "organic": [
            {
                "remedy": "Trichoderma atroviride / gamsii Wound Dressing (Vintec)",
                "ingredient": "Beneficial bio-protectant fungus",
                "dosage": "2 g per Liter water",
                "instructions": "Spray or paint over fresh pruning cuts to biological bar Esca pathogens."
            },
            {
                "remedy": "Horsetail (Equisetum arvense) Extract",
                "ingredient": "Silica-rich herbal decoction",
                "dosage": "50 ml per Liter water",
                "instructions": "Strengthens plant cuticle and xylem vessel walls."
            }
        ],
        "prevention": [
            "Delay pruning until late winter when vine sap bleed pushes out invading spores.",
            "Sterilize pruning shears between vines with alcohol or 10% bleach solution.",
            "Mark symptomatic vines and prune them last to prevent mechanical spread."
        ]
    },

    # 14. Grape - Leaf Blight
    "Grape - Leaf blight": {
        "crop": "Grape (Vitis vinifera)",
        "pathogen": "Pseudocercospora vitis (Phaeoisariopsis vitis)",
        "risk_level": "Moderate",
        "recovery_time": "10 - 14 Days",
        "brief": "Grape leaf blight creates angular brown spots on leaves during wet monsoon periods. Severe attacks cause premature defoliation, preventing grape berries from accumulating sugars and ripening properly.",
        "symptoms": [
            "Irregular, angular, dark reddish-brown lesions on leaves.",
            "Olive to dark gray mold growth on the underside of spots in humid weather.",
            "Yellowing, drying, and extensive leaf shed starting from the bottom of canes."
        ],
        "medicines": [
            {
                "brand": "Score 250 EC / Tilt",
                "active": "Difenoconazole 25% EC",
                "dosage": "0.5 to 1.0 ml per Liter water",
                "timing": "Spray at onset of rainy season.",
                "type": "Systemic Triazole"
            },
            {
                "brand": "Blitox 50 / Indofil M-45",
                "active": "Copper Oxychloride 50% WP or Mancozeb 75% WP",
                "dosage": "2.5 g per Liter water",
                "timing": "Contact spray every 10-14 days.",
                "type": "Contact Protectant"
            }
        ],
        "organic": [
            {
                "remedy": "Bordeaux Mixture (0.8%)",
                "ingredient": "Copper sulfate + Lime",
                "dosage": "80g Copper + 80g Lime in 10L water",
                "instructions": "Spray under leaves to halt spore propagation."
            },
            {
                "remedy": "Bio-formulation Trichoderma viride",
                "ingredient": "Bio-fungicide culture",
                "dosage": "5 g per Liter water",
                "instructions": "Foliar mist in late afternoon."
            }
        ],
        "prevention": [
            "Thin out dense leaf canopy to facilitate fast evaporation of rain and dew.",
            "Collect and burn fallen infected leaves after harvest."
        ]
    },

    # 15. Grape - Healthy
    "Grape - Healthy": {
        "crop": "Grape (Vitis vinifera)",
        "pathogen": "None (Healthy)",
        "risk_level": "Safe",
        "recovery_time": "Optimal Growth",
        "brief": "Grapevine canopy is in pristine condition with lush green five-lobed leaves, strong cane elongation, and healthy fruit cluster development.",
        "symptoms": ["Vibrant green leaves, uniform margins, no spots, and intact tendrils."],
        "medicines": [{"brand": "None needed", "active": "None", "dosage": "None", "timing": "N/A", "type": "Maintenance"}],
        "organic": [{"remedy": "Potassium Humate + Seaweed Spray", "ingredient": "Bio-stimulant", "dosage": "2 ml per Liter water", "instructions": "Improves bunch size, berry uniform sizing, and sugar brix."}],
        "prevention": ["Continue proactive vine training and balanced irrigation."]
    },

    # 16. Orange - Citrus Greening (HLB)
    "Orange - Citrus greening": {
        "crop": "Citrus / Orange (Citrus sinensis)",
        "pathogen": "Candidatus Liberibacter asiaticus (Bacterial Phloem Parasite)",
        "risk_level": "Critical",
        "recovery_time": "Vector Control & Management",
        "brief": "Citrus greening (Huanglongbing or HLB) is the most destructive citrus disease in the world. Spread by the Asian citrus psyllid (Diaphorina citri), it clogs the tree's phloem vascular system. Leaves show asymmetric blotchy mottle, fruit stays green and bitter, and trees decline irreversibly.",
        "symptoms": [
            "Asymmetrical blotchy mottle yellowing across leaf veins (pattern does not match on both halves of leaf).",
            "Small, upright, chlorotic leaves resembling zinc deficiency.",
            "Lopsided, small, bitter fruit with dark aborted seeds that fail to color (fruit stays green at stylar end).",
            "Severe branch dieback and root collapse."
        ],
        "medicines": [
            {
                "brand": "Actara / Confidor (Psyllid Vector Control)",
                "active": "Thiamethoxam 25% WG or Imidacloprid 17.8% SL",
                "dosage": "0.5 g / ml per Liter water",
                "timing": "Target flush flushes to eliminate psyllid insect vectors.",
                "type": "Systemic Insecticide"
            },
            {
                "brand": "Plantomycin / Streptocycline + Copper",
                "active": "Streptomycin Sulphate 9% + Tetracycline 1% (Agrimycin)",
                "dosage": "1 g per 10 Liters water + Copper Oxychloride 25g",
                "timing": "Foliar bactericidal suppression spray on new flush flushes.",
                "type": "Agricultural Antibiotic / Bactericide"
            }
        ],
        "organic": [
            {
                "remedy": "Botanical Neemastra / Agniastra Spray",
                "ingredient": "Neem oil 10,000 PPM (5ml/L) + Pongamia (Karanja) oil (2ml/L)",
                "dosage": "Foliar mist every 10 days on young flushes",
                "instructions": "Suffocates psyllid nymphs and deters adult feeding."
            },
            {
                "remedy": "Micronutrient Phloem Booster",
                "ingredient": "Foliar Zinc Sulphate (0.5%) + Ferrous Sulphate (0.2%) + Boron (0.1%)",
                "dosage": "5 g Zinc + 2 g Iron + 1 g Boron per Liter water",
                "instructions": "Helps bypass clogged phloem and sustain tree vigor."
            }
        ],
        "prevention": [
            "Plant only certified disease-free budwood grown in insect-proof screened nurseries.",
            "Scout weekly with yellow sticky traps for Asian citrus psyllids.",
            "Eradicate and burn confirmed severely infected trees to protect surrounding orchard."
        ]
    },

    # 17. Peach - Bacterial Spot
    "Peach - Bacterial spot": {
        "crop": "Peach (Prunus persica)",
        "pathogen": "Xanthomonas arboricola pv. pruni (Bacterium)",
        "risk_level": "High",
        "recovery_time": "10 - 15 Days",
        "brief": "Bacterial spot strikes peach leaves, twigs, and fruit, particularly in warm, sandy, windy regions with frequent rains. Leaves develop angular water-soaked lesions that drop out, producing a distinct 'shot-hole' appearance followed by severe defoliation.",
        "symptoms": [
            "Small angular, water-soaked purplish-gray spots on leaf tips and margins.",
            "Dead tissue centers drop out, leaving a perforated 'shot-hole' pattern.",
            "Deep, pitted, gum-oozing cracks on peach fruit surface.",
            "Spring and summer cankers on 1-year-old twigs."
        ],
        "medicines": [
            {
                "brand": "Kocide 3000 / Cuprofix",
                "active": "Copper Hydroxide or Basic Copper Sulfate",
                "dosage": "1.5 g per Liter water",
                "timing": "Apply at dormant, bud swell, and low doses post-bloom.",
                "type": "Protective Bactericide"
            },
            {
                "brand": "Mycoshield / Agrimycin",
                "active": "Oxytetracycline or Streptomycin",
                "dosage": "1.0 g per 5 Liters water",
                "timing": "Apply during bloom and petal fall during rainy forecasts.",
                "type": "Antibiotic Bactericide"
            }
        ],
        "organic": [
            {
                "remedy": "Copper Octanoate (Soap) Spray",
                "ingredient": "Low-dose organic copper fatty acid salt",
                "dosage": "3 ml per Liter water",
                "instructions": "Gentle on sensitive peach leaves while suppressing bacteria."
            },
            {
                "remedy": "Bacillus subtilis (Serenade ASO)",
                "ingredient": "Beneficial bio-bactericide",
                "dosage": "4 ml per Liter water",
                "instructions": "Apply every 7 days during shoot elongation."
            }
        ],
        "prevention": [
            "Plant windbreaks around orchards to reduce wind-blown sand abrasions that introduce bacteria.",
            "Avoid over-fertilizing with nitrogen, which promotes lush, thin-cuticled susceptible leaves."
        ]
    },

    # 18. Peach - Healthy
    "Peach - Healthy": {
        "crop": "Peach (Prunus persica)",
        "pathogen": "None (Healthy)",
        "risk_level": "Safe",
        "recovery_time": "Optimal Growth",
        "brief": "Peach foliage is in prime condition with glossy lanceolate leaves, vigorous green shoot growth, and clean unblemished bark.",
        "symptoms": ["Vibrant lanceolate green leaves without shot-holes, leaf curl, or cankers."],
        "medicines": [{"brand": "None needed", "active": "None", "dosage": "None", "timing": "N/A", "type": "Maintenance"}],
        "organic": [{"remedy": "Zinc & Potassium Foliar Boost", "ingredient": "Chelated zinc 12% + SOP 00-00-50", "dosage": "1.5 g each per Liter water", "instructions": "Enhances fruit sizing, sugar content, and bud winter hardiness."}],
        "prevention": ["Apply single dormant copper spray in autumn after leaf fall to prevent peach leaf curl."]
    },

    # 19. Pepper, Bell - Bacterial Spot
    "Pepper, bell - Bacterial spot": {
        "crop": "Bell Pepper / Capsicum (Capsicum annuum)",
        "pathogen": "Xanthomonas euvesicatoria (Bacterium)",
        "risk_level": "High",
        "recovery_time": "8 - 14 Days",
        "brief": "Bacterial spot on bell peppers leads to devastating leaf loss, exposed sunscalded fruit, and crater-like fruit scabs. It spreads rapidly through wind-driven rains, sprinkler irrigation, and handling wet plants.",
        "symptoms": [
            "Small water-soaked, circular-to-irregular lesions that turn brown with yellow margins.",
            "Lesions prominent on leaf undersides, appearing slightly raised or blister-like.",
            "Widespread leaf drop causing bare stems and sunburned peppers.",
            "Raised, wart-like brown scab spots on bell pepper fruits."
        ],
        "medicines": [
            {
                "brand": "Blitox 50 + Streptocycline",
                "active": "Copper Oxychloride 50% WP (2.5g) + Streptomycin Sulphate (0.1g/L)",
                "dosage": "2.5 g Copper + 1 g Streptocycline per 10 Liters water",
                "timing": "Spray immediately upon first symptom; repeat every 7-10 days.",
                "type": "Broad-Spectrum Bactericide Combo"
            },
            {
                "brand": "Kasumin 3% SL",
                "active": "Kasugamycin 3% SL",
                "dosage": "2.0 ml per Liter water",
                "timing": "Systemic antibiotic spray safe for vegetable crops.",
                "type": "Antibiotic Bactericide"
            }
        ],
        "organic": [
            {
                "remedy": "Fresh Garlic & Onion Bulb Bio-Extract",
                "ingredient": "Crushed raw garlic (50g) steeped in 1L water + 2ml neem oil",
                "dosage": "Dilute 1:5 in water and spray",
                "instructions": "Natural allicin compounds exhibit strong antibacterial properties."
            },
            {
                "remedy": "Bacillus amyloliquefaciens (Double Nickel)",
                "ingredient": "Beneficial microbial antagonist",
                "dosage": "4 g per Liter water",
                "instructions": "Competitively excludes Xanthomonas on pepper foliage."
            }
        ],
        "prevention": [
            "Soak non-certified pepper seeds in 50°C hot water for 25 minutes prior to sowing.",
            "Never work in pepper fields while foliage is wet from rain or dew.",
            "Implement drip irrigation; strictly avoid overhead sprinklers."
        ]
    },

    # 20. Pepper, Bell - Healthy
    "Pepper, bell - Healthy": {
        "crop": "Bell Pepper / Capsicum (Capsicum annuum)",
        "pathogen": "None (Healthy)",
        "risk_level": "Safe",
        "recovery_time": "Optimal Growth",
        "brief": "Capsicum leaves display rich green pigmentation, sturdy branching, and thriving blossom nodes with zero signs of anthracnose or bacterial spot.",
        "symptoms": ["Lush, firm, smooth leaves with intact margins and vigorous white flowers."],
        "medicines": [{"brand": "None needed", "active": "None", "dosage": "None", "timing": "N/A", "type": "Maintenance"}],
        "organic": [{"remedy": "Calcium-Boron Foliar Spray", "ingredient": "Chelated Calcium (1g) + Boron 20% (0.5g/L)", "dosage": "Foliar spray during flowering", "instructions": "Prevents blossom end rot and improves fruit wall thickness."}],
        "prevention": ["Maintain balanced staking and soil moisture consistency."]
    },

    # 21. Potato - Early Blight
    "Potato - Early blight": {
        "crop": "Potato (Solanum tuberosum)",
        "pathogen": "Alternaria solani (Fungus)",
        "risk_level": "High",
        "recovery_time": "7 - 12 Days",
        "brief": "Early blight is a widespread potato disease targeting senescing foliage during alternating dry and humid warm spells (24-30°C). It produces concentric brown rings resembling a target board, leading to premature vine death and undersized tubers.",
        "symptoms": [
            "Dark brown to black circular-to-angular spots showing concentric target rings on older lower leaves.",
            "Chlorotic yellowing around leaf lesions spreading across leaflets.",
            "Leaves turn brown, dry up, and hang like paper on lower stems.",
            "Dark, sunken, dry rot spots on potato tubers during storage."
        ],
        "medicines": [
            {
                "brand": "Revus Top / Amistar Top",
                "active": "Mandipropamid + Difenoconazole or Azoxystrobin + Difenoconazole",
                "dosage": "1.0 ml per Liter water",
                "timing": "Apply at tuber initiation and repeat after 12-14 days.",
                "type": "Systemic Translaminar"
            },
            {
                "brand": "Indofil M-45 / Dithane",
                "active": "Mancozeb 75% WP",
                "dosage": "2.5 g per Liter water",
                "timing": "Preventive barrier spray before canopy closure.",
                "type": "Contact Protectant"
            },
            {
                "brand": "Sectin / Antracol",
                "active": "Fenamidone 10% + Mancozeb 50% WG",
                "dosage": "2.0 g per Liter water",
                "timing": "High curative efficacy against severe Alternaria outbreaks.",
                "type": "Dual Contact-Systemic"
            }
        ],
        "organic": [
            {
                "remedy": "Trichoderma viride 1% WP",
                "ingredient": "Bio-fungicide culture",
                "dosage": "5 g per Liter water + 50g jaggery",
                "instructions": "Spray on lower canopy to suppress spore buildup."
            },
            {
                "remedy": "Neem Oil 10,000 PPM + Cow Urine",
                "ingredient": "Neem oil (5ml) + Fermented cow urine (50ml) in 1L water",
                "dosage": "Foliar mist every 10 days",
                "instructions": "Botanical antifungal spray popular in Indian organic potato farming."
            }
        ],
        "prevention": [
            "Maintain optimal crop nutrition; plants stressed for nitrogen or potassium suffer worst.",
            "Destroy and bury all potato cull piles before planting new seasons.",
            "Harvest only after vine skin has set properly to prevent tuber skinning."
        ]
    },

    # 22. Potato - Late Blight
    "Potato - Late blight": {
        "crop": "Potato (Solanum tuberosum)",
        "pathogen": "Phytophthora infestans (Oomycete Water Mold)",
        "risk_level": "Critical",
        "recovery_time": "5 - 10 Days (Emergency Action)",
        "brief": "Late blight is the infamous pathogen behind the Irish Potato Famine. Under cool, damp conditions (10-21°C and >90% humidity), this devastating water mold can completely destroy an entire potato crop in just 4 to 7 days if left untreated.",
        "symptoms": [
            "Irregular, water-soaked, dark olive to black lesions on leaves and petioles that expand aggressively.",
            "White, velvety fungal mold visible on the underside of leaves around the margin of lesions during early mornings.",
            "Entire vine wilts, blackens, and collapses with a distinct pungent decaying odor.",
            "Tubers develop dry, granular, reddish-brown subsurface rot."
        ],
        "medicines": [
            {
                "brand": "Ridomil Gold MZ / Curzate M8",
                "active": "Metalaxyl-M 4% + Mancozeb 64% WP or Cymoxanil 8% + Mancozeb 64% WP",
                "dosage": "2.5 g per Liter water",
                "timing": "Immediate emergency curative spray upon first localized blight alert.",
                "type": "Systemic Curative & Protective"
            },
            {
                "brand": "Acrobat / Infinito",
                "active": "Dimethomorph 50% WP (1g/L) or Fluopicolide + Propamocarb (1.5ml/L)",
                "dosage": "1.0 - 1.5 ml/g per Liter water",
                "timing": "Top-tier translaminar protection against metalaxyl-resistant strains.",
                "type": "Translaminar Oomycete Specialist"
            },
            {
                "brand": "Kavach / Bravo",
                "active": "Chlorothalonil 75% WP",
                "dosage": "2.0 g per Liter water",
                "timing": "Protective cover spray before rain periods.",
                "type": "Multi-site Contact Protectant"
            }
        ],
        "organic": [
            {
                "remedy": "Bordeaux Mixture 1% (Copper Sulfate + Lime)",
                "ingredient": "Copper Sulfate (100g) + Lime (100g) in 10L water",
                "dosage": "Fresh spray covering all foliage",
                "instructions": "Standard organic barrier against Phytophthora zoospore germination."
            },
            {
                "remedy": "Sour Fermented Buttermilk + Copper Coin",
                "ingredient": "6-day fermented buttermilk (1L in 10L water)",
                "dosage": "Spray on lower leaves",
                "instructions": "Provides natural lactic acid bio-shield against water molds."
            }
        ],
        "prevention": [
            "Plant only certified disease-free, blue-tagged seed tubers.",
            "Hill up soil high around rows to create a thick barrier preventing zoospores from washing down into tubers.",
            "Kill potato vines (haulm cutting/defoliation) at least 14 days before harvest if late blight is present."
        ]
    },

    # 23. Potato - Healthy
    "Potato - Healthy": {
        "crop": "Potato (Solanum tuberosum)",
        "pathogen": "None (Healthy)",
        "risk_level": "Safe",
        "recovery_time": "Optimal Growth",
        "brief": "Potato foliage demonstrates superior canopy vigor, strong vegetative stems, and zero signs of early or late blight.",
        "symptoms": ["Lush dark green leaves, crisp leaflets, sturdy petioles, and robust flower clusters."],
        "medicines": [{"brand": "None needed", "active": "None", "dosage": "None", "timing": "N/A", "type": "Maintenance"}],
        "organic": [{"remedy": "NPK Bio-Fertilizer Drench", "ingredient": "Azotobacter + PSB + KMB bio-consortium", "dosage": "2 kg per Acre in irrigation water", "instructions": "Maximizes tuber bulking, starch synthesis, and uniform tuber size."}],
        "prevention": ["Maintain consistent hilling and monitor regional weather blight forecasts."]
    },

    # 24. Raspberry - Healthy
    "Raspberry - Healthy": {
        "crop": "Raspberry (Rubus idaeus)",
        "pathogen": "None (Healthy)",
        "risk_level": "Safe",
        "recovery_time": "Optimal Growth",
        "brief": "Raspberry canes and compound leaves exhibit healthy green foliage free of cane blight, rust, or root rot.",
        "symptoms": ["Vigorous canes with serrated, clean green compound leaves."],
        "medicines": [{"brand": "None needed", "active": "None", "dosage": "None", "timing": "N/A", "type": "Maintenance"}],
        "organic": [{"remedy": "Compost Mulch & Drip Water", "ingredient": "Organic leaf mold", "dosage": "2-3 inch mulch layer", "instructions": "Protects shallow raspberry roots from temperature extremes."}],
        "prevention": ["Prune spent floricanes immediately after summer fruiting."]
    },

    # 25. Soybean - Healthy
    "Soybean - Healthy": {
        "crop": "Soybean (Glycine max)",
        "pathogen": "None (Healthy)",
        "risk_level": "Safe",
        "recovery_time": "Optimal Growth",
        "brief": "Soybean plants display trifoliate foliage with active root nodulation, vibrant green coloration, and zero Asian rust or Cercospora blight.",
        "symptoms": ["Healthy trifoliate leaves, uniform dark green color, active pod development."],
        "medicines": [{"brand": "None needed", "active": "None", "dosage": "None", "timing": "N/A", "type": "Maintenance"}],
        "organic": [{"remedy": "Rhizobium japonicum Seed Inoculation", "ingredient": "Symbiotic nitrogen-fixing bacteria", "dosage": "200 g per 10 kg seeds", "instructions": "Enhances atmospheric nitrogen fixation and saves urea fertilizer."}],
        "prevention": ["Scout for early girdle beetle and tobacco caterpillar."]
    },

    # 26. Squash - Powdery Mildew
    "Squash - Powdery mildew": {
        "crop": "Squash / Cucurbit (Cucurbita pepo)",
        "pathogen": "Podosphaera xanthii (Erysiphe cichoracearum)",
        "risk_level": "Moderate to High",
        "recovery_time": "6 - 10 Days",
        "brief": "Powdery mildew creates talcum-like white powdery dust on squash leaves and stems. It flourishes in warm, dry weather (20-27°C) with high shade and morning dew, leading to rapid yellowing, leaf necrosis, and premature vine death.",
        "symptoms": [
            "White circular powdery spots on upper and lower surfaces of older leaves and petioles.",
            "Spots merge rapidly to cover the entire leaf surface in a white powdery felt.",
            "Infected leaves turn yellow, then dry, brown, and brittle like parchment paper.",
            "Reduced fruit size and sunburn damage on exposed squashes."
        ],
        "medicines": [
            {
                "brand": "Karathane / Tilt 250 EC",
                "active": "Dinocap 48% EC or Propiconazole 25% EC",
                "dosage": "1.0 ml per Liter water",
                "timing": "Spray immediately at first sight of white powdery specks.",
                "type": "Systemic Eradicant"
            },
            {
                "brand": "Sulfex / Thiovit Jet",
                "active": "Wettable Sulfur 80% WDG",
                "dosage": "2.5 g per Liter water",
                "timing": "Protective spray; do NOT spray in extreme midday heat (>32°C).",
                "type": "Contact Protectant"
            }
        ],
        "organic": [
            {
                "remedy": "Potassium Bicarbonate / Baking Soda Spray",
                "ingredient": "Potassium Bicarbonate (5g) + 2ml Horticultural Oil + 1L water",
                "dosage": "Spray every 7 days",
                "instructions": "Alters leaf surface pH to alkaline, destroying powdery mildew mycelium instantly."
            },
            {
                "remedy": "Diluted Milk Foliar Spray",
                "ingredient": "1 part cow milk to 9 parts water",
                "dosage": "Spray under direct sunlight",
                "instructions": "Milk proteins generate natural antiseptic free radicals under UV light."
            }
        ],
        "prevention": [
            "Select resistant squash varieties (labeled PMR).",
            "Plant with ample spacing (4-6 feet between rows) in full sun to eliminate moist shaded microclimates."
        ]
    },

    # 27. Strawberry - Leaf Scorch / Leaf Blight
    "Strawberry - Leaf blight": {
        "crop": "Strawberry (Fragaria × ananassa)",
        "pathogen": "Diplocarpon earlianum (Phomopsis obscurans)",
        "risk_level": "Moderate",
        "recovery_time": "8 - 14 Days",
        "brief": "Strawberry leaf blight and scorch produce purplish to dark red spots that coalesce, causing leaf margins to curl up and look burned or scorched. Heavy attacks sap plant energy and curtail runner and berry production.",
        "symptoms": [
            "Small irregular purple-to-dark brown spots on upper leaf surfaces without light centers.",
            "Lesions multiply, coalesce, and give the entire leaf margin a scorched, burned appearance.",
            "Petioles and fruit calyxes turn brown and wither, causing 'button berries'."
        ],
        "medicines": [
            {
                "brand": "Captan 50% WP / Switch 62.5 WG",
                "active": "Captan 50% WP (2g/L) or Cyprodinil + Fludioxonil (0.8g/L)",
                "dosage": "1.0 - 2.0 g per Liter water",
                "timing": "Apply at early crown emergence and pre-bloom.",
                "type": "Broad-Spectrum Protectant"
            },
            {
                "brand": "Quadris / Amistar",
                "active": "Azoxystrobin 23% SC",
                "dosage": "1.0 ml per Liter water",
                "timing": "Systemic foliar spray during vegetative runner growth.",
                "type": "Strobilurin Systemic"
            }
        ],
        "organic": [
            {
                "remedy": "Liquid Copper Octanoate Spray",
                "ingredient": "Organic copper fatty acid soap",
                "dosage": "2.5 ml per Liter water",
                "instructions": "Protective spray during cool, rainy spring weather."
            },
            {
                "remedy": "Bio-fungicide Bacillus subtilis",
                "ingredient": "Serenade ASO",
                "dosage": "4 ml per Liter water",
                "instructions": "Suppresses fungal spore germination naturally."
            }
        ],
        "prevention": [
            "Renovate strawberry beds after harvest by mowing and burning infected foliage.",
            "Use straw or black plastic mulch to elevate strawberry leaves above moist soil."
        ]
    },

    # 28. Strawberry - Healthy
    "Strawberry - Healthy": {
        "crop": "Strawberry (Fragaria × ananassa)",
        "pathogen": "None (Healthy)",
        "risk_level": "Safe",
        "recovery_time": "Optimal Growth",
        "brief": "Strawberry plants show robust trifoliate leaves, healthy runner development, vibrant crowns, and no leaf spots or crown rot.",
        "symptoms": ["Lush green trifoliate leaves, glossy surface, healthy white blossoms."],
        "medicines": [{"brand": "None needed", "active": "None", "dosage": "None", "timing": "N/A", "type": "Maintenance"}],
        "organic": [{"remedy": "Potassium & Boron Foliar Spray", "ingredient": "SOP 0-0-50 + Boron 20%", "dosage": "1.5 g SOP + 0.5 g Boron per Liter water", "instructions": "Produces sweeter, firmer strawberries with vibrant red color."}],
        "prevention": ["Maintain clean straw mulching and drip irrigation."]
    },

    # 29. Tomato - Bacterial Spot
    "Tomato - Bacterial spot": {
        "crop": "Tomato (Solanum lycopersicum)",
        "pathogen": "Xanthomonas perforans / Xanthomonas vesicatoria (Bacterium)",
        "risk_level": "High",
        "recovery_time": "8 - 14 Days",
        "brief": "Bacterial spot on tomatoes thrives in warm, wet weather (24-30°C) with driving rain. It causes water-soaked, greasy spots on leaves, stems, and fruits. Left unmanaged, it defoliates plants rapidly and marks fruits with unmarketable scabby craters.",
        "symptoms": [
            "Small (less than 3mm), dark brown to black water-soaked spots on leaves.",
            "Spots have a greasy appearance and often merge, causing leaf margins to yellow, brown, and curl.",
            "Leaves die and remain clinging to the stem, exposing green tomatoes to solar scalding.",
            "Green fruits exhibit raised, blister-like black spots that become rough, brown, and crater-like."
        ],
        "medicines": [
            {
                "brand": "Blitox 50 + Plantomycin",
                "active": "Copper Oxychloride 50% WP (2.5g) + Streptomycin Sulphate 90% (0.1g/L)",
                "dosage": "2.5 g Copper + 1 g Streptomycin per 10 Liters water",
                "timing": "Spray every 7-10 days during warm rainy forecasts.",
                "type": "Copper-Bactericide Combination"
            },
            {
                "brand": "Kasumin 3% SL",
                "active": "Kasugamycin 3% SL",
                "dosage": "2.0 ml per Liter water",
                "timing": "Modern systemic agricultural antibiotic with zero copper toxicity.",
                "type": "Systemic Antibiotic"
            }
        ],
        "organic": [
            {
                "remedy": "Pure Cold-Pressed Neem Oil + Liquid Soap",
                "ingredient": "Neem Oil 10,000 PPM (5ml) + 1ml dish soap in 1L water",
                "dosage": "Foliar mist every 7 days",
                "instructions": "Forms an antiseptic film on tomato leaves that impedes bacterial entry."
            },
            {
                "remedy": "Bacillus amyloliquefaciens (Double Nickel 55)",
                "ingredient": "Beneficial bacterial colonizer",
                "dosage": "3 g per Liter water",
                "instructions": "Outcompetes Xanthomonas on leaf stomata."
            }
        ],
        "prevention": [
            "Use certified disease-free seeds or treat seeds with 50°C hot water for 25 minutes.",
            "Switch exclusively to drip irrigation; eliminate overhead sprinkler splash.",
            "Avoid working in tomato fields when leaves are wet to prevent mechanical transmission."
        ]
    },

    # 30. Tomato - Early Blight
    "Tomato - Early blight": {
        "crop": "Tomato (Solanum lycopersicum)",
        "pathogen": "Alternaria solani (Fungal Pathogen)",
        "risk_level": "High",
        "recovery_time": "7 - 12 Days",
        "brief": "Early blight is one of the most common and damaging diseases of tomatoes worldwide. It thrives in warm, humid weather (24-29°C) with heavy dew. Characterized by dark target-board rings on older foliage, it defoliates vines from the ground up, causing up to 50% yield loss.",
        "symptoms": [
            "Dark brown to black circular lesions with distinct concentric rings ('bullseye' or target board pattern) on older lower leaves.",
            "Pronounced yellow chlorotic halo surrounding each lesion, expanding until leaflets yellow and drop.",
            "Dark, sunken, leathery cankers on stems near the soil surface (collar rot).",
            "Dark, sunken, leathery lesions developing at the fruit stem-end."
        ],
        "medicines": [
            {
                "brand": "Dithane M-45 / Indofil M-45",
                "active": "Mancozeb 75% WP",
                "dosage": "2.5 g per 1 Liter water",
                "timing": "Protective cover spray; apply every 10-12 days.",
                "type": "Protective Contact Fungicide"
            },
            {
                "brand": "Score 250 EC / Amistar Top",
                "active": "Difenoconazole 25% EC or Azoxystrobin + Difenoconazole",
                "dosage": "1.0 ml per 1 Liter water",
                "timing": "Curative systemic action; apply at first sign of target spots.",
                "type": "Systemic Translaminar Fungicide"
            },
            {
                "brand": "Kavach 75 WP / Bravo",
                "active": "Chlorothalonil 75% WP",
                "dosage": "2.0 g per 1 Liter water",
                "timing": "Broad-spectrum multi-site protectant against spore germination.",
                "type": "Contact Protectant"
            }
        ],
        "organic": [
            {
                "remedy": "Bio-fungicide Drench & Foliar Spray",
                "ingredient": "Trichoderma viride 1% WP",
                "dosage": "5 g per Liter water + 50g jaggery solution",
                "instructions": "Spray on foliage and drench root zone; biologically parasitizes Alternaria."
            },
            {
                "remedy": "Cold-Pressed Neem Oil (10,000 PPM)",
                "ingredient": "Pure Azadirachtin Neem Oil (5ml) + 1ml liquid soap",
                "dosage": "5 ml per Liter water",
                "instructions": "Spray thoroughly on upper and lower leaf surfaces in late afternoon."
            },
            {
                "remedy": "Fermented Sour Buttermilk (Desi Chhachh)",
                "ingredient": "5-day fermented sour buttermilk (1L in 10L water)",
                "dosage": "Foliar mist every 8-10 days",
                "instructions": "Natural lactic acid and copper spray with proven antifungal action."
            }
        ],
        "prevention": [
            "Prune the bottom 12-18 inches of tomato foliage to prevent soil-splash onto lower leaves.",
            "Apply straw, dry grass, or plastic mulch around the plant base.",
            "Implement a strict 3-year crop rotation (do not plant after potato, pepper, or eggplant).",
            "Always use drip irrigation to keep tomato foliage dry."
        ]
    },

    # 31. Tomato - Late Blight
    "Tomato - Late blight": {
        "crop": "Tomato (Solanum lycopersicum)",
        "pathogen": "Phytophthora infestans (Oomycete Water Mold)",
        "risk_level": "Critical",
        "recovery_time": "5 - 10 Days (Emergency Action)",
        "brief": "Late blight is the most aggressively destructive disease of tomatoes. Under cool, damp, foggy conditions (12-22°C and >90% humidity), it can wipe out an entire tomato patch within a week, turning lush vines into rotting, foul-smelling black mush.",
        "symptoms": [
            "Large, irregular water-soaked pale green to dark brown lesions that expand with lightning speed.",
            "White cottony fungal bloom on the underside of leaves during damp early mornings.",
            "Petioles and main stems develop dark brown-to-black greasy lesions that collapse the plant.",
            "Green and ripe fruits develop large, firm, greasy golden-brown to dark brown wrinkled rots."
        ],
        "medicines": [
            {
                "brand": "Ridomil Gold MZ / Curzate M8",
                "active": "Metalaxyl-M 4% + Mancozeb 64% WP or Cymoxanil + Mancozeb",
                "dosage": "2.5 g per Liter water",
                "timing": "Immediate emergency spray at first localized blight warning.",
                "type": "Systemic Translaminar Curative"
            },
            {
                "brand": "Acrobat 50 WP / Infinito",
                "active": "Dimethomorph 50% WP (1g/L) or Fluopicolide + Propamocarb (1.5ml/L)",
                "dosage": "1.0 - 1.5 ml/g per Liter water",
                "timing": "High-efficiency modern anti-oomycete chemistry.",
                "type": "Systemic Oomycide"
            },
            {
                "brand": "Blitox 50 / Blue Copper",
                "active": "Copper Oxychloride 50% WP",
                "dosage": "3.0 g per Liter water",
                "timing": "Protective contact shield on foliage.",
                "type": "Contact Fungicide"
            }
        ],
        "organic": [
            {
                "remedy": "Bordeaux Mixture 1% (Copper + Lime)",
                "ingredient": "Copper Sulfate (100g) + Slaked Lime (100g) in 10L water",
                "dosage": "Fresh 1% spray covering whole canopy",
                "instructions": "Standard organic treatment to prevent Phytophthora zoospore motility."
            },
            {
                "remedy": "Sour Fermented Buttermilk + Bio-fungicide",
                "ingredient": "Sour buttermilk (10%) + Trichoderma harzianum (5g/L)",
                "dosage": "Foliar mist every 5 days during cloudy foggy weather",
                "instructions": "Lactic acid bio-shield against water molds."
            }
        ],
        "prevention": [
            "Avoid planting tomatoes near potatoes (common host reservoir).",
            "Destroy and bury all infected plant material immediately; do NOT put in compost.",
            "Ensure wide spacing and high staking to maximize airflow and dry out morning dew."
        ]
    },

    # 32. Tomato - Leaf Mold
    "Tomato - Leaf Mold": {
        "crop": "Tomato (Solanum lycopersicum)",
        "pathogen": "Passalora fulva (Cladosporium fulvum)",
        "risk_level": "Moderate",
        "recovery_time": "8 - 12 Days",
        "brief": "Tomato leaf mold primarily strikes tomatoes grown in high-humidity greenhouses, polyhouses, or damp sheltered gardens (>85% RH and 22-26°C). It creates pale yellow patches on leaf uppersides with olive-green velvety mold underneath.",
        "symptoms": [
            "Pale yellow, indistinct chlorotic spots on upper leaf surfaces.",
            "Dense, velvety, olive-green to brown fungal mold on the corresponding lower leaf surface.",
            "Leaves curl, wither, turn brown, and drop prematurely, starting from the lower canopy.",
            "Rarely attacks fruit directly, but defoliation stunts fruit size and delays ripening."
        ],
        "medicines": [
            {
                "brand": "Score 250 EC / Quadris",
                "active": "Difenoconazole 25% EC or Azoxystrobin 23% SC",
                "dosage": "1.0 ml per Liter water",
                "timing": "Spray at first sign on lower canopy.",
                "type": "Systemic Fungicide"
            },
            {
                "brand": "Kavach / Dithane M-45",
                "active": "Chlorothalonil 75% WP or Mancozeb 75% WP",
                "dosage": "2.0 g per Liter water",
                "timing": "Protective cover spray before humidity spikes.",
                "type": "Contact Protectant"
            }
        ],
        "organic": [
            {
                "remedy": "Potassium Bicarbonate Foliar Mist",
                "ingredient": "Potassium Bicarbonate 4g + 1ml horticultural oil",
                "dosage": "4 g per Liter water",
                "instructions": "Eradicates Passalora mold by raising leaf surface pH."
            },
            {
                "remedy": "Neem Oil 10,000 PPM",
                "ingredient": "Azadirachtin cold-pressed neem oil",
                "dosage": "4 ml per Liter water + mild soap",
                "instructions": "Natural botanical fungistat."
            }
        ],
        "prevention": [
            "Ventilate greenhouses aggressively; run circulation fans to reduce relative humidity below 80%.",
            "Prune lower suckers and foliage to increase interior light and air circulation.",
            "Select leaf-mold resistant tomato hybrids (labeled with Cf-1 through Cf-9 resistance)."
        ]
    },

    # 33. Tomato - Septoria Leaf Spot
    "Tomato - Septoria leaf spot": {
        "crop": "Tomato (Solanum lycopersicum)",
        "pathogen": "Septoria lycopersici (Fungus)",
        "risk_level": "Moderate to High",
        "recovery_time": "8 - 14 Days",
        "brief": "Septoria leaf spot is a destructive foliar disease causing numerous small, circular spots with light gray centers and dark brown margins. It spreads from the bottom leaves upward during wet, warm spells, stripping plants of foliage and leaving fruit exposed.",
        "symptoms": [
            "Numerous circular spots (1.5 - 3 mm across) with dark brown margins and sunken grayish-white centers.",
            "Tiny, black, pimple-like fruiting bodies (pycnidia) clearly visible in the center of mature spots under magnification.",
            "Severe leaf yellowing, browning, and progressive defoliation from ground level up.",
            "Fruit is rarely infected directly, but defoliation leads to sunscald and unmarketable fruit."
        ],
        "medicines": [
            {
                "brand": "Bravo Weather Stik / Kavach",
                "active": "Chlorothalonil 75% WP",
                "dosage": "2.0 g per Liter water",
                "timing": "Spray immediately upon first leaf spot; repeat every 7-10 days.",
                "type": "Contact Protectant"
            },
            {
                "brand": "Tilt 250 EC / Nativo",
                "active": "Propiconazole 25% EC or Tebuconazole + Trifloxystrobin",
                "dosage": "1.0 ml / 0.8 g per Liter water",
                "timing": "Curative systemic control for advanced Septoria outbreaks.",
                "type": "Systemic Fungicide"
            }
        ],
        "organic": [
            {
                "remedy": "Liquid Copper Fungicide (Copper Octanoate)",
                "ingredient": "Organic low-toxicity copper soap",
                "dosage": "3 ml per Liter water",
                "instructions": "Apply every 7-10 days during rainy conditions."
            },
            {
                "remedy": "Trichoderma harzianum Bio-Mist",
                "ingredient": "Bio-fungicide formulation",
                "dosage": "5 g per Liter water",
                "instructions": "Colonizes lower canopy to intercept splash-dispersed spores."
            }
        ],
        "prevention": [
            "Prune off all infected lower leaves as soon as spots appear; dispose in garbage, not compost.",
            "Mulch heavily around tomato plants with clean straw or plastic to block rain splash from soil.",
            "Implement a strict 3-year crop rotation."
        ]
    },

    # 34. Tomato - Spider Mites
    "Tomato - Spider mites": {
        "crop": "Tomato (Solanum lycopersicum)",
        "pathogen": "Tetranychus urticae (Two-Spotted Spider Mite - Arachnid Pest)",
        "risk_level": "High",
        "recovery_time": "6 - 10 Days",
        "brief": "Two-spotted spider mites are microscopic arachnids that proliferate explosively during hot, dry, dusty weather (over 30°C). They pierce plant leaf cells and suck out chlorophyll, causing fine yellow stippling and enveloping terminal shoots in dense silky webbing.",
        "symptoms": [
            "Fine white, yellow, or bronze stippling / speckling on the upper surface of leaves.",
            "Fine silky webbing visible on leaf undersides, growing tips, and between stems.",
            "Leaves turn bronze, dry, brittle, and drop, giving the plant a scorched appearance.",
            "Microscopic red/yellow mites moving on the underside of leaves when tapped over white paper."
        ],
        "medicines": [
            {
                "brand": "Oberon 240 SC / Magister",
                "active": "Spiromesifen 22.9% SC or Fenazaquin 10% EC",
                "dosage": "1.0 ml per Liter water",
                "timing": "Apply at first sign of stippling; kills mite eggs, nymphs, and adults.",
                "type": "Selective Acaricide / Miticide"
            },
            {
                "brand": "Vertimec / Abamectin 1.9% EC",
                "active": "Abamectin 1.9% EC",
                "dosage": "0.5 ml per Liter water",
                "timing": "Powerful translaminar miticide; sprays penetrate leaf tissue to reach mites.",
                "type": "Translaminar Acaricide"
            }
        ],
        "organic": [
            {
                "remedy": "Cold-Pressed Neem Oil (10,000 PPM) + Potassium Soap",
                "ingredient": "Pure Neem oil (5ml) + insecticidal soap (2ml) in 1L water",
                "dosage": "Spray undersides of leaves thoroughly",
                "instructions": "Disrupts mite hormonal molting and suffocates nymphs."
            },
            {
                "remedy": "Strong Water Jet Spray + Predatory Mites",
                "ingredient": "Pressurized water spray + Phytoseiulus persimilis",
                "dosage": "Spray undersides in morning to wash away webbing; introduce predatory mites",
                "instructions": "Natural predatory mites consume 20-30 spider mites per day."
            }
        ],
        "prevention": [
            "Maintain soil moisture and hose down dusty farm paths; dry dust promotes mite outbreaks.",
            "Avoid broad-spectrum pyrethroid insecticides which kill beneficial predatory mites."
        ]
    },

    # 35. Tomato - Target Spot
    "Tomato - Target Spot": {
        "crop": "Tomato (Solanum lycopersicum)",
        "pathogen": "Corynespora cassiicola (Fungus)",
        "risk_level": "Moderate to High",
        "recovery_time": "8 - 14 Days",
        "brief": "Target spot affects leaves, stems, and fruits in warm, humid tropical and subtropical climates (20-32°C). It produces circular brown lesions with distinct concentric rings that can easily be confused with early blight, causing substantial canopy destruction.",
        "symptoms": [
            "Small pinpoint brown lesions expanding to circular brown spots with faint concentric rings.",
            "Centers of lesions frequently crack, tear, or fall out, giving a ragged appearance.",
            "Stem lesions are dark and elongated; fruit spots start small, sunken, and turn dark brown.",
            "Upper canopy defoliation when humidity remains high."
        ],
        "medicines": [
            {
                "brand": "Luna Tranquility / Priaxor",
                "active": "Fluopyram + Pyrimethanil or Pyraclostrobin + Fluxapyroxad",
                "dosage": "1.0 ml per Liter water",
                "timing": "Apply upon first appearance on lower leaves.",
                "type": "Systemic Broad-Spectrum"
            },
            {
                "brand": "Dithane M-45 / Saaf",
                "active": "Mancozeb 75% WP or Carbendazim + Mancozeb",
                "dosage": "2.0 g per Liter water",
                "timing": "Protective cover spray every 10-14 days.",
                "type": "Protectant Fungicide"
            }
        ],
        "organic": [
            {
                "remedy": "Copper Hydroxide (Kocide 3000)",
                "ingredient": "Copper Hydroxide",
                "dosage": "2.0 g per Liter water",
                "instructions": "Protects leaf surfaces against Corynespora spore germination."
            },
            {
                "remedy": "Neemastra Bio-Spray",
                "ingredient": "Botanical extract formulation",
                "dosage": "50 ml per Liter water",
                "instructions": "Foliar mist every 8 days."
            }
        ],
        "prevention": [
            "Prune suckers to facilitate rapid drying of foliage after rain or irrigation.",
            "Rotate crops away from cucurbits, soybeans, and peppers which host Corynespora."
        ]
    },

    # 36. Tomato - Tomato Yellow Leaf Curl Virus (TYLCV)
    "Tomato - Tomato Yellow Leaf Curl Virus": {
        "crop": "Tomato (Solanum lycopersicum)",
        "pathogen": "Tomato Yellow Leaf Curl Geminivirus (Vector: Bemisia tabaci Whitefly)",
        "risk_level": "Critical",
        "recovery_time": "Vector Control & Management",
        "brief": "TYLCV is one of the most economically devastating tomato viruses worldwide. Transmitted by the sweetpotato whitefly (Bemisia tabaci), it arrests plant growth completely. Infected plants become severely stunted, bushy, leaves cup upward with intense yellow margins, and flower drop prevents fruit formation.",
        "symptoms": [
            "Severe upward curling and cupping of leaflets ('spooning').",
            "Prominent yellowing (chlorosis) along leaf margins and interveinal areas.",
            "Severe plant stunting, shortened internodes, and bushy, upright growth habit.",
            "Heavy blossom drop; fruit production halts completely if infected early."
        ],
        "medicines": [
            {
                "brand": "Confidor / Actara (Vector Control)",
                "active": "Imidacloprid 17.8% SL (0.5ml/L) or Thiamethoxam 25% WG (0.5g/L)",
                "dosage": "0.5 ml/g per Liter water",
                "timing": "Drench nursery seedlings and spray field crops to eliminate whiteflies.",
                "type": "Systemic Neonicotinoid Insecticide"
            },
            {
                "brand": "Benevia 100 OD / Movento",
                "active": "Cyantraniliprole 10.26% OD or Spirotetramat 15.31% OD",
                "dosage": "1.5 ml per Liter water",
                "timing": "Cross-spectrum systemic control of sucking whitefly vectors.",
                "type": "Systemic Diamide / Tetramic Acid"
            }
        ],
        "organic": [
            {
                "remedy": "Yellow Sticky Traps + Neem Oil 10,000 PPM",
                "ingredient": "Install 20-25 yellow sticky cards per acre + Neem Oil (5ml/L)",
                "dosage": "Spray neem oil on undersides of leaves weekly",
                "instructions": "Traps adult whiteflies and disrupts egg hatching."
            },
            {
                "remedy": "Agniastra / Dashaparni Ark",
                "ingredient": "Traditional Indian botanical extract with tobacco, chili, garlic, neem",
                "dosage": "30 ml per Liter water",
                "instructions": "Natural repellent and contact killer for sucking pests."
            }
        ],
        "prevention": [
            "Plant TYLCV-resistant or tolerant hybrid varieties (e.g. Tyking, Abhinav, US-440).",
            "Use UV-reflective silver plastic mulches to disorient whiteflies from landing.",
            "Immediately rogue (pull out and burn) early-infected viral plants to stop vector acquisition."
        ]
    },

    # 37. Tomato - Tomato Mosaic Virus (ToMV)
    "Tomato - Tomato mosaic virus": {
        "crop": "Tomato (Solanum lycopersicum)",
        "pathogen": "Tomato Mosaic Tobamovirus (ToMV)",
        "risk_level": "High",
        "recovery_time": "Sanitation & Management",
        "brief": "Tomato mosaic virus is an exceptionally stable and contagious tobamovirus. Unlike insect-spread viruses, ToMV spreads mechanically through hands, pruning tools, trellis stakes, seeds, and even tobacco products handled by workers. It causes mottled leaves, fern-like distortion, and internal fruit browning.",
        "symptoms": [
            "Mottling of leaves with alternating light green and dark green mosaic patterns.",
            "Distorted, blistered, puckered leaves, sometimes narrowing into a 'shoestring' or fern-like shape.",
            "Stunted plant growth and reduced fruit yield.",
            "Internal brown necrotic rings (brown wall) inside tomato fruit flesh."
        ],
        "medicines": [
            {
                "brand": "Virazole / Trisodium Phosphate (Disinfectant)",
                "active": "Trisodium Phosphate (TSP 10%) or 20% Non-Fat Dry Milk Solution",
                "dosage": "100 g TSP per Liter water for tool and hand wash",
                "timing": "Wash pruning shears and hands between handling each plant.",
                "type": "Sterilizing Decontaminant"
            },
            {
                "brand": "No Direct Curative Chemical Cure Exists",
                "active": "Viral disease - Focus on sanitation and resistance",
                "dosage": "N/A",
                "timing": "N/A",
                "type": "Hygiene Management"
            }
        ],
        "organic": [
            {
                "remedy": "Skimmed Milk Dip & Spray",
                "ingredient": "20% Reconstituted non-fat dry milk in water",
                "dosage": "Dip hands and tools before touching plants; spray seedlings",
                "instructions": "Milk proteins inactivate tobamovirus coat proteins mechanically."
            },
            {
                "remedy": "Bio-stimulant Plant Immunizer",
                "ingredient": "Chitosan / Salicylic acid spray (100 PPM)",
                "dosage": "1.0 ml per Liter water",
                "instructions": "Triggers Systemic Acquired Resistance (SAR) inside tomato tissues."
            }
        ],
        "prevention": [
            "Plant ToMV-resistant tomato cultivars (labeled with 'Tm' or 'ToMV' resistance).",
            "Never smoke, chew, or handle tobacco near tomato plants; wash hands with soap before entering.",
            "Rogue and bag infected plants carefully without brushing against neighboring healthy plants."
        ]
    },

    # 38. Tomato - Healthy
    "Tomato - Healthy": {
        "crop": "Tomato (Solanum lycopersicum)",
        "pathogen": "None (Plant is Healthy)",
        "risk_level": "Safe",
        "recovery_time": "Optimal Growth",
        "brief": "The tomato specimen exhibits vigorous vegetative growth, rich dark green foliage, pristine leaf margins, and robust turgor pressure. Continue standard cultural maintenance and balanced crop nutrition.",
        "symptoms": [
            "Lush, deep emerald green compound leaves without chlorosis or necrotic lesions.",
            "Sturdy, erect stems with dense glandular trichomes (leaf hairs).",
            "Healthy yellow blossom clusters and uniform fruit set."
        ],
        "medicines": [
            {
                "brand": "No Chemical Intervention Required",
                "active": "None",
                "dosage": "0 g / L (Save chemical input cost)",
                "timing": "N/A",
                "type": "Preventive Maintenance"
            }
        ],
        "organic": [
            {
                "remedy": "Jeevamrut Soil & Foliar Drench",
                "ingredient": "Fermented organic cow dung, urine, jaggery, and gram flour culture",
                "dosage": "200 Liters per Acre every 15 days",
                "instructions": "Multiplies beneficial soil microbes and strengthens natural immunity."
            },
            {
                "remedy": "Panchagavya Foliar Spray",
                "ingredient": "5 sacred cow products fermented bio-promoter",
                "dosage": "30 ml per Liter water",
                "instructions": "Spray during flowering and fruit setting for larger, tastier tomatoes."
            }
        ],
        "prevention": [
            "Stake or trellis plants properly to keep fruit and leaves elevated above the ground.",
            "Water regularly at ground level using drip irrigation to prevent blossom end rot.",
            "Inspect weekly for early hornworm or aphid activity."
        ]
    }
}


def get_disease_details(disease_name):
    """
    Looks up disease details in the database using exact or fuzzy key matching.
    Returns complete structured details.
    """
    clean_name = disease_name.strip()
    
    # 1. Direct match
    if clean_name in DISEASE_DATABASE:
        return DISEASE_DATABASE[clean_name]
        
    # 2. Case-insensitive / partial match
    clean_lower = clean_name.lower().replace("_", " ")
    for key, data in DISEASE_DATABASE.items():
        key_lower = key.lower().replace("_", " ")
        if key_lower == clean_lower:
            return data
            
    for key, data in DISEASE_DATABASE.items():
        key_lower = key.lower().replace("_", " ")
        if key_lower in clean_lower or clean_lower in key_lower:
            return data
            
    # Check if healthy
    if "healthy" in clean_lower:
        return {
            "crop": clean_name.split("-")[0].strip() if "-" in clean_name else "Crop Specimen",
            "pathogen": "None (Healthy)",
            "risk_level": "Safe",
            "recovery_time": "Optimal Growth",
            "brief": "The plant specimen is vigorous, healthy, and completely free of visible foliar pathogens. Keep maintaining balanced organic nutrition, adequate sunlight, and proper irrigation.",
            "symptoms": ["Lush green foliage", "Uniform leaf blade expansion without necrotic spots", "Intact cuticle layer"],
            "medicines": [{"brand": "None needed", "active": "None", "dosage": "None", "timing": "N/A", "type": "Maintenance"}],
            "organic": [{"remedy": "Jeevamrut / Vermicompost", "ingredient": "Organic bio-stimulant", "dosage": "Foliar & soil drench", "instructions": "Maintains vibrant leaf health."}],
            "prevention": ["Continue routine field monitoring and avoid overwatering."]
        }
        
    # Default fallback for uncataloged anomalies
    return {
        "crop": clean_name.split("-")[0].strip() if "-" in clean_name else "Field Crop",
        "pathogen": "Suspected Foliar Anomaly",
        "risk_level": "Moderate",
        "recovery_time": "7 - 14 Days",
        "brief": f"The model detected symptoms indicative of {clean_name}. Inspect the underside of leaves for spores or pests, check soil moisture, and isolate affected branches if spreading.",
        "symptoms": ["Abnormal leaf discoloration or spotting", "Potential moisture or fungal stress"],
        "medicines": [
            {
                "brand": "Dithane M-45 / Blitox 50",
                "active": "Mancozeb 75% WP or Copper Oxychloride 50% WP",
                "dosage": "2.5 g per Liter water",
                "timing": "Broad-spectrum protective foliar spray",
                "type": "Contact Fungicide"
            }
        ],
        "organic": [
            {
                "remedy": "Cold-Pressed Neem Oil (10,000 PPM)",
                "ingredient": "Pure Neem Oil + mild soap",
                "dosage": "5 ml per Liter water",
                "instructions": "Broad-spectrum organic protection against foliar fungal and insect stress."
            }
        ],
        "prevention": [
            "Prune symptomatic leaves and sanitize tools.",
            "Avoid wetting leaves during evening watering."
        ]
    }
