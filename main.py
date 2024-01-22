from p3dray import *

set_environment_texture("meadow_2_2k.jpg")


rotateY(radians(30))
translate(0,0,5)

set_material(base_color=[1,0.8,0.8], metalic=1, roughness=1)
box(2.2,2.2,2.2)


render(sample_N=5)