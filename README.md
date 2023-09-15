# OpenLP-OSC

OpenLP-OSC Project that can leads to use with OSC(Open Sound Control). This simple python application to bridge Open Sound Control (OSC) to OpenLP - APIs


# Setup
Launch the application \
``pip3 install python-osc `` \
``pip3 install request `` 

``python3 <Program>`` \
and it tooks the System local IP. Then, send OSC command to the application. OSC command begins with /osc/openlp/

# TouchOSC Setup
TouchOSC OSC Connections Setup \
  Host: <Machine IP> \
  Send Port: 4318 \
  Receive Port: 1234 \
  ZeroConf: Default

# Commands to Send
/osc/openlp/service_new     - Create a new service \
/osc/openlp/service_list    - List the service items in the service \
/osc/openlp/next_slide      - Go to the specified slide \
/osc/openlp/previous_slide  - Go to the specified slide \
/osc/openlp/next_service    - Progress to the next or previous service item \
/osc/openlp/previous_service- Progress to the next or previous service item \
/osc/openlp/clear_live       - Clears a controller \
/osc/openlp/clear_preview    - Clears a controller \
/osc/openlp/display_hide     - Displays or hides the live view \
/osc/openlp/display_show     - Displays or hides the live view \
/osc/openlp/display_blank    - Displays or hides the live view \
/osc/openlp/display_theme    - Displays or hides the live view \
/osc/openlp/display_desktop  - Displays or hides the live view 


# OpenLP-HTTP-API Documentation
https://gitlab.com/openlp/wiki/-/wikis/Documentation/HTTP-API#service
