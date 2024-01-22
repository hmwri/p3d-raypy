from p3dray.scene import scene
from p3dray.geometry import Surface, Vertex, Object


def __plane(v1:Vertex, v2:Vertex, v3:Vertex ,v4:Vertex) -> list[Surface]:
    return [Surface(v1, v2, v3),
    Surface(v3, v4, v1)]

def box(x_l, y_l, z_l):
    scene.objects.append(
        # フロント面
        Object([
            *__plane(
                Vertex(-x_l / 2, -y_l / 2, z_l / 2),
                Vertex(x_l / 2, -y_l / 2, z_l / 2),
                Vertex(x_l / 2, y_l / 2, z_l / 2),
                Vertex(-x_l / 2, y_l / 2, z_l / 2)
            ),

            # バック面
            *__plane(
                Vertex(-x_l / 2, -y_l / 2, -z_l / 2),
                Vertex(x_l / 2, -y_l / 2, -z_l / 2),
                Vertex(x_l / 2, y_l / 2, -z_l / 2),
                Vertex(-x_l / 2, y_l / 2, -z_l / 2)
            ),

            # トップ面
            *__plane(
                Vertex(-x_l / 2, y_l / 2, -z_l / 2),
                Vertex(x_l / 2, y_l / 2, -z_l / 2),
                Vertex(x_l / 2, y_l / 2, z_l / 2),
                Vertex(-x_l / 2, y_l / 2, z_l / 2)
            ),

            # ボトム面
            *__plane(
                Vertex(-x_l / 2, -y_l / 2, -z_l / 2),
                Vertex(x_l / 2, -y_l / 2, -z_l / 2),
                Vertex(x_l / 2, -y_l / 2, z_l / 2),
                Vertex(-x_l / 2, -y_l / 2, z_l / 2)
            ),


            *__plane(
                Vertex(-x_l / 2, -y_l / 2, -z_l / 2),
                Vertex(-x_l / 2, -y_l / 2, z_l / 2),
                Vertex(-x_l / 2, y_l / 2, z_l / 2),
                Vertex(-x_l / 2, y_l / 2, -z_l / 2)
            ),
            #
            # ライト面
            *__plane(
                Vertex(x_l / 2, -y_l / 2, -z_l / 2),
                Vertex(x_l / 2, -y_l / 2, z_l / 2),
                Vertex(x_l / 2, y_l / 2, z_l / 2),
                Vertex(x_l / 2, y_l / 2, -z_l / 2)
            )
        ])

    )
