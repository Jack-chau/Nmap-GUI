import customtkinter as ctk
from PIL import Image, ImageTk
import os


class SwitchMenu( ctk.CTkFrame ) :
    def __init__( self, master ) :
        super().__init__( master )
        self.menu_gray = '#808080'
        # Icon
        self.menu_icon = ctk.CTkImage( light_image = Image.open( "images/resized_images/menu.png" ), 
                                          dark_image = Image.open( "images/resized_images/menu.png" ), 
                                          size=( 100, 100 )
                                       )
        self.nmap_icon = ctk.CTkImage( light_image = Image.open( 'images/resized_images/nmap.png' ),
                                          dark_image = Image.open( "images/resized_images/nmap.png" ), 
                                          size=( 100, 100 )
                                       )
        self.ansible_icon = ctk.CTkImage( light_image = Image.open( 'images/resized_images/ansible.png' ),
                                          dark_image = Image.open( "images/resized_images/ansible.png" ), 
                                          size=( 100, 100 )
                                       )
        self.docker_icon = ctk.CTkImage( light_image = Image.open( 'images/resized_images/docker.png' ),
                                          dark_image = Image.open( "images/resized_images/docker.png" ), 
                                          size=( 100, 100 )
                                       )
        self.schedule_icon = ctk.CTkImage( light_image = Image.open( 'images/resized_images/schedule.png' ),
                                          dark_image = Image.open( "images/resized_images/schedule.png" ), 
                                          size=( 100, 100 )
                                       )
        self.github_icon = ctk.CTkImage( light_image = Image.open( 'images/resized_images/github.png' ),
                                          dark_image = Image.open( "images/resized_images/github.png" ), 
                                          size=( 100, 100 )
                                       )
        self.close_icon = ctk.CTkImage( light_image = Image.open( 'images/resized_images/close.png' ),
                                          dark_image = Image.open( "images/resized_images/close.png" ), 
                                          size=( 100, 100 )
                                       )
        # menu frame
        self.menu_frame = ctk.CTkFrame( master, width = 150, fg_color = self.menu_gray, corner_radius = 0 )
        self.menu_frame.grid( row = 0, column = 1, rowspan = 4, sticky = 'nsew' )
        self.menu_frame.grid_columnconfigure( 0, weight = 0)
        self.menu_frame.grid_columnconfigure( 1, weight = 8)
        self.menu_frame.rowconfigure( 0, weight = 3)

        self.indicator_frame = ctk.CTkFrame( self.menu_frame, fg_color = self.menu_gray, corner_radius = 0, border_width = 0 )
        self.indicator_frame.grid( column = 0, sticky = 'nsew' )

        # Indicator
        self.blk_indicator_1 = ctk.CTkLabel( self.indicator_frame, fg_color = self.menu_gray, width = 8, height = 430, text = ''   )
        self.blk_indicator_1.pack( side = 'top', expand = False, fill = 'both')
        
        self.nmap_icon_btn_indicator = ctk.CTkLabel( self.indicator_frame, fg_color = '#f6f1e9', width = 8, height = 150, text = ''   )
        self.nmap_icon_btn_indicator.pack( side = 'top', expand = False, fill = 'both')

        self.blk_indicator_2 = ctk.CTkLabel( self.indicator_frame, fg_color = self.menu_gray, width = 8, height = 55, text = ''   )
        self.blk_indicator_2.pack( side = 'top', expand = False, fill = 'both' )

        self.ansible_icon_btn_indicator = ctk.CTkLabel( self.indicator_frame, fg_color = self.menu_gray, width = 8, height = 150, text = ''   )
        self.ansible_icon_btn_indicator.pack( side = 'top', expand = False, fill = 'both' )

        self.blk_indicator_3 = ctk.CTkLabel( self.indicator_frame, fg_color = self.menu_gray, width = 8, height = 70, text = ''   )
        self.blk_indicator_3.pack( side = 'top', expand = False, fill = 'both' )

        self.docker_icon_btn_indicator = ctk.CTkLabel( self.indicator_frame, fg_color = self.menu_gray, width = 8, height = 150, text = ''   )
        self.docker_icon_btn_indicator.pack( side = 'top', expand = False, fill = 'both' )

        self.blk_indicator_4 = ctk.CTkLabel( self.indicator_frame, fg_color = self.menu_gray, width = 8, height = 50, text = ''   )
        self.blk_indicator_4.pack( side = 'top', expand = False, fill = 'both' )

        self.schedule_icon_btn_indicator = ctk.CTkLabel( self.indicator_frame, fg_color = self.menu_gray, width = 8, height = 150, text = ''   )
        self.schedule_icon_btn_indicator.pack( side = 'top', expand = False, fill = 'both' )

        self.blk_indicator_5 = ctk.CTkLabel( self.indicator_frame, fg_color = self.menu_gray, width = 8, height = 55, text = ''   )
        self.blk_indicator_5.pack( side = 'top', expand = False, fill = 'both' )

        self.github_icon_btn_indicator = ctk.CTkLabel( self.indicator_frame, fg_color = self.menu_gray, width = 8, height = 150, text = ''   )
        self.github_icon_btn_indicator.pack( side = 'top', expand = False, fill = 'both' )


        
        self.button_frame = ctk.CTkFrame( self.menu_frame, fg_color = self.menu_gray, corner_radius = 0, border_width = 0 )
        self.button_frame.grid( row = 0, column = 1, sticky = 'nsew' )
        # Button
        self.menu_btn = ctk.CTkButton( self.button_frame, image = self.menu_icon, width = 30, text='' , fg_color='transparent', border_width = 0, hover_color = self.menu_gray, command = self.print_fun )
        self.menu_btn.pack(  side = 'top', expand = True, fill = 'both' )

        self.blank_btn_1 = ctk.CTkButton( self.button_frame, text='' , width = 30, fg_color='transparent', border_width = 0, hover_color = self.menu_gray )
        self.blank_btn_1.pack( side = 'top', expand = True, fill = 'both', ipady = 30 )

        self.nmap_icon = ctk.CTkButton( self.button_frame, image = self.nmap_icon, width = 30, text='' , fg_color='transparent', border_width = 0, hover_color = self.menu_gray, command = self.print_fun )
        self.nmap_icon.pack( side = 'top', expand = True, fill = 'both' )

        self.ansible_icon = ctk.CTkButton( self.button_frame, image = self.ansible_icon, width = 30, text='' , fg_color='transparent', border_width = 0, hover_color = self.menu_gray, command = self.print_fun )
        self.ansible_icon.pack( side = 'top', expand = True, fill = 'both' )
                  
        self.docker_icon = ctk.CTkButton( self.button_frame, image = self.docker_icon, width = 30, text='' , fg_color='transparent', border_width = 0, hover_color = self.menu_gray, command = self.print_fun )
        self.docker_icon.pack( side = 'top', expand = True, fill = 'both' )

        self.schedule_icon = ctk.CTkButton( self.button_frame, image = self.schedule_icon, width = 30, text='' , fg_color='transparent', border_width = 0, hover_color = self.menu_gray, command = self.print_fun )
        self.schedule_icon.pack( side = 'top', expand = True, fill = 'both' )

        self.github_icon = ctk.CTkButton( self.button_frame, image = self.github_icon, width = 30, text='' , fg_color='transparent', border_width = 0, hover_color = self.menu_gray, command = self.print_fun )
        self.github_icon.pack( side = 'top', expand = True, fill = 'both' )

        self.blank_btn_6 = ctk.CTkButton( self.button_frame, text='' , width = 30, fg_color='transparent', border_width = 0, hover_color = self.menu_gray )
        self.blank_btn_6.pack( side = 'top', expand = True, fill = 'both', ipady = 10 )

    def print_fun( self ):
        print( 'fun' )
