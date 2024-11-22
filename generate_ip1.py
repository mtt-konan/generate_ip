def parse_input(ip_format):
    """Parse the input IP format and ensure it's valid."""
    parts = ip_format.split(".")
    if len(parts) != 4:
        return None, "Invalid format: IP must have four segments separated by dots."
    
    fixed_positions = {}
    variable_positions = []
    
    for i, part in enumerate(parts):
        if part.isdigit():
            fixed_positions[i] = int(part)
        elif part == "*":
            variable_positions.append(i)
        else:
            return None, f"Invalid segment '{part}': Each segment must be a number or '*'."
    
    return fixed_positions, variable_positions, None

def generate_ips(ip_format, output_file):
    """Generate IPs based on the input format and save to a file."""
    fixed_positions, variable_positions, error = parse_input(ip_format)
    if error:
        print(error)
        return

    # Precompute fixed segments
    ip_template = [None] * 4
    for pos, value in fixed_positions.items():
        ip_template[pos] = value

    # Optimize based on the number of variable positions
    ranges = [range(256) if i in variable_positions else [ip_template[i]] for i in range(4)]

    with open(output_file, "w") as f:
        for ip_parts in ((a, b, c, d) for a in ranges[0] for b in ranges[1] for c in ranges[2] for d in ranges[3]):
            f.write(".".join(map(str, ip_parts)) + "\n")

if __name__ == "__main__":
    ip_format = input("Enter the IP format (e.g., 1.2.3.*): ").strip()
    output_file = "ip1.txt"
    generate_ips(ip_format, output_file)
    print(f"IPs have been generated and saved to {output_file}.")
