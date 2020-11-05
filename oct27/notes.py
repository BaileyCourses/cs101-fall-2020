from PIL import Image

def grey(image):
    image = image.copy()
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            
#            gPix = grayPixel(pixel)
            gPix = blurPixel(image, x, y)
            image.putpixel((x, y), gPix)
    return image

def luminance(pixel):
    (r, g, b) = pixel

    return (r + g + b) // 3

def grayPixel(pixel):
    shade = luminance(pixel)

    return (shade, shade, shade)

def bwPixel(pixel):
    shade = luminance(pixel)

    if shade < 128:
        return (0, 0, 0)
    else:
        return (255, 255, 255)

def sepiaPixel(pixel):
    (red, green, blue) = pixel

    red = int(red * .393 + green * .769 + blue * .189)
    green = int(red * .349 + green * .686 + blue * .168)
    blue = int(red * .272 + green * .534 + blue * .131)
    return (red, green, blue)

def blurPixel(image, x, y):

    (width, height) = image.size

    count = 1
    (red, green, blue) = image.getpixel((x, y))

    if x + 1 < width:
        (r, g, b) = image.getpixel((x + 1, y))
        count += 1
        red += r
        green += g
        blue += b

    if x - 1 >= 0:
        (r, g, b) = image.getpixel((x - 1, y))
        count += 1
        red += r
        green += g
        blue += b

    if y + 1 < height:
        (r, g, b) = image.getpixel((x, y + 1))
        count += 1
        red += r
        green += g
        blue += b

    if y - 1 >= 0:
        (r, g, b) = image.getpixel((x, y - 1))
        count += 1
        red += r
        green += g
        blue += b

    red //= count
    green//= count
    blue //= count

    pixel = (red, green, blue)

    return pixel

def start():
    pic = Image.open("ginger.jpeg")

    print(pic.size)

    print(pic.size[0]*pic.size[1])

#    pic = pic.crop((0, 0, 1000, 1000))

#    pic = pic.resize((500, 500))

     pic = pic.reduce(4)

#    pic.show()

    pic = grey(pic)
    
    pic = grey(pic)
    
    pic.show()

#    pic.save("ginger-sepia.jpeg", "JPEG")

if __name__ == "__main__":
    start()
