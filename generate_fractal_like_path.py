import matplotlib.pyplot as plt
import random

def generate_fractal_like_path(num_points=1000000, step=1):
    x, y = 0, 0
    direction = (1, 0)
    path = [(x, y)]
    visited = {(x, y)}  

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while len(path) < num_points:
        if random.random() < 0.2:
            turn = random.choice([-1, 1])
            idx = directions.index(direction)
            direction = directions[(idx + turn) % 4]

        dx, dy = direction
        next_x = x + dx * step
        next_y = y + dy * step
        next_point = (next_x, next_y)

        if next_point not in visited:
            x, y = next_x, next_y
            path.append((x, y))
            visited.add((x, y))
        else:
            available_directions = []
            for dx, dy in directions:
                test_x = x + dx * step
                test_y = y + dy * step
                if (test_x, test_y) not in visited:
                    available_directions.append((dx, dy))

            if available_directions:
                direction = random.choice(available_directions)
                x += direction[0] * step
                y += direction[1] * step
                path.append((x, y))
                visited.add((x, y))
            else:
                if len(path) > 1:
                    path.pop()  
                    x, y = path[-1]  
                else:
                    break

    return path

def draw_path(path, title="Fractal-like Path"):
    x, y = zip(*path)
    plt.figure(figsize=(14, 12))
    plt.plot(x, y, linewidth=0.3, color='mediumpurple')
    plt.title(f"{title} (n={len(path)})")
    plt.axis("equal")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    path = generate_fractal_like_path(num_points=1000000, step=1)
    draw_path(path)
