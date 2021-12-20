import random

class Display():
    """Displayクラス
    入出力系
    """

    def __init__(self, power_feed=[0, 0]):
        self.power_feed = power_feed

    def output(self, map_list, player_pos, enemy_pos, map_array=None):
        """output関数
        画面出力及びfeedの数を返す関数

        Args:
            map_list (list): txtファイルから読み込んだマップのリスト
            player_pos (list[x, y]): プレイヤーの座標
            enemy_pos (dic{'enemy1': [x, y], ...}): エネミーの座標
            map_array (ndarray): map_listをndarrayに変換したもの

        Returns:
            count (int): feedの数を返す

        Examples:
            >>> feed = output(map_list, player_pos, enemy_pos)
        """

        count = 0
        map_list[player_pos[1]][player_pos[0]] = '\033[33m' + 'P' + '\033[0m'
        enemy_pos_list = [enemy_pos[f'enemy{i+1}'] for i in range(len(enemy_pos))]
        for enemy_pos in enemy_pos_list:
            map_list[enemy_pos[1]][enemy_pos[0]] = '\033[31m' + 'E' + '\033[0m'

        for i, line in enumerate(map_list):
            for j, element in enumerate(line):
                if element == ' ':
                    if map_array is not None:
                        if map_array[i][j] == 2:
                            print('•', end='')
                        else:
                            print('\033[36m' + element + '\033[0m', end='')
                    else:
                        print('•', end='')
                        count += 1
                else:
                    if len(line) - 1 == j:
                        print('\033[36m' + element + '\033[0m')
                    else:
                        print('\033[36m' + element + '\033[0m', end='')
        return count

    def player_input(self):
        """player_input関数
        画面入力の関数

        Returns:
            move_pos (list[x, y]): 標準入力に対応した移動先座標を返す

        Examples:
            >>> pos = player_input()  # Playerの移動
        """

        while True:
            print('Please enter the direction.(W, A, S, D): ', end='')
            key = input().strip()
            if key == 'w' or key == 'W':
                move_pos = [0, -1]
                break
            elif key == 'a' or key == 'A':
                move_pos = [-1, 0]
                break
            elif key == 's' or key == 'S':
                move_pos = [0, 1]
                break
            elif key == 'd' or key == 'D':
                move_pos = [1, 0]
                break
            else:
                print('Type it again.')
        return move_pos

    def enemy_input(self, num):
        """enemy_input関数
        エネミーの移動先の座標を返す関数

        Args:
            num (int): エネミーの数

        Returns:
            move_pos_dic (dic{'enemy1': [x, y], ...}): エネミーの移動先の座標を返す

        Examples:
            >>> pos = enemy_input(self.num)
        """

        move_pos_dic = {}
        for i in range(num):
            move_pos = random.choice([[0, 1], [0, -1], [1, 0], [-1, 0]])
            dic_tmp = {f'enemy{i+1}': move_pos}
            move_pos_dic.update(dic_tmp)
        return move_pos_dic