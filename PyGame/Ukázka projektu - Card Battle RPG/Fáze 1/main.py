
import pygame
import pygame_menu
import settings as st

pygame.init()

screen = pygame.display.set_mode(
    (st.SCREEN_WIDTH, st.SCREEN_HEIGHT)
)
pygame.display.set_caption("Card Battle RPG")


# -------------------------
# CALLBACKS
# -------------------------

def start_game():
    print("Spouštím hru...")


def update_menu_size():
    """Aktualizuje velikost obou menu podle aktuální obrazovky."""
    width, height = screen.get_size()
    resolution = (width, height)

    main_menu.resize(
        width,
        height,
        screen_dimension=resolution,
        recursive=True
    )

    settings_menu.resize(
        width,
        height,
        screen_dimension=resolution,
        recursive=True
    )


def change_resolution(value, resolution):
    global screen

    print(f"Rozlišení: {resolution}")

    # Aktualizace nastavení
    st.SCREEN_WIDTH, st.SCREEN_HEIGHT = resolution

    # Změna velikosti okna
    screen = pygame.display.set_mode(resolution)

    update_menu_size()


def change_fullscreen(value):
    global screen

    if value:
        # Zapnutí fullscreen
        screen = pygame.display.set_mode(
            (0, 0),
            pygame.FULLSCREEN
        )
        print("Fullscreen: Zapnuto")

    else:
        # Návrat do okna
        screen = pygame.display.set_mode(
            (st.SCREEN_WIDTH, st.SCREEN_HEIGHT)
        )
        print("Fullscreen: Vypnuto")

    update_menu_size()


def change_volume(value):
    print(f"Hlasitost: {value} %")


# -------------------------
# SETTINGS MENU
# -------------------------

settings_menu = pygame_menu.Menu(
    "Nastavení",
    st.SCREEN_WIDTH,
    st.SCREEN_HEIGHT,
    theme=pygame_menu.themes.THEME_BLUE
)

settings_menu.add.selector(
    "Rozlišení: ",
    [
        ("800 x 600", (800, 600)),
        ("1280 x 720", (1280, 720)),
        ("1920 x 1080", (1920, 1080))
    ],
    onchange=change_resolution
)

settings_menu.add.range_slider(
    "Hlasitost: ",
    default=50,
    range_values=(0, 100),
    increment=5,
    onchange=change_volume
)

settings_menu.add.toggle_switch(
    "Fullscreen: ",
    default=False,
    onchange=change_fullscreen
)

settings_menu.add.button(
    "Zpět",
    pygame_menu.events.BACK
)


# -------------------------
# MAIN MENU
# -------------------------

main_menu = pygame_menu.Menu(
    "Card Battle RPG",
    st.SCREEN_WIDTH,
    st.SCREEN_HEIGHT,
    theme=pygame_menu.themes.THEME_BLUE
)

main_menu.add.button("Nová hra", start_game)

main_menu.add.button(
    "Nastavení",
    settings_menu
)

main_menu.add.button(
    "Konec",
    pygame_menu.events.EXIT
)


# -------------------------
# MAIN LOOP
# -------------------------

main_menu.mainloop(screen)

pygame.quit()
