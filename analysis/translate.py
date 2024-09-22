def read_and_rewrite_data(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    mol_id = 0
    output_lines = []

    # Process the input data
    for i in range(2, len(lines)):  # Start processing from the 3rd line (index 2)
        line = lines[i].strip()

        # Check if the row contains only one value (new molecule ID)
        if len(line.split()) == 1:
            mol_id += 1  # Increment molecule ID
        else:
            values = line.split()
            if len(values) >= 3:  # Ensure there are at least 3 values for x, y, z
                x, y, z = values[:3]  # Only take the first 3 values
                output_lines.append(f"{mol_id:<6}   {x:<12} {y:<12} {z:<12}\n")

    # Write to the output file
    with open(output_file, 'w') as outfile:
        outfile.write(f"{len(output_lines)-1}\n")  # Write the total number of lines as the first line
        outfile.writelines(output_lines)  # Write the processed data




# Example usage
input_file = '/projects/p32439/arman/TESTING/PPA+.dat'
output_file = 'reformatted_data.txt'
read_and_rewrite_data(input_file, output_file)
