Information Gathering Tool

Project Overview

The Information Gathering Tool is a Python-based command-line tool that allows users to gather essential information about a given website. Upon execution, the tool fetches the website’s IP address, along with its geographical location and ISP details. The information is obtained using the ipinfo.io API and is presented in JSON format.

This tool can be useful for cybersecurity reconnaissance, allowing ethical hackers and security analysts to quickly obtain valuable information about the infrastructure of a website.

Table of Contents

Features
Technologies Used
Installation
Usage
Code Explanation
Limitations
Future Enhancements
License
Acknowledgments
Features

IP Address Resolution: Resolves the domain name of a website into its corresponding IP address.
Geolocation Information: Retrieves the geographical location (city, region, country) associated with the IP address.
ISP Information: Provides details about the Internet Service Provider (ISP) and organization associated with the IP address.
Command-Line Interface: The tool can be executed through the command line, making it easy to integrate into other cybersecurity workflows.
Technologies Used

Python: The primary programming language for this project.
socket: A Python library used to resolve a website's domain name to an IP address.
requests: A Python library for making HTTP requests to the ipinfo.io API to fetch geolocation and ISP details.
json: A Python library used to handle the JSON response from the API.
ipinfo.io API: The service used to retrieve information about an IP address, including location and ISP details.
Installation

1. Clone the Repository
First, clone this repository to your local machine using Git:

git clone https://github.com/kushisonu/information-gathering-tool.git
2. Install Dependencies
Ensure that Python is installed on your machine. Then, install the required Python libraries by running the following command:

pip install -r requirements.txt
Alternatively, you can install the libraries individually:

pip install requests
pip install socket
Usage

Run the Script
To use the tool, navigate to the project directory and execute the following command:
python infotool.py <website-url>
Example:

python infotool.py google.com
Output
The tool will return the IP address, location, and ISP information of the given website in a JSON format. For example:
{
    "ip": "172.217.10.46",
    "city": "Mountain View",
    "region": "California",
    "country": "US",
    "loc": "37.4056,-122.0775",
    "org": "AS15169 Google LLC"
}
Code Explanation

1. Importing Libraries
The script uses the following libraries:

import sys
import socket
import requests
import json
2. Command-Line Argument
The website URL is captured using the sys.argv function:

website_url = sys.argv[1]
3. Resolving IP Address
The socket.gethostbyname() function is used to resolve the IP address of the website:

ip_address = socket.gethostbyname(website_url)
4. Making the API Request
An HTTP GET request is made to the ipinfo.io API to retrieve the information:

response = requests.get(f'https://ipinfo.io/{ip_address}/json')
5. Parsing the Response
The JSON response from the API is parsed and displayed in a readable format:

data = response.json()
print(json.dumps(data, indent=4))
Limitations

API Rate Limits: The ipinfo.io API has rate limits for free-tier users. If the tool is used excessively, requests may be blocked.
Geolocation Accuracy: The geolocation returned may not always be 100% accurate, especially when websites use CDNs or cloud hosting.
Dependency on Active Internet Connection: The tool requires an internet connection to make requests to the API.
Limited Features: Currently, the tool only retrieves basic information like IP address, location, and ISP details. It doesn't include advanced features like WHOIS lookups or DNS queries.
Future Enhancements

WHOIS Data Retrieval: Add functionality to retrieve WHOIS registration information for websites.
DNS Lookups: Implement DNS lookup features to fetch additional records like A records, MX records, and CNAME records.
Error Handling Improvements: Enhance error handling to manage API errors, invalid URLs, and timeouts.
GUI Version: Develop a Graphical User Interface (GUI) for non-technical users to interact with the tool.
Integration with Other APIs: Expand the tool's capabilities by integrating with other useful APIs like Shodan and Censys for more detailed information.
License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

ipinfo.io: For providing the geolocation API used to gather location and ISP information.
Python Community: For the comprehensive and well-documented libraries like requests, socket, and json that made this project possible.
GitHub: For providing an open-source platform to share this project with others.
