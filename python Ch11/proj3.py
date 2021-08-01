#pizza sprite
#demo creating sprite

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

azm_image = games.load_image("azm.jpg", transparent = False)
games.screen.background = azm_image

pizza_image = games.load_image("pizza.bmp")
pizza = games.Sprite(image = pizza_image, x = 320, y = 240)
games.screen.add(pizza)

games.screen.mainloop()
