import socket
import requests
import json

def get_ip_address(website_url):
    """Get the IP address of the given website."""
    try:
        ip = socket.gethostbyname(website_url)
        return ip
    except socket.gaierror:
        print("Error: Unable to resolve the domain.")
        return None

def get_location_info(ip):
    """Fetch location details using the IP address."""
    url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # Return JSON response
        else:
            print("Error: Unable to fetch location details.")
            return None
    except requests.RequestException:
        print("Error: Unable to connect to the API.")
        return None

def save_to_json(data, filename):
    """Save data to a JSON file."""
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"\nData saved to {filename}")

def main():
    """Main function to handle user input and execute the tool."""
    website = input("Enter website URL (without https://): ")
    
    ip = get_ip_address(website)
    if ip:
        print(f"\nIP Address of {website}: {ip}")
        
        location_info = get_location_info(ip)
        if location_info:
            print("\nLocation Information:")
            for key, value in location_info.items():
                print(f"{key}: {value}")

            # Save the result in a JSON file
            filename = f"{website.replace('.', '_')}_info.json"
            save_to_json(location_info, filename)

if __name__ == "__main__":
    main()

