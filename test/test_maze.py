
import unittest
import importlib.util
from importlib.machinery import SourceFileLoader
from pathlib import Path

GAME_FILE = Path(__file__).resolve().parents[1] / "Maze-Game"

loader = SourceFileLoader("maze_game", str(GAME_FILE))
spec = importlib.util.spec_from_loader(loader.name, loader)
game = importlib.util.module_from_spec(spec)
loader.exec_module(game)


class TestMazeGame(unittest.TestCase):

    def test_maze_exists(self):
        """Check that the maze is not empty."""
        self.assertGreater(len(game.MAZE), 0)

    def test_maze_rows_equal(self):
        """Check that all rows have equal length."""
        width = len(game.MAZE[0])

        for row in game.MAZE:
            self.assertEqual(len(row), width)

    def test_start_position(self):
        """Check that the player starts on a valid tile."""
        tile = game.MAZE[game.START_ROW][game.START_COLUMN]
        self.assertNotEqual(tile, "#")

    def test_exit_position(self):
        """Check that the level exit exists."""
        tile = game.MAZE[game.EXIT_ROW][game.EXIT_COLUMN]
        self.assertEqual(tile, "G")

    def test_second_level_generation(self):
        """Check that level 2 is generated correctly."""
        maze = game.generate_new_maze()

        self.assertEqual(maze, game.LEVEL_TWO_MAZE)

    def test_second_level_is_copy(self):
        """Check that generating level 2 returns a new list."""
        maze = game.generate_new_maze()

        self.assertIsNot(maze, game.LEVEL_TWO_MAZE)

    def test_maze_borders(self):
        """Check that the outer maze borders are walls."""
        for row in game.MAZE:
            self.assertEqual(row[0], "#")
            self.assertEqual(row[-1], "#")

        self.assertTrue(
            all(tile == "#" for tile in game.MAZE[0])
        )
        self.assertTrue(
            all(tile == "#" for tile in game.MAZE[-1])
        )


if __name__ == "__main__":
    unittest.main()
