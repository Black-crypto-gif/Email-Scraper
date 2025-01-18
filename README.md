  
                                                                                                                        
                                                                                                                        
                                                                                  
                    NOTE! : I'M NOT RESPONSIBLE FOR ANY ILLEGAL USAGE.
                    CODED BY : Black-Crypto-Gif
                    VERSION : 1.0

# Email Scraper with GUI

## Overview
This project is a simple email scraper with a graphical user interface (GUI) built using Python and Tkinter. It uses Selenium for web scraping to extract valid email addresses from a given URL. The program is intended for educational purposes only. Please use it responsibly.

## Features
- **Logo Animation:** A colorful terminal logo displayed when the program starts.
- **Email Validation:** Ensures extracted email addresses are valid.
- **Web Scraping:** Uses Selenium to scrape email addresses from web pages.
- **Graphical User Interface:** Simple Tkinter-based interface for ease of use.
- **Log Output:** Displays results and status messages in the GUI.

## Requirements
Before running the program, ensure you have the following installed:

1. Python 3.x
2. Selenium WebDriver
3. Google Chrome and ChromeDriver

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/Email-Scraper.git
   cd Email-Scraper
   ```
2. Install the required Python packages:
   ```bash
   pip install selenium
   ```
3. Download the ChromeDriver that matches your Chrome version from [here](https://chromedriver.chromium.org/downloads).
4. Place the ChromeDriver executable in your system PATH or in the project directory.

## Usage
1. Run the program:
   ```bash
   python email_scraper.py
   ```
2. Enter the URL in the text field and click "Scrape Emails."
3. View extracted emails in the log box.

## Program Walkthrough


### Email Validation
The `is_valid_email` function checks if the extracted email addresses match a valid email format using regular expressions.

### Email Scraping
The `scrape_emails_from_url` function:
- Launches ChromeDriver using Selenium.
- Extracts email addresses using regex from the page source.
- Validates and removes duplicates from the extracted emails.

### Graphical User Interface
- Built using Tkinter for simplicity and compatibility.
- Features a text field for entering the URL and a button to start scraping.
- Displays logs and results in a scrollable text box.

## File Structure
- `email_scraper.py`: Main Python script.
- `README.md`: Documentation (this file).

## Screenshots
### GUI Overview

![Capture](https://github.com/user-attachments/assets/41481b7a-52d6-44ba-8965-b9a4709b25ac)

### Scraping in Action

![fffff](https://github.com/user-attachments/assets/425b2094-31ba-4fbd-ab45-4372391383f2)


## Notes
- The program is for educational purposes. The developer is not responsible for any misuse.
- Ensure compliance with website terms of service and legal guidelines when using web scraping.

## Author
Coded by Black-Crypto-gif

## License
This project is licensed under the MIT License. See the LICENSE file for details.



