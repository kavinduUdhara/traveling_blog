# Open the input file
with open('input.txt', 'r') as f:
    # Read the contents of the file
    contents = f.read()
    # Split the contents by newlines
    lines = contents.split('\n')
    # Remove any empty lines
    lines = [line.strip() for line in lines if line.strip()]
    # Loop through each line and output it in the desired format
    for line in lines:
        # Extract the city name from the line
        city = line.split(',')[0].replace('(image)', '').strip()
        # Extract the description from the line
        description = line.split(':')[1].strip()
        # Output the line in the desired format
        print(f'<li><span class="code-style-1">{city}:</span> {description}</li>')
