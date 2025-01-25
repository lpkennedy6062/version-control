import datetime

with open("../version.md", "w") as f:
	f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
