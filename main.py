# Taizo CDL
# gr.407
# Tp5, paysage avec arcade

import arcade

#Mettre l'arrière plan du portrait.

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
WINDOW_TITLE = "Tutoriel Arcade"

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()

#Dessiner les trois montagne comme arrière-plan.

arcade.draw.draw_triangle_filled(400, 700, 0, 0,800, 0,arcade.color.GRAY)
arcade.draw.draw_triangle_filled(500, 770, 100, 0,900, 0,arcade.color.GRAY)
arcade.draw.draw_triangle_filled(630, 650, 230, 0,1030, 0,arcade.color.GRAY)

arcade.draw.draw_triangle_filled(900, 500, 400, 0,1200, 0,arcade.color.GRAY)
arcade.draw.draw_triangle_filled(1000, 570, 500, 0,1400, 0,arcade.color.GRAY)
arcade.draw.draw_triangle_filled(1130, 450, 730, 0,1530, 0,arcade.color.GRAY)

arcade.draw.draw_triangle_filled(200, 540, -200, 0,600, 0,arcade.color.GRAY)
arcade.draw.draw_triangle_filled(100, 570, -400, 0,500, 0,arcade.color.GRAY)

#Dessiner le soleil qui est dans le coin.

arcade.draw.draw_circle_filled(-100, 1000, 400, arcade.color.YELLOW, num_segments=100, tilt_angle=35)

#Dessiner le sol.

arcade.draw.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT / 4, arcade.csscolor.DARK_GREEN)

#Dessiner le petit lac.

arcade.draw.draw_ellipse_filled(100, 100, 500, 100,arcade.color.AIR_FORCE_BLUE)

#Dessiner le toit de la maison.

arcade.draw.draw_arc_filled(370, 260, 120, 100,arcade.color.BLUE, 217, 326, num_segments=100)

#Dessiner la structure de la maison

arcade.draw.draw_lrbt_rectangle_filled(320, 420, 130, 230,arcade.color.BROWN)

#Dessiner les pistes de la voitures sur le sol.

arcade.draw.draw_line(460, 130, 10000, 400,arcade.color.BROWN)

arcade.draw.draw_line(460, 170, 10000, 400,arcade.color.BROWN)

points = [(360, 200), (380, 200), (385, 180), (380,160), (360, 160), (355, 180)]
arcade.draw.draw_polygon_filled(points, arcade.color.AIR_SUPERIORITY_BLUE)

#Écrire le petit text au coin du portrait.

affichage = arcade.Text("Ceci est une petite maison sur le bout de la montagne...", 800, SCREEN_HEIGHT - 40, arcade.color.ARMY_GREEN)
affichage.draw()

arcade.finish_render()

arcade.run()

