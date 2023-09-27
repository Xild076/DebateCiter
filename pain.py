import tkinter as tk
from tkinter import Entry, Button, Label, Text
from bs4 import BeautifulSoup
import requests
from dateutil import parser as date_parser
import datetime

def analyze_article():
    result_label.delete('1.0', tk.END)
    try:
        url = url_entry.get()
        name = author_entry.get()
        date_str = date_entry.get()
        occupations = occupations_entry.get()
        publisher = publisher_entry.get()
        ur_alias = alias_entry.get()

        # Download the web page content using requests
        response = requests.get(url)
        html_content = response.text

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract the article title
        article_title = soup.title.string if soup.title else "No Title Found"

        # Parse the date using dateutil.parser
        try:
            article_date = date_parser.parse(date_str)
            date_formatted = article_date.strftime("%m/%d/%y")
        except ValueError:
            date_formatted = "Invalid Date Format"

        current_date = datetime.datetime.now()
        current_date_str = current_date.strftime("%m/%d/%y")

        result_label.insert(
            tk.END,
            f"{name}, {occupations.split(',')[0]}, {date_str} [{name}; {occupations}; {publisher}; '{article_title}'; {date_formatted}; {url}; DOA: {current_date_str}] // {ur_alias}"
        )
    except Exception as e:
        # Provide an informative error message to the user
        result_label.insert(tk.END, f"Error: {str(e)}")


# Start the Tkinter main loop
root = tk.Tk()
root.title("Article Analyzer")

url_label = Label(root, text="URL:")
url_entry = Entry(root)
author_label = Label(root, text="Author:")
author_entry = Entry(root)
date_label = Label(root, text="Date [format: m/d/y]:")
date_entry = Entry(root)
occupations_label = Label(root, text="Occupations (split by commas):")
occupations_entry = Entry(root)
publisher_label = Label(root, text="Publisher:")
publisher_entry = Entry(root)
alias_label = Label(root, text="Your name/alias uwu:")
alias_entry = Entry(root)

analyze_button = Button(root, text="Analyze", command=analyze_article)

result_label = Text(root, wrap=tk.WORD, height=5, width=40)

url_label.grid(row=0, column=0)
url_entry.grid(row=0, column=1)
author_label.grid(row=1, column=0)
author_entry.grid(row=1, column=1)
date_label.grid(row=2, column=0)
date_entry.grid(row=2, column=1)
occupations_label.grid(row=3, column=0)
occupations_entry.grid(row=3, column=1)
publisher_label.grid(row=4, column=0)
publisher_entry.grid(row=4, column=1)
alias_label.grid(row=5, column=0)
alias_entry.grid(row=5, column=1)
analyze_button.grid(row=6, columnspan=2)
result_label.grid(row=7, columnspan=2)

root.mainloop()
