import customtkinter as ctk
from PIL import Image, ImageTk

class menu_config( ) :
    #Config
    menu_gray = '#808080'
    icon_width = 50
    icon_height = 50
    selected_color = '#606060'

    # Icon Location
    menu_icon = ctk.CTkImage( 
                                light_image = Image.open( "images/resized_images/menu.png" ), 
                                dark_image = Image.open( "images/resized_images/menu.png" ), 
                                size=( icon_width , icon_height )
                        )
    nmap_icon = ctk.CTkImage( 
                                light_image = Image.open( 'images/resized_images/nmap.png' ),
                                dark_image = Image.open( "images/resized_images/nmap.png" ), 
                                size=( icon_width , icon_height )
                            )
    ansible_icon = ctk.CTkImage( 
                                    light_image = Image.open( 'images/resized_images/ansible.png' ),
                                    dark_image = Image.open( "images/resized_images/ansible.png" ), 
                                    size=( icon_width , icon_height )
                            )
    docker_icon = ctk.CTkImage( 
                                    light_image = Image.open( 'images/resized_images/docker.png' ),
                                    dark_image = Image.open( "images/resized_images/docker.png" ), 
                                    size=( icon_width , icon_height )
                                     )
    schedule_icon = ctk.CTkImage( 
                                    light_image = Image.open( 'images/resized_images/schedule.png' ),
                                    dark_image = Image.open( "images/resized_images/schedule.png" ), 
                                    size=( icon_width , icon_height )
                                )
    github_icon = ctk.CTkImage( 
                                    light_image = Image.open( 'images/resized_images/github.png' ),
                                    dark_image = Image.open( "images/resized_images/github.png" ), 
                                    size=( icon_width , icon_height )
                                )
    close_icon = ctk.CTkImage( 
                                light_image = Image.open( 'images/resized_images/close.png' ),
                                dark_image = Image.open( "images/resized_images/close.png" ), 
                                size=( icon_width , icon_height )
                            )
    