# Website Crawler

## Overview

The Website Crawler script is designed for penetration testing, specifically for crawling and identifying all links within a target website. The script utilizes Python libraries such as `requests`, `re`, and `urllib.parse` for making HTTP requests, extracting links, and URL parsing.

## Dependencies

- `requests`: For making HTTP requests.
- `re`: For using regular expressions.
- `urllib.parse`: For URL parsing and manipulation.

## Usage

The script is intended to be run from the command line. It requires the target URL to start the crawling process.

## Functions

### `extract_links_from(url)`

- Extracts all href links from the given URL.
- Parameters:
  - `url` (str): The URL from which to extract links.
- Returns:
  - `list`: A list of extracted links.

### `crawl(url)`

- Recursively crawls the target URL to discover all linked pages.
- Parameters:
  - `url` (str): The URL to start crawling from.

## Example Usage

To run the script, use the following command:

```bash
python website_crawler.py
```

### Notes

1. Ensure that you have the required dependencies installed.
2. Use responsibly and with permission on target websites.
3. The script can be enhanced by adding more functionalities such as identifying forms and checking for vulnerabilities.


# Website Crawler for Directory Discovery

## Overview

The Website Crawler for Directory Discovery script is designed for penetration testing, specifically for discovering subdomains and directories within a target website. The script utilizes Python's `requests` library to make HTTP requests and identify valid subdomains and directories.

## Dependencies

- `requests`: For making HTTP requests.

## Usage

The script is intended to be run from the command line. It requires the target URL, a list of potential subdomains, and a list of potential directories to check.

## Input Files

- `subdomains.list`: A file containing a list of potential subdomains.
- `file_directory_word.list`: A file containing a list of potential directories.

## Functions

### `request(url)`

- Sends a GET request to the specified URL.
- Parameters:
  - `url` (str): The URL to send the request to.
- Returns:
  - `requests.Response`: The response object if the request is successful, otherwise None.

### `discover_subdomain()`

- Reads the `subdomains.list` file and checks each subdomain for validity.
- Adds discovered subdomains to the `discovered_subdomains` list.
- Prints each discovered subdomain.

### `discover_directory()`

- Reads the `file_directory_word.list` file and checks each directory for validity.
- Adds discovered directories to the `discovered_subdomains` list.
- Prints each discovered directory.

## Example Usage

To run the script, use the following command:

```bash
python directory_crawler.py
```

### Notes

1. Ensure that you have the required dependencies installed.
2. Use responsibly and with permission on target websites.
3. The script can be enhanced by adding more functionalities such as multi-threading for faster discovery and more comprehensive error handling.


# Login Guessing Script

## Overview

The Login Guessing script is designed for penetration testing, specifically for guessing login credentials by attempting to brute-force the password field. The script utilizes Python's `requests` library to send POST requests to the target login URL.

## Dependencies

- `requests`: For making HTTP requests.

## Usage

The script is intended to be run from the command line. It requires the target URL and a list of potential passwords to test.

## Input Files

- `subdomains.list`: A file containing a list of potential passwords.

## Script Details

### Variables

- `target_url`: The URL of the login page to test.
- `data_dic`: A dictionary containing the login form data. Adjust the keys to match the names of the form fields in the target login page.

### Script Logic

1. Open the `subdomains.list` file and read each potential password.
2. For each password, update the `data_dic` dictionary with the current password.
3. Send a POST request to the target URL with the updated form data.
4. Check the response content for a specific word or phrase that indicates a failed login attempt.
5. If the specific word or phrase is not found, print the discovered password and exit the script.

## Example Usage

To run the script, use the following command:

```bash
python login_guesser.py
```


### Notes

1. Ensure that you have the required dependencies installed.
2. Use responsibly and with permission on target websites.
3. Adjust the data_dic dictionary keys to match the form fields of the target login page.
4. Replace "[any_word_that is on failed page]" with the actual word or phrase that indicates a failed login attempt on the target website.
5. The script can be enhanced by adding more functionalities such as multi-threading for faster guessing and more comprehensive error handling.
