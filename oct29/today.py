from PIL import Image

def sepia(pixel):
    (r, g, b) = pixel
    
    r = int(r * .393 + g * .769 + b * .189)
    g = int(r * .349 + g * .686 + b * .168)
    b = int(r * .272 + g * .534 + b * .131)
    
    return (r, g, b)
    
def luminance(pixel):
    (r, g, b) = pixel
    
    return (r + g + b) // 3


def filter(image):
    pic = image.copy()
    
   
    
    for x in range(image.width):
        for y in range(image.height):
            (r, g, b) = image.getpixel((x, y))


#            if luminance((r, g, b)) < 128:
#                (r, g, b) = (0, 0, 0)
#            else:
#                (r, g, b) = (255, 255, 255)    
#            factor = 1.1
            
#            r = int(r * factor)
#            g = int(g * factor)
#            b = int(b * factor)

            (r, g, b) = sepia((r, g, b))
#            r = g = b = luminance((r, g, b))
            
            

            pic.putpixel((x, y), (r, g, b))

    return pic

def blur(image):
    for _ in range(4):
        image = blurSmall(image)

    return image

def blurSmall(image):
    pic = image.copy()
    
    
    for x in range(image.width):
        for y in range(image.height):
            (r, g, b) = image.getpixel((x, y))
            count = 1
            
            if x > 0:
                (red, green, blue) = image.getpixel((x - 1, y))
                r += red
                g += green
                b += blue
                count += 1

            if x < image.width - 1:
                (red, green, blue) = image.getpixel((x + 1, y))
                r += red
                g += green
                b += blue
                count += 1

            if y > 0:
                (red, green, blue) = image.getpixel((x, y - 1))
                r += red
                g += green
                b += blue
                count += 1

            if y < image.height - 1:
                (red, green, blue) = image.getpixel((x, y + 1))
                r += red
                g += green
                b += blue
                count += 1

            r = r // count
            g = g // count
            b = b // count
            
            pic.putpixel((x, y), (r, g, b))

    return pic

def distance(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** .5

def circleCut(image, center, width, bwidth):
    for x in range(image.width):
        for y in range(image.height):
            (r, g, b) = image.getpixel((x, y))

            if distance(center, (x, y)) > width:
                lum = luminance((r, g, b))
                (r, g, b) = (lum, lum, lum)
            elif distance(center, (x, y)) > width:
                amt = abs(width - distance(center, (x, y)))
                (r, g, b) = (int(r + (255 - r) * (amt / bwidth)), int(g + (255 - g) * (amt / bwidth)), int(b + (255 - b)* (amt / bwidth)))

            image.putpixel((x, y), (r, g, b))
    return image

def start():
    pic = Image.open("ginger.jpeg")
    
#    pic = pic.resize((500, 500))
    
    pic = pic.reduce(4)
#    pic.show()
    
    pic = circleCut(pic, (pic.width // 2, pic.height // 2), 200, 60)
    
    pic.show()

if __name__ == "__main__":
    start()
