                                                                                                           
![Capturef](https://github.com/user-attachments/assets/dde5ed04-be7e-49f7-b871-80b576b62ba4)
                                                                       
                    NOTE! : I'M NOT RESPONSIBLE FOR ANY ILLEGAL USAGE.
                    CODED BY : Black-Crypto-Gif
                    VERSION : 1.0

# Email Scraper Application

This project is a **GUI-based email scraper** built with **Python** using the `tkinter` library for the graphical interface and **Selenium** for web scraping. It includes features such as email extraction, validation, IP address retrieval, and CSV export. The program runs in a multi-threaded environment and allows customizable scraping delays.

---

## Features

- **Load URLs**: Load a text file containing a list of websites to scrape.
- **Email Extraction**: Extract and validate email addresses from the provided websites.
- **IP Address Retrieval**: Extract and display the IP address of the scanned website.
- **Progress Tracking**: Visualize progress using a progress bar.
- **Save Emails**: Export the list of emails into a CSV file.
- **Theme Toggle**: Switch between light and dark modes.
- **Customizable Delays**: Set minimum and maximum delays for scraping operations.
- **Logs**: View detailed logs for scanning and validation in separate log boxes.
- **Clear Logs**: Clear all logs with a single click.
- **Tooltip Support**: Hover over buttons for helpful tips about their functions.

---

## Prerequisites

Ensure you have the following installed:

- **Python 3.7+**
- **Google Chrome**
- **ChromeDriver** compatible with your Chrome version
- **Selenium** (`pip install selenium`)

---

## Installation

1. Clone this repository or download the source code.
2. Install required Python packages:
   ```bash
   pip install selenium
   ```
3. Place the `chromedriver` executable in your system's PATH or in the project directory.

---

## Usage

1. Run the application:
   ```bash
   python email_scraper.py
   ```
2. Use the following controls within the GUI:

   - **Load Websites File**: Upload a `.txt` file containing URLs (one URL per line).
   - **Set Delays**: Adjust the minimum and maximum delay (in seconds) for scraping.
   - **Start Scraping**: Begin the email extraction process.
   - **Save Emails**: Export the collected email addresses into a `.csv` file.
   - **Clear Logs**: Clear the displayed scanning and validation logs.
   - **Toggle Theme**: Switch between light and dark themes.

---

## File Structure

- **Main Script**: Contains the GUI and all core functionalities.
- **Logs**: Separated into scanning logs (URL/IP-related) and validation logs (email-related).
- **Settings**: Adjustable delays for rate-limiting the scraping process.

---

## Key Functions

### `is_valid_email(email)`
Validates email addresses using a regular expression.

### `get_ip_address(url)`
Extracts the IP address of a given URL.

### `scrape_websites_from_file(file_path, delay_range)`
Extracts email addresses from a list of websites, validates them, and retrieves IP addresses.

### `save_emails_to_csv(emails)`
Saves a list of emails to a CSV file.

### `log_message(message, log_type, log_area)`
Logs messages with color-coded types (info, success, warning, error).

### `toggle_theme()`
Switches between light and dark themes for the GUI.

---

## Screenshots

![Capture](https://github.com/user-attachments/assets/f104da33-7cbf-43df-b78e-84c9fbeebeec)


- **Main Window**: 
  - Control buttons for loading files, saving emails, and clearing logs.
  - Progress bar and log boxes for real-time updates.
- **Settings Section**:
  - Input fields for customizing scraping delays.
- **Logs**: 
  - Separate boxes for scanning and validation logs.

![fffff](https://github.com/user-attachments/assets/4f19633a-38d2-4ffc-8b05-dd639b818c2a)


---

## Notes

- Ensure the URLs in your input file are valid and accessible.
- Avoid setting very short delays to prevent server bans or blocks.
- If ChromeDriver is not properly set up, the script will fail to launch.

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it as needed.

---

## Acknowledgments

Special thanks to the open-source community for providing amazing tools like Selenium and Tkinter!


## License
This project is licensed under the MIT License. See the LICENSE file for details.



