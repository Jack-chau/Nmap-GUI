import tkinter as tk
from PIL import Image

# menu_icon = Image.open( "images/menu.png" )
# menu_icon = menu_icon.resize( ( 123, 123 ) )
# menu_icon.save( "resize_menu.png" )

root = tk.Tk()
root.geometry( '1000x1400' )
root.title( 'Change Pages' )

menu_bar_color = '#474747'
#https://www.color-hex.com/color-palettes/?keyword=back

# menu bar frame
menu_bar_frame = tk.Frame( root, bg=menu_bar_color )
menu_bar_frame.pack( side = tk.LEFT, fill = tk.Y, pady = 6, padx = 6 )
menu_bar_frame.pack_propagate( flag = False )
menu_bar_frame.config( width = 120 )

# icons
menu_icon = tk.PhotoImage( file='images/resized_images/menu.png' )
nmap_icon = tk.PhotoImage( file = 'images/resized_images/nmap.png' )
ansible_icon = tk.PhotoImage( file = 'images/resized_images/ansible.png' )
docker_icon = tk.PhotoImage( file = 'images/resized_images/docker.png' )
schedule_icon = tk.PhotoImage( file = 'images/resized_images/schedule.png' )
github_icon = tk.PhotoImage( file = 'images/resized_images/github.png' )

# icons button location
menu_btn = tk.Button( menu_bar_frame, image=menu_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, highlightthickness=0 )
menu_btn.place( x = 4, y = 10 )

nmap_icon_btn = tk.Button( menu_bar_frame, image=nmap_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, highlightthickness=0, command = lambda:switch_indicator( indicator = nmap_icon_btn_indicator) )
nmap_icon_btn.place( x=12, y=330 )

ansible_icon_btn = tk.Button( menu_bar_frame, image=ansible_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, highlightthickness=0, command = lambda:switch_indicator( indicator = ansible_icon_btn_indicator) )
ansible_icon_btn.place( x=12, y=460)

docker_icon_btn = tk.Button( menu_bar_frame, image=docker_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, highlightthickness=0, command = lambda:switch_indicator( indicator = docker_icon_btn_indicator) )
docker_icon_btn.place( x=12, y=590)

schedule_icon_btn = tk.Button( menu_bar_frame, image=schedule_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, highlightthickness=0, command = lambda:switch_indicator( indicator = schedule_icon_btn_indicator) )
schedule_icon_btn.place( x=12, y=720)


github_icon_btn = tk.Button( menu_bar_frame, image=github_icon, bg=menu_bar_color, bd=0, activebackground=menu_bar_color, highlightthickness=0, command = lambda:switch_indicator( indicator = github_icon_btn_indicator) )
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

def switch_indicator( indicator ) :
    nmap_icon_btn_indicator.config( bg=menu_bar_color )
    ansible_icon_btn_indicator.config( bg=menu_bar_color )
    docker_icon_btn_indicator.config( bg=menu_bar_color )
    schedule_icon_btn_indicator.config( bg=menu_bar_color )
    github_icon_btn_indicator.config( bg=menu_bar_color )
    indicator.config( bg = '#f6f1e9' )

root.mainloop()