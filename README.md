# update-data
This is a set of Python scripts aimed at image manipulation, information updates, sending automatic PDF reports and performing system health checks. When relevant, they include user input (i.e. declaring email addresses, file location, etc.) but for each of these inputs there is also a commented code to use with fixed values.

<h2>changeImage.py </h2>
This script opens a list of images in a given directory and converts them to a 640 x 480, RGB, JPEG format version. Also included is an alternative version where the user inputs the width/height and format.

<h2>emails.py </h2>
This is a module for generating and sending emails with and without attachments. It is used in **report_email.py** and **health_check.py**.

<h2>health_check.py</h2>
This script reports an error via email if:
- CPU usage is over 80%
- Available disk space is lower than 20%
- Available memory is less than 500 MB
- The localname 'localhost' cannot be resolved to '127.0.0.1'

<h2>report_email.py</h2>
This script sends a report of the data uploaded with the **run.py** script. 

<h2>reports.py</h2>
This is a module that assists **report_email** in generating the report.

<h2>run.py</h2>
This script posts JSON information to a Django framework website. The fields can be customized.

<h2>supplier_image_upload.py</h2>
This script uploads images locally using the Python requests module.

## Usage ##

In the host environment there should be a running server with a basic Django website. This is part of the Google IT Automation certificate where the website is a online fruit shop. As such, some functionality is specific to this website (i.e. the valid JSON fields to upload the information). Everything in the code can be change to reflect other situations. A typical usage would be as follows:
1. changeImage.py in order to convert images to the correct format/size.
2. supplier_image_upload.py to upload the images.
3. run.py to upload the JSON information to the Django framework.
4. report_email.py to send a report of what's been uploaded.
5. health_check.py with a Cron Job to perform periodic checks.
6. Relax and enjoy life while the scripts take care of things.

