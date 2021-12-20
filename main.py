from player import Player
from enemy import Enemy
from map import Map
from display import Display

class Game():
    """Gameクラス
    統括系
    """

    def __init__(self):
        self.player = Player(pos=[14, 7])
        self.enemy = Enemy(enemy1_pos=[6, 4], enemy2_pos=[21, 4], enemy3_pos=[6, 12], enemy4_pos=[21, 12])
        self.map = Map()
        self.display = Display()

    def play(self):
        """play関数
        ゲームを統括する関数

        Examples:
            >>> play()
        """

        i = 0
        map_list = self.map.read_map(self.player.pos, map_type=1)
        player_pos = self.player.get_position()
        self.map.feed_update(player_pos)
        enemy_pos = self.enemy.get_position()
        feed = self.display.output(map_list, player_pos, enemy_pos)
        total_feed = feed
        while True:
            print('step: ', i)
            print('feed:', feed, '/', total_feed)
            while True:
                move_pos = self.display.player_input()  # Playerの移動
                if self.map.player_collision_judge(player_pos, move_pos):
                    break
            player_pos = self.player.move(move_pos)
            feed = self.map.feed_update(player_pos, total_feed=feed)
            if self.map.game_over(player_pos, enemy_pos, feed):  # GameOverを判定
                break
            while True:
                move_pos = self.display.enemy_input(self.enemy.num)  # Enemyの移動
                if self.map.enemy_collision_judge(enemy_pos, move_pos):
                    break
            enemy_pos = self.enemy.move(move_pos)
            map_list = self.map.get_map_list()
            if self.map.game_over(player_pos, enemy_pos, feed):  # GameOverを判定
                break
            self.display.output(map_list, player_pos, enemy_pos, map_array=self.map.map_array)
            i += 1


if __name__ == "__main__":
    game = Game()
    game.play()
