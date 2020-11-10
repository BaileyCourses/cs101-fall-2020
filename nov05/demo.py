from PIL import Image

White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

def menu():
    choice = "No choice"
    while choice not in "CDKLSXGEZNWA":
        print()
        print("C - Copy image A to image B")
        print("D - Display image A")
        print("K - Catinate image B to image A")
        print("L - Load image from file into image A")
        print("S - Save image A to file")
        print("X - Exchange image A and B")
        print("G - Grayscale A")
        print("Z - Show sizes of images")
        print("N - New York Times process image")
        print("A - compute number of colors in an image")
        print("W - warmup")
        print("E - Exit")
        choice = input("Which menu item? ").upper()
        
    print("Executing...")
    return choice

def manip(image):
    result = image.copy()

    for y in range(image.width):
        for x in range(y, image.width):
            pixel = image.getpixel((x, y))
            result.putpixel((y, x), pixel)

    return result

def catinate(left, right):

    # This function only works for images of the same height!

    result = Image.new("RGB", (left.width + right.width, left.height))
    
    for x in range(left.width):
        for y in range(left.height):
            pixel = left.getpixel((x, y))
            result.putpixel((x, y), pixel)
            pixel = right.getpixel((x, y))
            result.putpixel((left.width + x, y), pixel)

    return result

def luminance(pixel):
    (r, g, b) = pixel
    return (r + g + b) // 3
    
def nytimes(image):
    result = image.copy()
    
    pixels = []
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            lum = luminance(pixel)
            pixels.append((lum, pixel))
            
    pixels.sort()
    
    index = 0
    for y in range(image.height):
        for x in range(image.width):
            lum, pixel = pixels[index]
            result.putpixel((x, y), pixel)
            index += 1

    return result

def numColors(image):
    colors = {}
    
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            if pixel in colors:
                colors[pixel] += 1
            else:
                colors[pixel] = 1
        print(len(colors.keys()))
                
    return len(colors.keys())

def first1():
    favColors = {}
    
    favColors["Mike"] = "Blue"
    favColors["Mark"] = "Red"
    favColors["Sue"] = "Green"
    favColors["David"] = "Indigo"
    favColors["Sam"] = (255, 255, 255)
    
    print(favColors["David"])
    
    for key in favColors:
        print(key, favColors[key])
        

def first():
    choice = menu()
    imageA = Image.new("RGB", (100, 100))
    imageB = Image.new("RGB", (100, 100))

    imageA = Image.open("ginger.jpeg")
    imageA = reshape(imageA)

    while choice != "E":
        if choice == "C":
            imageB = imageA.copy()
            
        elif choice == "A":
            num = numColors(imageA)
            print("Number of colors is", num)

        elif choice == "D":
            print("Displaying image...")
            imageA.show()
            print(imageA.size)

        elif choice == "K":
            imageA = catinate(imageA, imageB)
            
        elif choice == "L":
            print("Loading file...")
            name = input("Enter the name of the file: ")
            imageA = Image.open(name)
            imageA = reshape(imageA)

        elif choice == "S":
            name = input("Enter the name of the file: ")
            imageA.save(name)

        elif choice == "X":
            tmp = imageB
            imageB = imageA
            imageA = tmp

        elif choice == "R":
            imageA = reshape(imageA)

        elif choice == "G":
            imageA = grayScale(imageA)

        elif choice == "F":
            imageA = findEdges(imageA)

        elif choice == "A":
            imageA = addEdges(imageA, imageB)

        elif choice == "N":
            imageA = nytimes(imageA)
            
        elif choice == "W":
            imageA = manip(imageA)
            
        elif choice == "Z":
            print("Image A:", imageA.size)
            print("Image B:", imageB.size)

        choice = menu()

def grayPixel(pixel):
    lum = luminance(pixel)
    return (lum, lum, lum)


def avePixels(pixels):
    Rave = Gave = Bave = 0

    for (r, g, b) in pixels:
        Rave += r
        Gave += g
        Bave += b
    Rave //= len(pixels)
    Gave //= len(pixels)
    Bave //= len(pixels)

    return (Rave, Gave, Bave)
    

def grayScale(image):
    result = image.copy()
    
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            pixel = grayPixel(pixel)
            result.putpixel((x, y), pixel)

    return result

def nytimes1(image):
    result = image.copy()

    pixels = []
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            lum = luminance(pixel)
            pixels.append((lum, pixel))

    pixels.sort()

    index = 0
    for y in range(image.height):
        for x in range(image.width):
            lum, pixel = pixels[index]
            result.putpixel((x, y), pixel)
            index += 1

    return result

def addEdges(imageA, imageB):
    result = imageA.copy()
    
    for x in range(imageA.width):
        for y in range(imageA.height):
            edge = imageB.getpixel((x, y))
            if edge == Black:
                result.putpixel((x, y), Black)

    return result


def findEdges(image, thresh = 10):
    result = image.copy()
    
    for x in range(image.width - 1):
        for y in range(image.height - 1):
            pixel = image.getpixel((x, y))
            right = image.getpixel((x + 1, y))
            down = image.getpixel((x, y + 1))

            if ((abs(luminance(pixel) - luminance(right)) > thresh) or
                (abs(luminance(pixel) - luminance(down)) > thresh)):
                pixel = Black
            else:
                pixel = White
                
            result.putpixel((x, y), pixel)

    for x in range(image.width):
        result.putpixel((x, image.height - 1), White)
    for y in range(image.height - 1):
        result.putpixel((image.width - 1, y), White)

    return result

def reshape(image, size = (800, 800)):
    width, height = size

    # If the original is too wide, we need to cut off the sides

    if (image.width / image.height) > (width / height):

        newWidth = int(height / image.height * image.width)
        newHeight = height

        image = image.resize((newWidth, newHeight))

        image = image.crop(((newWidth - width) // 2, 0, (newWidth - width) // 2 + width, height))

    # If the original is too tall, we need to cut off the top and bottom

    elif (image.width / image.height) < (width / height):

        newWidth = width
        newHeight = int(width / image.width * image.height)

        image = image.resize((newWidth, newHeight))
        
        image = image.crop((0, (newHeight - height) // 2, width, (newHeight - height) // 2 + height))

    # If everything is equal, we are set

    else:

        image = image.resize((width, height))

    return image

if __name__ == "__main__":
    first()
