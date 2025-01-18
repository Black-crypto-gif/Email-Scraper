import tkinter as tk
from tkinter import filedialog, ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import csv
import random
import threading
import socket

# Email validation function
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

# Extract IP address from URL
def get_ip_address(url):
    try:
        hostname = re.search(r"https?://(www\.)?([^/]+)", url).group(2)
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        return f"Error: {e}"

# Save emails to a CSV file
def save_emails_to_csv(emails):
    file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                             filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Email Address"])
            for email in emails:
                writer.writerow([email])
        log_message("Emails saved to " + file_path, "info")

# Log message with color coding
def log_message(message, log_type="info", log_area="general"):
    colors = {"info": "blue", "success": "green", "warning": "orange", "error": "red"}
    color = colors.get(log_type, "black")
    target_box = validation_log_box if log_area == "validation" else scanning_log_box
    target_box.tag_config(log_type, foreground=color)
    target_box.insert(tk.END, message + "\n", log_type)
    target_box.see(tk.END)

# Update progress bar
def update_progress(progress):
    progress_var.set(progress)
    progress_bar.update()

# Scraping function
def scrape_websites_from_file(file_path, delay_range):
    try:
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file.readlines() if line.strip()]
    except Exception as e:
        log_message(f"Error loading file: {str(e)}", "error", "validation")
        return

    driver = webdriver.Chrome()
    emails = set()
    total_urls = len(urls)

    for index, url in enumerate(urls, start=1):
        log_message(f"Scanning URL {index}/{total_urls}: {url}", "info", "scanning")
        try:
            # Get IP Address
            ip_address = get_ip_address(url)
            log_message(f"IP Address: {ip_address}", "info", "scanning")

            driver.get(url)
            time.sleep(random.uniform(*delay_range))  # Rate limiting

            # Extract emails from the page source
            page_emails = set(re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', driver.page_source))
            valid_emails = {email for email in page_emails if is_valid_email(email)}
            emails.update(valid_emails)

            for email in valid_emails:
                log_message(f"Email found: {email}", "success", "validation")

        except Exception as e:
            log_message(f"Error scanning URL {url}: {str(e)}", "error", "scanning")

        update_progress((index / total_urls) * 100)

    driver.quit()
    update_progress(100)
    log_message("Scanning completed.", "success", "scanning")

    if emails:
        log_message("\nTotal Emails Found:", "info", "validation")
        for email in emails:
            log_message(email, "info", "validation")
    else:
        log_message("No emails found.", "warning", "validation")

    return emails

# Start scraping in a separate thread
def start_scraping():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        log_message("No file selected.", "warning", "validation")
        return

    delay_range = (min_delay.get(), max_delay.get())

    def run():
        progress_var.set(0)
        emails = scrape_websites_from_file(file_path, delay_range)
        if emails:
            emails_found.extend(emails)

    threading.Thread(target=run).start()

# Clear logs
def clear_logs():
    scanning_log_box.delete(1.0, tk.END)
    validation_log_box.delete(1.0, tk.END)

# Dark/Light Mode Toggle
def toggle_theme():
    current_theme = root.tk.call("ttk::style", "theme", "use")
    new_theme = "clam" if current_theme == "alt" else "alt"
    root.tk.call("ttk::style", "theme", "use", new_theme)

# Add Tooltip
def add_tooltip(widget, text):
    tooltip = tk.Toplevel(widget)
    tooltip.wm_overrideredirect(True)
    tooltip.wm_geometry("1x1+0+0")
    tooltip_label = ttk.Label(tooltip, text=text, relief="solid", padding=(5, 2))
    tooltip_label.pack()

    def enter(event):
        tooltip.geometry(f"+{event.x_root+10}+{event.y_root+10}")
        tooltip_label.update_idletasks()
        tooltip.deiconify()

    def leave(event):
        tooltip.withdraw()

    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", leave)

# GUI setup
root = tk.Tk()
root.title("Email Scraper")
root.geometry("1000x800")

# Notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

# Main Frame
frame = ttk.Frame(notebook, padding="10")
notebook.add(frame, text="Scraper")

# Input Section
input_frame = ttk.LabelFrame(frame, text="Scraper Controls")
input_frame.pack(fill=tk.X, padx=5, pady=5)

load_button = ttk.Button(input_frame, text="Load Websites File", command=start_scraping)
load_button.pack(side=tk.LEFT, padx=5, pady=5)
add_tooltip(load_button, "Load a text file containing URLs.")

save_button = ttk.Button(input_frame, text="Save Emails", command=lambda: save_emails_to_csv(emails_found))
save_button.pack(side=tk.LEFT, padx=5, pady=5)
add_tooltip(save_button, "Save all extracted emails to a CSV file.")

clear_button = ttk.Button(input_frame, text="Clear Logs", command=clear_logs)
clear_button.pack(side=tk.LEFT, padx=5, pady=5)
add_tooltip(clear_button, "Clear the scanning and validation logs.")

# Dark/Light Mode Toggle
theme_button = ttk.Button(input_frame, text="Toggle Theme", command=toggle_theme)
theme_button.pack(side=tk.LEFT, padx=5, pady=5)
add_tooltip(theme_button, "Switch between light and dark themes.")

# Delay Settings
settings_frame = ttk.LabelFrame(frame, text="Settings")
settings_frame.pack(fill=tk.X, padx=5, pady=5)

min_delay_label = ttk.Label(settings_frame, text="Min Delay (s):")
min_delay_label.pack(side=tk.LEFT, padx=5, pady=5)
min_delay = tk.DoubleVar(value=2)
min_delay_entry = ttk.Entry(settings_frame, textvariable=min_delay, width=5)
min_delay_entry.pack(side=tk.LEFT, padx=5, pady=5)

max_delay_label = ttk.Label(settings_frame, text="Max Delay (s):")
max_delay_label.pack(side=tk.LEFT, padx=5, pady=5)
max_delay = tk.DoubleVar(value=5)
max_delay_entry = ttk.Entry(settings_frame, textvariable=max_delay, width=5)
max_delay_entry.pack(side=tk.LEFT, padx=5, pady=5)

# Progress Bar
progress_frame = ttk.LabelFrame(frame, text="Progress")
progress_frame.pack(fill=tk.X, padx=5, pady=5)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(progress_frame, variable=progress_var, maximum=100)
progress_bar.pack(fill=tk.X, padx=5, pady=5)

# Log Box Frame
log_frame = ttk.LabelFrame(frame, text="Logs")
log_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

log_box_splitter = ttk.PanedWindow(log_frame, orient=tk.HORIZONTAL)
log_box_splitter.pack(fill=tk.BOTH, expand=True)

# Scanning Log Box
scanning_log_frame = ttk.LabelFrame(log_box_splitter, text="Scanning Logs")
log_box_splitter.add(scanning_log_frame, weight=1)
scanning_log_box = tk.Text(scanning_log_frame, wrap=tk.WORD, height=20, width=50)
scanning_log_box.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Validation Log Box
validation_log_frame = ttk.LabelFrame(log_box_splitter, text="Validation Logs")
log_box_splitter.add(validation_log_frame, weight=1)
validation_log_box = tk.Text(validation_log_frame, wrap=tk.WORD, height=20, width=50)
validation_log_box.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
  # Add summary tab
summary_frame = ttk.Frame(notebook, padding="10")
notebook.add(summary_frame, text="Summary")
summary_label = ttk.Label(summary_frame, text="Summary will appear here after scraping.", anchor="center")
summary_label.pack(fill=tk.BOTH, expand=True)

    # Global list to store emails
emails_found = []

    # Start the main application loop
root.mainloop()
