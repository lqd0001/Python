import csv
import requests
from urllib.parse import quote
status_dict = {"Website": "Status"}
def main():
    with open("./websites.txt", "r") as fr:
        for line in fr:
            website = line.strip()
            encoded_website = quote(website, safe=':/')
            print(website)
            try:
                status = requests.get(encoded_website).status_code
                status_dict[website] = "working" if status == 200 else "not working"
            except requests.exceptions.RequestException as e:
                status_dict[website] = "error: " + str(e)

    with open("website_status.csv", "w", newline="") as fw:
        csv_fieldnames = ["Website", "Status"]
        csv_writer = csv.DictWriter(fw, fieldnames=csv_fieldnames)

        csv_writer.writeheader()
        for website, status in status_dict.items():
            csv_writer.writerow({"Website": website, "Status": status})

if __name__ == "__main__":
    main()
