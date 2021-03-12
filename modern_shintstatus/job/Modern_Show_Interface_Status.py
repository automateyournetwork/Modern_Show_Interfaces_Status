# ----------------
# Copywrite
# ----------------
# Written by John Capobianco, March 2021 
# Copyright (c) 2021 John Capobianco

# ----------------
# Python
# ----------------
import sys
import time
import logging
import csv
import json

# ----------------
# Jinja2
# ----------------
from jinja2 import Environment, FileSystemLoader
template_dir = '../templates'
env = Environment(loader=FileSystemLoader(template_dir))

# ----------------
# Import pyATS and the pyATS Library
# ----------------
from genie.testbed import load
from pyats.log.utils import banner

# Get logger for script
log = logging.getLogger(__name__)

# ----------------
# Template sources
# ----------------
csv_template = env.get_template('show_int_status_csv.j2')
md_template = env.get_template('show_int_status_md.j2')
html_template = env.get_template('show_int_status_html.j2')

# ----------------
# Enable logger
# ----------------
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')
log = logging.getLogger(__name__)

# ----------------
# Load the testbed
# ----------------
log.info(banner("Loading testbed"))
testbed = load('../testbed/3850.yaml')
log.info("\nPASS: Successfully loaded testbed '{}'\n".format(testbed.name))

# --------------------------
# Connect to device 3850
# --------------------------
log.info(banner("Connect to device '3850'"))
device = testbed.devices['3850']
device.connect(via='cli')
log.info("\nPASS: Successfully connected to device '3850'\n")

# ---------------------------------------
# Execute parser to show interface status
# ---------------------------------------
log.info(banner("Executing parser to get show interface status and create documentation..."))
parsed_show_int_status = device.parse("show interfaces status")

# ---------------------------------------
# Template Results
# ---------------------------------------
output_from_parsed_csv_template = csv_template.render(to_parse_interfaces=parsed_show_int_status['interfaces'])
output_from_parsed_md_template = md_template.render(to_parse_interfaces=parsed_show_int_status['interfaces'])
output_from_parsed_html_template = html_template.render(to_parse_interfaces=parsed_show_int_status['interfaces'])

# ---------------------------------------
# Create Files
# ---------------------------------------
with open("../output/show_int_status_csv.csv", "w") as fh:
    fh.write(output_from_parsed_csv_template)

with open("../output/show_int_status_md.md", "w") as fh:
    fh.write(output_from_parsed_md_template)

with open("../output/show_int_status_html.html", "w") as fh:
    fh.write(output_from_parsed_html_template)