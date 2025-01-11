import re

def format_code(code: str, indent_size: int = 4) -> str:
    """Formats the given code by standardizing indentation and removing extra blank lines."""
    lines = code.split('\n')
    formatted_lines = []
    indent_level = 0

    for line in lines:
        stripped = line.strip()
        if not stripped:
            # Skip extra blank lines
            if formatted_lines and formatted_lines[-1] != '':
                formatted_lines.append('')
            continue

        # Adjust indentation level for blocks
        if stripped.endswith('}'):
            indent_level = max(indent_level - 1, 0)

        formatted_lines.append(' ' * (indent_size * indent_level) + stripped)

        if stripped.endswith('{'):
            indent_level += 1

    return '\n'.join(formatted_lines).strip()

if __name__ == "__main__":
    input_file = input("Enter the path of the file to format: ").strip()
    output_file = input("Enter the path to save the formatted file: ").strip()

    try:
        with open(input_file, 'r') as f:
            unformatted_code = f.read()

        formatted_code = format_code(unformatted_code)

        with open(output_file, 'w') as f:
            f.write(formatted_code)

        print(f"Formatted code saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")
