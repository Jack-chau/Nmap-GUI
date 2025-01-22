import customtkinter as ctk
from PIL import Image, ImageTk

import os

class Notorious( ctk.CTk ) :
    def __init__( self ) :
        super( ).__init__( )

        ctk.set_appearance_mode( "dark" )
        ctk.set_default_color_theme( 'green' )

        # root window size
        self.title( "Dream Big" )
        self.geometry( f'{2800}x{1500}+{800}+{300}' )
        # define grid
        self.grid_columnconfigure( 0, weight = 0 )
        self.grid_columnconfigure( 2, weight = 1 )
        self.grid_columnconfigure( 3,  weight = 2 )
        self.grid_columnconfigure( 4,  weight = 1 )
        self.grid_rowconfigure( ( 0, 1, 2 ), weight = 1 )

        #https://colorhunt.co/palette/f2f9ffffcce1e195abfff5d7
        # menu frame
        self.menu_frame = ctk.CTkFrame( self, width = 150, corner_radius = 5, fg_color = '#FFCCE1' )
        self.menu_frame.grid( row = 0, column = 0, rowspan = 4, sticky = 'nsew' )
        self.menu_frame.grid_rowconfigure( 4, weight = 1)

        # Icon
        self.menu_icon = ctk.CTkImage( light_image = Image.open( "images/resized_images/menu.png" ), 
                                       dark_image = Image.open( "images/resized_images/menu.png" ), 
                                       size=( 80, 100 )
                                    )
        # self.nmap_icon = ctk.CTkImage( file = 'images/resized_images/nmap.png' )
        # self.ansible_icon = ctk.CTkImage( file = 'images/resized_images/ansible.png' )
        # self.docker_icon = ctk.CTkImage( file = 'images/resized_images/docker.png' )
        # self.schedule_icon = ctk.CTkImage( file = 'images/resized_images/schedule.png' )
        # self.github_icon = ctk.CTkImage( file = 'images/resized_images/github.png' )
        # self.close_icon = ctk.CTkImage( file = 'images/resized_images/close.png' )


        self.menu_btn = ctk.CTkButton( self.menu_frame, image = self.menu_icon, text='' , fg_color='transparent')
        self.menu_btn.place( x = 4, y = 10 )

        # nmap_icon_btn = tk.Button( menu_bar_frame, image = nmap_icon, bg = menu_bar_color, bd = 0, activebackground = menu_bar_color, highlightthickness = 0, command = lambda:switch_indicator( indicator = nmap_icon_btn_indicator, page = namp_page ) )
        # nmap_icon_btn.place( x=12, y=330 )

        # ansible_icon_btn = tk.Button( menu_bar_frame, image=ansible_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, highlightthickness=0, command = lambda:switch_indicator( indicator = ansible_icon_btn_indicator, page = ansible_page) )
        # ansible_icon_btn.place( x=12, y=460)

        # docker_icon_btn = tk.Button( menu_bar_frame, image=docker_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, highlightthickness=0, command = lambda:switch_indicator( indicator = docker_icon_btn_indicator, page = docker_page ) )
        # docker_icon_btn.place( x=12, y=590)

        # schedule_icon_btn = tk.Button( menu_bar_frame, image=schedule_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, highlightthickness=0, command = lambda:switch_indicator( indicator = schedule_icon_btn_indicator, page = schedule_page ) )
        # schedule_icon_btn.place( x=12, y=720)


        # github_icon_btn = tk.Button( menu_bar_frame, image=github_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, highlightthickness=0, command = lambda:switch_indicator( indicator = github_icon_btn_indicator, page = github_page ) )
        # github_icon_btn.place( x=12, y=850)
