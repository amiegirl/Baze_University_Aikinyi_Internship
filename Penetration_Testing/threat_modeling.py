import itertools

# STRIDE threat categories
THREAT_CATEGORIES = {
    "Spoofing": "Impersonating a user or system.",
    "Tampering": "Altering data or code.",
    "Repudiation": "Performing an action without a trace.",
    "Information Disclosure": "Leaking sensitive information.",
    "Denial of Service": "Disrupting service availability.",
    "Elevation of Privilege": "Gaining unauthorized access."
}

# Example assets
assets = [
    "User Authentication",
    "Database",
    "Web API",
    "File Storage",
    "Network Communication"
]

# Mapping assets to potential threats
THREAT_MODEL = {
    "User Authentication": ["Spoofing", "Tampering", "Elevation of Privilege"],
    "Database": ["Tampering", "Information Disclosure", "Denial of Service"],
    "Web API": ["Spoofing", "Tampering", "Denial of Service"],
    "File Storage": ["Tampering", "Information Disclosure"],
    "Network Communication": ["Spoofing", "Denial of Service", "Information Disclosure"]
}

def generate_threat_report():
    print("### Threat Modeling Report ###\n")
    
    for asset, threats in THREAT_MODEL.items():
        print(f"Asset: {asset}")
        for threat in threats:
            print(f"  - {threat}: {THREAT_CATEGORIES[threat]}")
        print("-" * 40)

    print("\nPotential attack combinations:")
    for attack_vector in itertools.combinations(THREAT_CATEGORIES.keys(), 2):
        print(f"  * {attack_vector[0]} + {attack_vector[1]}")

if __name__ == "__main__":
    generate_threat_report()