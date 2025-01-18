import tkinter
import customtkinter
import nmap 
import sqlite3
from sqlite3 import Error 
from datetime import datetime

customtkinter.set_appearance_mode( "System" )
customtkinter.set_default_color_theme( 'green' )

class PartABC( customtkinter.CTk ) :

    def __init__( self ) :
        super( ).__init__( )

        # define instance variables
        self.database = r'saspdemo.db'
        self.conn = self.create_connection( self.database )
        self.data = self.select_all_records( )

        # configure winodw
        self.title( "SASP EA Assignment - Part C By Group 4" )
        self.geometry( f"{1100} x {600} " )

        # configure grid layout ( 3 x 3 )
        self.grid_columnconfigure( 1, weight = 1)
        self.grid_columnconfigure( ( 2, 3 ), weight = 0 )
        self.grid_rowconfigure( ( 0, 1, 2 ), weight = 1 )

        # left sidebar text
        self.sidebar_frame = customtkinter.CTkFrame( self, width=140, corner_radius=0 )
        self.sidebar_frame.grid( row=0, column=0, rowspan=4, sticky='nsew' )
        self.sidebar_frame.grid_rowconfigure( 4, weight=1 )
        self.logo_label = customtkinter.CTkLabel( self.sidebar_frame, text = "LOVE & PEACE", font=customtkinter.CTkFont("Comic Sans MS", 20, ) )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # left sidebar window 1
        self.scan_network = customtkinter.CTkButton( self.sidebar_frame, 
                                                     text="Scan Network",
                                                     command = self.scan_network
                                                    )
        self.scan_network.grid(row=1, column=0, padx=20, pady=10)

        # left sidebar window 1
        self.save_btn = customtkinter.CTkButton(self.sidebar_frame, text = "Save", command = self.save_results )
        self.save_btn.grid(row=2, column=0, padx=20, pady=10)

        # Save Btn
        # self.save_button = customtkinter.CTkButton(self.sidebar_frame, text = "Save", command = self.save_results )
        # self.save_button.grid(row=4, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["System", "Light", "Dark"],
                                                                       command=self.change_appearance_mode_event,
                                                                       state = "disabled")
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["50%", "80%", "100%", "120%", "140%"],
                                                               command=self.change_scaling_event,
                                                               state = "disabled")
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create entry and button
        self.vip_entry = customtkinter.CTkEntry(self, placeholder_text = "Love Secret?" )
        self.vip_entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.vip_button = customtkinter.CTkButton(self, text = "PEACE" ,fg_color="transparent", 
                                                        border_width=2, text_color=("gray10", "#DCE4EE"),
                                                        command = self.vip_function )
        self.vip_button.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create text box
        self.textbox = customtkinter.CTkTextbox(self, width=650, height=200, corner_radius = 1, border_width=10, border_color='grey20', font=customtkinter.CTkFont( size=15, weight='bold' ) )
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), rowspan = 3, sticky="nsew")

        # Configure box
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, columnspan = 2 , padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.tabview.add( 'Scan Config' )
        self.tabview.add( 'Scanning History' )
        self.target_label = customtkinter.CTkLabel(self.tabview.tab( 'Scan Config' ), text = "Target IP : ")
        self.target_label.grid(row=0, column=0, padx=(20, 0), pady=(20, 5), sticky="ew")

        self.target_ipbox = customtkinter.CTkEntry(self.tabview.tab( 'Scan Config' ), placeholder_text = "IP address" )
        self.target_ipbox.grid(row=0, column=1, padx=(2,5), pady=(20, 10), sticky="ew")
        
        # Scan Options
        nmap_version_radio_var = customtkinter.StringVar( value = "off" )
        self.nmap_version_radio = customtkinter.CTkCheckBox(
                                                            self.tabview.tab( 'Scan Config' ), 
                                                            text="Nmap Version",
                                                            variable = nmap_version_radio_var,
                                                            onvalue = "on",
                                                            offvalue = "off"
                                                            )
        self.nmap_version_radio.grid(row=1, column=0, padx=(5,5), pady=(20, 10), sticky="n")

        number_of_host_radio_var = customtkinter.StringVar( value = "off" )
        self.number_of_host_radio = customtkinter.CTkCheckBox(
                                                        self.tabview.tab( 'Scan Config' ), 
                                                        text="Number of Hosts",
                                                        variable = number_of_host_radio_var,
                                                        onvalue = "on",
                                                        offvalue = "off"
                                                    )
        self.number_of_host_radio.grid(row=1, column=1, padx=(5,5), pady=(20, 10), sticky="n")


        ip_radio_var = customtkinter.StringVar( value = "off" )
        self.ip_radio = customtkinter.CTkCheckBox(
                                                    self.tabview.tab( 'Scan Config' ), 
                                                    text="IP addresses",
                                                    variable = ip_radio_var,
                                                    onvalue = "on",
                                                    offvalue = "off"
                                                )
        self.ip_radio.grid(row=2, column=0, padx=(5,5), pady=(20, 10), sticky="n")

        service_radio_var = customtkinter.StringVar( value = "off" )
        self.service_radio = customtkinter.CTkCheckBox(
                                                        self.tabview.tab( 'Scan Config' ), 
                                                        text="Running Service",
                                                        variable = service_radio_var,
                                                        onvalue = "on",
                                                        offvalue = "off"
                                                        )
        self.service_radio.grid(row=2, column=1, padx=(5,5), pady=(20, 10), sticky="n")

        os_radio_var = customtkinter.StringVar( value = "off" )
        self.os_radio = customtkinter.CTkCheckBox(
                                                    self.tabview.tab( 'Scan Config' ), 
                                                    text="OS Version",
                                                    variable = os_radio_var,
                                                    onvalue = "on",
                                                    offvalue = "off"
                                                    )
        self.os_radio.grid(row=3, column=0, padx=(5,5), pady=(20, 10), sticky="n")

        server_name_radio_var = customtkinter.StringVar( value = "off" )
        self.server_name_radio = customtkinter.CTkCheckBox(
                                                            self.tabview.tab( 'Scan Config' ), 
                                                            text="Server Name" ,
                                                            variable = server_name_radio_var,
                                                            onvalue = "on",
                                                            offvalue = "off")
        self.server_name_radio.grid(row=3, column=1, padx=(0,5), pady=(20, 10), sticky="n")

        # History Box
        self.display_button = customtkinter.CTkButton(
                                                        self.tabview.tab( 'Scanning History' ), 
                                                        text="Display History", 
                                                        command = self.display_to_text
                                                        #command = lambda: self.display_to_text( self.data ),
                                                    )
        self.display_button.grid(row=2, column=0, columnspan=1, padx=(50,10), pady=(20, 10), sticky="n")

        #clear Box
        self.clean_database_button = customtkinter.CTkButton(self.tabview.tab( 'Scanning History' ), text="Delete All Data", command= self.clean_database )
        self.clean_database_button.grid(row=4, column=0, columnspan=1, padx=(50,10), pady=(20, 10), sticky="n")


        # create remark frame
        self.remark_box = customtkinter.CTkTextbox(self)
        self.remark_box.grid(row=1, column=2, columnspan=2, rowspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.remark_box.insert( "0.0",
                                    "Remarks:\n"
                                    "Number of hosts:\nScan all the hosts in the target network.\n"
                                    "IP addresses:\nShows the IP addresses of the hosts.\n"
                                    "Running Service:\nShows hosts running service.\n"
                                    "OS Version:\nShows hosts OS Version\n"
                                    "Server name:\nServer name (If server was found)\n"
                                    "Nmap Version:\nShows Nmap version\n"
                              )


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def vip_function( self ) :
        vip = self.vip_entry.get()
        vip = vip.lower()
        if vip == "jack is so handsome!!!" :
            self.appearance_mode_optionemenu.configure( state = "normal" )
        elif vip == "jack is so smart!!!" :
            self.scaling_optionemenu.configure( state = 'normal' )
        elif vip == "jack is so handsome and smart!!!" :
            self.appearance_mode_optionemenu.configure( state = "normal" )
            self.scaling_optionemenu.configure( state = 'normal' )
        else:
            self.clean_textbox( )

### scan_network

    def scan_network( self ):
        try :
            scanner = nmap.PortScanner( )
            target_ip = self.target_ipbox.get( )
            # clean text box first
            self.clean_textbox( )

            # shows nmap version
            if self.nmap_version_radio.get( ) == "on" :
                display_nmap_version = f"The Nmap Version is: \t{ scanner.nmap_version()[0] }.{ scanner.nmap_version()[1] }\n"
                self.textbox.insert('end', display_nmap_version )

            if target_ip != '' :
                scanner.scan( target_ip, arguments = '-sS', sudo = True)
                host_list = scanner.all_hosts()

                # Show the command executed
                command_used = f"The comman used for nmap is:\n{ scanner.command_line() }"
                self.textbox.insert( 'end', "\n" )
                self.textbox.insert( 'end', command_used )

                # Scan the option(s) selected
                if self.number_of_host_radio.get( ) == "on" :
                    display_number_of_host = f"\nTotal number of Hosts: { str( len( host_list ) ) }"
                    self.textbox.insert( 'end', "\n" )
                    self.textbox.insert( 'end', display_number_of_host )

                if self.ip_radio.get( ) == 'on' :
                    self.textbox.insert( 'end', "\nThe hosts ip are:\n" )
                    show_ip = ""
                    for num, host in enumerate( host_list, start=1 ) :
                        show_ip += f"{num}.  {host}\n"
                    self.textbox.insert( 'end', "\n" )
                    self.textbox.insert( 'end', show_ip )
                
                if self.service_radio.get( ) == 'on' :
                    display_service = ''
                    for host in host_list :
                        scanner.scan( host, arguments = '-v -sS', sudo = True )
                        display_service += f"\ncommand used: \n{ scanner.command_line()}\n"
                        open_ports = scanner[ host ][ 'tcp'].keys()
                        scanned_results = scanner[ host ][ 'tcp' ]
                        display_service += f"\n{"Open Port"}\t\t{"Service"}\t\t{"Scan Type"}\n"
                        for open_port in open_ports :
                            display_service += f"     {open_port}\t\t{scanned_results[open_port]['name']}\t\t  {scanned_results[open_port]['reason']}\n"
                    self.textbox.insert( 'end', display_service )
                    self.textbox.insert( 'end', "\n" )
                        
                if self.os_radio.get( ) == 'on' :
                    display_os_info = ''
                    for host in host_list :
                        scanner.scan( host, arguments = '-O', sudo = True )
                        display_os_info += f"\ncommand used: \n{ scanner.command_line()}\n"
                        if 'osmatch' in scanner[host]:
                            for osmatch in scanner[host]['osmatch']:
                                if 'osclass' in osmatch:
                                    for osclass in osmatch['osclass']:
                                        display_os_info += f"\nIp Address : {host}\n"
                                        display_os_info += f"OS name : {osmatch['name']}\n"
                                        display_os_info += f"OS type : {osclass['type']}\n"
                                        display_os_info += f"OS vendor : {osclass['vendor']}\n"
                                        display_os_info += f"OS family : {osclass['osfamily']}\n"
                    self.textbox.insert( 'end', display_os_info )
                    self.textbox.insert( 'end', "\n" )

                if self.server_name_radio.get() == 'on' :
                    display_server_name = ''
                    for host in host_list :
                        display_server_name += f"\ncommand used: \n{ scanner.command_line()}\n"
                        scanner.scan( host, arguments = '-A', sudo = True )
                        if 'hostscript' in scanner[host]:
                            for d in scanner[host]['hostscript'] :
                                for key, value in d.items():
                                    if "NetBIOS name" in value:
                                        script_output = value
                                        name = script_output.split( ':' )
                                        name = name[1].split(',')
                                        server_name = f"The Server Name is: {name[0]}"
                                        display_server_name += server_name
                        else :
                            display_server_name += "This is not a server!"
                    self.textbox.insert( 'end', display_server_name )
                    self.textbox.insert( 'end', "\n" )

            else :
                no_ip = "Please enter target IP."
                self.textbox.insert('end', no_ip )

        except nmap.PortScannerError as e:
            print("Nmap PortScannerError:", e)
        except Exception as e:
            print("An error occurred:", e)

    def save_results( self ) :
        target_ip = self.target_ipbox.get()
        option_list = list( )
        if self.nmap_version_radio.get( ) == 'on' :
            option_list.append( 'Nmap Version' )
        if self.number_of_host_radio.get( ) == "on" :
            option_list.append( 'Scan Number of Hosts' )
        if self.ip_radio.get( ) == 'on' :
            option_list.append( 'Show scan ip' )
        if self.service_radio.get( ) == 'on' :
            option_list.append( 'Scan Services' )
        if self.os_radio.get( ) == 'on' :
            option_list.append( 'Scan OS' )
        if self.server_name_radio.get() == 'on' :
            option_list.append( 'Scan Server Name' )

        scan_date = self.get_current_date( )
        scan_time = self.get_current_time( )

        if self.textbox.get != '' :
            scan_result = self.textbox.get( '0.0', 'end' )

        output_filename = scan_date + scan_time + '.txt'
        outputfilename_with_path = './outputfiles/' + output_filename 
        new_data = [ str(target_ip), str( option_list ), str(scan_date), str(scan_time), str(output_filename) ]
        self.insert_record( new_data )
        self.results_output_to_file( scan_result , outputfilename_with_path  )
        
    def insert_record( self, new_data ):
        self.new_data = new_data
        cur = self.conn.cursor()
        sql = "INSERT INTO scanning_history (scanning_target, options, date, time, outputfilename ) VALUES ( ?, ?, ?, ?, ? )"
        cur.execute( sql, self.new_data )
        self.conn.commit()
                
    def clean_database( self ) :
        cur = self.conn.cursor()
        cur.execute( "DELETE FROM scanning_history" )
        self.conn.commit()
        self.clean_textbox( )
        self.textbox.insert('end', "\nAll data in database has been deleted\n" )

    def results_output_to_file( self, output, file_name ) :
        text_file = open( file_name, 'a+' )
        text_file.write( output )
        text_file.close()

    def clean_textbox( self ) :
        self.textbox.delete( '0.0', "end" )
# part B

    def get_current_date( self ):
        current_data = datetime.now()
        return current_data.strftime('%Y%m%d')

    def get_current_time( self ):
        now = datetime.now()
        return now.strftime('%H%M%S')

    def create_connection(self, db_file):
        self.db_file = db_file
        conn = None
        try:
            conn = sqlite3.connect( self.db_file )
        except Error as e:
            print(e)
        return conn

    def select_all_records( self ):
        # self.conn = conn
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM scanning_history")
        rows = cur.fetchall()
        data = list( )
        for row in rows :
            data.append([ row[0], row[1], row[2], row[3], row[4], row[5] ] )
        return data


# def callback(event):
#     filepath = "./outputfiles/"
#     # get the index of the mouse click
#     index = event.widget.index("@%s,%s" % (event.x, event.y))

#     # get the indices of all "adj" tags
#     tag_indices = list(event.widget.tag_ranges('tag'))

#     # iterate them pairwise (start and end index)
#     for start, end in zip(tag_indices[0::2], tag_indices[1::2]):
#         # check if the tag matches the mouse click index
#         if event.widget.compare(start, '<=', index) and event.widget.compare(index, '<', end):
#             # return string between tag start and end
#             filename = filepath + event.widget.get(start, end)
#             print(filename)
#             file1 = open(filename,'r')
#             lines = file1.readlines()
#             d = ""
#             for line in lines:
#                 d += line.strip() + "\n"

#             open_popup(d)

    def display_to_text(self):
        data = self.select_all_records()
        self.textbox.insert( 'end' , 'ID' + "\t" + "Scanning Target" + "\t" + "Options" + "\t" + "Date" + "\t" + "Time" + "\t" + "Output File\n")
        self.textbox.insert( 'end' , '==' + "\t" + "=======" + "\t" + "=======" + "\t" + "====" + "\t" + "====" + "\t" + "===========\n")
        for row in data:
            self.textbox.insert( 'end' , str(row[0]) + "\t" + row[1] + "\t" + row[2] + "\t" + row[3] + " " + row[4] + "\t")
            self.textbox.insert( 'end' ,row[5],"tag")
            self.textbox.insert( 'end' ,"\n")