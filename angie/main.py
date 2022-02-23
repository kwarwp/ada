# ada.angie.main.py
OCEANO = "https://i.imgur.com/NRi5i6d.jpg"
colorPalette = ["#9B2E69", "#D93750", "#E2724F", "#F3DC7B", "#4E9397"]
ELIPSE = "https://imgur.com/Gea0Z3c.png"
ARVORE = "https://imgur.com/VkBQmuU.jpg"
BLACK = "https://i.imgur.com/cQogon6.jpg"
from _spy.vitollino.main import Cena, STYLE, Elemento
from browser import svg, alert
from random import randint, random
import colorsys

STYLE.update(width=1350, height="650px")
class Retangulos:
    def __init__(self):
        self.tela = svg.svg(version="1.1", viewBox="400 250 1000 600", width="1600", height="800")
        self.cena = Cena(ARVORE)
        self.rects = Elemento('', x=0, y=0, w=1350, h=800, cena=self.cena)
        self.cena.vai()
        self.rects.elt <= self.tela
        
    def make_nodes(self):
        cena = self.cena
        class Node(Elemento):
            def __init__(self, x, y, w, c, h=33):
                super().__init__(ELIPSE, x=x, y=y, w=w, h=h, o=0.45, cena=cena, vai=self.nomeia)
                self.siz= (w,100)
                self.pos= (0, c)
                self.text = ""
            def nomeia(self, *_):
                from browser import html
                self.text = input("nomei os parentes aqui")
                self.elt.html = ""
                self.elt <= html.PRE(self.text, style=dict(
                    position='relative', top=0, left=0, backgroundColor='transparent', padding="0.5rem 1.5rem"))
                self.o =1
        [Node(x, y, w, c) for x, y, w, c in [
            [85, 479, 180, -66],[410, 493, 180, -66],[850, 458, 180, -66],
            [410, 55, 170, -33],[380, 100, 170, -33],[425, 145, 190, -33],
            [280, 143, 150, 0],[560, 120, 150, 0],[560, 180, 150, 0]
        ]]


    def make_rects(self, maxX, maxY):
        for rect in range(1000):
            r = svg.rect(
            x=randint(0, maxX + 50) - 50,
            y=randint(0, maxY + 50) - 50,
            width=randint(0, 200) + 20,
            height=randint(0, 200) + 20,
            opacity=0.8*randint(0, 10),
            fill=colorPalette[randint(0,4)],
            transform=f"rotate({3*randint(0, 30)})"
            )
            self.tela <= r
            transform = svg.animateTransform(
            attributeName="transform",
            begin="0s",
            dur="20s",
            to="360 60 60",
            repeatCount="indefinite")
            transform.setAttribute("type","rotate")
            transform.setAttribute("from","0 60 60")
            r <= transform

class Linhas:
    def __init__(self):
        self.tela = svg.svg(version="1.1", viewBox="150 -10 300 300", width="1600", height="800")
        self.cena = Cena(BLACK)
        self.rects = Elemento('', x=0, y=0, w=1350, h=800, cena=self.cena)
        self.cena.vai()
        self.rects.elt <= self.tela

    def generate_art(self):
        print("Generating art")

        # Figure out where we are going to put it.
        #output_dir = os.path.join("output", collection)
        #image_path = os.path.join(output_dir, f"{name}.png")

        # Set size parameters.
        rescale = 2
        image_size_px = 128 * rescale
        padding = 12 * rescale

        # Create the directory and base image.
        # os.makedirs(output_dir, exist_ok=True)
        bg_color = (0, 0, 0)
        # image = Image.new("RGB", (image_size_px, image_size_px), bg_color)

        # How many lines do we want to draw?
        num_lines = 18
        points = []

        # Pick the colors.
        start_color = self.random_color()
        end_color = self.random_color(0.4)

        # Generate points to draw.
        for _ in range(num_lines):
            point = (
                self.random_point(image_size_px, padding),
                self.random_point(image_size_px, padding),
            )
            points.append(point)

        # Center image.
        # Find the bounding box.
        min_x = min([p[0] for p in points])
        max_x = max([p[0] for p in points])
        min_y = min([p[1] for p in points])
        max_y = max([p[1] for p in points])

        # Find offsets.
        x_offset = (min_x - padding) - (image_size_px - padding - max_x)
        y_offset = (min_y - padding) - (image_size_px - padding - max_y)

        # Move all points by offset.
        for i, point in enumerate(points):
            points[i] = (point[0] - x_offset // 2, point[1] - y_offset // 2)

        # Draw the points.
        current_thickness = 1 * rescale
        n_points = len(points) - 1
        ypoints = points[1:]+[points[0]]
        liner = zip(points, ypoints)
        #alert(list(liner))
        for i, ((i, j), (k, l)) in enumerate(liner):
            factor = i / n_points
            line_color = self.interpolate(start_color, end_color, factor=factor)
            r, g, b = *line_color
            style = {'stroke':f'rgb({r},{g},{b})', 'stroke-width':current_thickness, 'stroke-linecap':"round" }
            lin = svg.line (x1=i, y1=j, x2=k, y2=l, style=style)
            self.tela <= lin

            # Increase the thickness.
            current_thickness += rescale

        # Image is done! Now resize it to be smooth.
        '''
        image = image.resize(
            (image_size_px // rescale, image_size_px // rescale), resample=Image.ANTIALIAS
        )

        # Save the image.
        image.save(image_path)
        '''

 

    def random_color(self, delta=0):

        # I want a bright, vivid color, so max V and S and only randomize HUE.
        h = random()
        s = 1 - 0.3*random()
        v = 1
        float_rbg = colorsys.hsv_to_rgb(h, s, v)
        h = (((h + delta)*1000 ) // 1000) / 1000

        # Return as integer RGB.
        return (
            int(float_rbg[0] * 255),
            int(float_rbg[1] * 255),
            int(float_rbg[2] * 255),
        )


    def random_point(self, image_size_px: int, padding: int):
        return randint(padding, image_size_px - padding)

    def interpolate(self, start_color, end_color, factor: float):
        # Find the color that is exactly factor (0.0 - 1.0) between the two colors.
        new_color_rgb = []
        for i in range(3):
            new_color_value = factor * end_color[i] + (1 - factor) * start_color[i]
            new_color_rgb.append(int(new_color_value))

        return tuple(new_color_rgb)
       
    def make_nodes(self):
        cena = self.cena
import turtle
from browser import document

class Tartaruga:

    def __init__(self):

        turtle.set_defaults(turtle_canvas_wrapper = document['pydiv'])
        window = turtle.Screen()

        window.setup(width=800, height=600, startx=10, starty=0.5)
        self.blahaj = blahaj = turtle.Turtle() 
        blahaj.shape("turtle")
        blahaj.penup()
        blahaj.setpos(-390, 0)
        blahaj.pendown()
    def draw(self):

        current = 0  
        scale = 5 
        seen = set()
        blahaj = self.blahaj
        for step_size in range(1, 100):

            backwards = current - step_size
            if backwards > 0 and backwards not in seen:
                blahaj.setheading(90)
                blahaj.circle(scale * step_size/2, 180)
                current = backwards
                seen.add(current)

            else:
                blahaj.setheading(270) 
                blahaj.circle(scale * step_size/2, 180)
                current += step_size
                seen.add(current)

        #turtle.done()

Tartaruga().draw()
#Linhas().generate_art() #.make_rects(1300, 800)