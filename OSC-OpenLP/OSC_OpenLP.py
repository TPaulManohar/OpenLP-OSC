# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#	OSC-OpenLP-API						    #
#	A bridge between Open Sound Control (OSC) and REST APIs     #
#	Office Hours Global Community Project                       #
#	Created and maintained by Paul - India.                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#OSC variables & libraries
from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import osc_message_builder
from pythonosc import udp_client 
from pythonosc import osc_bundle
from pythonosc import osc_bundle_builder

#Argument management
import argparse

#system
import sys

#REST
import requests
import json

# Socket for Machine IP
import socket


# Enter the OpenLP Server IP along with 4316
Openlpserver = "http://192.168.4.201:4316"

#GET Request
#OpenLP - Service New
def serviceNew(unused_addr, *args):
	print("Received info for GET Request for Service New")
	# OpenLP Service item
	url = "/api/v2/service/new"
	response = requests.get(Openlpserver + url)

	#if a file name was provided, save the response to disk and notify via OSC
	if(response.status_code == 204):
		osc_str = "/osc/openlp/service_new"
		client.send_message(osc_str, 1)
	#otherwise, send the entire response via OSC
	else:
		print("Sending response via OSC")
		osc_str = "/osc/openlp/service_new"
		client.send_message(osc_str, 0)

#OpenLP - Service List
def serviceList(unused_addr, stringdata):
	print("Received info for GET Request for Service List")
	# OpenLP Service item
	url = "/api/v2/service/items"
	response = requests.get(Openlpserver + url)
	#if a file name was provided, save the response to disk and notify via OSC
	if(response.status_code == 200):
		data = response.json()
		for items in data:
			filtered_data = (items['title'])
			#plain_text = filtered_data.encode('utf-8').decode('unicode_escape')
			json_str = json.dumps(plain_text)	
		osc_str = "/osc/openlp/service_list"
		client.send_message(osc_str, [json_str])
	else:
	 print(f"Request failed with status code: {response.status_code}")

#POST Request
#OpenLP - Service Item Next Slide
def nextSlide(unused_addr, url):
	print("Received info for POST request for Next Slide")
	url = "/api/v2/controller/progress"
	body = { "action": "next" }
	reply = requests.post(Openlpserver + url, json = body)

	osc_str = "/osc/openlp/next_slide"
	client.send_message(osc_str, 0)

#OpenLP - Service Item Previous Slide
def previousSlide(unused_addr, url):
	print("Received info for POST request for Previous Slide")
	url = "/api/v2/controller/progress"
	body = { "action": "previous" }
	reply = requests.post(Openlpserver + url, json = body)

	osc_str = "/osc/openlp/previous_slide"
	client.send_message(osc_str, 0)

#OpenLP - Service Next
def nextService(unused_addr, url):
	print("Received info for POST request for Next Service")
	url = "/api/v2/service/progress"
	body = { "action": "next" }
	reply = requests.post(Openlpserver + url, json = body)


	osc_str = "/osc/openlp/next_service"
	client.send_message(osc_str, 0)

#OpenLP - Service Previous
def previousService(unused_addr, url):
	print("Received info for POST request for Previous Service")
	url = "/api/v2/service/progress"
	body = { "action": "previous" }
	reply = requests.post(Openlpserver + url, json = body)

	osc_str = "/osc/openlp/previous_service"
	client.send_message(osc_str, 0)

#OpenLP - Clear Live
def clearLive(unused_addr, url):
	print("Received info for POST request for Clear Live")
	url = "/api/v2/controller/clear/live"
	reply = requests.post(Openlpserver + url)


	osc_str = "/osc/openlp/clear_live"
	client.send_message(osc_str, 0)

#OpenLP - Preview Live
def clearPreview(unused_addr, url):
	print("Received info for POST request for Clear Preview")
	url = "/api/v2/controller/clear/preview"
	reply = requests.post(Openlpserver + url)

	osc_str = "/osc/openlp/clear_preview"
	client.send_message(osc_str, 0)

#OpenLP - Display Hide
def displayHide(unused_addr, url):
	print("Received info for POST request for Display Hide Screen")
	url = "/api/v2/core/display"
	body = { "display" : "hide" }
	reply = requests.post(Openlpserver + url, json = body)

	osc_str = "/osc/openlp/display_hide"
	client.send_message(osc_str, 0)

#OpenLP - Display Show
def displayShow(unused_addr, url):
	print("Received info for POST request for Display Show Screen")
	url = "/api/v2/core/display"
	body = { "display" : "show" }
	reply = requests.post(Openlpserver + url, json = body)

	osc_str = "/osc/openlp/display_show"
	client.send_message(osc_str, 0)

#OpenLP - Display Blank
def displayBlank(unused_addr, url):
	print("Received info for POST request for Display Blank Screen")
	url = "/api/v2/core/display"
	body = { "display" : "blank" }
	reply = requests.post(Openlpserver + url, json = body)

	osc_str = "/osc/openlp/display_blank"
	client.send_message(osc_str, 0)

#OpenLP - Display Theme
def displayTheme(unused_addr, url):
	print("Received info for POST request for Display Theme")
	url = "/api/v2/core/display"
	body = { "display" : "theme" }
	reply = requests.post(Openlpserver + url, json = body)

	osc_str = "/osc/openlp/display_theme"
	client.send_message(osc_str, 0)

#OpenLP - Display Desktop
def displayDesktop(unused_addr, url):
	print("Received info for POST request for Display Desktop Screen")
	url = "/api/v2/core/display"
	body = { "display" : "Desktop" }
	reply = requests.post(Openlpserver + url, json = body)

	osc_str = "/osc/openlp/display_desktop"
	client.send_message(osc_str, 0)


#Main execution script--------------------------------------
if __name__ == "__main__":

	#Greeting
	print("Welcome to OSC-OpenLP-API")
	print("Created by Paul")
	print("This program establishes a bidirectional OSC interface with OpenLP APIs")
	print()


	#OSC Setup
	hostname = socket.gethostname()
	
	# Get the IP address associated with the hostname
	ip_address = socket.gethostbyname(hostname)
	
	print(f"\n The IP address of the system is {ip_address}")

	print("OSC Message RecevingPort: 1234 \n 7050 (SendingPort)")
	
	send_port = 1234
	receive_port = 4318

	#create the osc sending client
	client = udp_client.SimpleUDPClient(ip_address,send_port)

	#catches OSC messages
	dispatcher = dispatcher.Dispatcher()

	#map functions here:
	dispatcher.map("/osc/openlp/service_new", serviceNew)
	dispatcher.map("/osc/openlp/service_list", serviceList)
	dispatcher.map("/osc/openlp/next_slide", nextSlide)
	dispatcher.map("/osc/openlp/previous_slide", previousSlide)
	dispatcher.map("/osc/openlp/next_service", nextService)
	dispatcher.map("/osc/openlp/previous_service", previousService)
	dispatcher.map("/osc/openlp/clear_live", clearLive)
	dispatcher.map("/osc/openlp/clear_preview", clearPreview)	
	dispatcher.map("/osc/openlp/display_hide", displayHide)	
	dispatcher.map("/osc/openlp/display_show", displayShow)
	dispatcher.map("/osc/openlp/display_blank", displayBlank)
	dispatcher.map("/osc/openlp/display_theme", displayTheme)
	dispatcher.map("/osc/openlp/display_desktop", displayDesktop)
	
	
	#set up server to listen for osc messages
	server = osc_server.ThreadingOSCUDPServer((ip_address,receive_port),dispatcher)

	#Print the info
	#sys.stdout.write("OpenLP Server: ")
	#sys.stdout.write(openlp_server_ip + openlp_server_port )
	#sys.stdout.write('\n')
	sys.stdout.write("Opened Client on: ")
	sys.stdout.write(ip_address)
	sys.stdout.write(":")
	sys.stdout.write(str(send_port))
	sys.stdout.write('\n')
	sys.stdout.write("Listening on: ")
	sys.stdout.write(str(receive_port))
	sys.stdout.write('\n')

	print()

	#begin the infinite loop
	server.serve_forever()
