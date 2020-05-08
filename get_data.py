# importing the requests library
import requests
import json
import csv
import os
# defining the api-endpoint
list_file = "stock_list.txt"
#url = "https://www.vndirect.com.vn/portal/ajax/listed/SearchHistoricalPriceForSymbol.shtml"
url = "https://www.vndirect.com.vn/portal/ajax/listed/DownloadReportForSymbol.shtml"
i=0

if not os.path.exists("feed.txt"):
	print("Can not find feed.txt")
else:
	file = open("feed.txt","r")
	feeds =  file.readlines()
	file.close()

	for line in feeds:
		i+=1
		print(i)

		line = line.split(",")
		symbol = line[0] #"VNM"
		sta_date = line[1]#"01/01/2019"
		end_date = line[2]#"02/01/2020"

		filename = "data/" + symbol + "_" + sta_date.replace("/", ".") + "_" + end_date.replace("/", ".") + ".csv"
		print("Processing....", line)
		if os.path.exists(filename):
			print("File exist...next!")
			continue

		# data to be sent to api
		data = {
			"model.downloadType":"$HP_DL_TYPE$",
			"pagingInfo.indexPage": 1,
			"searchMarketStatisticsView.symbol": symbol,
			"strFromDate": sta_date,
			"strToDate": end_date
		}

		# sending post request and saving response as response object
		r = requests.post(url=url, data=data)

		file1 = open(filename, "w")

		file1.write(r.text)
		print(r.text)
		file1.close()  # to change file access modes
		# extracting response text

print("Done!")