import tkinter as tk
from PIL import Image

# menu_icon = Image.open( "images/menu.png" )
# menu_icon = menu_icon.resize( ( 123, 123 ) )
# menu_icon.save( "resize_menu.png" )

root = tk.Tk()
root.geometry( '1500x1400' )
root.title( 'Change Pages' )

def namp_page( ) :
    nmap_page_fm = tk.Frame( page_frame )
    lb = tk.Label( nmap_page_fm, text = "Nmap Page", font = ("Bold", 20) )
    lb.place( x = 450, y = 500 )
    nmap_page_fm.pack( fill = tk.BOTH, expand = True )

def ansible_page( ) :
    ansible_page_fm = tk.Frame( page_frame )
    lb = tk.Label( ansible_page_fm, text = "Ansible Page", font = ("Bold", 20) )
    lb.place( x = 450, y = 500 )
    ansible_page_fm.pack( fill = tk.BOTH, expand = True )

def docker_page( ) :
    docker_page_fm = tk.Frame( page_frame )
    lb = tk.Label( docker_page_fm, text = "Docker Page", font = ("Bold", 20) )
    lb.place( x = 450, y = 500 )
    docker_page_fm.pack( fill = tk.BOTH, expand = True )

def schedule_page( ) :
    schedule_page_fm = tk.Frame( page_frame )
    lb = tk.Label( schedule_page_fm, text = "Schedule Page", font = ("Bold", 20) )
    lb.place( x = 450, y = 500 )
    schedule_page_fm.pack( fill = tk.BOTH, expand = True )

def github_page( ) :
    github_page_fm = tk.Frame( page_frame )
    lb = tk.Label( github_page_fm, text = "Github Page", font = ("Bold", 20) )
    lb.place( x = 450, y = 500 )
    github_page_fm.pack( fill = tk.BOTH, expand = True )

# Page Frame
page_frame = tk.Frame( root )
page_frame.place( relwidth = 1.0, relheight = 1, x = 130 )
namp_page()

menu_bar_color = '#474747'
#https://www.color-hex.com/color-palettes/?keyword=back

# menu bar frame
menu_bar_frame = tk.Frame( root, bg=menu_bar_color )
menu_bar_frame.pack( side = tk.LEFT, fill = tk.Y, pady = 6, padx = 6 )
menu_bar_frame.pack_propagate( flag = False )
menu_bar_frame.config( width = 120 )

# icons
menu_icon = tk.PhotoImage( file = 'images/resized_images/menu.png' )
nmap_icon = tk.PhotoImage( file = 'images/resized_images/nmap.png' )
ansible_icon = tk.PhotoImage( file = 'images/resized_images/ansible.png' )
docker_icon = tk.PhotoImage( file = 'images/resized_images/docker.png' )
schedule_icon = tk.PhotoImage( file = 'images/resized_images/schedule.png' )
github_icon = tk.PhotoImage( file = 'images/resized_images/github.png' )
close_icon = tk.PhotoImage( file = 'images/resized_images/close.png' )

def switch_indicator( indicator, page ):
    nmap_icon_btn_indicator.config( bg=menu_bar_color )
    ansible_icon_btn_indicator.config( bg=menu_bar_color )
    docker_icon_btn_indicator.config( bg=menu_bar_color )
    schedule_icon_btn_indicator.config( bg=menu_bar_color )
    github_icon_btn_indicator.config( bg=menu_bar_color )
    indicator.config( bg = '#f6f1e9' )

    if menu_bar_frame.winfo_width( ) > 120 :
        fold_menu_bar( )
    
    for frame in page_frame.winfo_children( ) :
        frame.destroy()
    
    page()

def extend_menu_bar( ):
    extending_animation()
    menu_btn.config( image = close_icon )
    menu_btn.config( command = fold_menu_bar )

def fold_menu_bar( ) :
    folding_animation( )
    menu_btn.config( image = menu_icon )
    menu_btn.config( command = extend_menu_bar )

def extending_animation( ) :
    current_width = menu_bar_frame.winfo_width( )
    if not current_width > 550 :
        current_width += 10
        menu_bar_frame.config( width = current_width )
        root.after( ms = 8, func = extending_animation )

def folding_animation( ):
    current_width = menu_bar_frame.winfo_width( )
    if  current_width != 120 :
        current_width -= 10
        menu_bar_frame.config( width = current_width )
        root.after( ms = 8, func = folding_animation )


# icons button location
menu_btn = tk.Button( menu_bar_frame, image = menu_icon, bg = menu_bar_color, bd = 0, activebackground = menu_bar_color, highlightthickness = 0, command = extend_menu_bar )
menu_btn.place( x = 4, y = 10 )

nmap_icon_btn = tk.Button( menu_bar_frame, image = nmap_icon, bg = menu_bar_color, bd = 0, activebackground = menu_bar_color, highlightthickness = 0, command = lambda:switch_indicator( indicator = nmap_icon_btn_indicator, page = namp_page ) )
nmap_icon_btn.place( x=12, y=330 )

ansible_icon_btn = tk.Button( menu_bar_frame, image=ansible_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, highlightthickness=0, command = lambda:switch_indicator( indicator = ansible_icon_btn_indicator, page = ansible_page) )
ansible_icon_btn.place( x=12, y=460)

docker_icon_btn = tk.Button( menu_bar_frame, image=docker_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, highlightthickness=0, command = lambda:switch_indicator( indicator = docker_icon_btn_indicator, page = docker_page ) )
docker_icon_btn.place( x=12, y=590)

schedule_icon_btn = tk.Button( menu_bar_frame, image=schedule_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, highlightthickness=0, command = lambda:switch_indicator( indicator = schedule_icon_btn_indicator, page = schedule_page ) )
schedule_icon_btn.place( x=12, y=720)


github_icon_btn = tk.Button( menu_bar_frame, image=github_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, highlightthickness=0, command = lambda:switch_indicator( indicator = github_icon_btn_indicator, page = github_page ) )
github_icon_btn.place( x=12, y=850)

# indicator '#eedf3c'
nmap_icon_btn_indicator = tk.Label( menu_bar_frame, bg = '#f6f1e9' )
nmap_icon_btn_indicator.place( x = 3, y = 330, height=100, width=5 )

ansible_icon_btn_indicator = tk.Label( menu_bar_frame, bg = menu_bar_color )
ansible_icon_btn_indicator.place( x = 3, y = 460, height=100, width=5 )

docker_icon_btn_indicator = tk.Label( menu_bar_frame, bg = menu_bar_color )
docker_icon_btn_indicator.place( x = 3, y = 590, height=100, width=5 )

schedule_icon_btn_indicator = tk.Label( menu_bar_frame, bg = menu_bar_color )
schedule_icon_btn_indicator.place( x = 3, y = 720, height=100, width=5 )

github_icon_btn_indicator = tk.Label( menu_bar_frame, bg = menu_bar_color )
github_icon_btn_indicator.place( x = 3, y = 850, height=100, width=5 )

nmap_page_lb = tk.Label( menu_bar_frame, text = "Nmap Page", bg = menu_bar_color, fg = 'black', font = ( 'Bold', 13 ), anchor = tk.W )
nmap_page_lb.place( x = 160, y = 340 )
nmap_page_lb.bind( '<Button-1>', lambda e : switch_indicator( indicator = nmap_icon_btn_indicator, page = namp_page ) )

ansible_page_lb = tk.Label( menu_bar_frame, text = "Ansible Page", bg = menu_bar_color, fg = 'black', font = ( 'Bold', 13 ), anchor = tk.W )
ansible_page_lb.place( x = 160, y = 470 )
ansible_page_lb.bind( '<Button-1>', lambda e : switch_indicator( indicator = ansible_icon_btn_indicator, page = ansible_page ) )

docker_page_lb = tk.Label( menu_bar_frame, text = "Docker Page", bg = menu_bar_color, fg = 'black', font = ( 'Bold', 13 ), anchor = tk.W )
docker_page_lb.place( x = 160, y = 600 )
docker_page_lb.bind( '<Button-1>', lambda e : switch_indicator( indicator = docker_icon_btn_indicator, page = docker_page ) )

schedule_page_lb = tk.Label( menu_bar_frame, text = "Schedule Page", bg = menu_bar_color, fg = 'black', font = ( 'Bold', 13 ), anchor = tk.W )
schedule_page_lb.place( x = 160, y = 730 )
schedule_page_lb.bind( '<Button-1>', lambda e : switch_indicator( indicator = schedule_icon_btn_indicator, page = schedule_page ) )

github_page_lb = tk.Label( menu_bar_frame, text = "Github Page", bg = menu_bar_color, fg = 'black', font = ( 'Bold', 13 ), anchor = tk.W )
github_page_lb.place( x = 160, y = 870 )
github_page_lb.bind( '<Button-1>', lambda e : switch_indicator( indicator = github_icon_btn_indicator, page = github_page ) )

root.mainloop()