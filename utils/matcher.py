from rapidfuzz import process, fuzz

# Sample local medicine database
MEDICINE_DATABASE = [
    {"name": "Aspirin", "category": "Blood Thinner / NSAID", "interactions": ["Ibuprofen", "Warfarin"]},
    {"name": "Ibuprofen", "category": "NSAID", "interactions": ["Aspirin", "Aspirin 81mg", "Naproxen"]},
    {"name": "Paracetamol", "category": "Analgesic", "interactions": ["Alcohol", "Warfarin"]},
    {"name": "Metformin", "category": "Antidiabetic", "interactions": ["Alcohol", "Contrast Dye"]},
    {"name": "Atorvastatin", "category": "Statin", "interactions": ["Grapefruit Juice", "Clarithromycin"]}
]

def match_medicine(query_name, threshold=70):
    """
    Uses RapidFuzz to match user-inputted medicine names against the database.
    """
    med_names = [med["name"] for med in MEDICINE_DATABASE]
    result = process.extractOne(query_name, med_names, scorer=fuzz.WRatio)
    
    if result and result[1] >= threshold:
        matched_name = result[0]
        # Find full medicine details
        for med in MEDICINE_DATABASE:
            if med["name"] == matched_name:
                return med
    return None