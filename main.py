import json
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# JSON読み込み
with open("src/polygons_rocket.json", "r") as f:
    data = json.load(f)

polygons = data["items"] if "items" in data else data

# 保存フォルダ作成
save_dir = "polygon_images"
os.makedirs(save_dir, exist_ok=True)

# まとめ用の図を作成
fig_all, ax_all = plt.subplots(figsize=(6, 6))
ax_all.set_aspect("equal")
ax_all.set_xlim(-5.5, 5.5)  # 座標範囲を -5.5～5.5 に変更
ax_all.set_ylim(-5.5, 5.5)
ax_all.set_title("All Polygons")
ax_all.set_xlabel("X")
ax_all.set_ylabel("Z")
ax_all.grid(True)

# 各ポリゴンごとに個別画像保存
for i, poly in enumerate(polygons):
    verts = [(v["x"], v["z"]) for v in poly["vertices"]]
    
    # --- 個別画像 ---
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect("equal")
    plt.title(f"Polygon ID {i}")
    plt.xlabel("X")
    plt.ylabel("Z")
    ax.set_xlim(-5.5, 5.5)  # 座標範囲を -5.5～5.5 に変更
    ax.set_ylim(-5.5, 5.5)
    ax.grid(True)

    patch = Polygon(verts, fill=False, linewidth=2)
    ax.add_patch(patch)

    cx = sum(v[0] for v in verts) / len(verts)
    cy = sum(v[1] for v in verts) / len(verts)
    ax.text(cx, cy, str(i), color="red", fontsize=12)

    plt.savefig(f"{save_dir}/polygon_{i:03d}.png")
    plt.close()

    # --- 全体図に追加 ---
    patch_all = Polygon(verts, fill=False, linewidth=1)
    ax_all.add_patch(patch_all)
    ax_all.text(cx, cy, str(i), color="blue", fontsize=8)

# 全ポリゴンまとめ画像保存
plt.savefig(f"{save_dir}/all_polygons.png")
plt.close()

print(f"保存完了！ → {save_dir}/ 内に生成されました 🎉")
