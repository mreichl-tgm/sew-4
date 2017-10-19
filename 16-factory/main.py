import pyglet

from factories import FileFactory, MockupFactory

if __name__ == "__main__":
    # Pyglet stuff
    player = pyglet.media.Player()
    window = pyglet.window.Window()
    label = pyglet.text.Label('Hello, world',
                              font_name='Times New Roman',
                              font_size=36,
                              x=window.width // 2, y=window.height // 2,
                              anchor_x='center', anchor_y='center')
    @window.event
    def on_draw():
        window.clear()
        label.draw()
    # Factories
    mockup_factory = MockupFactory(player)
    file_factory = FileFactory(player)
    # Test the mockup factory
    mockup_factory.play()
    # Test the file factory
    file_factory.play()
