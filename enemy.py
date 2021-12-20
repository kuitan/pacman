from player import Player

class Enemy(Player):
    """Enemyクラス
    敵キャラクター
    """

    def __init__(self, enemy1_pos=[0, 0], enemy2_pos=[1, 0], enemy3_pos=[0, 1], enemy4_pos=[1, 1]):
        self.pos = {'enemy1': enemy1_pos,
                    'enemy2': enemy2_pos,
                    'enemy3': enemy3_pos,
                    'enemy4': enemy4_pos}
        self.num = len(self.pos)

    def move(self, pos):
        """move関数
        エネミーの移動後の座標を返す関数

        Args:
            pos (dic{'enemy1': [x, y], ...}): 移動先のエネミーの座標

        Returns:
            self.pos (dic{'enemy1': [x, y], ...}): 移動後のエネミーの座標

        Examples:
            >>> enemy_pos = move(move_pos)
        """

        for i in range(self.num):
            self.pos[f'enemy{i+1}'][0] += pos[f'enemy{i+1}'][0]
            self.pos[f'enemy{i+1}'][1] += pos[f'enemy{i+1}'][1]
        return self.pos