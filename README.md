# MCAAC-Ticket-Request-Survey-Generator

Getting Started
To run the event survey generator script and create a Qualtrics survey to streamline MCAAC committee member ticket request submissions, the required input is an Excel file with the following columns (not named in the header, following the format linked in this repo): "event name", "date", "time", "link", "notes". This can be refactored in the script if the input changes (see lines 9-16, which parses the file and extracts the relevant data).
<img width="1384" height="125" alt="Screenshot 2025-09-01 at 9 23 34 pm" src="https://github.com/user-attachments/assets/5d2b58fb-990d-4262-8803-80e6d93c0958" />
After cloning, in the terminal inside the working directory of the repo, run the following:
python3 event_survey_generator.py [event info file]

The script will generate a QSF file named "Mondavi Center Spring Quarter Events for MCAAC.qsf" (or "name.qsf", depending on the name specified in the script at line 6).

Upload the QSF file to Qualtrics by accessing "Tools" > "Import / Export" > "Import Survey." This will generate a new Qualtrics survey project corresponding to the inputs provided:
<img width="950" height="789" alt="Screenshot 2025-09-01 at 9 24 42 pm" src="https://github.com/user-attachments/assets/cd5dab8c-d0fe-4843-81aa-faee96242338" />
The current UI of the survey follows the format:

page 1: required information collected per user (name, email, accessibility)

<img width="1010" height="769" alt="Screenshot 2025-09-01 at 9 25 35 pm" src="https://github.com/user-attachments/assets/94edd976-8b1c-44d1-b364-503c21b3bca0" />
page 2: select events of interest, request tickets per event

<img width="988" height="777" alt="Screenshot 2025-09-01 at 9 26 03 pm" src="https://github.com/user-attachments/assets/07d95609-fc18-4467-8e21-b756072a6254" />
page 3: rank events by priority
<img width="1372" height="728" alt="Screenshot 2025-09-01 at 9 26 25 pm" src="https://github.com/user-attachments/assets/17e5436d-293b-4ae7-8a04-d7e4b4953b01" />

The setup currently sends a confirmation email with user response values upon survey submission.

