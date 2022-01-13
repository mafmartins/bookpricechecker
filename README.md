# bookpricechecker
A simple python script to check prices on thebookdepository.com.

## Requirements

- Python >3.*

## How to use

1. Install requirements. `pip install -r requirements.txt`
2. Add `GMAIL_ADDRESS` and `GMAIL_PASSWORD` environment variables or add them in a new local_settings.py file.
3. Run the script: `python scrapper.py <url> <price_limit> <email>`

## Run it on a regular basis
To run this on a regular basis you can add it as a cronjob or use another kind of recurrent task worker to run the command.
