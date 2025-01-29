import customtkinter as ctk
from config import menu_config


class SwitchMenu( ctk.CTkFrame, menu_config ) :
   def __init__( self, master ) :
      super().__init__( master )
      # Configure
      self.menu_gray = '#808080'
      self.indicator_width = 5

      # Menu frame
      self.menu_frame = ctk.CTkFrame( master, width = 150, fg_color = self.menu_gray, corner_radius = 0 )
      self.menu_frame.grid( row = 0, column = 1, rowspan = 4, sticky = 'nsew' )
      self.menu_frame.grid_columnconfigure( 0, weight = 0)
      self.menu_frame.grid_columnconfigure( 1, weight = 8)
      self.menu_frame.rowconfigure( 0, weight = 3)

      # Indicator Frame
      self.indicator_frame = ctk.CTkFrame( 
                                             self.menu_frame, 
                                             fg_color = self.menu_gray, 
                                             corner_radius = 0, 
                                          )
      self.indicator_frame.grid( row = 0, column = 0, sticky = 'nsew' )

      # Indicators
      self.blk_indicator_1 = ctk.CTkLabel( 
                                             self.indicator_frame, 
                                             fg_color = self.menu_gray, 
                                             width = self.indicator_width, 
                                             height = 20, 
                                             text = '' 
                                          )
      self.blk_indicator_1.pack( side = 'top', expand = True, fill = 'both')

      self.blk_indicator_2 = ctk.CTkLabel( 
                                             self.indicator_frame, 
                                             fg_color = self.menu_gray, 
                                             width = self.indicator_width, 
                                             height = 80, 
                                             text = '' 
                                          )
      self.blk_indicator_2.pack( side = 'top', expand = True, fill = 'both')      
        
      self.nmap_indicator = ctk.CTkLabel( 
                                             self.indicator_frame, 
                                             fg_color = '#f6f1e9', 
                                             width = self.indicator_width, 
                                             height = 45, 
                                             text = '' 
                                        )
      self.nmap_indicator.pack( side = 'top', expand = True, fill = 'both')

      self.ansible_indicator = ctk.CTkLabel( 
                                             self.indicator_frame, 
                                             fg_color = self.menu_gray, 
                                             width = self.indicator_width, 
                                             height = 45, 
                                             text = '' 
                                          )
      self.ansible_indicator.pack( side = 'top', expand = True, fill = 'both' )

      self.docker_indicator = ctk.CTkLabel( 
                                             self.indicator_frame, 
                                             fg_color = self.menu_gray, 
                                             width = self.indicator_width,
                                             height = 45,
                                             text = '' 
                                          )
      self.docker_indicator.pack( side = 'top', expand = True, fill = 'both' )

      self.schedule_indicator = ctk.CTkLabel( 
                                                self.indicator_frame, 
                                                fg_color = self.menu_gray, 
                                                width = self.indicator_width, 
                                                height = 45, 
                                                text = '' 
                                             )
      self.schedule_indicator.pack( side = 'top', expand = True, fill = 'both' )

      self.github_indicator = ctk.CTkLabel( 
                                             self.indicator_frame, 
                                             fg_color = self.menu_gray, 
                                             width = self.indicator_width, 
                                             height = 45, 
                                             text = '' 
                                          )
      self.github_indicator.pack( side = 'top', expand = True, fill = 'both' )

      self.blk_indicator_3 = ctk.CTkLabel( 
                                             self.indicator_frame, 
                                             fg_color = self.menu_gray, 
                                             width = self.indicator_width, 
                                             height = 30, 
                                             text = '' 
                                          )
      self.blk_indicator_3.pack( side = 'top', expand = True, fill = 'both')

      # Button Frame
      self.button_frame = ctk.CTkFrame( 
                                          self.menu_frame, 
                                          fg_color = self.menu_gray, 
                                          corner_radius = 0, 
                                          border_width = 0 
                                       )
      self.button_frame.grid( row = 0, column = 1, sticky = 'nsew' )

      # Buttons
      self.menu_btn = ctk.CTkButton( self.button_frame, 
                                    image = menu_config.menu_icon, 
                                    width = 30, text='' , 
                                    fg_color='transparent', 
                                    border_width = 0, 
                                    hover_color = self.menu_gray, 
                                    command = self.print_fun 
                                 )
      self.menu_btn.pack(  side = 'top', expand = True, fill = 'both' )

      self.blank_btn_1 = ctk.CTkButton( 
                                          self.button_frame, 
                                          text='' , 
                                          width = 30, 
                                          fg_color='transparent', 
                                          border_width = 0, 
                                          hover_color = self.menu_gray 
                                       )
      self.blank_btn_1.pack( side = 'top', expand = True, fill = 'both', ipady = 30 )

      self.nmap_btn = ctk.CTkButton( 
                                     self.button_frame, 
                                     image = menu_config.nmap_icon, 
                                     width = 30, text='' , 
                                     fg_color='transparent', 
                                     border_width = 0, 
                                     hover_color = self.menu_gray, 
                                     command = lambda : self.switch_indicator( indicator = self.nmap_indicator ) 
                                    )
      self.nmap_btn.pack( side = 'top', expand = True, fill = 'both' )

      self.ansible_btn = ctk.CTkButton( self.button_frame,
                                        image = menu_config.ansible_icon,
                                        width = 30, text='' ,
                                        fg_color='transparent',
                                        border_width = 0,
                                        hover_color = self.menu_gray,
                                        command = lambda : self.switch_indicator( indicator = self.ansible_indicator ) )
      self.ansible_btn.pack( side = 'top', expand = True, fill = 'both' )
                  
      self.docker_icon = ctk.CTkButton( self.button_frame, 
                                        image = menu_config.docker_icon,
                                        width = 30, text='' ,
                                        fg_color='transparent',
                                        border_width = 0,
                                        hover_color = self.menu_gray,
                                        command = lambda : self.switch_indicator( indicator = self.docker_indicator ) )
      self.docker_icon.pack( side = 'top', expand = True, fill = 'both' )

      self.schedule_btn = ctk.CTkButton( self.button_frame, 
                                         image = menu_config.schedule_icon, 
                                         width = 30, text='' , 
                                         fg_color='transparent', 
                                         border_width = 0, 
                                         hover_color = self.menu_gray, 
                                         command = lambda : self.switch_indicator( indicator = self.schedule_indicator ) 
                                       )
      self.schedule_btn.pack( side = 'top', expand = True, fill = 'both' )

      self.github_btn = ctk.CTkButton( self.button_frame, 
                                       image = menu_config.github_icon, 
                                       width = 30, text='' , 
                                       fg_color='transparent', 
                                       border_width = 0, 
                                       hover_color = self.menu_gray, 
                                       command = lambda : self.switch_indicator( indicator = self.github_indicator ) )
      self.github_btn.pack( side = 'top', expand = True, fill = 'both' )

      self.blank_btn_2 = ctk.CTkButton( self.button_frame,
                                        text='' , 
                                        width = 30, 
                                        fg_color='transparent', 
                                        border_width = 0, 
                                        hover_color = self.menu_gray 
                                       )
      self.blank_btn_2.pack( side = 'top', expand = True, fill = 'both', ipady = 10 )

   def print_fun( self ):
      print( 'fun' )

   def switch_indicator( self, indicator ) :
      self.nmap_indicator.configure( fg_color = self.menu_gray )
      self.ansible_indicator.configure( fg_color = self.menu_gray )
      self.docker_indicator.configure( fg_color = self.menu_gray )
      self.schedule_indicator.configure( fg_color = self.menu_gray )
      self.github_indicator.configure( fg_color = self.menu_gray )
      indicator.configure( fg_color = '#f6f1e9' )


