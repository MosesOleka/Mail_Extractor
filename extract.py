import requests

def extract_phone_numbers(text):
    phone_regex = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
    phone_numbers = re.findall(phone_regex, text)
    return phone_numbers

def extract_email_addresses(text):
    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    email_addresses = re.findall(email_regex, text)
    return email_addresses

def extract_links(text):
    link_regex = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    links = re.findall(link_regex, text)
    return links

def save_emails_to_file(emails):
    with open("extracted_emails.txt", "w") as file:
        file.write("\n".join(emails))

def main():
    url = input("Enter the website URL: ")
    response = requests.get(url)
    text = response.text

    phone_numbers = extract_phone_numbers(text)
    email_addresses = extract_email_addresses(text)
    links = extract_links(text)

    print("Phone Numbers:")
    for phone_number in phone_numbers:
        print(phone_number)

    print("Email Addresses:")
    for email_address in email_addresses:
        print(email_address)

    print("Links:")
    for link in links:
        print(link)

    save_emails_to_file(email_addresses)
    print("Extracted email addresses saved to 'extracted_emails.txt'.")

if __name__ == "_main_":
    main()



# #We import the necessary libraries. re is the regular expression library used for pattern matching, and requests is used to make HTTP requests to retrieve the website content.

# We define three functions: extract_phone_numbers, extract_email_addresses, and extract_links. These functions use regular expressions to find phone numbers, email addresses, and links in a given text.

# The save_emails_to_file function takes a list of email addresses and saves them to a file named "extracted_emails.txt" using the open function and the write method.

# The main function is the entry point of the program. It prompts the user to enter the website URL.

# The program makes an HTTP GET request to the provided URL using requests.get and assigns the response to the response variable.

# The text variable stores the content of the response in text format using response.text.

# We call the three extraction functions (extract_phone_numbers, extract_email_addresses, and extract_links) passing the text variable as input. These functions use regular expressions to find the desired information in the text.

# We iterate over the extracted phone numbers, email addresses, and links and print them on the console.

# We call the save_emails_to_file function and pass the extracted email addresses to it. This function writes the email addresses to a file named "extracted_emails.txt".

# Finally, we run the main function when the script is executed.

# To use the code, save it in a Python file (e.g., extract_info.py). Make sure you have the requests library installed (pip install requests). Then, run the script, enter the website URL when prompted, and it will extract the phone numbers, email addresses, and links from the website. The extracted email addresses will be saved to a file named extracted_emails.txt.