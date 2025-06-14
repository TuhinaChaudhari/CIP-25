from graphics import Canvas
import random
import time

WIDTH, HEIGHT = 600, 500

# Sample words
words = ["ocean", "forest", "mountain", "city", "desert"]

# Color palette (good for mental health)
palette_colors = ["#3F88C5", "#FFF44F", "#FFC0CB", "#C8A2C8", "#006400", "#8B4513"]  

def draw_palette(canvas):
    box_size = 50
    spacing = 10
    for i, color in enumerate(palette_colors):
        x = spacing + i * (box_size + spacing)
        y = 10
        canvas.create_rectangle(x, y, x + box_size, y + box_size, color)

def draw_word(canvas, word):
    # Draw centered text using create_text
    text_width = 100  
    text_height = 20  
    x = (WIDTH // 2) - (text_width // 2)
    y = 100
    canvas.create_text(x, y, word)

def get_related_words():
    print("Enter 5 things you relate to the word on Canvas (press Enter after each):")
    related = []
    for i in range(5):
        word = input(f"Related word {i+1}: ")
        related.append(word)
    return related

def draw_related_words(canvas, words_list, y_pos=130):
    full_text = ", ".join(words_list)
    text_width = 300  # approximate width
    x = (WIDTH // 2) - (text_width // 2)
    canvas.create_text(x, y_pos, full_text)

def main():
    canvas = Canvas(WIDTH, HEIGHT)
    canvas.create_rectangle(0, 0, WIDTH, HEIGHT, "white")  # white background

    draw_palette(canvas)

    current_word = random.choice(words)
    draw_word(canvas, current_word)

    related_words = get_related_words()
    draw_related_words(canvas, related_words)

    print("Program started. Click on canvas to draw.")

    # Default color is first in palette
    current_color = palette_colors[0]
    box_size = 50
    spacing = 10
    clicks_handled = 0

    while True:
        # Check for clicks
        clicks = canvas.get_new_mouse_clicks()
        for click in clicks:
            try:
                x_str, y_str = str(click).split(",")
                x, y = float(x_str), float(y_str)
            except Exception as e:
                print(f"Error parsing click coordinates: {e}")
                continue

            # Check if click is inside palette to change color
            for i, color in enumerate(palette_colors):
                px = spacing + i * (box_size + spacing)
                py = 10
                if px <= x <= px + box_size and py <= y <= py + box_size:
                    current_color = color
                    print(f"Selected color: {current_color}")
                    break
            else:
                # Draw circle on canvas at click position using selected color
                canvas.create_oval(x - 10, y - 10, x + 10, y + 10, current_color)

        time.sleep(0.05)

if __name__ == "__main__":
    main()
