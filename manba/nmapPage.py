import customtkinter as ctk
import threading
from features import Clock, Appearance, Textbox, Progressbar
import nmap
# import sqlite3
# from sqlite3 import Error
from datetime import datetime
import psycopg2

class NmapPage( ctk.CTkFrame ) :
    def __init__( self, master ) :
        super( ).__init__( master )
        # Configuration
        # self.database = r'sasqdemo.db'
        # self.conn = self.create_connection( self.database )
        # self.data = self.select_all_records( )
        self.font_style = ( "Helventica bold", 15 )

        # Nmap Sidebar Frame
        self.nmap_sidebar = ctk.CTkFrame( 
            master, 
            width = 70, 
            corner_radius = 0 
        )
        self.nmap_sidebar.grid( 
            row = 0, 
            rowspan = 4, 
            column = 2, 
            sticky = 'nsew' 
        )
        self.date_label = Clock( self.nmap_sidebar ).date_label
        self.date_label.pack(
            side = 'top',
            pady = ( 10, 0 )
        )
        self.day_label = Clock( self.nmap_sidebar ).day_label
        self.day_label.pack(
            side = 'top',
        )
        self.time_label = Clock( self.nmap_sidebar ).time_label
        self.time_label.pack(
            side = 'top',
            pady = ( 20 , 0)
        )     
        # Sidebar
        self.page_label = ctk.CTkLabel( 
            self.nmap_sidebar, 
            text = "Nmap Page", 
            font = ctk.CTkFont("Segoe Script", 30 ),
        )
        self.page_label.pack( 
            side = 'top',
            pady = ( 40, 30 ),
        )
        # left sidebar window 1


        self.scan_network = ctk.CTkButton( 
            self.nmap_sidebar, 
            text="Scan Network",
            width = 180,
            height = 50,
            font = ctk.CTkFont( "Segoe Script", 15 ),
            command = self.scan_network()
        )
        self.scan_network.pack( 
            side = 'top',
            pady = ( 20, 20 ),
            padx = ( 0, 0 )

        )

        self.save_btn = ctk.CTkButton(
            self.nmap_sidebar, 
            text = "Save Record", 
            width = 180,
            height = 50,
            font = ctk.CTkFont("Segoe Script", 15 ),
            #command = self.save_results 
        )
        self.save_btn.pack(
            side = 'top',
            pady = ( 10 , 50 ),
            padx = ( 0 , 0 ),
        )
        self.clear_btn = ctk.CTkButton(
            self.nmap_sidebar, 
            text = "Clear", 
            width = 180,
            height = 50,
            font = ctk.CTkFont("Segoe Script", 15 ),
            command = self.clear_textbox_thread
        )
        self.clear_btn.pack(
            side = 'top',
            pady = ( 10 , 50 ),
            padx = ( 0 , 0 )
        )

        # Appearance
        self.appearance_label = Appearance( self.nmap_sidebar ).appearance_label
        self.appearance_label.configure( 
            font = ctk.CTkFont("Segoe Script", 20 )
        )
        self.appearance_label.pack( 
            side = 'top',
            pady = ( 150, 20 )
        )

        self.appearance_optionmenu = Appearance( self.nmap_sidebar ).appearance_optionmenu
        self.appearance_optionmenu.configure(
            width = 150,
            height = 40, 
            font = ctk.CTkFont("Segoe Script", 15 ),
            dropdown_font = ctk.CTkFont("Segoe Script", 15 ),
        )
        self.appearance_optionmenu.pack( 
            side = 'top',
            pady = ( 20, 20 )
        )

        self.scale_label = Appearance( self.nmap_sidebar ).scale_label
        self.scale_label.configure( 
            font = ctk.CTkFont("Segoe Script", 20 )
        )
        self.scale_label.pack( 
            side = 'top',
            pady = ( 10, 20 )
        )

        self.scale_optionmenu = Appearance( self.nmap_sidebar ).scale_optionmenu
        self.scale_optionmenu.configure(
            width = 150,
            height = 40,
            font = ctk.CTkFont("Segoe Script", 15 ),
            dropdown_font = ctk.CTkFont("Segoe Script", 15 ),
        )
        self.scale_optionmenu.pack(
            side = 'top',
        )

        # Text Box Frame
        self.nmap_textbox_frame = ctk.CTkFrame( 
            master, 
            width = 70, 
            corner_radius = 0 
        )
        self.nmap_textbox_frame.grid( 
            row = 0, 
            rowspan = 4, 
            column = 4, 
            sticky = 'nsew',
        )
        # Textbox
        self.nmap_textbox = Textbox( self.nmap_textbox_frame ).textbox
        self.nmap_textbox.pack(
            side = 'top',
            padx = ( 0,0 ),
            pady = ( 0, 0 ),
            expand = True,
            fill = 'both',
        )
        # Progress bar
        self.progressbar = Progressbar( self.nmap_textbox_frame ).progressbar
        self.progressbar.pack(
            side = 'top',
            fill = 'both',
            padx = (10,10),
            pady = (10,10),
        )
        self.progressbar.set( 0.52 )
        # self.progressbar.forget()

        # Configuration Frame
        self.config_frame = ctk.CTkFrame( 
            master, 
            width = 300,
            border_width = 10,
        )
        self.config_frame.grid( 
            row = 0, 
            column = 6, 
            rowspan = 2,
            sticky = 'nsew',
        )
        self.nmap_tab = ctk.CTkTabview(
            self.config_frame,
            width = 80,
            height = 400,
        )
        self.nmap_tab.pack(
            side = 'top',
        )
        self.nmap_tab.add( 'Scan Config' )
        self.nmap_tab.add( 'Scan Log' )
        self.ip_label = ctk.CTkLabel(
            self.nmap_tab.tab( 'Scan Config' ), 
            text = "Target IP : ",
            font = ( "Comic Sans MS", 20 ),
        )
        self.ip_label.grid(
            row = 0, 
            column = 0, 
            padx = (10, 0), 
            pady = (20, 5), 
            sticky = "ew"
        )
        self.ip_entry = ctk.CTkEntry(
            self.nmap_tab.tab( 'Scan Config' ), 
            placeholder_text = "IP address",
            width= 200,
        )
        self.ip_entry.grid(
            row=0, 
            column=1, 
            padx=(10,10), 
            pady=(25, 10), 
            sticky="ew"
        )

        # Scan Options
        self.nmap_version_radio_var = ctk.StringVar( value = "off" )
        self.nmap_version_radio = ctk.CTkCheckBox(
            self.nmap_tab.tab( 'Scan Config' ), 
            text="Nmap Version",
            variable = self.nmap_version_radio_var,
            onvalue = "on",
            offvalue = "off",
            font = ( "Comic Sans MS", 15 )
        )
        self.nmap_version_radio.grid(
            row=1, 
            column=0, 
            padx=(30, 30), 
            pady=(30, 20), 
            sticky="nsew"
        )

        self.number_of_host_radio_var = ctk.StringVar( value = "off" )
        self.number_of_host_radio = ctk.CTkCheckBox(
            self.nmap_tab.tab( 'Scan Config' ), 
            text="Number of Hosts",
            variable = self.number_of_host_radio_var,
            onvalue = "on",
            offvalue = "off",
            font = ( "Comic Sans MS", 15 )
        )
        self.number_of_host_radio.grid(
            row=1, 
            column=1, 
            padx=(30,0), 
            pady=(40, 30), 
            sticky="nsew"
        )

        self.ip_radio_var = ctk.StringVar( value = "off" )
        self.ip_radio = ctk.CTkCheckBox(
            self.nmap_tab.tab( 'Scan Config' ), 
            text="IP addresses",
            variable = self.ip_radio_var,
            onvalue = "on",
            offvalue = "off",
            font = ( "Comic Sans MS", 15 )
        )
        self.ip_radio.grid(
            row=2, 
            column=0, 
            padx=(30,30), 
            pady=(30, 20), 
            sticky="nsew"
        )

        self.service_radio_var = ctk.StringVar( value = "off" )
        self.service_radio = ctk.CTkCheckBox(
            self.nmap_tab.tab( 'Scan Config' ), 
            text="Running Service",
            variable = self.service_radio_var,
            onvalue = "on",
            offvalue = "off",
            font = ( "Comic Sans MS", 15 )
        )
        self.service_radio.grid(
            row=2, 
            column=1, 
            padx = ( 30, 0 ), 
            pady = ( 30, 30 ), 
            sticky="nsew"
        )

        self.os_radio_var = ctk.StringVar( value = "off" )
        self.os_radio = ctk.CTkCheckBox(
            self.nmap_tab.tab( 'Scan Config' ), 
            text="OS Version",
            variable = self.os_radio_var,
            onvalue = "on",
            offvalue = "off",
            font = ( "Comic Sans MS", 15 )
        )
        self.os_radio.grid(
            row=3,
            column=0,
            padx=( 30, 30),
            pady=( 30, 0 ),
            sticky="nsew"
        )

        self.server_name_radio_var = ctk.StringVar( value = "off" )
        self.server_name_radio = ctk.CTkCheckBox(
            self.nmap_tab.tab( 'Scan Config' ), 
            text="Server Name" ,
            variable = self.server_name_radio_var,
            onvalue = "on",
            offvalue = "off",
            font = ( "Comic Sans MS", 15 )
        )
        self.server_name_radio.grid(
            row=3,
            column=1,
            padx=( 30, 0 ),
            pady=( 30, 0 ),
            sticky="nwse"
        )

        # History Box
        self.display_button = ctk.CTkButton(
            self.nmap_tab.tab( 'Scan Log' ), 
            text = "Display Records",
            font = ( "Comic Sans MS", 20 ),
            width = 250,
            height = 50,
            #command = self.display_to_text
            #command = lambda: self.display_to_text( self.data ),
        )
        self.display_button.grid(
            row=2, 
            column=0,
            columnspan = 2,
            rowspan = 2,
            padx=( 10, 10 ), 
            pady=( 30, 20), 
            sticky="nwse"
        )

        self.del_id_label = ctk.CTkLabel(
            self.nmap_tab.tab( 'Scan Log' ), 
            text = "Delete ID : ",
            font = ( "Comic Sans MS", 20 ),
        )
        self.del_id_label.grid( 
            row=5, 
            column=0,
            padx=(0, 0), 
            pady=( 40, 20 ), 
            sticky="nwse" 
        )

        self.del_id_box = ctk.CTkEntry(
            self.nmap_tab.tab( 'Scan Log' ), 
            placeholder_text = "data id", 
            font = ( "Comic Sans MS", 20 ),
            width = 220,
            justify = 'center'
        )
        self.del_id_box.grid(
            row=5, 
            column=1, 
            padx = ( 0, 20 ), 
            pady=( 20, 0), 
            sticky="nwse"
        )

        self.del_data_label = ctk.CTkLabel(
            self.nmap_tab.tab( 'Scan Log' ), 
            text = "Delete Data : ",
            font = ( "Comic Sans MS", 20 ),
        )
        self.del_data_label.grid( 
            row=7, 
            column=0,
            padx=( 10, 0), 
            pady=( 40,0 ), 
            sticky="nwse" 
        )

        self.del_data_btn = ctk.CTkButton(
            self.nmap_tab.tab( 'Scan Log' ),
            text = "Delete Data", 
            font = ( "Comic Sans MS", 20 ),
            width=100,
            height=50,
            fg_color= 'orange',
            hover_color = 'red'
            # command = self.delete_data 
        )
        self.del_data_btn.grid(
            row=7, 
            column=1, 
            padx=( 10, 0 ), 
            pady=( 40, 0 ) ,
            sticky="nwse",
        )
        # Remark Frame
        self.remark_frame = ctk.CTkFrame( 
            master, 
            width = 300,
            border_width = 20,
            corner_radius = 10,
        )
        self.remark_frame.grid( 
            row = 2, 
            column = 6,
            rowspan = 2,
            sticky = 'nsew',
        )
        self.remark_box = ctk.CTkTextbox(
            self.remark_frame,
            font = ( "Comic Sans MS", 20 ),
            border_width = 10,
        )
        self.remark_box.pack(
            side = 'top',
            expand = True,
            fill = 'both'
    
        )
        self.remark_box.insert( 
            "0.0",
            "\nRemarks:\n\n"
            "1. Number of hosts:\n    Scan all the hosts in the target network.\n"
            "2. IP addresses:\n    Shows the IP addresses of the hosts.\n"
            "3. Running Service:\n    Shows hosts running service.\n"
            "4. OS Version:\n    Shows hosts OS Version\n"
            "5. Server name:\n    Server name (If server was found)\n"
            "6. Nmap Version:\n    Shows Nmap version"
        )
    
    def clear_textbox( self ) :
        self.nmap_textbox.delete( '0.0', 'end' )
    def clear_textbox_thread( self ) :
        clear_textbox_thread = threading.Thread( target= self.clear_textbox )
        clear_textbox_thread.start()
        
    def scan_network( self ) :
        try :
            scanner = nmap.PortScanner( )
            target_ip = self.ip_entry.get( )
            self.clear_textbox( )

            # Show Nmap Version
            if self.nmap_version_radio.get( ) == 'on' :
                    display_nmap_version = f"The Namp Version is : \t { scanner.nmap_version()[0] }.{ scanner.nmap_version()[1] }\n"
                    self.nmap_textbox.insert( 'end', display_nmap_version )

            # Scan All Hosts
            if target_ip != '' :
                    scanner.scan( target_ip, arguments = '-sS -Pn' ) #, sudo = True )
                    host_list = scanner.all_hosts()
                        
            # Show the command executed
            command_executed = f"The command executed is:\n{ scanner.command_line() }"
            self.nmap_textbox.insert( 'end', '\n' )
            self.nmap_textbox.insert( 'end', command_executed )

            # Show target IP                       
            if self.ip_radio.get( ) == 'on' :
                self.nmap_textbox.insert( 'end', '\nThe hosts ip are:\n' )
                show_ip = ''
                for num, host in enumerate( host_list, start = 1 ) :
                    show_ip += f"{num} . {host}\n"
                    self.nmap_textbox.insert( 'end', '\n' )
                    self.nmap_textbox.insert( 'end', show_ip )

            # Scan Service
            if self.service_radio.get() == 'on' :
                display_service = ''
                for host in host_list :
                    scanner.scan( host, arguments='-v -sS -Pn')#, sudo = True )
                    display_service += f"\ncommand executed: \n{ scanner.command_line() }\n"
                    open_ports = scanner[ host ][ 'tcp' ].keys()
                    scanned_results = scanner[ host ][ 'tcp' ]
                    display_service += f"\n{"Open Port"}\t\t{"Service"}\t\t{"Scan Type"}\n"
                    for open_port in open_ports :
                        display_service += f"      {open_port}\t\t{scanned_results[open_port]['name']}\t\t {scanned_results[open_port]['reason']}\n"
                self.nmap_textbox.insert( 'end', display_service )
                self.nmap_textbox.insert( 'end', '\n' )
            
            # Scan OS
            if self.os_radio.get( ) == 'on' :
                display_os_info = ''
                for host in host_list :
                    scanner.scan( host, arguments='-O' ) # sudo = True
                    display_os_info += f"\ncommand executed: \n{ scanner.command_line()}\n"
                    if 'osmatch' in scanner[ host ] :
                        for osmatch in scanner[host]['osmatch']:
                            if 'osclass' in osmatch:
                                for osclass in osmatch['osclass']:
                                    display_os_info += f"\nIp Address : {host}\n"
                                    display_os_info += f"OS name : {osmatch['name']}\n"
                                    display_os_info += f"OS type : {osclass['type']}\n"
                                    display_os_info += f"OS vendor : {osclass['vendor']}\n"
                                    display_os_info += f"OS family : {osclass['osfamily']}\n"
                self.nmap_textbox.insert( 'end', display_os_info )
                self.nmap_textbox.insert( 'end', "\n" )
            # Scan Server Name
            if self.server_name_radio.get() == 'on' :
                display_server_name = ''
                for host in host_list :
                    display_server_name += f"\ncommand executed: \n{ scanner.command_line()}\n"
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
                                                self.nmap_textbox.insert( 'end', display_server_name )
                                                self.nmap_textbox.insert( 'end', "\n" )
            else :
                self.nmap_textbox.insert('end', "Please enter target IP." )
            # scan_network_thread = threading.Thread( target = self.scan_network )
            # scan_network_thread.start()
        except nmap.PortScannerError as e :
                print( "Nmap PortScannerError: ", e )
        except Exception as e :
                print( "An error occured: ", e )

    # def scan_network_thread( self ) :
    #     scan_network_thread = threading.Thread( target = self.scan_network )
    #     scan_network_thread.start()

    def insert_record( self, new_data ) :
        self.new_data = new_data
        cur = self.conn.cursor( )
        sql = "INSERT INTO scanning_history ( scanning_target, )"