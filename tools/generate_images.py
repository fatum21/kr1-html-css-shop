# -*- coding: utf-8 -*-
"""Генератор локальных SVG-изображений для проекта kr1-html-css-shop.
Все картинки — векторные, поэтому проект полностью автономен и работает офлайн.
"""
import os

BASE = r"C:\Users\ROMA\Desktop\kr1-html-css-shop\images"
os.makedirs(BASE, exist_ok=True)


def glyph(kind):
    """Простая векторная иконка-силуэт устройства."""
    white = "#ffffff"
    glass = "rgba(15,23,42,0.22)"
    g2 = "rgba(15,23,42,0.35)"
    if kind == "laptop":
        return f'''  <ellipse cx="400" cy="392" rx="230" ry="26" fill="rgba(15,23,42,0.18)"/>
  <rect x="252" y="168" width="296" height="196" rx="16" fill="{white}"/>
  <rect x="270" y="186" width="260" height="160" rx="9" fill="{glass}"/>
  <path d="M206 372 h388 l32 42 h-452 z" fill="{white}"/>'''
    if kind == "phone":
        return f'''  <ellipse cx="400" cy="440" rx="150" ry="22" fill="rgba(15,23,42,0.18)"/>
  <rect x="326" y="112" width="188" height="316" rx="30" fill="{white}"/>
  <rect x="342" y="146" width="156" height="252" rx="14" fill="{glass}"/>
  <rect x="388" y="124" width="64" height="11" rx="6" fill="{g2}"/>'''
    if kind == "tablet":
        return f'''  <ellipse cx="400" cy="424" rx="190" ry="22" fill="rgba(15,23,42,0.18)"/>
  <rect x="286" y="126" width="268" height="288" rx="24" fill="{white}"/>
  <rect x="304" y="150" width="232" height="232" rx="12" fill="{glass}"/>
  <circle cx="420" cy="398" r="7" fill="{g2}"/>'''
    if kind == "watch":
        return f'''  <rect x="366" y="86" width="68" height="90" rx="16" fill="{g2}"/>
  <rect x="366" y="344" width="68" height="90" rx="16" fill="{g2}"/>
  <rect x="344" y="140" width="152" height="230" rx="44" fill="{white}"/>
  <rect x="362" y="166" width="116" height="178" rx="26" fill="{glass}"/>'''
    if kind == "headphones":
        return f'''  <path d="M250 300 v-40 a150 150 0 0 1 300 0 v40" fill="none" stroke="{white}" stroke-width="30" stroke-linecap="round"/>
  <rect x="222" y="286" width="66" height="120" rx="30" fill="{white}"/>
  <rect x="512" y="286" width="66" height="120" rx="30" fill="{white}"/>
  <rect x="236" y="306" width="38" height="80" rx="18" fill="{glass}"/>
  <rect x="526" y="306" width="38" height="80" rx="18" fill="{glass}"/>'''
    if kind == "console":
        return f'''  <ellipse cx="400" cy="392" rx="210" ry="24" fill="rgba(15,23,42,0.18)"/>
  <rect x="252" y="180" width="296" height="180" rx="30" fill="{white}"/>
  <circle cx="336" cy="270" r="26" fill="{glass}"/>
  <circle cx="464" cy="270" r="26" fill="{glass}"/>
  <rect x="330" y="330" width="140" height="12" rx="6" fill="{g2}"/>'''
    if kind == "monitor":
        return f'''  <ellipse cx="400" cy="424" rx="200" ry="22" fill="rgba(15,23,42,0.18)"/>
  <rect x="228" y="146" width="344" height="216" rx="16" fill="{white}"/>
  <rect x="248" y="166" width="304" height="176" rx="9" fill="{glass}"/>
  <rect x="382" y="362" width="36" height="46" fill="{white}"/>
  <rect x="314" y="404" width="172" height="16" rx="8" fill="{white}"/>'''
    if kind == "keyboard":
        rows = ""
        for r in range(3):
            for c in range(10):
                rows += f'<rect x="{238 + c*33}" y="{230 + r*34}" width="26" height="26" rx="6" fill="{g2}"/>'
        return f'''  <ellipse cx="400" cy="404" rx="200" ry="22" fill="rgba(15,23,42,0.18)"/>
  <rect x="220" y="196" width="360" height="176" rx="20" fill="{white}"/>
  {rows}
  <rect x="238" y="332" width="200" height="26" rx="6" fill="{g2}"/>'''
    if kind == "mouse":
        return f'''  <ellipse cx="400" cy="424" rx="130" ry="22" fill="rgba(15,23,42,0.18)"/>
  <rect x="324" y="150" width="152" height="252" rx="76" fill="{white}"/>
  <rect x="392" y="166" width="16" height="52" rx="8" fill="{glass}"/>
  <path d="M326 254 h148" stroke="{glass}" stroke-width="8"/>'''
    if kind == "camera":
        return f'''  <ellipse cx="400" cy="418" rx="190" ry="22" fill="rgba(15,23,42,0.18)"/>
  <rect x="248" y="196" width="304" height="200" rx="28" fill="{white}"/>
  <circle cx="400" cy="296" r="66" fill="{glass}"/>
  <circle cx="400" cy="296" r="34" fill="{g2}"/>
  <rect x="356" y="168" width="88" height="34" rx="10" fill="{white}"/>
  <circle cx="300" cy="228" r="12" fill="{g2}"/>'''
    if kind == "speaker":
        return f'''  <ellipse cx="400" cy="424" rx="160" ry="22" fill="rgba(15,23,42,0.18)"/>
  <rect x="312" y="140" width="176" height="288" rx="28" fill="{white}"/>
  <circle cx="400" cy="212" r="38" fill="{glass}"/>
  <circle cx="400" cy="318" r="52" fill="{glass}"/>
  <circle cx="400" cy="318" r="24" fill="{g2}"/>'''
    if kind == "router":
        return f'''  <ellipse cx="400" cy="392" rx="200" ry="22" fill="rgba(15,23,42,0.18)"/>
  <rect x="258" y="262" width="284" height="120" rx="22" fill="{white}"/>
  <path d="M330 262 l-30 -96" stroke="{white}" stroke-width="16" stroke-linecap="round"/>
  <path d="M470 262 l30 -96" stroke="{white}" stroke-width="16" stroke-linecap="round"/>
  <circle cx="330" cy="332" r="11" fill="{g2}"/>
  <circle cx="366" cy="332" r="11" fill="{g2}"/>
  <circle cx="402" cy="332" r="11" fill="{g2}"/>'''
    return f'<rect x="300" y="200" width="200" height="200" rx="24" fill="{white}"/>'


def product_svg(title, subtitle, kind, c1, c2):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" role="img" aria-label="{title}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{c1}"/>
      <stop offset="1" stop-color="{c2}"/>
    </linearGradient>
  </defs>
  <rect width="800" height="600" fill="url(#bg)"/>
  <circle cx="120" cy="110" r="140" fill="rgba(255,255,255,0.12)"/>
  <circle cx="700" cy="500" r="180" fill="rgba(255,255,255,0.10)"/>
  {glyph(kind)}
  <text x="400" y="524" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="40" font-weight="700" fill="#ffffff">{title}</text>
  <text x="400" y="562" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="24" fill="rgba(255,255,255,0.85)">{subtitle}</text>
</svg>
'''


PRODUCTS = [
    ("product-laptop.svg", "Aurora 14 Pro", "Ноутбук", "laptop", "#2b59ff", "#6d5bff"),
    ("product-smartphone.svg", "Nexus X5", "Смартфон", "phone", "#0ea5e9", "#2563eb"),
    ("product-headphones.svg", "SonicBuds Pro", "Наушники", "headphones", "#7c3aed", "#c026d3"),
    ("product-watch.svg", "Pulse S2", "Умные часы", "watch", "#059669", "#10b981"),
    ("product-tablet.svg", "Slate 11", "Планшет", "tablet", "#f97316", "#f59e0b"),
    ("product-console.svg", "Vortex One", "Консоль", "console", "#e11d48", "#f43f5e"),
    ("product-monitor.svg", "ViewPro 27", "Монитор", "monitor", "#0891b2", "#0ea5e9"),
    ("product-keyboard.svg", "MechType K70", "Клавиатура", "keyboard", "#475569", "#64748b"),
    ("product-mouse.svg", "GlideX Pro", "Мышь", "mouse", "#db2777", "#ec4899"),
    ("product-camera.svg", "SnapLens R6", "Камера", "camera", "#334155", "#1e293b"),
    ("product-speaker.svg", "BoomCube Mini", "Колонка", "speaker", "#ea580c", "#f97316"),
    ("product-router.svg", "AirLink AX6", "Роутер", "router", "#0284c7", "#38bdf8"),
    ("product-laptop-lite.svg", "Aurora 14 Lite", "Ноутбук", "laptop", "#3b82f6", "#60a5fa"),
    ("product-laptop-aurora16.svg", "Aurora 16 Max", "Ноутбук", "laptop", "#1d4ed8", "#3b82f6"),
    ("product-laptop-slatebook.svg", "Slate Book Air", "Ноутбук", "laptop", "#0ea5e9", "#22d3ee"),
    ("product-laptop-workbook.svg", "WorkBook 15", "Ноутбук", "laptop", "#64748b", "#94a3b8"),
    ("product-laptop-titan.svg", "Titan GX16", "Ноутбук", "laptop", "#dc2626", "#f97316"),
    ("product-laptop-angle2.svg", "Aurora 14 Pro", "Вид сбоку", "laptop", "#2b59ff", "#5a7cff"),
    ("product-laptop-angle3.svg", "Aurora 14 Pro", "Корпус", "laptop", "#1c3fd6", "#4b6bff"),
]

for fname, title, subtitle, kind, c1, c2 in PRODUCTS:
    with open(os.path.join(BASE, fname), "w", encoding="utf-8") as f:
        f.write(product_svg(title, subtitle, kind, c1, c2))

# Логотип
logo = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="Логотип ТехноМарт">
  <defs>
    <linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#2b59ff"/>
      <stop offset="1" stop-color="#6d5bff"/>
    </linearGradient>
  </defs>
  <rect width="64" height="64" rx="16" fill="url(#lg)"/>
  <path d="M20 22h24v6H36v18h-8V28h-8z" fill="#ffffff"/>
</svg>
'''
with open(os.path.join(BASE, "logo.svg"), "w", encoding="utf-8") as f:
    f.write(logo)
with open(os.path.join(BASE, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(logo)

# Иллюстрация для hero-блока
hero = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 480" role="img" aria-label="Иллюстрация витрины электроники">
  <defs>
    <linearGradient id="hb" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#e6ecff"/>
      <stop offset="1" stop-color="#f4f0ff"/>
    </linearGradient>
  </defs>
  <rect width="640" height="480" rx="24" fill="url(#hb)"/>
  <rect x="70" y="90" width="300" height="190" rx="14" fill="#ffffff"/>
  <rect x="86" y="106" width="268" height="150" rx="8" fill="#2b59ff" opacity="0.18"/>
  <path d="M40 280 h360 l28 36 H12 z" fill="#ffffff"/>
  <rect x="400" y="150" width="150" height="230" rx="26" fill="#ffffff"/>
  <rect x="416" y="176" width="118" height="178" rx="12" fill="#6d5bff" opacity="0.22"/>
  <rect x="452" y="160" width="46" height="10" rx="5" fill="#c7cede"/>
  <circle cx="150" cy="360" r="10" fill="#2b59ff"/>
  <circle cx="120" cy="360" r="10" fill="#9fb0ff"/>
  <circle cx="90" cy="360" r="10" fill="#d7dcff"/>
  <rect x="330" y="350" width="240" height="18" rx="9" fill="#ffffff"/>
  <rect x="330" y="384" width="190" height="18" rx="9" fill="#ffffff"/>
</svg>
'''
with open(os.path.join(BASE, "hero-devices.svg"), "w", encoding="utf-8") as f:
    f.write(hero)

# Стилизованная «карта» для страницы контактов
map_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" role="img" aria-label="Схема расположения магазина">
  <rect width="800" height="420" fill="#e9eef7"/>
  <path d="M0 150 H800" stroke="#ffffff" stroke-width="26"/>
  <path d="M0 300 H800" stroke="#ffffff" stroke-width="26"/>
  <path d="M220 0 V420" stroke="#ffffff" stroke-width="26"/>
  <path d="M560 0 V420" stroke="#ffffff" stroke-width="26"/>
  <rect x="40" y="40" width="140" height="90" rx="8" fill="#dbe3f2"/>
  <rect x="270" y="180" width="240" height="90" rx="8" fill="#dbe3f2"/>
  <rect x="610" y="40" width="150" height="90" rx="8" fill="#dbe3f2"/>
  <rect x="610" y="330" width="150" height="60" rx="8" fill="#dbe3f2"/>
  <path d="M395 120 c-30 0 -54 24 -54 54 c0 40 54 96 54 96 s54 -56 54 -96 c0 -30 -24 -54 -54 -54 z" fill="#2b59ff"/>
  <circle cx="395" cy="174" r="20" fill="#ffffff"/>
  <text x="395" y="300" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="20" fill="#5a6377">ТехноМарт, Москва, ул. Программистов, 15</text>
</svg>
'''
with open(os.path.join(BASE, "map.svg"), "w", encoding="utf-8") as f:
    f.write(map_svg)

print("Готово:", len(os.listdir(BASE)), "файлов в", BASE)
print("\n".join(sorted(os.listdir(BASE))))
