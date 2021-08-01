#background image
#demo srtting the background image of graphics screen

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

azm_image = games.load_image("azm.jpg", transparent = False)
games.screen.background = azm_image

games.screen.mainloop()
