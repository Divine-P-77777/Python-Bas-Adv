import argparse   # Parse command-line arguments
import requests   # Make HTTP requests


def download_content(url, output):
    """
    Download text content from a URL and save to a file.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad responses

        with open(output, 'w', encoding='utf-8') as file:
            file.write(response.text)

        print(f"Saved content to {output}")

    except requests.exceptions.RequestException as e:
        print(f"Download failed: {e}")


# Create CLI parser
parser = argparse.ArgumentParser(
    description="Simple CLI tool to download webpage content"
)

# Required positional argument → URL
parser.add_argument(
    "url",
    help="URL to download from",type=str
)

# Optional argument → -o / --output
parser.add_argument(
    "-o", "--output",
    default="output.txt",  # default file if not provided
    help="Output file name (default: output.txt)"
)

# Parse arguments
args = parser.parse_args()

# Call function
download_content(args.url, args.output)

# python main.py https://example.com output.txt  