class Player():
    """Playerクラス
    プレイヤー
    """

    def __init__(self, pos=[0, 0]):
        self.pos = pos

    def move(self, pos):
        """move関数
        プレイヤーの移動後の座標を返す関数

        Args:
            pos (list[x, y]): 移動先のプレイヤーの座標

        Returns:
            self.pos (list[x, y]): 移動後のプレイヤーの座標

        Examples:
            >>> player_pos = move(move_pos)
        """

        self.pos[0] += pos[0]
        self.pos[1] += pos[1]
        return self.pos

    def get_position(self):
        """get_position関数
        プレイヤーの座標を返す関数

        Returns:
            self.pos (list[x, y]): プレイヤーの座標

        Examples:
            >>> player_pos = get_position()
        """

        return self.pos