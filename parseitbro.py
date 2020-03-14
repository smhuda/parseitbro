import pandas as pd
import datetime
from ipaddress import ip_address
from jinja2 import Environment, FileSystemLoader

# Use current date and time module
now = datetime.datetime.now()
x = now.strftime("%Y-%m-%d %H:%M:%S")
print "\n"                                                                
print "##########      Author: Syed Huda      ##########"          
print "##########      Script: Parse it bro!  ##########"
print "##########      Version: v0.1          ##########"
print '---------\t'+x
print "\n"
# Settings
LOGFILE_NAME = file(raw_input("Enter filename: "), 'r')
OUTPUT_REPORT = x+ '_report.html'

# Get report template
templates = Environment(loader=FileSystemLoader('.'))
report_template = templates.get_template('report_template.html')

# Load tab delimited logfile ignoring lines starting with a #
df = pd.read_csv(LOGFILE_NAME, delimiter='\t', header=None, comment='#', encoding='utf-8')

# Gather stats
content_types = df[26].value_counts()
browser_os = df[11].value_counts()
hosts = df[8].value_counts()
ips1 = df[2].value_counts()
ips2 = df[4].value_counts()
ports = df[5].value_counts()

# Pass stats to template to render and write to output file
report_template.stream(
    filename=LOGFILE_NAME,
    df=df,
    browsers_table=browser_os.to_frame('count'),
    ip1_table=ips1.to_frame('count'),
    ip2_table=ips2.to_frame('count'),
    port_table=ports.to_frame('count'),
    host_table=hosts.to_frame('count'),
    content_type_table=content_types.to_frame('count')
).dump(OUTPUT_REPORT)
print "\n"
print "Processing......."
print "Still processing......."
print "\n"
print "File: [["+OUTPUT_REPORT+ "]] has been parsed successfully!"
print "-------------------------------" 
