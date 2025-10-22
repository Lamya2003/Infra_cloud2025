def get_net_prefix(subnet_mask):
    try:
        # Split het masker in 4 octetten
        octets = subnet_mask.split(".")
        if len(octets) != 4:
            raise ValueError("Invalid subnet mask format")
        
        # Tel het aantal '1'-bits in elk octet
        bits = sum(bin(int(octet)).count("1") for octet in octets)
        return bits
    except:
        return "Wrong input: garbage in, garbage out"

# Testen
print(get_net_prefix("255.252.0.0"))   # Output: 14
print(get_net_prefix("255.255.0.0"))   # Output: 16
