import curses
import random

def generate_random_box(rows, cols):
    box = []
    for _ in range(rows):
        row = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(cols))
        box.append(row)
    return box

def draw_box(stdscr, box, start_row, start_col):
    for i, row in enumerate(box):
        stdscr.addstr(start_row + i, start_col, row)

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    box_rows = 4
    box_cols = 9
    box_start_row = 2
    box_start_col = 2

    box = generate_random_box(box_rows, box_cols)
    draw_box(stdscr, box, box_start_row, box_start_col)

    while True:
        key = stdscr.getch()

        if key == ord('r') or key == ord('R'):
            random_row = random.randint(0, box_rows - 1)
            random_col = random.randint(0, box_cols - 1)
            box[random_row] = box[random_row][:random_col] + random.choice('abcdefghijklmnopqrstuvwxyz') + box[random_row][random_col + 1:]
            
            stdscr.clear()
            draw_box(stdscr, box, box_start_row, box_start_col)
        
        elif key == ord('q') or key == ord('Q'):
            break

if __name__ == "__main__":
    curses.wrapper(main)
