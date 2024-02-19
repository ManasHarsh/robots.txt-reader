import requests

def fetch_robots_txt(url):
    try:    
        robots_url = "https://" + url.rstrip("/") + "/robots.txt"               
        response = requests.get(robots_url)
        
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to fetch robots.txt. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    website_url = input("Enter the website domain: ")
    robots_content = fetch_robots_txt(website_url)
    print("\nContents of robots.txt file:")
    print(robots_content)
