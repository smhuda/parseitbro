# Parse it bro! 
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## What does it do?
 The parsing takes place in from the formatting of the bro logs provided exported to HTML format. Further to the parsing this data from raw format of these logs, an analysis of these logs has been a part of this project and research. The analysis include the count of public and private IP adddresses, active IP addresses and what country they belong to. It also includes the most commonly repeated domain in the logs and count of its occurence. After the counting top domains that have an occurence in the logs, top 15 are mentioned in this project revealing how many of them are active on a plain HTTP or a Secure HTTPS connection. From MAC addresses, the NIC manufacturers are also analysed and listed through the parsing script.

## Dependandices

```shell
pip install pandas
```

## Usage
```shell
python parseitbro.py
```

## Want to know more about this project?
I have written a full lenght project description describing how I created it and how it exactly works. If it interests you, you can read up on the project [here](https://smhuda.com/projects/bro-log-parsing-and-analysis)
