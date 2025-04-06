import matplotlib.pyplot as plt
import random

def generate_closed_orthogonal_polygon(num_points=100000, step=1):
    assert num_points >= 4 and num_points % 2 == 0, "Số điểm nên là chẵn và >= 4 để đóng kín"

    x, y = 0, 0
    direction = (1, 0)  # bắt đầu đi sang phải
    path = [(x, y)]

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # phải, lên, trái, xuống

    for _ in range(num_points - 2):  # -2 vì còn 1 điểm cuối để đóng kín
        # Ngẫu nhiên rẽ trái hoặc phải, hoặc đi thẳng
        if random.random() < 0.3:
            turn = random.choice([-1, 1])  # rẽ trái hoặc phải
            idx = directions.index(direction)
            direction = directions[(idx + turn) % 4]

        dx, dy = direction
        x += dx * step
        y += dy * step
        path.append((x, y))

    # Đóng kín polygon bằng cách quay về điểm đầu
    path.append(path[0])
    return path

def draw_path(path, title="Closed Orthogonal Polygon"):
    x, y = zip(*path)
    plt.figure(figsize=(12, 10))
    plt.plot(x, y, linewidth=0.5, color='blue')
    plt.title(f"{title} (n={len(path)})")
    plt.axis("equal")
    plt.axis("off")
    plt.show()

# ------ MAIN -------
if __name__ == "__main__":
    path = generate_closed_orthogonal_polygon(num_points=100000, step=1)
    draw_path(path)
