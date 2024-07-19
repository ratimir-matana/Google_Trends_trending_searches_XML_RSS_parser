# Google Trends - trending searches XML/RSS parser
# Google Trends URL: https://trends.google.com/trends/trendingsearches/daily?geo=US&hl=en-US
# RSS format: https://trends.google.com/trends/trendingsearches/daily/rss?geo=US
# Just copy data from RSS format in raw_data variable in module xml_data.py and then run script to get Python list of
# trending searches

import xml.etree.ElementTree as ET
import re
import xml_data


# Define a function to preprocess the XML data
def preprocess_xml_data(entry_data):
    # Replace problematic characters with entities
    entry_data = entry_data.replace(' & ', ' &amp; ')
    entry_data = entry_data.replace('&nbsp;', '&#160;')  # Character: (space)
    entry_data = entry_data.replace('&apos;', '&#39;')  # Character: '
    # Add more replacements as needed for other problematic characters
    # Ensure &amp; remains unchanged and properly handle & characters
    modified_data = re.sub(r'&(?!amp;|lt;|gt;|quot;|apos;|#160;|#39;)', '&amp;', entry_data)
    return modified_data


def main():
    # Preprocess the XML data
    preprocessed_xml_data = preprocess_xml_data(xml_data.raw_data)

    # Empty list
    end_result = []

    # Parse the preprocessed XML data
    try:
        root = ET.fromstring(preprocessed_xml_data)
        # Process the XML tree here
        # For example:
        items = root.findall('.//item')
        for item in items:
            title = item.find('title').text
            # print(title)
            end_result.append(title)
        print(end_result)

    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")


if __name__ == "__main__":
    main()
