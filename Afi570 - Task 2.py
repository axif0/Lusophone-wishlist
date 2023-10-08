import requests
import csv
import validators
import concurrent.futures

def get_status_code(url_site):
    """
    Send an HTTP GET request to the given URL and return the status code.

    Args:
        url_site (str): The URL to send the request to.

    Returns:
        tuple: A tuple containing the URL and the HTTP status code or "error" if the request fails.
    """
    try:
        response = requests.get(url_site)
        return url_site, response.status_code
    except requests.exceptions.RequestException as e:
        return url_site, "error"

def read_urls_from_csv(csv_file):
    """
    Read a list of valid URLs from a CSV file.

    Args:
        csv_file (str): The path to the CSV file containing the URLs.

    Returns:
        list: A list of URL strings.
    """
    valid_urls = []
    with open(csv_file, 'r', newline='') as file:
        urls_from_file = file.readlines()
    for url in urls_from_file:
        url = url.strip()
        if validators.url(url):
            valid_urls.append(url)
    return valid_urls

def save_output_to_file(output_file, status_code_results):
    """
    Save the status code results to a text file.

    Args:
        output_file (str): The path to the output text file.
        status_code_results (list): A list of tuples containing URL and status code.

    Returns:
        None
    """
    with open(output_file, 'w') as file:
        for url, status_code in status_code_results:
            file.write(f'({status_code}) {url}\n')

def main():
    """
    Main function to check the status codes of URLs from a CSV file.

    This function reads the CSV file, processes the URLs concurrently using a ThreadPoolExecutor,
    and prints the status codes for each URL.
    """
    # Specify the CSV file containing the URLs
    csv_file = 'urls.csv'

    # Read valid URLs from the CSV file
    valid_urls = read_urls_from_csv(csv_file)

    # Create a list to store the results of status code checks
    status_code_results = []

    # Use a ThreadPoolExecutor with a specified number of worker threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # Use executor.map to asynchronously process the URLs and retrieve status codes
        results = executor.map(get_status_code, valid_urls)

        # Iterate over the results to print status codes and store them
        for url, status_code in results:
            print(f'({status_code}) {url}')
            status_code_results.append((url, status_code))

    output_file = 'output.txt'
    save_output_to_file(output_file, status_code_results)

if __name__ == "__main__":
    # Call the main function when the script is executed
    main()
