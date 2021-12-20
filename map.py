class Map():
    """Mapクラス
    マップ生成系
    """

    def __init__(self, map_array=[], file_name='map1.txt'):
        self.map_array = map_array
        self.file_name = file_name
        self.feed_num = 0

    def read_map(self, player_pos, map_type=0):
        """read_map関数
        マップを読み込む関数

        Args:
            player_pos (list[x, y]): プレイヤーの初期座標
            map_type (int): マップの種類

        Returns:
            lines (list): txtファイルからマップを読み込みリストを返す

        Examples:
            >>> map_list = read_map([0, 0], map_type=0)
        """

        lines = []
        if map_type == 0:
            self.file_name = 'map1.txt'
        if map_type == 1:
            self.file_name = 'map2.txt'
        f = open(self.file_name, 'r')
        while True:
            line = f.readline()
            if line == '':
                break
            lines.append(list(line.rstrip('\n')))

        width = len(lines[0])
        height = len(lines)
        self.map_array = [[1 for _ in range(width)] for _ in range(height)]
        for i, line in enumerate(lines):
            for j, element in enumerate(line):
                if element == ' ':
                    self.map_array[i][j] = 2
                elif i == player_pos[1] and j == player_pos[0]:
                    self.map_array[i][j] = 0
        return lines

    def player_collision_judge(self, init_pos, move_pos):
        """player_collision_judge関数
        プレイヤーが壁に衝突したかを判定する関数

        Args:
            init_pos (list[x, y]): プレイヤーの初期座標
            move_pos (list[x, y]): 移動したプレイヤーの座標

        Returns:
            flag (bool): 壁に衝突したらFalse, 衝突していなかったらTrue を返す

        Examples:
            >>> if player_collision_judge([0, 0], [-1, 0]):
        """

        if self.map_array[init_pos[1]+move_pos[1]][init_pos[0]+move_pos[0]] == 1:  # 壁に衝突した
            print('Collided with the wall.')
            flag = False
        else:  # 壁に衝突していない
            flag = True
        return flag

    def enemy_collision_judge(self, init_pos, move_pos):
        """enemy_collision_judge関数
        エネミーが壁に衝突したかを判定する関数

        Args:
            init_pos (dic{'enemy1': [x, y], ...}): エネミーの初期座標
            move_pos (dic{'enemy1': [x, y], ...}): 移動したエネミーの座標

        Returns:
            flag (bool): 壁に衝突したらFalse, 衝突していなかったらTrue を返す

        Examples:
            >>> if enemy_collision_judge([0, 0], [-1, 0]):
        """

        for i in range(len(init_pos)):
            pos_x = init_pos[f'enemy{i+1}'][1]+move_pos[f'enemy{i+1}'][1]
            pos_y = init_pos[f'enemy{i+1}'][0]+move_pos[f'enemy{i+1}'][0]
            if self.map_array[pos_x][pos_y] == 1:  # 壁に衝突した
                flag = False
                break
            else:  # 壁に衝突していない
                flag = True
        return flag

    def game_over(self, player_pos, enemy_pos, feed):
        """game_over関数
        ゲームオーバー及びゲームクリアを判定する関数

        Args:
            player_pos (list[x, y]): プレイヤーの座標
            enemy_pos (dic{'enemy1': [x, y], ...}): エネミーの座標
            feed (int): 餌の数

        Returns:
            flag (bool): ゲームクリア時にTrue, それ以外でFalse を返す

        Examples:
            >>> if game_over(player_pos, enemy_pos, feed):  # GameOverを判定
        """

        for i in range(len(enemy_pos)):
            if player_pos == enemy_pos[f'enemy{i+1}']:  # 壁に衝突した
                print('Game Over!')
                flag = True
                break
            else:  # 壁に衝突していない
                flag = False
        if feed == 0:
            print('Game Clear!')
            flag = True
        return flag

    def get_map_list(self):
        """get_map_list関数
        map_listを返す関数

        Returns:
            lines (list): map.txtから読み込んだlist

        Examples:
            >>> map_list = get_map_list()
        """

        lines = []
        f = open(self.file_name, 'r')
        while True:
            line = f.readline()
            if line == '':
                break
            lines.append(list(line.rstrip('\n')))
        return lines

    def feed_update(self, pos, total_feed=None):
        """feed_update関数
        残りのfeedをカウントする関数

        Args:
            pos (list[x, y]): プレイヤーの座標
            total_feed (int): 現在のfeedの数

        Returns:
            feed (int): feedを食べた場合，残りのfeedを返す
            total_feed (int): feedを食べなかった場合，そのままtotal_feedを返す

        Examples:
            >>> feed_update(player_pos)
        """

        if self.map_array[pos[1]][pos[0]] != 0:
            self.map_array[pos[1]][pos[0]] = 0
            if total_feed is not None:
                feed = total_feed - 1
                return feed
        else:
            if total_feed is not None:
                return total_feed

