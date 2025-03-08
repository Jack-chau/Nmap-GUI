from time import *
from tkinter import *

def update( ) :
    time_string = strftime( "%H:%M:%S %p" )
    time_label.config( text = time_string )
    day_string = strftime( "%A" )
    day_label.config( text = day_string )
    date_string = strftime( "%B %d, %Y" )
    date_label.config( text=date_string )
    time_label.after( 1000, func = update )

window = Tk()

time_label = Label( window, font = ( "Araial", 50 ), fg = "#00FF00", bg = "black" )
time_label.pack( )

day_label = Label( window, font=( "Ink Free", 25 ) )
day_label.pack( )

date_label = Label( window, font = ( "Ink Free", 25 ) )
date_label.pack( ) 

update( )

window.mainloop()